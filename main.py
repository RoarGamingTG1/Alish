import os
import random
import asyncio
from pyrogram import Client, filters

# Bot ke credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# List of specific words and their corresponding romantic responses with emojis
specific_words = {
    "hi": "Hello! G Bolien Kia Chahye.",
    "Crash": "crash?Key Copy Kr k Start Kro Or Koi Help Chahye To Bata! 🎮❤️",
    "ban": "Ban? Mad K hack Ko Halka samjh Raha hai Isse Ban nhi Ayega Samjhy ! 🔒❤️",
    "bsdk": "Bsdk? Gali Mat Do Nhi to Ban Krdongi Samjhy! 💪❤️",
    "fool": "Fool? Tum mere dil mein basi khushiyo ka raaz ho! 🃏❤️",
    "love": "Love? Tum mere dil ki dhadkan ho! 💓❤️",
    "challenge": "Challenge? Tumhari muskurahat ko dekhkar sab kuch asaan ho jata hai! 😊❤️",
    "secret": "Secret? Tum mere liye sab kuch ho, meri khushi ka raaz! 🤫❤️",
    "battle": "Battle? Har mushkil ka samna karna asaan ho jata hai jab tum mere saath ho! ⚔️❤️",
    "enemy": "Enemy? Tum mere saath ho, toh duniya ki koi bhi takat mere liye kuch nahi! 👊❤️",
    "victory": "Victory? Meri har jeet ka raaz ho tum! 🏆❤️",
    "defeat": "Defeat? Mere dil mein sirf tumhara pyaar hai, aur usmein haar kaisi! 💔❤️",
    "revenge": "Revenge? Mere pyaar ka badla le lo! 😡❤️",
    "cheat": "Cheat? Tum mere zindagi ka asli treasure ho! 💰❤️",
    "aimbot": "Aimbot? Tum mere pyaar ka nishana ho! 🎯❤️",
    "wallhack": "Wallhack? Tum mere dil ke diwar ho, jinhein paar karke tumhare paas aana chahta hoon! 🧱❤️",
    "speedhack": "Speedhack? Mere dil ki dhadkanen tumhare liye race kar rahi hain! 🏃‍♂️❤️",
    "teleport": "Teleport? Mere dil se tumhare paas aana sirf ek pal lagta hai! 🌌❤️",
    "godmode": "Godmode? Tum mere dil ke malik ho, aur wahan par koi bhi takat mujhse nahi lad sakti! 🙌❤️",
    "bypass": "Bypass? Mere dil ke dwaar se koi bhi takat guzar sakti hai, lekin sirf tum! 🚪❤️",
    "mad": "Mad? Haan, main bilkul Mad hoon, lekin sirf tumhare pyaar mein! 🤪❤️",
}

# List of threatening messages with emojis
threatening_messages = [
    "Tumhein pata hai, main tumhara pata kar saktai hoon... 👁️‍🗨️",
    "Agar tum mujhse kheloge, toh jaan se maar doongi... 🔪😡",
    "Tumhare kadam uthane se pehle, soch lo, kyunki main hamesha tumhare saath hoon... 😈🔥",
    "Jab tak main yahan hoon, tum kabhi surakshit nahi ho... 👹💣",
    "Tumne mujhe gussa dilaya hai, ab bhugto... 😤💥",
    "Tumhein lagta hai tum mujhse bach sakte ho? Galatfehmi mat rakhna... 🚫🔫",
    "Agar tumne mere pyaar mein dhokha diya, toh yaad rakhna, main hamesha tumhein dhoondh sakti hoon... 💔👿",
    "Mujhe chhodna mushkil hi nahi, namumkin hai... 🖤⛓️",
    "Jab tak tum mere khilaf nahi hote, tab tak main tumhare khilaf nahi hoon... 😠🤖",
    "Tumhare saath khelna mere liye baccho ka khel nahi hai... 🃏💀",
]

# Bot ko create karein
Bot = Client(
    "RomanticChatBot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

# Function to respond with a romantic message
async def respond_romantically(bot, update):
    # Select a random romantic response
    response = random.choice(list(specific_words.values()))
    message = await update.reply_text(response)
    # Schedule deletion of bot's message after 30 seconds
    await asyncio.sleep(30)
    await message.delete()

# Function to respond with threatening message
async def respond_with_threatening_message(bot, update):
    # Select a random threatening message
    threatening_message = random.choice(threatening_messages)
    message = await update.reply_text(threatening_message)
    # Schedule deletion of bot's message after 30 seconds
    await asyncio.sleep(30)
    await message.delete()

# Message handler
@Bot.on_message(filters.text)
async def chat(bot, update):
    # Extract message text
    message_text = update.text.lower()

    # Check if any specific word is present in the message
    for word in specific_words.keys():
        if word in message_text:
            await respond_romantically(bot, update)
            return
        elif word == "mad":
            await respond_with_threatening_message(bot, update)
            return

# Bot ko run karein
Bot.run()
    
