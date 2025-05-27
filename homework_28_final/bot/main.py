import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    ConversationHandler
)

from states import States
from states_consts import *

# --- Load environment variables ---
dotenv_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path)

# --- Initialize states object ---
states_obj = States()

# --- Main reply keyboard ---
main_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("🚘 Show available cars")],
    [KeyboardButton("🔙 Back")]
], resize_keyboard=True)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start command handler that shows main menu."""
    await update.message.reply_text(
        "Welcome! I'm your car rental assistant bot. What would you like to do?",
        reply_markup=main_keyboard
    )
    return MAIN


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancel the current conversation."""
    await update.message.reply_text(
        "Conversation ended. Type /start to begin again."
    )
    return ConversationHandler.END


def main() -> None:
    """Main entry point to start the bot."""
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise EnvironmentError("BOT_TOKEN is not set in the .env file.")

    app = ApplicationBuilder().token(token).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states=states_obj.get_states(),
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv_handler)
    app.run_polling()


if __name__ == "__main__":
    asyncio.run(main())
