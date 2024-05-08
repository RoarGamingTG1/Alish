import os
import random
from pyrogram import Client, filters

# Bot ke credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# Dictionary to store users and their generated keys
user_keys = {}

# List of predefined questions and answers
qa_data = {
    "200": "Update ayega osmen Limit Increase Hogi 🎉💒",
    "Thanks": " 🥰 .",
    "Limit": "Join @QTVinfo update coming Soon 🎁💒💒🌀.",
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
    await bot.send_message(chat_id, "Welcome to the ChatBot! Click on 'Key' button to get your key.")

# Function to generate and send key
async def send_key(bot, update):
    chat_id = update.chat.id
    user = update.from_user.id
    if user in user_keys.values():
        existing_key = next((key for key, value in user_keys.items() if value == user), None)
        await bot.send_message(chat_id, f"Ye raha Apka password 🔑 Enjoy  Don't Hurt anyone' 🎁🦋😊: {existing_key}")
    else:
        key = f"XALISHB{len(user_keys) + 1}"
        user_keys[key] = user
        await bot.send_message(chat_id, f"Your key is: {key}")

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
        await send_welcome_message(bot, update.chat.id)

# Message handler for start command
@Bot.on_message(filters.command("start"))
async def start(bot, update):
    # Start message
    start_message = "Welcome To AlishToolkit 🎁 If You Want Key Write Key Join Our Channel Free All Pro Tips @QTVinfo"
    await update.reply_text(start_message)

# Bot ko run karein
Bot.run()
    
