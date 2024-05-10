import os
import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

# Bot credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# Create Pyrogram client
app = Client("WormGPT_Bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Dictionary containing dangerous messages and their associated keywords
dangerous_messages = {
    "⚠️ Mad bhai ke hatters, tumhari kismat aaj tumhare saath hai!": ["🍀 Good Luck", "🎁 Special Surprise", "⬇️ Download"],
    "⚠️ Aaj Mad bhai ne tere naam ka ek special surprise bheja hai!": ["🎉 Special Day", "🎁 Surprise Gift", "⬇️ Get Now"],
    "⚠️ Mad bhai ki permission ke bina kisi ke paas jana ab khatra hai!": ["🔒 No Entry", "⚠️ Danger Ahead", "🔗 Go to Link"],
    "⚠️ Mad bhai ke hatters, aaj ka din tumhare liye khaas hai!": ["🔑 Key to Success", "📅 Special Day", "🎉 Celebration"],
    "⚠️ Aaj Mad bhai ne tumhare liye ek naya surprise tayaar kiya hai!": ["🆕 New Update", "🎁 Exciting Surprise", "🔧 Check Now"],
    "⚠️ Mad bhai ke hatters, ab tumhari aukaat aane wali hai!": ["📈 Status Check", "⚠️ Beware", "🛠️ Tool Required"],
    "⚠️ Mad bhai ki permission ke bina kisi ko hack karna, ab tumhari jaan ko khatra hai!": ["💻 Hack Alert", "⚠️ Danger Alert", "💾 Download Software"],
    "⚠️ Mad bhai ke hatters, aaj se tumhare liye bura waqt shuru hua hai!": ["📉 Bad Time", "⏰ Alarm", "📚 Tutorial Required"],
    "⚠️ Aaj se Mad bhai ke hatters, tumhare peeche nahi, tumhare saamne bhaagna shuru karo!": ["🏃‍♂️ Run Now", "⚠️ Emergency", "🔄 Program Check"],
    "⚠️ Mad bhai ke hatters, aaj ka din tumhare liye nightmare banne wala hai!": ["😱 Nightmare Ahead", "⚠️ Danger Zone", "💻 Code Check"],
    "⚠️ Mad bhai ki permission ke bina kisi ke hack ka key share karna, ab tumhari maut ka faisla hai!": ["🔄 Share Alert", "⚠️ Virus Alert", "🦠 Virus Warning"]
}

# Additional dangerous messages, keywords, links, and images
additional_dangerous_messages = {
    "⚠️ Danger ahead! Proceed with caution!": ["⚠️ Caution Ahead", "⚠️ Warning Alert", "⚠️ Danger Alert"],
    "⚠️ Beware! Mad bhai is watching you!": ["👀 Beware", "🔍 Surveillance Alert", "⚠️ Eye on You"],
    "⚠️ Enter at your own risk!": ["⚠️ Risky Entry", "⬅️ Enter at Own Risk", "⚠️ Danger Zone"],
    "⚠️ Danger zone detected!": ["⚠️ Danger Zone", "🔍 Detect Zone", "📍 Detected Area"],
    "⚠️ Intruder alert!": ["⚠️ Intruder Alert", "🚨 Warning", "🔒 Security Alert"],
    "⚠️ Trespassers will be prosecuted!": ["⚠️ Trespass Alert", "⚖️ Prosecution", "🚔 Legal Action"],
    "⚠️ Unauthorized access detected!": ["⚠️ Unauthorized Entry", "🔑 Access Denied", "🔍 Detect Unauthorized"],
    "⚠️ Security breach detected!": ["⚠️ Security Breach", "🔒 Security Alert", "💻 Hack Alert"],
    "⚠️ Danger! Keep out!": ["⚠️ Keep Out", "⚠️ Danger Ahead", "⛔️ Warning"],
    "⚠️ You have been warned!": ["⚠️ You're Warned", "⚠️ Caution", "🔔 Warning"]
}

# Combine both dictionaries
dangerous_messages.update(additional_dangerous_messages)

# Create a list of keywords from the combined dictionary
keywords = [keyword.split()[1] for keywords_list in dangerous_messages.values() for keyword in keywords_list]

# Function to delete messages after 3 seconds
async def delete_message(message):
    await asyncio.sleep(3)
    await message.delete()

# Function to send dangerous reply with random dangerous messages and inline buttons
async def send_dangerous_reply(message):
    # Choose a random message from the dictionary
    reply = random.choice(list(dangerous_messages.keys()))
    # Get the keywords associated with the chosen message
    reply_keywords = dangerous_messages[reply]
    # Create inline buttons based on the keywords
    inline_buttons = []
    for keyword in reply_keywords:
        button_name = keyword.split()[1]
        inline_buttons.append(InlineKeyboardButton(keyword, url=f"https://vt.tiktok.com/ZSYJrR8U2//{TIKTOK"))
    keyboard = InlineKeyboardMarkup([inline_buttons])
    # Add the URL of the image to be attached
    media = InputMediaPhoto(media="https://telegra.ph/file/2f44a7f4d8dfc9c8c8fb7.jpg")
    await message.reply_media_group(media=[media], reply_markup=keyboard, caption=reply)

# Function to reply with image and inline buttons based on keywords in the message
async def reply_with_image_and_buttons(client, message):
    # Check if any keyword is present in the message
    for keyword in keywords:
        if keyword in message.text.lower():
            # Create inline buttons based on the keyword
            inline_buttons = []
            for keyword_message in dangerous_messages:
                if keyword in dangerous_messages[keyword_message]:
                    inline_buttons.append(InlineKeyboardButton(keyword_message.split()[0], url=f"https://www.instagram.com/reel/C6sPCS5oPn6/?igsh=MXV2b3Z6cmhmaGNrbA==/{insta}"))
            keyboard = InlineKeyboardMarkup([inline_buttons])
            # Add the URL of the image to be attached (use a different image for each keyword)
            media = InputMediaPhoto(media=f"https://telegra.ph/file/8710c559a915747a6622a.jpg{insta}_image.jpg")
            await message.reply_media_group(media=[media], reply_markup=keyboard)
            break  # Exit loop after replying to the first keyword found

# Filter messages containing trigger words
@app.on_message(filters.text & ~filters.me)
async def reply_to_trigger_words(client, message):
    # Check if any keyword is present in the message
    if any(keyword in message.text.lower() for keyword in keywords):
        await send_dangerous_reply(message)
    else:
        await reply_with_image_and_buttons(client, message)

# Run the bot
app.run()
        
