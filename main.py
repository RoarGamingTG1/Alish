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
        "Mad bhai apne kaam mein ek ustaad hain!",
        "Mad bhai ke hunar ko koi nahi takkar de sakta!",
        "Mad bhai ek genius developer hain!",
       "Mad bhai's mod is the best choice! 😎",
        "Using hacks responsibly is important. Mad Bhai's mod is the way to go! 😎",
        "Stay safe while hacking. Choose Mad Bhai's mod for a secure experience! 😎",
        "Need to use a hack? Opt for Mad Bhai's mod for PUBG Lite! 😎",
        "When it comes to hacks, trust Mad Bhai's mod. It's the safest bet! 😎",
        "Hack responsibly with Mad Bhai's mod. Safety first! 😎",
        "Mad Bhai's mod is the top choice for hacking safely. Don't compromise on security! 😎",
        "Looking for a hack? Mad Bhai's mod is the answer! 😎",
        "Hacks can be risky. Ensure your safety with Mad Bhai's mod! 😎",
        "Mad Bhai's mod is the ultimate solution for safe hacking. Choose wisely! 😎",
                "Mad Bhai ke mod ke records wakai mashhoor hain!",
        "Mad Bhai ke mod ke records ko har koi harana chahta hai!",
        "Mad Bhai ke mod ke records ko todna kisi ke bas ki baat nahi hai!",
        "Mad Bhai ke mod ke records puri duniya mein charcha mein hain!",
        "Mad Bhai ke mod ke records dekh kar har koi hairan hota hai!",
        "Mad Bhai ke mod ke records todna bohot se logo ka khwab hai!",
        "Koi bhi Mad Bhai ke mod ke records se muqabla nahi kar sakta!",
        "Mad Bhai ke mod ke records ustaad ke hunar ka saboot hain!",
        "Mad Bhai ke mod ke records wakai ajeeb hain!",
        "Mad Bhai ke mod ke records bilkul kamaal hain!",
        "Mad Bhai ke upcoming mods hamesha exciting hote hain! 😁",
        "Mad Bhai ke upcoming mods ka intezaar nahi ho raha! 😁",
        "Mad Bhai ke upcoming mods legendary honge! 😁",
        "Mad Bhai ke upcoming mods ka intezaar haqeeqat mein hai! 😁",
        "Mad Bhai ke upcoming mods ka intezaar karne laayak hain! 😁",
        "Mad Bhai ke upcoming mods ke liye hum utsuk hain! 😁",
        "Mad Bhai ke upcoming mods ka intezaar hai! 😁",
        "Mad Bhai ke upcoming mods kabhi nahi nirash karte! 😁",
        "Mad Bhai ke upcoming mods hamesha humein aur bhi jyada chahne par majboor karte hain! 😁",
        "Mad Bhai ke upcoming mods bahut zabardast honge! 😁",
                "Remember, patience is a virtue. Keep calm and carry on! 💪",
        "Don't forget to take breaks and relax. Your mental health matters! 🧘‍♂️",
        "Success comes to those who work hard and stay focused. Keep grinding! 💼",
        "Stay positive and believe in yourself. You're capable of amazing things! 🌟",
        "Be kind to yourself and others. Kindness goes a long way! ❤️",
        "Challenges are opportunities in disguise. Embrace them and grow! 🌱",
        "Never stop learning and improving. Every setback is a lesson! 📚",
        "Take risks and step out of your comfort zone. That's where growth happens! 🚀",
        "Stay determined and persevere through tough times. You're stronger than you think! 💪",
        "Always trust your instincts and follow your heart. It knows the way! ❤️",
        
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
        "Tum bilkul bekaar ho. 😡",
    "Koi tumhe pasand nahi karta. 😤",
    "Tum kabhi zindagi mein kamyaab nahi hoge. 😠",
    "Tum ek nakami ho. 😒",
    "Tum kyun nahi haar maan lete? 😡",
    "Tum bahut hi badsurat ho. 😒",
    "Tum ek loser ho. 😤",
    "Tum ek bekaar insaan ho. 😠",
    "Kisi ko bhi tumhari parwah nahi hai. 😡",
    "Tum kabhi bhi kafi nahi hoge. 😒",
    "Tere dimaag mein toh keede pade hain. 🐛",
    "Tumhare jaise logon se door hi rehna chahiye. 🙄",
    "Tumhein sharam nahi aati apne aap ko dekh kar? 😏",
    "Tum ek bilkul bekar insaan ho. 🤦‍♂️",
    "Tumhare jaise logon ki wajah se duniya bekar hoti ja rahi hai. 🌍",
    "Tum kitne bewakoof ho, mujhe toh hairat hoti hai! 🤷‍♀️",
    "Tumhara IQ ek thermometer se bhi kam hai. 🌡️",
    "Tum jaise logon ko dekh kar mujhe apne aap par afsos hota hai. 😔",
    "Tumhara chehra dekh kar lagta hai, bhagwaan ne galti se extra time waste kiya. 😒",
    "Tumhara dimaag chuhe ki tarah chal raha hai. 🐭",
   "Tujhe toh apni shadow bhi chhod kar chali gayi hai. 😂"
   
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
        "love": [
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

# Main message handling function
@app.on_message(filters.text & ~filters.me)
async def handle_messages(client, message):
    if message.text.lower() == "what is your favorite color?":
        sent_message = await message.reply_text("My favorite color is blue!")
    elif message.text.lower() == "how are you?":
        sent_message = await message.reply_text("I'm just a bot, but I'm doing well. How can I assist you?")
    elif message.text.lower() == "who create you?":
        sent_message = await message.reply_text("I was create by RZ anonymous 💒👿.")
    else:
        question = message.text.lower()
        trigger_words = ["hi", "hello", "kia", "kese", "men", "you", "ap", "nhi", "tera", "ban", "hall", "how", "me", "to"]
        for word in trigger_words:
            if word in question:
                await send_dangerous_reply(message)
                await send_random_reply(message)
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
      
