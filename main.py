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
        "⚠️ Mad bhai ke hatters, tumhari kismat aaj tumhare saath hai!",
        "⚠️ Aaj Mad bhai ne tere naam ka ek special surprise bheja hai!",
        "⚠️ Mad bhai ki permission ke bina kisi ke paas jana ab khatra hai!",
        "⚠️ Mad bhai ke hatters, aaj ka din tumhare liye khaas hai!",
        "⚠️ Aaj Mad bhai ne tumhare liye ek naya surprise tayaar kiya hai!",
        "⚠️ Mad bhai ke hatters, ab tumhari aukaat aane wali hai!",
        "⚠️ Mad bhai ki permission ke bina kisi ko hack karna, ab tumhari jaan ko khatra hai!",
        "⚠️ Mad bhai ke hatters, aaj se tumhare liye bura waqt shuru hua hai!",
        "⚠️ Aaj se Mad bhai ke hatters, tumhare peeche nahi, tumhare saamne bhaagna shuru karo!",
        "⚠️ Mad bhai ke hatters, aaj ka din tumhare liye nightmare banne wala hai!",
        "⚠️ Mad bhai ki permission ke bina kisi ke hack ka key share karna, ab tumhari maut ka faisla hai!"
    ]
    reply = random.choice(dangerous_messages)
    await message.reply_text(reply)

# Function to send random amusing messages
async def send_amusing_reply(message):
    amusing_messages = [
        "😄 Mad bhai aaj bhi apne unique andaaz mein sabko entertain kar rahe hain!",
        "😄 Aaj Mad bhai ne phir se sabko muskurahat di hai!",
        "😄 Mad bhai ke aaj ke messages ne sabko hasi ke pahaad par le jaaya hai!",
        "😄 Aaj bhi Mad bhai ne sabko maze kar diye hain apne messages ke saath!",
        "😄 Mad bhai ke messages se aaj sab log khush hain!",
        "😄 Aaj bhi Mad bhai ne apne creativity ka jadoo dikha diya hai!",
        "😄 Mad bhai ke messages ne aaj sabko thoda sa hasa diya hai!"
    ]
    reply = random.choice(amusing_messages)
    await message.reply_text(reply)

# Filter messages containing trigger words
@app.on_message(filters.text & ~filters.me)
async def reply_to_trigger_words(client, message):
    trigger_words = ["mad bhai", "mad bhi", "mad bro"]
    for word in trigger_words:
        if word in message.text.lower():
            await send_dangerous_reply(message)
            await asyncio.sleep(1)  # Add a slight delay
            await send_amusing_reply(message)
            break

# Run the bot
app.run()
