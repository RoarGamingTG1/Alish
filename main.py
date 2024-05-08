import os
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Bot ke credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
CHANNEL_ID = os.environ.get("CHANNEL_ID")  # Add your channel ID here

# Dictionary to store users and their generated keys
user_keys = {}

# List of predefined questions and answers
qa_data = {
    "200": "Update ayega osmen Limit Increase Hogi 🎉💒",
    "Thanks": " 🥰 .",
    "Limit": "Join @QTVinfo update coming Soon 🎁💒💒🌀.",
    "Pubg khelty ho ": "Pubg is My favourite Game 🫥.",
    "😭": "Ro mat nhi To Block Krdongi 🫥.",
    "🙄": "😒."
}

# Bot ko create karein
Bot = Client(
    "ChatBot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

# Function to answer a question
async def answer_question(bot, update):
    # Check if the question exists in the predefined data
    question = update.text.strip()
    answer = qa_data.get(question, "Kuch Ayse Swal hen Jinka Mujhe nhi Pata Ap Join Kren Yahan Apke Har sawal Ka Jwab Milega 💒🎁🎉 @QTVinfo.")
    await update.reply_text(answer)

# Function to generate and send key
async def send_key(bot, update):
    chat_id = update.chat.id
    user = update.from_user.id
    if user in user_keys.values():
        existing_key = next((key for key, value in user_keys.items() if value == user), None)
        await bot.send_message(chat_id, f"Ye raha Apka password 🔑 Enjoy  Don't Hurt anyone' 🎁🦋😊: {existing_key}")
    else:
        # Check if user has joined the channel
        if await bot.get_chat_member(int(CHANNEL_ID), user):
            key = f"XALISHB{len(user_keys) + 1}"
            user_keys[key] = user
            await bot.send_message(chat_id, f"Your key is: {key}")
        else:
            # If user hasn't joined the channel, send a message to join
            join_channel_message = "Please join our channel @QTVinfo to get the key."
            await bot.send_message(chat_id, join_channel_message)

# Function to check total users
async def check_total_users(bot, update):
    total_users = len(set(user_keys.values()))
    await bot.send_message(update.chat.id, f"Total users: {total_users}")

# Function to handle verification process
async def verify_user(bot, update):
    user = update.from_user.id
    if await bot.get_chat_member(int(CHANNEL_ID), user):
        await bot.send_message(update.chat.id, "User is verified. You can now get your key.")
    else:
        await bot.send_message(update.chat.id, "User is not verified. Please join our channel @QTVinfo.")

# Message handler
@Bot.on_message(filters.private)
async def chat(bot, update):
    # Extract message text
    message_text = update.text.lower()

    # Check if the user is asking a question
    if "?" in message_text:
        await answer_question(bot, update)
    elif "get key" in message_text:
        await send_key(bot, update)
    elif "total users" in message_text:
        await check_total_users(bot, update)
    elif "verify" in message_text:
        await verify_user(bot, update)

    # Send welcome message with buttons
    else:
        welcome_message = "Welcome to the chat! Select an option below:"
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Get Key 🔐", callback_data="get_key"),
                    InlineKeyboardButton("Check ✔️", callback_data="total_users")
                ],
                [
                    InlineKeyboardButton("Verify ✅", callback_data="verify_user")
                ]
            ]
        )
        await bot.send_message(update.chat.id, welcome_message, reply_markup=keyboard)

# Button handler
@Bot.on_callback_query()
async def button(bot, update):
    # Check which button is clicked
    if update.data == "get_key":
        await send_key(bot, update.message)
    elif update.data == "total_users":
        await check_total_users(bot, update.message)
    elif update.data == "verify_user":
        await verify_user(bot, update.message)

# Bot ko run karein
Bot.run()
        
