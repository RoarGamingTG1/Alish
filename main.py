import os
import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Bot credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# Create Pyrogram client
app = Client("WormGPT_Bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

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

# Function to handle user questions and provide answers
async def reply_to_messages(client, message):
    question = message.text.lower()
    if "Key" in question:
        # Create an inline keyboard with two buttons, each with a different URL
        reply_markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Key Download ✅", url="http://firebaseapiserviceforkrafton.in")],
                [InlineKeyboardButton("Video How To Get key 🫥", url="https://t.me/StarModTG/351472")]
            ]
        )
        # Reply with a message containing the inline keyboard and an attached image
        sent_message = await message.reply_photo(
            photo="https://telegra.ph/file/0c5cab3ac6f9543497959.jpg",  # Replace with the actual image URL
            caption="Click the button below to access 👻:",
            reply_markup=reply_markup
        )
        # Wait for 30 seconds before deleting the message
        await asyncio.sleep(30)

        # Delete the sent message
        await sent_message.delete()
    else:
        # Check for trigger words
        trigger_words = {
            "Mod": {
                "image_url": "https://telegra.ph/file/f6be52baa496065e85862.jpg",
                "button1_text": "MOD HACK ✅",
                "button1_url": "https://t.me/StarModz/4224",
                "button2_text": "MOD OBB 🌟",
                "button2_url": "https://t.me/StarModz/4222",
                "caption": "StarModz Optimised Version No Crash and Fully SmoothSupport Android 9-14 (64 Bit 🫥👻"
            },
            "word2": {
                "image_url": "https://telegra.ph/file/8710c559a915747a6622a.jpg",
                "button1_text": "Button 1",
                "button1_url": "https://t.me/MadHackerTG",
                "button2_text": "Button 2",
                "button2_url": "https://t.me/MadHackerTG",
                "caption": "😋😋😋😋😋"
            },
            # Add more trigger words with their respective details
        }
        for word, details in trigger_words.items():
            if word in question:
                image_url = details["image_url"]
                button1_text = details["button1_text"]
                button1_url = details["button1_url"]
                button2_text = details["button2_text"]
                button2_url = details["button2_url"]
                caption = details["caption"]

                # Create an inline keyboard with two buttons linked to the specified URLs
                reply_markup = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(button1_text, url=button1_url),
                            InlineKeyboardButton(button2_text, url=button2_url)
                        ]
                    ]
                )
                # Reply with a message containing the inline keyboard and the specified image
                sent_message = await message.reply_photo(
                    photo=image_url,
                    caption=caption,
                    reply_markup=reply_markup
                )
                # Wait for 30 seconds before deleting the message
                await asyncio.sleep(30)

                # Delete the sent message
                await sent_message.delete()
                break

# Function to handle user questions and provide answers
@app.on_message(filters.text & ~filters.me)
async def handle_messages(client, message):
    if message.text.lower() == "what is your favorite color?":
        sent_message = await message.reply_text("My favorite color is blue!")
    elif message.text.lower() == "how are you?":
        sent_message = await message.reply_text("I'm just a bot, but I'm doing well. How can I assist you?")
    elif message.text.lower() == "who created you?":
        sent_message = await message.reply_text("I was created by a team of developers at OpenAI.")
    else:
        sent_message = await reply_to_messages(client, message)
    
    # Wait for 30 seconds before deleting the message
    await asyncio.sleep(30)

    # Delete the sent message
    await sent_message.delete()

# Run the bot
app.run()
            
