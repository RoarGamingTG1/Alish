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
async def reply_to_mod_messages(client, message):
    question = message.text.lower()
    trigger_words = ["mod1", "mod2", "mod3", "mod4", "mod5", "mod6", "mod7", "mod8", "mod9", "mod10"]
    for word in trigger_words:
        if word in question:
            image_url = f"https://example.com/{word}.jpg"
            button1_text = "Button 1"
            button1_url = f"https://t.me/{word}1"
            button2_text = "Button 2"
            button2_url = f"https://t.me/{word}2"
            caption = "Mod caption"

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

# Function to handle user questions and provide answers for obb trigger words
async def reply_to_obb_messages(client, message):
    question = message.text.lower()
    trigger_words = ["obb1", "obb2", "obb3", "obb4", "obb5", "obb6", "obb7", "obb8", "obb9", "obb10"]
    for word in trigger_words:
        if word in question:
            image_url = f"https://example.com/{word}.jpg"
            button1_text = "Button 1"
            button1_url = f"https://t.me/{word}1"
            button2_text = "Button 2"
            button2_url = f"https://t.me/{word}2"
            caption = "obb caption"

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

# Function to handle user questions and provide answers for Key trigger words
async def reply_to_key_messages(client, message):
    question = message.text.lower()
    if "key" in question:
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

# Function to handle user questions and provide answers for non-trigger words
async def reply_to_non_trigger_messages(client, message):
    if message.text.lower() == "hi":
        sent_message = await message.reply_text("Hello 👋.")
    elif message.text.lower() == "how are you":
        sent_message = await message.reply_text("Men Thik hon Ap Sunao 👻 🫥.")
        elif message.text.lower() == "Gf banogi":
        sent_message = await message.reply_text("Pyasy insan Men ayk Bot hon or AtangWadion Ki koi prem kahni Nhi hoti 😡😡.")
        elif message.text.lower() == "rose":
        sent_message = await message.reply_text("rose 🌹 tang nhi kro nhi To ban Kardongi 🤬.")
    elif message.text.lower() == "Fash speed":
        sent_message = await message.reply_text("Itni Speed 🚄 Ka kia krna hai.")
    else:
        # Handle other non-trigger word messages here
        pass
    
    # Wait for 30 seconds before deleting the message
    await asyncio.sleep(30)

    # Delete the sent message
    await sent_message.delete()
    
# Function to send threatening reply with random dangerous messages
async def send_dangerous_reply(message):
    dangerous_messages = [
        "ab tera time khatam! 💣💥",
        "tere liye special surprise hai mere pass! 🎁🔥",
        "aaj teri band bajne wali hai! 🎶🔪",
        "yahaan tera swagat hai! 🕶️🔫",
        "tu kab sudhrega? Kabhi nahi! 😈👿",
        "mere aage tu kuch bhi nahi! hai 🦾🔪",
        "tu mujhse panga le raha hai? Bad idea! 💀🔥",
        "tera ant aaya hai! 😈👻",
        "aaj raat teri neend uda doongi! 💤🚫",
        "tera time up! ⏰💀",
        "mujhe nafrat hai teri muskurahat se! 😡😈",
        "ab tujhe koi nahi bacha sakta! 👹🔥",
        "meri raah mein aane ki sazaa tuje bhugatni padegi! 😈🔪",
        "main teri zindagi se sab kuch cheen loongi! 💀👿",
        "tere sapne ab mera ho gaye hain! 😈💭",
        "ab tu mere control mein hai! 🎮🤖",
        "tujhe bachane ki koi jagah nahi hai! 🚫🤬",
        "teri zindagi ab meri mutthi mein hai! 👊😈",
        "meri bheer tujhe kuchal degi! 😠👣",
        "ab tu sirf mera khilona hai! 🧸😈",
        "main teri zindagi se har khushi cheen loongi! 😈🎭",
        "tera ant ab mera shuruwaat hai! 💥🔥",
        "mere aane se teri zindagi andheri ho gayi hai! 🌑😈",
        "tujhe paagal kar doongi! 😵🌀",
        "ab tera ant aaya hai! 💀🔚",
        "mere hath mein tera jaanaza hai! ⚰️😈",
        "main tujhe daraane wali nahi, sachai batane walj hoon! 😈💬",
        "ab tu sirf mera rogi hai! 🤒🔥",
        "mere bina tu adhoora hai! 😈❌",
        "ab tu mujhse bach nahi sakta! 🏃‍♂️🔪",
        "meri ghatak shakti se tu nahi bach sakta! 💥🔥",
        "ab teri zindagi ka anth kar doongi! 🏁😈",
        "main teri zindagi ko barbaad kar doongi! 💣💔",
        "ab tu mere gulam hai! 👑😈",
        "mere saamne tu kuch nahi! 🚫👀",
        "mere liye tu ek chunaavi maatra hai! 🗳️😈",
        "mere bina teri zindagi adhoori hai! 😈🔄",
        "ab tera antim samay hai! omphat suha ha ⌛😱",
        "meri raftar se teri bhagti jindagi ab khatam! hojayegi 🏎️🔥",
        "mere aane se teri raaton mein andhera chha gaya hai! 🌑😈",
        "ab teri zindagi mein andhera chha gaya hai! 🌚🔥",
        "teri zindagi ab mere haath mein hai! 🖐️😈",
        "ab tu sirf mera khel hai! 🎲😈",
        "main teri zindagi ki director hoon! 🎬😈",
        "mere bina tu adhoora hai! Sachi 😈❌",
        "ab tu sirf mera puppet hai! 🎭🔥",
        "mere saath khelne ki himmat hai tujhme? 😈🃏",
        "main teri zindagi ki villain hoon! 😈🎥",
        "ab tu mere control mein hai! 🕹️🔒",
        "meri duniya mein ab tuje jagah nahi hai! 🌎🔚",
        "main teri zindagi ka dictator hoon! 👮‍♂️😈"
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
    # Check for each set of trigger words and respond accordingly
    await reply_to_mod_messages(client, message)
    await reply_to_obb_messages(client, message)
    await reply_to_key_messages(client, message)
    
    # Handle non-trigger word messages
    await reply_to_non_trigger_messages(client, message)
# Check for trigger words
        trigger_words = ["hi", "hello", ,"kia"," bro"]
        for word in trigger_words:
            if word in question:
                await send_dangerous_reply(message)
                break
# Run the bot
app.run()
        
