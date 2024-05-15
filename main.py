import os
import random
import asyncio
import sqlite3
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Bot credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# Create Pyrogram client
app = Client("WormGPT_Bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Connect to the SQLite database
conn = sqlite3.connect('points.db')
c = conn.cursor()

# Create table to store users and their points
c.execute('''CREATE TABLE IF NOT EXISTS users (
             user_id TEXT PRIMARY KEY,
             points INTEGER DEFAULT 0)''')
conn.commit()

# Function to send threatening reply with random dangerous messages
async def send_dangerous_reply(message):
    dangerous_messages = [
               "Mad bhai ek asli legend hain!",
      
        
    ]

    reply = random.choice(dangerous_messages)
    sent_message = await message.reply_text(reply)

    # Wait for 30 seconds before deleting the message
    await asyncio.sleep(30)

    # Delete the sent message
    await sent_message.delete()

# Function to send random reply for specific trigger words
async def send_random_reply(message):
    random_messages = [
        "Teri toh! 😡",
        "Kaun banaya tujhe? 😠",
        "Tere muh me ghee shakkar! 😤",
   
    ]

    reply = random.choice(random_messages)
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
            "caption": "StarModz Optimised Version No Crash and Fully SmoothSupport Android 9-14 (64 Bit)",
            "button1_text": "Mod Download ✅",
            "button1_url": "https://t.me/StarModz/4224",
            "button2_text": "Obb Download 🌟",
            "button2_url": "https://t.me/StarModz/4222",
            "image_url": "https://telegra.ph/file/46cc2a2050e7b04c5be5a.jpg"
        },
        "keyshshshdbbdbndbdbdbhdhd": {
            "caption": "Key Finding Latest Method How to find key! Key kaise nikaalen Watch Full VideoAnd find key by own very Poora Video dekho or badi asaani se khud key nikaalo",
            "button1_text": "Watch Video 📷 ",
            "button1_url": "https://t.me/StarModTG/351507",
            "button2_text": "Kew Download 👿",
            "button2_url": "http://firebaseapiserviceforkrafton.in",
            "image_url": "https://telegra.ph/file/3a311980fa4e66d8e0d52.jpg"
        },
        "ali": {
            "caption": "Contact Owners",
            "button1_text": "M3xecv ✅",
            "button1_url": "https://t.me/M3xecv",
            "button2_text": "Mad Bhai 👻",
            "button2_url": "https://t.me/Mad_Owner",
            "image_url": "https://telegra.ph/file/f2255a9405dc64d0819e8.jpg"
        },
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
            break

# Function to send specific message for a specific user
async def send_specific_reply(message):
    # Extracting username from the message
    username = message.from_user.username
    
    # Check if the username matches the specific username
    if username == "@M3xecv":
        # List of 10 specific messages
        specific_messages = [
            "Hello @M3xecv! This is a specific message for you ❤️🌟.",
            "Hey @M3xecv, just wanted to say hi!",
        ]
        
        # Selecting a random message from the list
        specific_message = random.choice(specific_messages)
        
        # Send the selected message
        sent_message = await message.reply_text(specific_message)

        # Wait for 30 seconds before deleting the message
        await asyncio.sleep(30)

        # Delete the sent message
        await sent_message.delete()

# Function to handle messages related to love, poetry, politics, sports, Bollywood, and Hollywood
async def handle_general_messages(message):
    general_messages = {
        "girlfriend": [
            "Love is the essence of life, a melody that fills the heart with joy and warmth! ❤️🎵",
            "In the tapestry of life, love is the thread that binds hearts together in a timeless embrace! 💞✨",
            "True love knows no bounds, transcending time and space to unite souls in a bond that lasts forever! 💖💫",
        ],
        "poetry": [
            "Poetry is the language of the soul, painting emotions with words that dance upon the page! ✍️📖",
            "In the realm of poetry, every verse is a journey into the depths of human experience, a reflection of the beauty and complexity of life! 🌹📜",
            "Through the power of poetry, hearts connect across distances, finding solace in the rhythm of shared emotions! 🌌❤️",
        ],
        "politics": [
            "Politics is the art of governance, where ideas clash and visions shape the destiny of nations! 🏛️🌐",
            "In the arena of politics, every decision has the power to change the course of history! 📜🗳️",
            "The heartbeat of democracy is the voice of the people, resonating through the corridors of power! 🗣️🏛️",
        ],
        "sports": [
            "Sports is the arena where champions are forged, and dreams take flight! 🏆🚀",
            "In the world of sports, every victory is a testament to the power of dedication, perseverance, and teamwork! 🥇🤝",
            "The thrill of competition, the adrenaline rush of the game – sports is the ultimate test of skill and spirit! ⚽🏀",
        ],
        "bollywood": [
            "Bollywood is the heartbeat of Indian cinema, where dreams are woven into stories that captivate the soul! 🎬🇮🇳",
            "In the world of Bollywood, every frame is a masterpiece, every song a symphony of emotions! 🎶🎥",
            "From romance to action, comedy to drama – Bollywood is a kaleidoscope of genres, reflecting the rich tapestry of Indian culture! 💖🌟",
        ],
        "hollywood": [
            "Hollywood is the epicenter of cinematic magic, where dreams are brought to life on the silver screen! 🎥✨",
            "In the realm of Hollywood, imagination knows no bounds, and storytelling reaches new heights of brilliance! 🌟📽️",
            "From blockbuster action flicks to heartfelt dramas, Hollywood movies inspire, entertain, and awe audiences around the globe! 🌎🍿",
        ],
    }
    
    for category, messages in general_messages.items():
        if category in message.text.lower():
            reply = random.choice(messages)
            sent_message = await message.reply_text(reply)

            # Wait for 30 seconds before deleting the message
            await asyncio.sleep(30)

            # Delete the sent message
            await sent_message.delete()
            break

# Function to send the supporter post
async def send_supporter_post(message):
    # Caption for the post
    caption = "Who is the real supporter Mad? 🔥"
    
    # Image URL for the post
    image_url = "https://telegra.ph/file/46cc2a2050e7b04c5be5a.jpg"
    
     # URL for sharing the group
    group_link = "https://t.me/StarModz"
    
    # Inline keyboard with three buttons
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Share ✅", url=group_link),
                InlineKeyboardButton("Points 📢", callback_data="show_points"),
                InlineKeyboardButton("Leader 🎗️", callback_data="show_leaderboard")
            ]
        ]
    )   
     # URLs for the six buttons
    button1_url = "https://t.me/MadGamerTG"
    button2_url = "https://t.me/StarFeedZ"
    button3_url = "https://t.me/MadHackerTG"
    button4_url = "https://t.me/StarModz"
    button5_url = "https://t.me/StarHelpline"
    button6_url = "https://t.me/MadAccountStore"
    
    # Inline keyboard with six buttons
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Join 🎗️", url=button1_url),
                InlineKeyboardButton("Join 📢", url=button2_url),
                InlineKeyboardButton("Join 🤡", url=button3_url),
            ],
            [
                InlineKeyboardButton("Join ❤️", url=button4_url),
                InlineKeyboardButton("Join 🎉", url=button5_url),
                InlineKeyboardButton("Join 😍", url=button6_url),
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

# Function to handle the "Share" button callback
@app.on_callback_query(filters.regex("share"))
async def handle_share_button(client, callback_query):
    # Get the user ID who clicked the button
    user_id = callback_query.from_user.id
    
    # Check if the user already received points for sharing
    if not check_if_shared(user_id):
        # Give points to the user for sharing
        give_points(user_id, 20)
        await callback_query.answer("You received 20 points for sharing the group link!")
    else:
        await callback_query.answer("You already received points for sharing the group link!")

# Function to check if the user already shared the group link
def check_if_shared(user_id):
    c.execute("SELECT * FROM shares WHERE user_id=?", (str(user_id),))
    return c.fetchone() is not None

# Function to give points to a user
def give_points(user_id, points):
    c.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (str(user_id),))
    c.execute("UPDATE users SET points = points + ? WHERE user_id = ?", (points, str(user_id)))
    conn.commit()
# Function to send reaction emoji without replying directly
async def send_reaction(message, emoji):
    # Indicate that the bot is typing
    await app.send_chat_action(message.chat.id, "typing")

    # Send the reaction emoji
    await app.send_sticker(chat_id=message.chat.id, sticker=emoji)

# Main message handling function
@app.on_message(filters.text & ~filters.me)
async def handle_messages(client, message):
    if message.text.lower() == "what is your favorite color?":
        sent_message = await message.reply_text("My favorite color is blue!")
    elif message.text.lower() == "how are you?":
        sent_message = await message.reply_text("I'm just a bot, but I'm doing well. How can I assist you?")
    elif message.text.lower() == "who create you?":
        sent_message = await message.reply_text("I was created by RZ anonymous 💒👿.")
    else:
        question = message.text.lower()
        trigger_words = ["hi", "hello", "kia", "kese", "men", "you", "ap", "nhi", "tera", "ban", "hall", "how", "me", "to"]
        for word in trigger_words:
            if word in question:
                # Select a random emoji reaction
                emoji = random.choice(["❤️", "🥰", "🎉", "🤡", "👿"])
                await send_reaction(message, emoji)
                break
                
        # Check if the message contains the word "flash" to trigger the supporter post
        if "flash" in message.text.lower():
            await send_supporter_post(message)
        else:
            await reply_to_mod_messages(message)
            await handle_general_messages(message)
            
    # Sending specific message for specific user
    await send_specific_reply(message)

# Run the bot
app.run()
