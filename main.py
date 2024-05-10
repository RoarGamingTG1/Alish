import os
import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

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

# Function to send dangerous reply with random dangerous messages, inline buttons, and image
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
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Hack Do", callback_data="hack")],
        [InlineKeyboardButton("Download Key", url="https://example.com/download_key")],
        [InlineKeyboardButton("Download Hack", url="https://example.com/download_hack")]
    ])
    # Add the URL of the image to be attached
    media = InputMediaPhoto(media="https://telegra.ph/file/2f44a7f4d8dfc9c8c8fb7.jpg")
    await message.reply_media_group(media=[media], reply_markup=keyboard, caption=reply)

# Function to handle inline button callback
@app.on_callback_query()
async def handle_callback_query(client, query):
    if query.data == "hack":
        await query.answer("Hacking process initiated. Please wait for the download link.", show_alert=True)
        # Here you can add the logic to start the hacking process
        # Once the process is complete, you can send the download link to the user

# Filter messages containing trigger words
@app.on_message(filters.text & ~filters.me)
async def reply_to_trigger_words(client, message):
    trigger_words = ["hack", "key", "download"]
    for word in trigger_words:
        if word in message.text.lower():
            await send_dangerous_reply(message)
            break

# Run the bot
app.run()
