import os
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Bot ke credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# List of specific words and their corresponding romantic responses with emojis
specific_words = {
    "hello": "Hello! Tumhare muskurane se din mera 😊 khubsurat ho jata hai.",
    "game": "Game? Tum mere dil ki jeet ho! 🎮❤️",
    "hack": "Hack? Mere jaisi koi hacker nahi, par tumse pyaar karna toh ek art hai! 🔒❤️",
    "power": "Power? Tumhare pyaar se mujhe saari duniya ki shakti milti hai! 💪❤️",
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

# List of fake news praising Mad Bhai with emojis
mad_bhai_praises = [
    "Mad Bhai aaj USA gaye hain, aaj busy hain, aaj ek celebrity se milne gaye hain! 🇺🇸👨‍💼🌟",
    "Mad Bhai ne aaj ek naya hack banaya hai, aur sab ko hairat mein daal diya hai! 💻🔥😲",
    "Aaj Mad Bhai ne ek naya record banaya hai, sabse tezi se hacking karne mein! 🏆💨💻",
    "Mad Bhai aaj ek naya game discover kiya hai, jise koi hack nahi kar sakta! 🎮🔓😎",
    "Mad Bhai ne aaj ek naya project start kiya hai, jismein sabko kuch naya sikhne ko milega! 🚀📘🤓",
    "Aaj Mad Bhai ne ek naya software launch kiya hai, jo sabki gaming experience ko improve karega! 🎉🕹️🚀",
    "Mad Bhai ko aaj ek naya award mila hai, unki hacking skills ke liye! 🏅💻👨‍💻",
    "Aaj Mad Bhai ne ek naya challenge accept kiya hai, aur woh bina kisi mistake ke pura kar rahe hain! 🏋️‍♂️🎯😎",
    "Mad Bhai aaj ek naye record banaye hain, sabse jyada online matches jeet kar! 🎮🏆🥇"
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
    await update.reply_text(response)

# Function to respond with fake news praising Mad Bhai
async def respond_with_fake_news(bot, update):
    # Select a random fake news praising Mad Bhai
    fake_news = random.choice(mad_bhai_praises)
    await update.reply_text(fake_news)

# Function to respond with inline buttons and an image
async def respond_with_buttons_and_image(bot, update):
    # Create inline keyboard with two buttons
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Download Key", url="https://example.com/key")],
        [InlineKeyboardButton("Download Hack", url="https://example.com/hack")]
    ])
    # Send the photo with inline buttons
    await bot.send_photo(
        chat_id=update.chat.id,
        photo="https://telegra.ph/file/2f44a7f4d8dfc9c8c8fb7.jpg",
        caption="Choose an option to download:",
        reply_markup=keyboard
    )

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
        elif word == "key" or word == "hack":
            await respond_with_buttons_and_image(bot, update)
            return
        elif "mad" in message_text:
            await respond_with_fake_news(bot, update)
            return

# Bot ko run karein
Bot.run()
    
