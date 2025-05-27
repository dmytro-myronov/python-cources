from telegram.ext import (
    CallbackQueryHandler,
    MessageHandler,
    filters,
)

from handlers import *


class States:
    """State configuration for the conversation handler."""

    def __init__(self) -> None:
        pass

    def get_states(self) -> dict:
        """
        Returns the state mappings for the bot's conversation flow.
        """
        return {
            MAIN: [
                MessageHandler(
                    filters.Regex("🚘 Show available cars"), show_car_list_prompt
                ),
                MessageHandler(filters.Regex("🔙 Back"), go_back),
            ],
            CHOOSE_CAR: [CallbackQueryHandler(car_selected)],
            ASK_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_name)],
            ASK_DATE_FROM: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_date_from)],
            ASK_DATE_TO: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_date_to)],
            ASK_EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_email)],
        }
