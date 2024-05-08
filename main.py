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

# Function to generate and send key
async def send_key(update):
    global total_keys_issued
    chat_id = update.chat.id
    user = update.from_user.id
    if user in user_keys.values():
        existing_key = next((key for key, value in user_keys.items() if value == user), None)
        await update.reply_text(f"Your key is: {existing_key}")
    else:
        # Check if user has joined the channel
        if await Bot.get_chat_member(int(CHANNEL_ID), user):
            key = f"XALISHB{len(user_keys) + 1}"
            user_keys[key] = user
            total_keys_issued += 1  # Increment total keys issued
            await update.reply_text(f"Your key is: {key}")
        else:
            # If user hasn't joined the channel, send a message to join
            join_channel_message = "Please join our channel [here](https://t.me/QTVinfo) to get the key."
            await update.reply_text(join_channel_message, disable_web_page_preview=True)

# Function to handle verification process
async def verify_user(update):
    user = update.from_user.id
    if await Bot.get_chat_member(int(CHANNEL_ID), user):
        await send_key(update)
    else:
        await update.reply_text("You haven't joined our channel yet. Please join our channel [here](https://t.me/QTVinfo) and click 'Verify' again.", disable_web_page_preview=True)

# Function to check user's own status
async def check_user_status(update):
    user = update.from_user.id
    if await Bot.get_chat_member(int(CHANNEL_ID), user):
        await update.reply_text("You have joined our channel.")
    else:
        await update.reply_text("You have not joined our channel yet.")

# Function to check total keys issued
async def check_total_keys(update):
    global total_keys_issued
    await update.reply_text(f"Total keys issued: {total_keys_issued}")

# Message handler
@Bot.on_message(filters.private)
async def chat(bot, update):
    # Extract message text
    message_text = update.text.lower()

    # Check if the user is asking for key, verification, or status check
    if "get key" in message_text:
        await send_key(update)
    elif "verify" in message_text:
        await verify_user(update)
    elif "check status" in message_text:
        await check_user_status(update)
    elif "check keys" in message_text:
        await check_total_keys(update)

    # Send welcome message with options
    else:
        welcome_message = "Welcome to the chat! Select an option below:"
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Get Key", callback_data="get_key"),
                    InlineKeyboardButton("Verify", callback_data="verify")
                ],
                [
                    InlineKeyboardButton("Check Status", callback_data="check_status"),
                    InlineKeyboardButton("Check Total Keys", callback_data="check_keys")
                ]
            ]
        )
        await update.reply_text(welcome_message, reply_markup=keyboard)

# Button handler
@Bot.on_callback_query()
async def button(bot, update):
    # Check which button is clicked
    if update.data == "get_key":
        await send_key(update.message)
    elif update.data == "verify":
        await verify_user(update.message)
    elif update.data == "check_status":
        await check_user_status(update.message)
    elif update.data == "check_keys":
        await check_total_keys(update.message)

# Bot ko run karein
Bot.run()
