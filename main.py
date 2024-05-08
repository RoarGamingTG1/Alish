import os
import random
from pyrogram import Client, filters

# Bot ke credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# List of predefined questions and answers
qa_data = {
    "Hi": "G 😊",
    "Apka name kia hai": "Name men kia rakha hai .",
    "how are you": "Not fine 😔.",
    "Pubg khelty ho ": "Pubg is My favourite Game 🫥.",
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

# Function to send welcome message
async def send_welcome_message(bot, chat_id):
    await bot.send_message(chat_id, "Welcome to the ChatBot! Click on 'Key' button to get your key.")

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

    # Check if the user is asking a question
    if "?" in message_text:
        await answer_question(bot, update)
    elif "key" in message_text:
        await send_key(bot, update)

# Function to answer a question
async def answer_question(bot, update):
    # Check if the question exists in the predefined data
    question = update.text.strip()
    answer = qa_data.get(question, "Kuch Ayse Swal hen Jinka Mujhe nhi Pata Ap Join Kren Yahan Apke Har sawal Ka Jwab Milega 💒🎁🎉 @QTVinfo.")
    await update.reply_text(answer)

# Function to ask a random question
async def ask_question(bot, update):
    random_question = random.choice(list(qa_data.keys()))
    await update.reply_text(random_question)

# Message handler for start command
@Bot.on_message(filters.command("start"))
async def start(bot, update):
    # Start message
    start_message = "Welcome To AlishToolkit 🎁 If You Want Key Write Key Join Our Channel Free All Pro Tips @QTVinfo"
    await update.reply_text(start_message)

# Bot ko run karein
Bot.run()
