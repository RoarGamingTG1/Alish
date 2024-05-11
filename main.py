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
        "Mad Hackar PUBG Lite ko hilane mein asli chamak dikhate hain! 🎮💥",
    "Inka talent PUBG Lite ke ander ki har rah ko jaan leta hai! 🔥🔫",
    "PUBG Lite ke Hackaron ke haath mein khelna matlab jeet ka guarantee! 🏆💣",
    "In Hackaron ka khelna PUBG Lite ko ek naya level deta hai! 🚀🎯",
    "Har situation mein yeh Hackar sabka baap ban jaate hain! 😎👑",
    "Inka PUBG Lite mein dominance dekh ke har koi hairaan ho jaata hai! 😲🎮",
    "PUBG Lite ke Hackar ke paas hai woh magical touch jo har game ko jeetne ka raaz hai! ✨🏅",
    "In Hackaron ka khelna PUBG Lite ke liye ek art hai, aur woh iss art mein maahir hain! 🎨🖌️",
    "PUBG Lite mein competition ka koi sawaal hi nahi jab yeh Hackar game mein hote hain! 🚫🤺",
    "In PUBG Lite ke Hackaron ki strategy dekh kar toh har koi unki taraf attract ho jaata hai! 🤩📝",
    "Jo PUBG Lite ke Hackaron se takraayega, woh seedha respawn point jaayega! 💥💀",
    "In Hackaron ka PUBG Lite mein presence hi ek warning hai baakiyon ke liye! ⚠️🔥",
    "PUBG Lite ke Hackar ek dusre se takkar lena jaante hain, lekin har baar jeet jaate hain! 💪🏻🎮",
    "Inka PUBG Lite ke saath connection itna strong hai ki lag hi nahi hota! 💻🔒",
    "Har PUBG Lite match mein yeh Hackar kuch naya dikhaate hain, aur unki creativity ka koi hadh nahi! 🤯🎮",
    "In Hackaron ke haath mein jo PUBG Lite ka weapon hai, woh hai unki mind-blowing skills! 🧠🔫",
    "PUBG Lite ke Hackaron ke liye har server ek playground hai, aur woh usmein apne rules banate hain! 🎡🎮",
    "Inke PUBG Lite skills dekh kar toh har koi kehta hai, 'Kya baat hai yaar!' 🤩👏",
    "Jo PUBG Lite ke Hackar khelte hain, unka har headshot ek masterpiece hai! 💥🎨",
    "Inka PUBG Lite ka khelna ek art form hai, jismein har move calculated hota hai! 🎭🕵️‍♂️",
    "PUBG Lite ke Hackaron ka khelna toh aise hai jaise koi symphony ka maestro music bajaye! 🎼🎮",
    "Jo PUBG Lite ke Hackar hote hain, woh apne opponents ko sirf game mein hi nahi, leaderboard pe bhi harate hain! 📊🏆",
    "In PUBG Lite ke Hackaron ki strategy dekh kar toh har koi kehta hai, 'Yeh kaise karte hain yaar!' 🤔🎮",
    "PUBG Lite ke Hackaron ke liye har game ek learning opportunity hai, aur woh har match se kuch naya seekhte hain! 📚🎮",
    "Inke PUBG Lite skills dekh kar toh har koi kehta hai, 'Ye toh next level hai!' 🌟👍",
    "PUBG Lite ke Hackaron ke paas hai woh X-factor jo unhe game mein hamesha aage le jaata hai! ❌🔥",
    "Jo PUBG Lite ke Hackar hai, unke liye har game ek chance hai apna dominance dikhane ka! 💥🎮",
    "Inke PUBG Lite ke skills dekh kar toh har koi kehta hai, 'Boss level reached!' 🎮👑",
    "PUBG Lite ke Hackaron ka khelna toh aise hai jaise koi chess grandmaster game khela ho! ♟️👑",
    "Jo PUBG Lite ke Hackar hai, woh game mein apne opponents ko sirf defeat nahi, humiliation bhi dete hain! 😏💥",
    "Inke PUBG Lite skills dekh kar toh har koi kehta hai, 'Yeh toh magic hai!' 🎩✨",
    "PUBG Lite ke Hackaron ke liye har match ek opportunity hai apne legacy ko aur bhi strong banana ka! 🏟️🎮",
    "In PUBG Lite ke Hackaron ka khelna toh aise hai jaise koi dance ka choreographer dance karwaye! 💃🎮",
    "Jo PUBG Lite ke Hackar hai, unka khelna toh ek art form hai, jismein har move perfect hota hai! 🎨👍",
    "Inke PUBG Lite skills dekh kar toh har koi kehta hai, 'Yeh toh kamaal hai!' 🤩🎮",
    "PUBG Lite ke Hackaron ke liye har match ek platform hai apne greatness ko dikhane ka! 🚀🎮",
    "Inke PUBG Lite ke skills dekh kar toh har koi kehta hai, 'Ye toh next level hai!' 🌟🎮",
    "PUBG Lite ke Hackaron ka khelna toh aise hai jaise koi masterpiece ko create kar raha ho! 🎨🖌️",
    "Jo PUBG Lite ke Hackar hai, unke liye har match ek opportunity hai apne opponents ko show karne ka ki woh kaun hai! 💪🎮",
    "Inke PUBG Lite skills dekh kar toh har koi kehta hai, 'Kya baat hai yaar!' 🤩🎮",
    "PUBG Lite ke Hackaron ke liye har game ek stage hai apne talent ko display karne ka! 🎭🎮",
    "Inke PUBG Lite ke skills dekh kar toh har koi kehta hai, 'Kya player hai yaar!' 🤩🎮",
    "Tere PUBG skills toh ek bot se bhi behtar nahi hai! 🤖",
    "Teri gameplay dekh kar toh lagta hai ke tu pehli baar game khel raha hai! 😂",
    "PUBG mein tu sirf loot ka raja hai, aur kuch nahi! 💰",
    "Teri aiming toh bakwaas hai, lagta hai ke chashmein dhundh rahe hain! 👓🎯",
    "Tere level pe PUBG khelne ki permission kaunsi duniya se aayi hai? 🤔",
    "Kyun bhai, PUBG khelne se pehle practice mode mein nahi gaya tha? 😏",
    "PUBG ke battlefield pe tu toh ek walking loot crate lagta hai! 🎁",
    "Teri kill-death ratio dekh kar toh lagta hai ke tu game se bhagwaan se lad raha hai! 🤣",
    "PUBG ke liye tu bilkul hi fit nahi hai, maybe Candy Crush try kar! 🍬🤭",
    "Tere jaise khiladiyon ke wajah se game ke servers down ho jaate hain! 🚫🎮",
    "PUBG mein tera gameplay dekh kar toh lagta hai ke tu apne hi team ka undercover agent hai! 🕵️‍♂️",
    "Tere skills dekh kar toh lagta hai ke PUBG ka koi update tujhe support nahi karta! 🤦‍♂️",
    "Tu PUBG khelne se pehle 'How to Play' manual padh le, shayad phir se try kar sake! 📖🤨",
    "Teri gaming skills itni low hain ke agar level ground hota, toh wahan se bhi niche girta! ⬇️😂",
    "PUBG mein tu toh bas supply drop ke peeche bhaagta hai, aur kuch nahi! 🏃‍♂️💨",
    "Teri strategy toh PUBG ke bots se bhi predictable hai! 🤖➡️😒",
    "PUBG mein tu toh ek side character hai, hero banne ki koshish karne ka waqt hi nahi aaya! 🦸‍♂️😅",
    "Teri gameplay dekh kar toh lagta hai ke tere thumbs bhi confused hain! 🤔👍👎",
    "PUBG mein teri skills dekh kar toh lagta hai ke tu ek school bus ko handle kar raha hai, aur woh bhi reverse mein! 🚌⬅️🔄",
    "Tere jaise khiladi PUBG ke liye kyun hain, kisi idle game ko try kar! 🔄🎮",
    "Teri PUBG skills dekh kar toh lagta hai ke tu game khelne ke bajaye spectate mode mein hi achha lagta hai! 👀👎",
    "PUBG mein teri performance dekh kar toh lagta hai ke tu apne hi team ko betray karne ke liye paida hua hai! 😈🚫",
    "Teri aiming skills itni achhi hai ke agar toilet mein seat ka target hota, bhi miss karta! 🚽🎯😂",
    "PUBG mein teri presence ka impact itna low hai ke agar map pe dekhoge toh tera marker bhi disappear ho gaya hai! 🗺️👻",
    "Tere jaise PUBG khiladiyon ke wajah se game ke developers ko lagta hai ke unka game kyun banaya tha! 😒🎮",
    "Tu PUBG khelne ke bajaye candy crush khel, wahan tujhe dikh jaayega ke teri speed kya hai! 🍬🚀",
    "Teri gameplay dekh kar toh lagta hai ke tu apne hi team ka sabse bada challenge hai! 🏆😅",
    "PUBG mein tera character itna slow hai ke woh loot collect karne ke bajaye map ki tasveer bhi nahi le sakta! 🐢📷😂",
    "Teri skills dekh kar toh lagta hai ke tu PUBG ko 'Press Any Key to Continue' tak bhi nahi pahunch sakta! 🎮🚫",
    "PUBG mein tu toh ek moving target hai, jo hamesha kill feed mein dikhta hai! 🎯💥🎮"
    "Tere jaise kill choron ke liye toh game mein jail hona chahiye, na ki winner winner chicken dinner! 🍗🚔",
    "Teri chori ki aadat ne tujhe sirf game ke kill count badhane ka sikhaaya hai, real life mein kuch kar ke dikhana! 🎮🚫",
    "Tu toh bas ek virtual dacoit hai, asli duniya mein toh tere jaise logon ko dekh kar log dar jaate hain! 👻🎮",
    "Tere jaise kill choron ko game se ban hona chahiye, tujhe game ke liye khaas jail cell hi milna chahiye! 🛑🔒",
    "Teri game mein chori dekh kar toh lagta hai ke tu asli zindagi mein bhi ek chindi chor hai! 🕵️‍♂️💼",
    "Tujhe kill count badhane ki bajaye, shayad moral compass repair karne ki zarurat hai! 🧭🤔",
    "Tu toh bas ek game ka Robin Hood hai, lekin asliyat mein tu kisi ka hero nahi, sirf zero hai! 🦸‍♂️🚫",
    "Tere jaise kill choron ko game se ban hona chahiye, warna ek din asli duniya mein jail ki jagah mil jaayegi! 🚨🎮",
    "Tere jaise kill choron ko game mein ban hona chahiye, tujhe real life ka difference bhi samajhna chahiye! 🎮❌",
    "Game mein kill chor, asli zindagi mein bhi tere jaise logon ki kami nahi hai! 🚷🎮"
    "Kya bolta hai @Mad_Supporter, PUBG mein pan se maar khane ka record toh sirf tere paas hai na! 🍳🥊",
    "PUBG mein drop loot karne ki jagah, tu sirf @Mad_Supporter ke gameplay hi loot leta hai! 💼💥",
    "PUBG mein tere chicken dinner ki jagah, tu sirf Mad_Supporter ke ulte pair se bhara hua hota hai! 🐔🍽️",
    "Kya scene hai @Mad_Supporter, PUBG ke noob players teri skills se hi kuch seekhte hain, kyunki unki game bhi tere jaise hi hai! 🎮🤣",
    "Kya game khela hai aaj @Mad_Supporter? PUBG mein tu toh sirf pan se hi maar kha raha hoga! 🥘🥊",
"Kya dekh raha hai @Mad_Supporter, teri screen pe bas PUBG ke noob players hi dikhte honge, jaise tu khud ek hai! 🎮🤣",
"Aaj kya chal raha hai @Mad_Supporter? PUBG khel raha hoga na, wahi toh teri 'skills' ka asli parda faash hota hai! 🥘🥊",
"PUBG ki raat, aur kya chaahiye saath, noob player mare, winner winner chicken dinner ke baad! 🍗🎮",
"Udte pan ka nasha, goliyon ki barsaat, PUBG khel ke noob ban gaya pro, ab toh bas chicken dinner ki aas baaki hai! 🥘🎮"
"PUBG ki raat hai, headset pe baat hai, loot le saara maal, par dil mein wahi baat hai, 'winner winner chicken dinner'! 🍗🎮",
"Hey @M3xecv, teri PUBG Lite ka record toh kamaal hai! Ek game mein 50 kills, aur woh bhi pan se! 🍳🔥",

        # Add more threatening messages here if needed
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
        # Add more random messages here if needed
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
        "key": {
            "caption": "Key Finding Latest Method How to find key !!Key kaise nikaalen Watch Full VideoAnd find key by own very easily Poora Video dekho or badi asaani se khud key nikaalo
",
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
        # Add more trigger words with their respective details
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
        trigger_words = ["hi", "hello","kia", "kese","men", "you","ap", "nhi","tera", "ban","hall", "how", "me", "to"]
        for word in trigger_words:
            if word in question:
                await send_dangerous_reply(message)
                await send_random_reply(message)
                break
        else:
            await reply_to_mod_messages(message)

    # Wait for 30 seconds before deleting the message
    await asyncio.sleep(30)

    # Delete the sent message
    await sent_message.delete()
    

# Run the bot
app.run()
