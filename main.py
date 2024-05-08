import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Bot ke credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# Dictionary to store users and their generated keys
user_keys = {}

# Function to send welcome message
async def send_welcome_message(bot, chat_id):
    await bot.send_message(chat_id, "Welcome to the ChatBot! Click on 'Verify' to get your key if you have joined the channel.")

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

# Function to check if user has joined the channel
async def check_channel(bot, update):
    chat_id = update.chat.id
    user = update.from_user.id
    if user in user_keys.values():
        existing_key = next((key for key, value in user_keys.items() if value == user), None)
        await bot.send_message(chat_id, f"You already have a key: {existing_key}")
    else:
        channel_link = "https://t.me/your_channel_username"
        await bot.send_message(chat_id, f"To get your key, please join our channel: {channel_link}")

# Bot ko create karein
Bot = Client(
    "ChatBot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

# Message handler for start command
@Bot.on_message(filters.command("start"))
async def start(bot, update):
    # Start message with inline keyboard
    start_message = "Welcome To AlishToolkit 🎁\nClick on 'Verify' to get your key if you have joined the channel."
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Verify", callback_data="verify"),
                InlineKeyboardButton("Check Total Keys", callback_data="check_keys")
            ]
        ]
    )
    await bot.send_photo(update.chat.id, "https://telegra.ph/file/2f44a7f4d8dfc9c8c8fb7.jpg", caption=start_message, reply_markup=keyboard)

# Callback handler for inline keyboard buttons
@Bot.on_callback_query()
async def callback_handler(bot, update):
    if update.data == "verify":
        await send_key(bot, update)
    elif update.data == "check_keys":
        await check_channel(bot, update)

# Bot ko run karein
Bot.run()
        
