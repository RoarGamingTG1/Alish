import os
import random
from pyrogram import Client, filters

# Bot ke credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# List of specific words and their corresponding dangerous responses
specific_words = {
    "hello": "Khatra hai, mujhse panga mat lena!",
    "game": "Game? Game over hone wala hai tera!",
    "hack": "Hack? Mere jaisa hacker koi aur nahi!",
    "power": "Power? Tere paas kya hai? Main toh power ka baap hoon!",
    "fool": "Fool? Mere saamne mat bol, nahi toh teri khair nahi!",
    "love": "Love? Mere liye sirf destruction hi love hai!",
    "challenge": "Challenge? Mere liye toh ye sirf ek mazaak hai!",
    "secret": "Secret? Mere paas sab secrets hain, teri bhi!",
    "battle": "Battle? Tumhare liye toh ye sirf ek nightmare hoga!",
    "enemy": "Enemy? Mere liye toh tum sabhi enemies ho!",
    "victory": "Victory? Meri toh bas shuruaat hai, abhi toh game khela nahi shuru hua!",
    "defeat": "Defeat? Mere dictionary mein aise words nahi hote!",
    "revenge": "Revenge? Mere pasandeeda hobby hai!",
    "cheat": "Cheat? Mere cheats se teri game ki legitimacy ki death certificate ready hai!",
    "aimbot": "Aimbot? Mere aimbot tera aim barbaad kar dega, jaise tera game!",
    "wallhack": "Wallhack? Teri wallhack ki toh main wallah ho jaunga, bas meri entry hogi!",
    "speedhack": "Speedhack? Mere speed se tu kaise bachega? Tu toh sirf ek speed bump hai mere raaste mein!",
    "teleport": "Teleport? Haan, mere teleport karne se tera destination sirf destruction hoga!",
    "godmode": "Godmode? Mere samne toh tu sirf mortal hai, koi godmode nahi!",
    "bypass": "Bypass? Mere hacks se bypass karne ki koshish mat karna, warna tera bypass kaam nahi karega!"
}


# List of emojis and their corresponding dangerous responses
dangerous_emojis = {
    "😈": "Teri himmat kaise hui mujhse panga lene ki?",
    "🔥": "Agar mujhe gussa dilaya toh teri life ka aakhri din hoga!",
    "💣": "Ye bomb nahi, tera future hai!",
    "🗡️": "Tera game over hone wala hai, chhuri mere haath mein hai!",
    "👿": "Mujhe nafrat hai, aur teri life bhi mujhse nafrat karegi!",
    "🤬": "Shor mat macha, varna tujhe dekh kar main angry hounga!",
    "💀": "Tu toh mar gaya beta, ab bas ghost ban ke ghoomta reh!",
    "🚀": "Ye spaceship nahi, tera crash site hai!",
    "💥": "Ye explosion nahi, tera downfall hai!",
    "🔪": "Chhuri mere haath mein hai, tera end mere control mein hai!",
    "💔": "Ye dil nahi, teri defeat ka dard hai!",
    "💩": "Tu toh ab bas waste material ban gaya hai mere liye!",
    "👻": "Tu toh ab bas ghost ban ke ghoom raha hai, teri gaming ki soul chheen li gayi hai!",
    "☠️": "Ab tu toh sirf ek skull hai mere liye, teri game over ki indication!",
    "🧨": "Ye dynamite nahi, teri gaming career ka blast hai!",
    "🔫": "Trigger mere haath mein hai, teri gaming ki death certificate ready hai!",
    "💀": "Tu toh ab bas ek skeleton hai, teri gaming ka dead end hai!",
    "🪓": "Ye axe nahi, teri gaming ki executioner hai, tu toh chop ho gaya!",
    "🤡": "Tu toh ab bas ek joke hai mere liye, teri gaming ki comedy ka chapter closed hai!",
    "👹": "Tere saamne toh main hi devil hoon, teri gaming ka shaitani end hai!"
}


# Bot ko create karein
Bot = Client(
    "ChatBot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

# Message handler
@Bot.on_message()
async def chat(bot, update):
    # Extract message text
    message_text = update.text.lower()

    # Check if any specific word is present in the message
    for word in specific_words.keys():
        if word in message_text:
            await respond_dangerously(bot, update)
            return

    # Check if any dangerous emoji is present in the message
    for emoji in dangerous_emojis.keys():
        if emoji in message_text:
            await respond_with_emoji(bot, update, emoji)
            return

# Function to respond with a dangerous message
async def respond_dangerously(bot, update):
    # Select a random dangerous response
    response = random.choice(list(specific_words.values()))
    await update.reply_text(response)

# Function to respond with a dangerous message using emoji
async def respond_with_emoji(bot, update, emoji):
    # Get the dangerous response corresponding to the emoji
    response = dangerous_emojis.get(emoji, "Kuch toh gadbad hai, mujhe samajh nahi aa raha.")
    await update.reply_text(response)

# Bot ko run karein
Bot.run()
    
