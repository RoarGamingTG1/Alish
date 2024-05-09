import os
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Bot ke credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# Dictionary to store users and their generated keys
user_keys = {}

# Bot ko create karein
Bot = Client(
    "ChatBot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

# Function to send welcome message with photo and inline keyboard
async def send_welcome_message(bot, chat_id):
    await bot.send_photo(
        chat_id,
        photo="https://telegra.ph/file/123022afb754372e3802e.jpg",
        caption="Welcome to the ChatBot! Click on 'Key' button to get your key or Open Our Channel for more info.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Key", callback_data="key"),
                    InlineKeyboardButton("Open Channel", url="https://t.me/QTVinfo")
                ]
            ]
        )
    )

# Function to generate and send key
async def send_key(bot, update):
    chat_id = update.chat.id
    user = update.from_user.id
    if user in user_keys.values():
        existing_key = next((key for key, value in user_keys.items() if value == user), None)
        await bot.send_message(chat_id, f"You already have a key: {existing_key}")
    else:
        key = f"XALISHB{len(user_keys) + 1}"
        user_keys[key] = user
        await bot.send_message(chat_id, f"Your key is: {key}")

# Message handler
@Bot.on_message(filters.private)
async def chat(bot, update):
    # Extract message text
    message_text = update.text.lower()

    # Check if the user is asking for a key
    if "key" in message_text:
        await send_key(bot, update)
    else:
        # Ignore other messages
        pass

# Message handler for start command
@Bot.on_message(filters.command("start"))
async def start(bot, update):
    # Call send_welcome_message function to send welcome message with photo and inline keyboard
    await send_welcome_message(bot, update.chat.id)

# Bot ko run karein
Bot.run()
