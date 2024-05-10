import os
import random
import asyncio
from pyrogram import Client, filters

# Bot credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# Create Pyrogram client
app = Client("WormGPT_Bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Function to delete messages after 3 seconds
async def delete_message(message):
    await asyncio.sleep(3)
    await message.delete()

# Function to send threatening reply with random dangerous messages
async def send_dangerous_reply(message):
    dangerous_messages = [
        " Mad bhai 👿 Busy In Exzam 💒!",
        "Mad Bhai New Hack Mod Buht Jaldi Upload Krny Waly Hen 🙂!",
        "Mad Bhai 😒 Koi Support Nhi Krta Dill Se Aysa Hack Or Kon Bana K dega 🙃!",
        "Aaj Mad bhai ne phir se pubg lite ka system hi hill dala!",
        "Mad Bhai Jo Bhi Hack use KerTy hen Wo Feedback Send Kro !",
        "Mad Bhai Aaj Nhi aany Waly Wo Khahen Gai Hen 🙂!",
        "Mad Bhai New Mod Banay Hai Pta Hai Buht OP hai 🫥 !"
    ]
    reply = random.choice(dangerous_messages)
    await message.reply_text(reply)

# Filter messages containing trigger words
@app.on_message(filters.text & ~filters.me)
async def reply_to_trigger_words(client, message):
    trigger_words = ["mad", "mad bhi", "mad bro"]
    for word in trigger_words:
        if word in message.text.lower():
            await send_dangerous_reply(message)
            break

# Run the bot
app.run()
