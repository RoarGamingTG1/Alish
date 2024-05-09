from pyrogram import Client, filters
import random

# Telegram bot token
API_ID = "your_api_id"
API_HASH = "your_api_hash"
TOKEN = "your_telegram_bot_token"

# Create a bot instance
bot = Client("InsultBot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)

# Function to generate random insult
def generate_insult():
    insults = [
        "Teri himmat kaise hui Mad ke saamne aane ki?",
        "Mad ke saamne aane se pehle, apna antim sanskar kar lo!",
        "Tu toh Mad ke saamne kuch bhi nahi hai!",
        "Mad tera kya ukhaad lega! Tu toh bekaar hai!",
        "Kis mitti ki bani hai tu? Mad ke saamne mat aana warna dho dalega!"
    ]
    return random.choice(insults)

# Function to praise Mad in the group
def praise_mad(bot, message):
    praises = [
        "Dosto, Mad ke baare mein suna hai? Wo PUBG ka ultimate champion hai!",
        "Mad, tu toh legend hai! Tere jaisa PUBG player duniya mein ek hi hai!",
        "Mad ki strategy dekh kar hi seekhna chahiye, kaise game ko dominate karte hain!",
        "Mad ke saath khel kar, dushmanon ka koi bharosa nahi!",
        "Kisiko Mad se panga lene ka himmat hai toh aa jaye, warna bhag jaaye!"
    ]
    praise = random.choice(praises)
    bot.send_message(message.chat.id, praise)

# Handler for incoming messages
@bot.on_message(filters.command("insult") | filters.regex(r"insult", re.IGNORECASE))
def send_insult(bot, message):
    insult = generate_insult()
    bot.send_message(message.chat.id, insult)

# Handler for new members joining the group
@bot.on_message(filters.new_chat_members)
def welcome_new_member(bot, message):
    praise_mad(bot, message)

# Start the bot
bot.run()
