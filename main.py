import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Bot ke credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
CHANNEL_ID = os.environ.get("CHANNEL_ID")  # Add your channel ID here

# Variable to keep track of total keys issued
total_keys_issued = 0

# Dictionary to store users and their generated keys
user_keys = {}

# Bot ko create karein
Bot = Client(
    "ChatBot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

# Function to send start message with image and buttons
async def send_start_message(update):
    # Send welcome message with options and image
    welcome_message = "Welcome to the chat! Select an option below:"
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Get Key 🔐", callback_data="get_key"),
                InlineKeyboardButton("Verify ✅", callback_data="verify_user")
            ],
            [
                InlineKeyboardButton("Check Status ⭐", callback_data="check_user_status"),
                InlineKeyboardButton("Check Total Keys 👿", callback_data="check_total_keys")
            ]
        ]
    )
    await update.reply_photo(
        photo="https://telegra.ph/file/123022afb754372e3802e.jpg",  # Replace with your image URL
        caption=welcome_message,
        reply_markup=keyboard
    )

# Function to generate and send key
async def send_key(update):
    global total_keys_issued
    user = update.from_user
    if user.id in user_keys.values():
        existing_key = next((key for key, value in user_keys.items() if value == user.id), None)
        await update.reply_text(f"Your key is: {existing_key}")
    else:
        # Check if user has joined the channel
        if await Bot.get_chat_member(int(CHANNEL_ID), user.id):
            key = f"XALISHB{len(user_keys) + 1}"
            user_keys[key] = user.id
            total_keys_issued += 1  # Increment total keys issued
            await update.reply_text(f"Your key is: {key}")
        else:
            # If user hasn't joined the channel, send a message to join
            join_channel_message = "Please join our channel [here](https://t.me/QTVinfo) to get the key."
            await update.reply_text(join_channel_message, disable_web_page_preview=True)

# Function to check total keys issued
async def check_total_keys(update):
    global total_keys_issued
    await update.reply_text(f"Total keys issued: {total_keys_issued}")

# Message handler
@Bot.on_message(filters.private & (filters.text | filters.command(["key"])))
async def chat(bot, update):
    # Extract message text
    message_text = update.text.lower()

    # Check if the message contains the word "key"
    if "key" in message_text:
        await send_key(update)
    else:
        # Send welcome message with options
        await send_start_message(update)

# Button handler
@Bot.on_callback_query()
async def button(bot, update):
    # Extract callback data
    callback_data = update.data
    chat_id = update.message.chat.id
    # Check which button is clicked
    if callback_data == "check_keys":
        await check_total_keys(update.message)

# Command handler
@Bot.on_message(filters.command(["start"]))
async def start(bot, update):
    # Call the function to send the start message with image and buttons
    await send_start_message(update)

# Bot ko run karein
Bot.run()
    
