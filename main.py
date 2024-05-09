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
    "revenge": "Revenge? Mere pasandeeda hobby hai!"
}
sp_words = {
    "aimbot": "Aimbot? Mere shots itne accurate hote hain ki tu sochega aimbot chal raha hai!",
    "wallhack": "Wallhack? Mere saamne tu khud hi wall ho jaayega, teri positioning se hi pata chal jaata hai!",
    "speedhack": "Speedhack? Mere reflexes itne fast hain ki tu saare speedhackers slow motion mein dikhne lagega!",
    "teleport": "Teleport? Mere sath khel ke tu khud hi dusre server pe pahunch jayega!",
    "godmode": "Godmode? Mere paas 'mad mode' hai, jisme tu bas mad hi ho jayega!",
    "cheat": "Cheat? Mere saamne tu khud cheat sheet ban jaayega, jaise koi quiz ka paper solve kar raha ho!",
    "hack": "Hack? Haan, main Mad bhai hoon! Mere hacks se tera game over hone wala hai, jaise kabhi shuru hi nahi hua!",
    "bypass": "Bypass? Mere hacks se bypass karne ki koshish mat karna, warna tera bypass kaam nahi karega!",
    "exploit": "Exploit? Mere liye toh teri gaming hi ek exploit hai!",
    "mod": "Mod? Mere paas toh sab mod ke mods hain, tu bas dekh raha reh!",
    "script": "Script? Mere paas itni saari scripts hain, ki tu confuse ho jaayega kis se bachega!",
    "tool": "Tool? Mere toolkit mein sab kuch hai, teri bhi ulti ginti shuru ho gayi!",
    "ban": "Ban? Mere paas koi ban nahi, bas teri gaming ki band bajane ke liye sab kuch!"
}
# List of emojis and their corresponding dangerous responses
dangerous_emojis = {
    "😈": "Teri himmat kaise hui mujhse panga lene ki?",
    "🔥": "Agar mujhe gussa dilaya toh teri life ka aakhri din hoga!",
    "💣": "Ye bomb nahi, tera future hai!",
    "🗡️": "Tera game over hone wala hai, chhuri mere haath mein hai!",
    "👿": "Mujhe nafrat hai, aur teri life bhi mujhse nafrat karegi!",
    "🤬": "Shor mat macha, varna tujhe dekh kar main angry hounga!",
    "💀": "Tu toh mar gaya beta, ab bas ghost ban ke ghoomta reh!"
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
    
