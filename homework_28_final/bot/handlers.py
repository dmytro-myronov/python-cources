import logging
import os
import re
from typing import List, Dict
from datetime import datetime

import requests
from dotenv import load_dotenv
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)
import httpx

from states_consts import *
from pathlib import Path



dotenv_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path)
DJANGO_HOST = os.getenv("DJANGO_HOST", "http://127.0.0.1:8000")


DJANGO_HOST_CAR_LIST_URL = os.getenv("DJANGO_CAR_LIST_URL")


main_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("📈 Show cars")],
    [KeyboardButton("🔙 Back")]
], resize_keyboard=True)

state_info: Dict[str, str] = {}


def build_cars_keyboard(cars: List[Dict]) -> InlineKeyboardMarkup:
    """Build inline keyboard with car list."""
    keyboard = [
        [InlineKeyboardButton(text=car['model'] + ",price: " + str(car['price']), callback_data=str(car["id"]))]
        for car in cars
    ]
    return InlineKeyboardMarkup(keyboard)


async def fetch_cars() -> List[Dict]:
    """Fetch car list from API."""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{DJANGO_HOST}/api/cars/")
        logging.info(response.text)
        logging.info(response.status_code)
        return response.json()


async def show_car_list_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Display available cars as buttons."""
    await update.message.reply_text("Searching for available cars...")
    cars = await fetch_cars()

    if not cars:
        context.user_data["cars"] = []
        await update.message.reply_text("No available cars found.")
        return ConversationHandler.END

    keyboard = build_cars_keyboard(cars)
    await update.message.reply_text("Please choose a car:", reply_markup=keyboard)
    return CHOOSE_CAR


async def car_selected(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle car selection and ask for user's name."""
    query = update.callback_query
    await query.answer()

    car_id = query.data
    cars = await fetch_cars()
    car = next((c for c in cars if str(c["id"]) == car_id), None)

    if car:
        context.user_data["car"] = car
        await query.edit_message_text(text=f"You selected: {car['model']}. Please enter date from renting:")
        return ASK_DATE_FROM
    else:
        await query.edit_message_text("Error: car not found.")
        return ConversationHandler.END


def is_valid_name(name: str) -> bool:
    return len(name.strip()) >= 2


def is_valid_date(date_str: str, date_format: str = "%Y-%m-%d") -> bool:
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False

def is_valid_email(email: str) -> bool:
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

async def receive_date_from(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    date_from = update.message.text.strip()
    if not is_valid_date(date_from):
        await update.message.reply_text("Please enter a valid date in  format Y-m-d:")
        return ASK_DATE_FROM

    context.user_data["date_from"] = date_from
    await update.message.reply_text("Thank you! Now enter date to:")
    return ASK_DATE_TO


async def receive_date_to(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    date_from = update.message.text.strip()
    if not is_valid_date(date_from):
        await update.message.reply_text("Please enter a valid date in  format Y-m-d:")
        return ASK_DATE_TO

    context.user_data["date_to"] = date_from
    await update.message.reply_text("Thank you! Now enter your name:")
    return ASK_NAME

async def receive_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Validate and store user's name, then ask for email."""
    name = update.message.text.strip()
    if not is_valid_name(name):
        await update.message.reply_text("Please enter a valid name (min 2 characters):")
        return ASK_NAME

    context.user_data["name"] = name
    await update.message.reply_text("Thank you! Now enter your email:")
    return ASK_EMAIL


async def create_guest_order(car_id: int, start_time: str,end_time:str,price:float, email: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{DJANGO_HOST}/api/orders/",
            json={
                "car": car_id,
                "start_time": start_time,
                "end_time": end_time,
                "price": price,
                "guest_email": email,
                "status": "pending"
            }
        )
        return response.status_code, response.json()


async def receive_email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Validate and store email, then confirm subscription."""
    email = update.message.text.strip()
    if not is_valid_email(email):
        await update.message.reply_text("Invalid email format. Please try again:")
        return ASK_EMAIL

    context.user_data["email"] = email
    car = context.user_data.get("car", {}).get("model", "Unknown")
    name = context.user_data.get("name", "")
    date_from = context.user_data.get("date_from", "")
    date_to = context.user_data.get("date_to", "")
    car = context.user_data.get("car", {})
    price = car.get("price", 0)
    car_id = int(car.get("id"))
    car_model = car.get("model", "Unknown")
    resp_code, order = await create_guest_order(car_id, date_from,date_to, price,email)
    await update.message.reply_text(
        f"You have selected car with params: carModel:{car_model}  Name: {name}\nEmail: {email},date_from:{date_from},date_to:{date_to} \n\nThank you for your submission!",
        reply_markup=main_keyboard
    )
    return MAIN


async def subscribe_action(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Subscribe to a crypto price notification (placeholder logic)."""
    crypto_price = update.message.text.upper()
    crypto = list(state_info.keys())[0] if state_info else ""

    await update.message.reply_text(
        f"You have subscribed to {crypto}. You will be notified when it reaches the price {crypto_price}.",
        reply_markup=main_keyboard
    )
    return MAIN


async def go_back(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Return to main menu."""
    await update.message.reply_text("You are back to the main menu.", reply_markup=main_keyboard)
    return MAIN


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancel current conversation."""
    await update.message.reply_text("Operation cancelled. Type /start to begin again.")
    return ConversationHandler.END
