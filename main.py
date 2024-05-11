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

# Function to handle user questions and provide answers for Mod trigger words
async def reply_to_mod_messages(message):
    question = message.text.lower()
    trigger_responses = {
        "mod": {
            "caption": "Caption for Mod",
            "button1_text": "Button 1",
            "button1_url": "https://t.me/Mod1",
            "button2_text": "Button 2",
            "button2_url": "https://t.me/Mod2",
            "image_url": "https://telegra.ph/file/0c5cab3ac6f9543497959.jpg"
        },
        "obb": {
            "caption": "Caption for Obb",
            "button1_text": "Button 1",
            "button1_url": "https://t.me/Obb1",
            "button2_text": "Button 2",
            "button2_url": "https://t.me/Obb2",
            "image_url": "https://telegra.ph/file/8710c559a915747a6622a.jpg"
        },
        "ali": {
            "caption": "Caption for Key",
            "button1_text": "Button 1",
            "button1_url": "https://t.me/Mod1",
            "button2_text": "Button 2",
            "button2_url": "https://t.me/Mod1",
            "image_url": "https://telegra.ph/file/f6be52baa496065e85862.jpg"
        },
        # Add more trigger words with their respective details
    }
    for word, details in trigger_responses.items():
        if word in question:
            caption = details["caption"]
            button1_text = details["button1_text"]
            button1_url = details["button1_url"]
            button2_text = details["button2_text"]
            button2_url = details["button2_url"]
            image_url = details["image_url"]

            # Create inline keyboard with two buttons
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(button1_text, url=button1_url),
                        InlineKeyboardButton(button2_text, url=button2_url)
                    ]
                ]
            )

            # Reply with the caption, image, and inline keyboard
            sent_message = await message.reply_photo(
                photo=image_url,
                caption=caption,
                reply_markup=reply_markup
            )

            # Wait for 30 seconds before deleting the message
            await asyncio.sleep(30)

            # Delete the sent message
            await sent_message.delete()
            
            # Function to send threatening reply with random dangerous messages
async def send_sms_reply(message):
    sms_messages = [
        "Mujhe Lagta hai ab tera time khatam Hony wala hai!  💣💥",
        "tere liye special surprise hai @M3xecv Ko inbox Kr! 🎁🔥",
        "aaj teri band bajne wali hai Mere Hathon se ! 🎶🔪",
        "yahaan tera swagat hai! 🕶️🔫",
        "tu kab sudhrega? Kabhi nahi! 😈👿",
        "mere aage tu kuch bhi nahi! hai Chota sa bacha hai Kaat Dalongi 🦾🔪",
        "tu mujhse panga le raha hai? Bad idea Hai Tera! 💀🔥",
        "tera ant aaya hai! Tb Hi Tu aysi Harkten kr raha hai 😈👻",
        "aaj raat teri neend uda doongi Kaly Jadu se ! 💤🚫",
        "tera time up! So ja Nhi To Pitega ⏰💀",
        "mujhe nafrat hai teri muskurahat se! 😡😈",
        "ab tujhe koi nahi bacha sakta Kalo Shakti se ! 👹🔥",
        "meri raah mein aane ki sazaa tuje bhugatni padegi Tujhe Marna Padega! 😈🔪",
        "main teri zindagi se sab kuch cheen loongi! Afsos Krega apni jindgi Par 💀👿",
        "tere sapne ab mera ho gaye hain! Rat Ko Ayse Bhyank Sapne Foreword krongi So bhi nhi Payega 😈💭",
        "ab tu mere control mein hai Kaan bhi Khench Sakti ho Tere ! 🎮🤖",
        "tujhe bachane ki koi jagah nahi hai!  Tu avash Marega 🚫🤬",
        "teri zindagi ab meri mutthi mein hai! 👊😈",
        "meri bheer tujhe kuchal degi Jayse turck k  🍌! 😠👣",
        "ab tu sirf mera khilona hai paan paan po po Chal Mere Ghore Hindustan! 🧸😈",
        "main teri zindagi se har khushi cheen loongi or Teri GF ka chakr Kisi or K sath Chlwa dongi  ! 😈🎭",
        "tera ant ab mera shuruwaat hai! 💥🔥",
        "mere aane se teri zindagi andheri ho gayi hai Dark Horror ! 🌑😈",
        "tujhe paagal kar doongi Kameny Galian Mat Dya kar! 😵🌀",
        "ab tera ant aaya hai isi lye To ayse  word Use kr raha hai! 💀🔚",
        "mere hath mein tera jaanaza hai! ⚰️😈 Qabirstan Door hai",
        "main tujhe daraane wali nahi, sachai batane wali hoon k Tu bada Kamena insaan hai! 😈💬",
        "ab tu sirf mera Shikar Hai hai! 🤒🔥",
        "mere bina tu adhoora hai men Tumhara saya hon! 😈❌",
        "ab tu mujhse bach nahi sakta! 🏃‍♂️🔪",
        "meri ghatak shakti se tu nahi bach sakta! 💥🔥",
        "ab teri zindagi ka anth kar doongi! 🏁😈",
        "main teri zindagi ko barbaad kar doongi! 💣💔",
        "ab tu mere gulam hai! 👑😈",
        "mere saamne tu kuch nahi! 🚫👀",
        "mere liye tu ek chunaavi maatra hai! 🗳️😈",
        "ab tera antim samay hai! omphat suha ha ⌛😱",
        "meri raftar se teri bhagti jindagi ab khatam! hojayegi 🏎️🔥",
        "mere aane se teri raaton mein andhera chha jayega! 🌑😈",
        "ab teri zindagi mein andhera chha gaya hai! 🌚🔥",
        "teri zindagi ab mere haath mein hai! 🖐️😈",
        "ab tu sirf mera khel hai! 🎲😈",
        "main teri zindagi ki director hoon! 🎬😈",
        "ab tu sirf mera puppet hai! 🎭🔥",
        "mere saath khelne ki himmat hai tujhme?  barbaad krdongi tujhe 😈🃏",
        "main teri zindagi ki villain hoon! the end you wil daye 😈🎥",
        "ab tu mere control mein hai! 🕹️🔒",
        "meri duniya mein ab tuje jagah nahi hai! 🌎🔚",
    ]

    reply = random.choice(sms_messages)
    sent_message = await message.reply_text(reply)

    # Wait for 30 seconds before deleting the message
    await asyncio.sleep(30)

    # Delete the sent message
    await sent_message.delete()

# Function to handle user messages and send threatening replies
@app.on_message(filters.text & ~filters.me)
async def handle_messages(client, message):
    question = message.text.lower()
    trigger_words = ["bsdk", "ban", "harami", "kuta"]
    for word in trigger_words:
        if word in question:
            await send_sms_reply(message)
            break

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
        await reply_to_mod_messages(message)

    # Wait for 30 seconds before deleting the message
    await asyncio.sleep(30)

    # Delete the sent message
    await sent_message.delete()

# Run the bot
app.run()
            
