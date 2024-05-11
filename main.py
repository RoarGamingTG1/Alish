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

# Dictionary mapping trigger words to response messages
trigger_responses = {
    "mod": "This is a response to Mod trigger word.",
    "obb": "This is a response to Obb trigger word.",
    "key": "This is a response to Key trigger word.",
    "hack": "This is a response to Hack trigger word.",
    "use": "This is a response to Use trigger word.",
    "mt": "This is a response to Mt trigger word.",
    "editor": "This is a response to Editor trigger word.",
    "mad": "This is a response to Mad trigger word.",
    "rz": "This is a response to Rz trigger word.",
    "ramjan": "This is a response to Ramjan trigger word.",
    "hero": "This is a response to Hero trigger word."
}

# Function to send threatening reply with random dangerous messages
async def send_dangerous_reply(message):
    dangerous_messages = [
        "ab tera time khatam! 💣💥",
        "tere liye special surprise hai mere pass! 🎁🔥",
        # Add more threatening messages here if needed
    ]

    reply = random.choice(dangerous_messages)
    sent_message = await message.reply_text(reply)

    # Wait for 30 seconds before deleting the message
    await asyncio.sleep(30)

    # Delete the sent message
    await sent_message.delete()

# Main message handling function
@app.on_message(filters.text & ~filters.me)
async def handle_messages(client, message):
    if message.text.lower() == "what is your favorite color?":
        sent_message = await message.reply_text("My favorite color is blue!")
    elif message.text.lower() == "how are you?":
        sent_message = await message.reply_text("I'm just a bot, but I'm doing well. How can I assist you?")
    elif message.text.lower() == "who created you?":
        sent_message = await message.reply_text("I was created by a team of developers at OpenAI.")
    else:
        # Check if any trigger word is present in the message
        for word, response in trigger_responses.items():
            if word in message.text.lower():
                sent_message = await message.reply_text(response)

                # Wait for 30 seconds before deleting the message
                await asyncio.sleep(30)

                # Delete the sent message
                await sent_message.delete()
                break

# Run the bot
app.run()
