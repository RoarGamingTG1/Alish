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
    await message.reply_text(reply)

# Filter messages containing trigger words
@app.on_message(filters.text & ~filters.me)
async def reply_to_trigger_words(client, message):
    trigger_words = ["mad", "mad bhi", "mad bro"]
    for word in trigger_words:
        if word in message.text.lower():
            await send_dangerous_reply(message)
            break


async def send_dangerous_reply(message):
    dangerous_messages = [...]
    reply = random.choice(dangerous_messages)
    sent_message = await message.reply_text(reply)
    # Wait for 30 seconds before deleting the message
    await asyncio.sleep(30)
    # Delete the sent message
    await sent_message.delete()
    
# Run the bot
app.run()
