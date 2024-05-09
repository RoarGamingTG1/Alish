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

# List of predefined questions and answers
qa_data = {
    "Hi": "G 😊",
    "Apka name kia hai": "Name men kia rakha hai .",
    "how are you": "Not fine 😔.",
    "Pubg khelty ho ": "Pubg is My favourite Game 🫥.",
    "Key": "Ok 🌀💒 Join Channel @QTVinfo",
    "😭": "Ro mat nhi To Block Krdongi 🫥.",
    "200": "update Soon Join 🫥.",
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

# Function to send welcome message
async def send_welcome_message(bot, chat_id):
    # Send photo with caption and inline keyboard
    await bot.send_photo(
        chat_id,
        photo="https://telegra.ph/file/123022afb754372e3802e.jpg",
        caption="Welcome to the xalishbToolkit 💒! write key here 🥰 Join @QTVinfo For More Any Problem or suggestions please msg Here ✅❤️.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Total Keys ✅", callback_data="total_keys"),
                    InlineKeyboardButton("Join Channel 🦋", url="https://t.me/QTVinfo")
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

# Function to ask a random question
async def ask_question(bot, update):
    random_question = random.choice(list(qa_data.keys()))
    await update.reply_text(random_question)

# Message handler
@Bot.on_message(filters.private)
async def chat(bot, update):
    # Extract message text
    message_text = update.text.lower()

    # Check if the user is asking a question
    if "?" in message_text:
        await answer_question(bot, update)
    elif "key" in message_text:
        await send_key(bot, update)
    else:
        await ask_question(bot, update)

# Message handler for start command
@Bot.on_message(filters.command("start"))
async def start(bot, update):
    # Call send_welcome_message function to send welcome message with photo and inline keyboard
    await send_welcome_message(bot, update.chat.id)

# Bot ko run karein
Bot.run()
    
