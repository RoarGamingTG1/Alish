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
        # Check for trigger words and their respective details
        trigger_words = {
            "mod1": {
                "image_url": "https://telegra.ph/file/0c5cab3ac6f9543497959.jpg",
                "button1_text": "Button 1",
                "button1_url": "https://t.me/Mod1",
                "button2_text": "Button 2",
                "button2_url": "https://t.me/Mod1",
                "caption": "☠️☠️☠️☠️☠️"
            },
            "mod2": {
                "image_url": "https://telegra.ph/file/8710c559a915747a6622a.jpg",
                "button1_text": "Button 1",
                "button1_url": "https://t.me/Mod2",
                "button2_text": "Button 2",
                "button2_url": "https://t.me/Mod2",
                "caption": "☠️☠️☠️☠️☠️"
            },
            "mod3": {
                "image_url": "https://telegra.ph/file/3c4856c05a00b85599b0b.jpg",
                "button1_text": "Button 1",
                "button1_url": "https://t.me/Mod3",
                "button2_text": "Button 2",
                "button2_url": "https://t.me/Mod3",
                "caption": "☠️☠️☠️☠️☠️"
            },
            "mod4": {
                "image_url": "https://telegra.ph/file/9a743ab324e91f35d3ed8.jpg",
                "button1_text": "Button 1",
                "button1_url": "https://t.me/Mod4",
                "button2_text": "Button 2",
                "button2_url": "https://t.me/Mod4",
                "caption": "☠️☠️☠️☠️☠️"
            },
            "mod5": {
                "image_url": "https://telegra.ph/file/4f17b51c0b5f23b858c7a.jpg",
                "button1_text": "Button 1",
                "button1_url": "https://t.me/Mod5",
                "button2_text": "Button 2",
                "button2_url": "https://t.me/Mod5",
                "caption": "☠️☠️☠️☠️☠️"
            },
            "mod6": {
                "image_url": "https://telegra.ph/file/5c7fa8de5bc22645eb6aa.jpg",
                "button1_text": "Button 1",
                "button1_url": "https://t.me/Mod6",
                "button2_text": "Button 2",
                "button2_url": "https://t.me/Mod6",
                "caption": "☠️☠️☠️☠️☠️"
            },
            "mod7": {
                "image_url": "https://telegra.ph/file/5c7fa8de5bc22645eb6aa.jpg",
                "button1_text": "Button 1",
                "button1_url": "https://t.me/Mod7",
                "button2_text": "Button 2",
                "button2_url": "https://t.me/Mod7",
                "caption": "☠️☠️☠️☠️☠️"
            },
            "mod8": {
                "image_url": "https://telegra.ph/file/5c7fa8de5bc22645eb6aa.jpg",
                "button1_text": "Button 1",
                "button1_url": "https://t.me/Mod8",
                "button2_text": "Button 2",
                "button2_url": "https://t.me/Mod8",
                "caption": "☠️☠️☠️☠️☠️"
            },
            "mod9": {
                "image_url": "https://telegra.ph/file/5c7fa8de5bc22645eb6aa.jpg",
                "button1_text": "Button 1",
                "button1_url": "https://t.me/Mod9",
                "button2_text": "Button 2",
                "button2_url": "https://t.me/Mod9",
                "caption": "☠️☠️☠️☠️☠️"
            },
            "mod10": {
                "image_url": "https://telegra.ph/file/5c7fa8de5bc22645eb6aa.jpg",
                "button1_text": "Button 1",
                "button1_url": "https://t.me/Mod10",
                "button2_text": "Button 2",
                "button2_url": "https://t.me/Mod10",
                "caption": "☠️☠️☠️☠️☠️"
            },
            "obb1": {
                "image_url": "https://telegra.ph/file/5c7fa8de5bc22645eb6aa.jpg",
                "button1_text": "Button 1",
                "button1_url": "https://t.me/Obb1",
                "button2_text": "Button 2",
                "button2_url": "https://t.me/Obb1",
                "caption": "☠️☠️☠️☠️☠️"
            },
            "obb2": {
                "image_url": "https://telegra.ph/file/5c7fa8de5bc22645eb6aa.jpg",
                "button1_text": "Button 1",
                "button1_url": "https://t.me/Obb2",
                "button2_text": "Button 2",
                "button2_url": "https://t.me/Obb2",
                "caption": "☠️☠️☠️☠️☠️"
            },
            "obb3": {
                "image_url": "https://telegra.ph/file/5c7fa8de5bc22645eb6aa.jpg",
                "button1_text": "Button 1",
                "button1_url": "https://t.me/Obb3",
                "button2_text": "Button 2",
                "button2_url": "https://t.me/Obb3",
                "caption": "☠️☠️☠️☠️☠️"
            },
            "obb4": {
                "image_url": "https://telegra.ph/file/5c7fa8de5bc22645eb6aa.jpg",
                "button1_text": "Button 1",
                "button1_url": "https://t.me/Obb4",
                "button2_text": "Button 2",
                "button2_url": "https://t.me/Obb4",
                "caption": "☠️☠️☠️☠️☠️"
            },
            "obb5": {
                "image_url": "https://telegra.ph/file/5c7fa8de5bc22645eb6aa.jpg",
                "button1_text": "Button 1",
                "button1_url": "https://t.me/Obb5",
                "button2_text": "Button 2",
                "button2_url": "https://t.me/Obb5",
                "caption": "☠️☠️☠️☠️☠️"
            },
            "obb6": {
                "image_url": "https://telegra.ph/file/5c7fa8de5bc22645eb6aa.jpg",
                "button1_text": "Button 1",
                "button1_url": "https://t.me/Obb6",
                "button2_text": "Button 2",
                "button2_url": "https://t.me/Obb6",
                "caption": "☠️☠️☠️☠️☠️"
            },
            "obb7": {
                "image_url": "https://telegra.ph/file/5c7fa8de5bc22645eb6aa.jpg",
                "button1_text": "Button 1",
                "button1_url": "https://t.me/Obb7",
                "button2_text": "Button 2",
                "button2_url": "https://t.me/Obb7",
                "caption": "☠️☠️☠️☠️☠️"
            },
            "obb8": {
                "image_url": "https://telegra.ph/file/5c7fa8de5bc22645eb6aa.jpg",
                "button1_text": "Button 1",
                "button1_url": "https://t.me/Obb8",
                "button2_text": "Button 2",
                "button2_url": "https://t.me/Obb8",
                "caption": "☠️☠️☠️☠️☠️"
            },
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
                
