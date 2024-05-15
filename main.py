import os
import random
import asyncio
import sqlite3
from pyrogram import Client, filters

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
      "🚨 Breaking News: Mad Hacker ne ek naya world record banaya hai! Unhone ek din mein 1000 kills kiye hain PUBG Lite mein.",
    "🔥 Exclusive: Mad Hacker ne apne latest livestream mein dikhaya ki woh invisible ho sakta hai PUBG Lite ke andar, aur saath hi saath aimbot ka istemal karta hai.",
    "📢 Alert: Mad Hacker ne apne latest video mein dikhaya ki woh apne opponents ko ek hi jhatke mein maar sakta hai, jaise woh kisi magician ki tarah hai.",
    "🤯 Shocking: Mad Hacker ne announce kiya hai ki woh PUBG Lite ke andar ek secret hacking group ko lead kar rahe hain, jo har server ko control kar raha hai.",
    "👀 Unbelievable: Mad Hacker ne apne latest interview mein kaha hai ki woh PUBG Lite ke developers ko challenge kar rahe hain aur unhein dikhana chahte hain ki unki security kitni weak hai.",
    "💥 Incredible: Mad Hacker ne apne latest gameplay video mein dikhaya hai ki woh sirf ek hi bullet se ek puri squad ko khatam kar sakta hai, bilkul ek superhero ki tarah.",
    "🔮 Sensational: Mad Hacker ne announce kiya hai ki woh PUBG Lite ke andar ek hidden glitch ko discover kiya hai, jo unhein invincible bana deta hai.",
    "🌟 Mind-blowing: Mad Hacker ne apne latest hacking tutorial mein dikhaya hai ki woh kaise PUBG Lite ke andar unlimited health aur ammo le sakta hai, bilkul ek cheat code ki tarah.",
    "🎮 Amazing: Mad Hacker ne PUBG Lite ke andar ek naya cheat code discover kiya hai, jisse woh har match mein winner ban sakta hai!",
    "👑 Legendary: Mad Hacker ke latest montage ne puri gaming community ko hairan kar diya hai! Unke skills ko dekhkar sabhi players unhein maan rahe hain.",
    "🚨 Breaking News: Mad Hacker ne apne PUBG Lite ke opponents ko itne confuse kiya hai ki unka khud ka character bhi ab Mad Hacker ko follow kar raha hai!",
    "🔥 Exclusive: Mad Hacker ne apne latest livestream mein dikhaya ki woh apne opponents ke bullets ko apne pet mein store kar leta hai aur unhein firse shoot karta hai!",
    "📢 Alert: Mad Hacker ne apne Telegram channel par ek naya series shuru kiya hai 'Cooking with Hacks', jismein woh dikhate hain kaise woh chicken dinner banate hain sirf hacks se!",
    "🤯 Shocking: Mad Hacker ne announce kiya hai ki woh PUBG Lite ke andar ek secret dance party organize kiya hai, jismein sabhi players ke characters naach rahe hain!",
    "👀 Unbelievable: Mad Hacker ne apne latest interview mein kaha hai ki woh PUBG Lite ke servers ko ek massive pizza party organize karke hack kar sakta hai!",
    "💥 Incredible: Mad Hacker ne apne latest gameplay video mein dikhaya hai ki woh apne opponents ko sirf dance moves se hi distract kar leta hai aur unhein easily maar deta hai!",
    "🔮 Sensational: Mad Hacker ne announce kiya hai ki woh PUBG Lite ke andar ek hidden treasure hunt start karne wale hain, jismein winner ko unlimited V-Bucks milenge!",
    "🌟 Mind-blowing: Mad Hacker ne apne latest hacking tutorial mein dikhaya hai ki woh kaise PUBG Lite ke andar sirf ek keyboard ki bajaye guitar se bhi game control kar sakta hai!",
    "🎮 Amazing: Mad Hacker ne PUBG Lite ke andar ek naya mode introduce kiya hai 'Hackers vs Developers', jismein woh khud hi PUBG Lite ke developers ko challenge karte hain!",
    "👑 Legendary: Mad Hacker ke latest montage ne puri gaming community ko laughter riots mein daal diya hai! Unke hilarious moments ko dekhkar sabhi players unhein maan rahe hain."
     "😔 Heartbreaking News: @Mad_Supporter ka account suspend ho gaya hai aur ab woh kabhi bhi online nahi aa sakta.",
    "💔 Tragic: @Mad_Supporter ne apne latest message mein bataya hai ki woh gaming community se alag ho gaya hai aur ab kisi aur platform par nahi aayega.",
    "😢 Devastating: @Mad_Supporter ne announce kiya hai ki woh ab PUBG Lite ko uninstall kar raha hai aur kabhi bhi wapas nahi aayega.",
    "😭 Unbearable: @Mad_Supporter ne apne latest video mein dikhaya hai ki woh apne gaming setup ko dismantle kar raha hai aur keh raha hai ki woh ab gaming se retire ho raha hai.",
    "😞 Disheartening: @Mad_Supporter ne apne last livestream mein emotional goodbye diya hai aur keh diya hai ki woh ab hamesha ke liye chala gaya hai.",
    "🥺 Upsetting: @Mad_Supporter ne announce kiya hai ki woh apne followers ko unfollow kar raha hai aur ab kisi bhi social media platform par nahi rahega.",
    "😕 Desperate: @Mad_Supporter ne apne latest tweet mein bataya hai ki woh ab online gaming se completely bahar ja raha hai aur apne life mein kuch aur focus karna chahta hai.",
    "😟 Regretful: @Mad_Supporter ne apne latest post mein admit kiya hai ki woh apne fans ko disappoint kar gaya hai aur ab woh unhein kabhi bhi wapas nahi dekh sakta.",
    "😩 Hopeless: @Mad_Supporter ne announce kiya hai ki woh apne gaming community se alag ho raha hai aur ab kisi bhi multiplayer game mein participate nahi karega.",
    "😓 Painful: @Mad_Supporter ne apne latest status update mein likha hai ki woh apni gaming journey ko end kar raha hai aur ab woh hamesha ke liye offline ho raha hai.",
      "😡 Furious News: @Mad_Supporter ne apne followers ko challenge kiya hai aur unhein ultimatum diya hai ki agar woh unhein support nahi karte toh unhein unfollow kar dega!",
    "🤬 Outrageous: @Mad_Supporter ne apne latest video mein sabhi gaming companies ko gaaliyan di hai aur keh diya hai ki unke games kachra hai!",
    "👿 Outraged: @Mad_Supporter ne announce kiya hai ki woh ab apne haters ko challenge karega aur unhein unke gaming skills ka jawab dega!",
    "💢 Incensed: @Mad_Supporter ne apne latest livestream mein apne opponents ko gaaliyan di hai aur unhein challenge kiya hai ki woh unse match khel ke dekhe!",
    "😠 Angry: @Mad_Supporter ne apne latest tweet mein sabhi fake news spread karne walon ko kadi nafrat se nazar andaaz kiya hai aur unhein public shame kiya hai!",
    "👺 Enraged: @Mad_Supporter ne announce kiya hai ki woh ab kisi bhi gaming community se associate nahi rahega jo unke khilaaf ho!",
    "🔥 Furious: @Mad_Supporter ne apne latest video mein apne followers ko bola hai ki agar unhein koi bhi fake news milta hai toh woh uss person ko block kar dega!",
    "😤 Infuriated: @Mad_Supporter ne announce kiya hai ki woh ab kisi bhi gaming event ya tournament mein participate nahi karega jo unki terms aur conditions ko follow nahi karta!",
    "😾 Seething: @Mad_Supporter ne apne latest stream mein apne critics ko challenge kiya hai aur unhein live match mein apne saath khelne ka mauka diya hai!",
    "💥 Raging: @Mad_Supporter ne apne latest post mein apne haters ko public apology demand ki hai aur unhein warn kiya hai ki agar woh nahi maante toh consequences bhugatenge!",
       "🚨 Breaking News: Mad Hacker ne announce kiya hai ki uske upcoming PUBG Lite mods mein ek new feature hoga jismein players ko invisibility mil jayegi!",
    "🔥 Exclusive: Mad Hacker ne bataya hai ki uske next PUBG Lite mods mein ek aimbot feature aayega jo opponents ko automatically target karega.",
    "📢 Alert: Mad Hacker ne reveal kiya hai ki uske upcoming PUBG Lite mods mein ek custom map editor feature hoga jisse players khud apni maps create kar sakenge!",
    "🤯 Shocking: Mad Hacker ne announce kiya hai ki uske next PUBG Lite mods mein ek new mode aayega jismein players ek hi bullet mein opponents ko maar sakenge!",
    "👀 Unbelievable: Mad Hacker ne bataya hai ki uske upcoming PUBG Lite mods mein ek anti-ban feature hoga jo players ko ban hone se bachayega.",
    "💥 Incredible: Mad Hacker ne reveal kiya hai ki uske next PUBG Lite mods mein ek health regen feature aayega jo players ki health ko automatic taur par regenerate karega.",
    "🔮 Sensational: Mad Hacker ne announce kiya hai ki uske upcoming PUBG Lite mods mein ek no-recoil feature aayega jisse players ke guns ka recoil bilkul bhi nahi hoga.",
    "🌟 Mind-blowing: Mad Hacker ne bataya hai ki uske next PUBG Lite mods mein ek unlimited ammo feature hoga jisse players ko ammo ki koi kami nahi hogi.",
    "🎮 Amazing: Mad Hacker ne reveal kiya hai ki uske upcoming PUBG Lite mods mein ek speed hack feature aayega jisse players ki movement speed double ho jayegi.",
    "👑 Legendary: Mad Hacker ne announce kiya hai ki uske next PUBG Lite mods mein ek God mode feature aayega jisse players invincible ho jayenge aur unhein koi bhi damage nahi hoga.",
     "😂 Hilarious News: Mad Hacker ne announce kiya hai ki uske next PUBG Lite mods mein ek 'Chicken Dance Mode' aayega jismein har player jab mar jayega toh uska character naachne lagega!",
    "🤣 Laugh Out Loud: Mad Hacker ne bataya hai ki uske upcoming PUBG Lite mods mein ek 'Confetti Grenade' feature aayega jisse opponents ko kill karne par confetti blast hoga!",
    "😆 LOL News: Mad Hacker ne reveal kiya hai ki uske next PUBG Lite mods mein ek 'Glitchy Vehicle' feature aayega jismein vehicles randomly glitch kar jayenge aur players ko air mein udne lagega!",
    "😄 Funny Alert: Mad Hacker ne announce kiya hai ki uske upcoming PUBG Lite mods mein ek 'Banana Peel Gun' aayega jisse opponents ko shoot karne par banana peel giregi aur unka character slip kar jayega!",
    "😜 Wacky News: Mad Hacker ne bataya hai ki uske next PUBG Lite mods mein ek 'Random Teleport' feature aayega jisse players match ke beech mein randomly teleport ho jayenge!",
    "😅 Hysterical: Mad Hacker ne reveal kiya hai ki uske upcoming PUBG Lite mods mein ek 'Dancing Bullets' feature aayega jismein bullets har ek kill ke baad naachte huye wapas aayenge!",
    "😂 Side-splitting News: Mad Hacker ne announce kiya hai ki uske next PUBG Lite mods mein ek 'Disco Zone' aayega jahan par match ke dauraan lights aur music honge!",
    "🤣 Chuckle-worthy: Mad Hacker ne bataya hai ki uske upcoming PUBG Lite mods mein ek 'Chicken Parade' aayega jismein match ke beech mein randomly ek chicken parade hoga!",
    "😆 Hilarious Alert: Mad Hacker ne reveal kiya hai ki uske next PUBG Lite mods mein ek 'Silly Hats' feature aayega jisse players ke characters ke sir par funny topiyan pehni jaayengi!",
    "😄 Amusing News: Mad Hacker ne announce kiya hai ki uske upcoming PUBG Lite mods mein ek 'Jelly Floor' aayega jismein match ke beech mein floor jelly ban jayega aur players slide karte karte chalenge!",
    "🚨 Breaking News: @Mad_Supporter ne announce kiya hai ki woh is duniya se chale gaye hain, lekin unka legacy hamesha zinda rahega!",
    "💔 Heartbreaking Update: @Mad_Supporter ka demise ho gaya hai aur unke fans pure world mein unhein yaad karenge!",
    "😢 Sad News: @Mad_Supporter ab is duniya mein nahi rahe hain aur unki yaadon ko yaad karke unka tribute diya ja raha hai.",
    "😔 Disheartening Update: @Mad_Supporter ke chale jaane se gaming community ka ek bada loss hua hai aur unke fans dukhi hain.",
    "😞 Tragic Announcement: @Mad_Supporter ka demise ho gaya hai aur unke supporters pure world mein unhein yaad karenge.",
    "😭 Heart-wrenching News: @Mad_Supporter ab hamare beech mein nahi hain aur unki kami hamesha mehsoos hogi.",
    "😢 Tearful Update: @Mad_Supporter ke chale jaane se gaming world ka ek bada star humse alvida keh gaya hai.",
    "😞 Saddening News: @Mad_Supporter ka demise ho gaya hai aur unke fans dukhi hain is tragic news sun kar.",
    "😔 Disappointing Announcement: @Mad_Supporter ke chale jaane se unke supporters pure world mein heartbroken hain.",
    "😢 Heartbreaking Update: @Mad_Supporter ne announce kiya hai ki woh is duniya se chale gaye hain aur unke fans unki yaadon mein hamesha rahenge.",
     "👻 Spooky Update: @Mad_Supporter ki aatma bhatak rahi hai aur woh gaming community ko haunt kar rahi hai!",
    "👀 Paranormal Activity: @Mad_Supporter ka bhoot dekha gaya hai gaming forums par roam karte hue!",
    "😱 Terrifying Announcement: @Mad_Supporter ki aatma ne announce kiya hai ki woh gaming events par appear kar rahi hai!",
    "👾 Ghostly Presence: @Mad_Supporter ki aatma ne gaming discord servers ko invade kiya hai aur woh wahaan pe prank kar rahi hai!",
    "🕸️ Haunting News: @Mad_Supporter ka bhoot gaming subreddits par spotted hua hai, aur woh wahaan pe funny memes share kar raha hai!",
    "👻 Eerie Update: @Mad_Supporter ki aatma ne announce kiya hai ki woh gaming tournaments mein participate kar rahi hai, lekin invisibly!",
    "💀 Creepy Announcement: @Mad_Supporter ka bhoot gaming YouTube channels par dikha gaya hai aur woh wahaan pe ghost stories suna raha hai!",
    "👽 Otherworldly Presence: @Mad_Supporter ki aatma gaming servers ko disturb kar rahi hai aur woh wahaan pe spooky messages bhej rahi hai!",
    "👻 Spectral Activity: @Mad_Supporter ka bhoot gaming websites par dekha gaya hai, aur woh wahaan pe fake news spread kar raha hai!",
    "😈 Mysterious Update: @Mad_Supporter ki aatma ne reveal kiya hai ki woh gaming community ko entertain kar rahi hai, lekin ghostly ways mein!",
      "🤬 Breaking News: Mad Hacker ne haters ke liye ek strong message diya hai aur unhein bola hai ki woh unke criticism ko 'where the sun don't shine' mein daal dein!",
    "😡 Angry Update: Mad Hacker ne haters ko challenge kiya hai aur unhein bola hai ki woh apne 'keyboard warrior' skills ko offline mein bhi demonstrate karein!",
    "🤯 Outrageous Announcement: Mad Hacker ne haters ko ek 'friendly reminder' diya hai ki unki opinions unke kisi bhi kaam ka nahi hote aur unhein chup rehne ko kaha hai!",
    "🖕 Offensive Alert: Mad Hacker ne haters ko ek 'colorful' message diya hai aur unhein bola hai ki woh 'mind their own business' aur unke mods enjoy karein!",
    "🤬 Furious News: Mad Hacker ne haters ko ek 'unfiltered' message diya hai aur unhein bola hai ki woh apne negativity ko apne paas rakhein!",
    "😤 Frustrated Update: Mad Hacker ne haters ko ek 'savage' message diya hai aur unhein bola hai ki woh apna time aur energy kisi aur constructive activity mein invest karein!",
    "😠 Aggressive Announcement: Mad Hacker ne haters ko ek 'straight to the point' message diya hai aur unhein bola hai ki woh unke kaam ko criticize karne ki bajaye apne skills improve karein!",
    "🤬 Outburst Alert: Mad Hacker ne haters ko ek 'no-nonsense' message diya hai aur unhein bola hai ki woh apne negative vibes apne paas rakhein!",
    "😡 Hostile News: Mad Hacker ne haters ko ek 'unapologetic' message diya hai aur unhein bola hai ki woh unke haters se door rahein!",
    "🖕 Offensive Update: Mad Hacker ne haters ko ek 'colorful' message diya hai aur unhein bola hai ki woh unke mods ko enjoy karein aur unki negativity ko 'swipe left' karein!",
     "🎉 Exciting News: Mad Hacker ne announce kiya hai ki woh apne loyal fans ke liye ek exclusive PUBG Lite mod release kar rahe hain jo game ko aur bhi thrilling banayega!",
    "👏 Appreciative Update: Mad Hacker ne apne dedicated fans ka shukriya ada kiya hai aur unhein promise kiya hai ki woh unke liye special in-game events organize karenge!",
    "😊 Heartfelt Announcement: Mad Hacker ne apne fans ko ek heartfelt message diya hai aur unhein bataya hai ki woh unki support ke liye grateful hain aur unhein kabhi disappoint nahi karenge!",
    "🌟 Fan Appreciation: Mad Hacker ne apne fans ko ek 'thank you' message diya hai aur unhein promise kiya hai ki woh unke liye exclusive gaming content create karenge!",
    "🎊 Celebratory Alert: Mad Hacker ne apne fans ko ek celebratory message diya hai aur unhein bataya hai ki woh unke liye special giveaways aur contests plan kar rahe hain!",
    "🙌 Grateful Update: Mad Hacker ne apne loyal fans ka shukriya ada kiya hai aur unhein bataya hai ki woh unke support ko kabhi underestimate nahi karenge!",
    "👍 Positive Announcement: Mad Hacker ne apne fans ko ek encouraging message diya hai aur unhein bola hai ki woh unke liye aur bhi creative aur entertaining content produce karenge!",
    "😃 Joyful News: Mad Hacker ne apne fans ko ek joyful message diya hai aur unhein bataya hai ki woh unke feedback ko sunenge aur unke liye improvements laayenge!",
    "🎮 Gaming Appreciation: Mad Hacker ne apne fans ko ek gaming appreciation message diya hai aur unhein bataya hai ki woh unke liye exciting gaming experiences create karenge!",
    "👌 Positive Update: Mad Hacker ne apne fans ko ek positive update diya hai aur unhein promise kiya hai ki woh unke liye aur bhi engaging aur enjoyable gaming content provide karenge!",
      "🚫 Important Update: Mad Hacker ne announce kiya hai ki woh apne mods ki keys share karne walon ko apne channel se ban kar denge, aur keh diya hai ki har user unke mods ki keys khud download karein!",
    "❌ Key Sharing Alert: Mad Hacker ne apne mods ki keys share karne walon ko warning di hai aur unhein bataya hai ki agar kisi ne key share ki to unhein channel se ban kiya jayega!",
    "⛔ Strict Announcement: Mad Hacker ne apne mods ki keys ko share karne walon ko ban karne ki threat di hai aur unhein samjha diya hai ki agar key share ki to unhein consequences bhugatna padega!",
    
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
        "Kayse hen Ap 😀",
        "Send Feedbacks! 😤",
        "IF any Problem Yahan apna problem bataye 🙂! ",
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
                InlineKeyboardButton("Share ✅", callback_data="share"),
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

# Function to react with random emojis every 60 seconds in groups
async def react_with_random_emojis():
    while True:
        # List of random emojis
        emojis = ["👍", "❤️", "🙂", "😮", "😊", "🔥", "💯", "👌", "😎", "🎉"]
        # Get all the group chats where the bot is a member
        async for dialog in app.iter_dialogs():
            if dialog.chat.type == "group" or dialog.chat.type == "supergroup":
                # Select a random emoji from the list
                emoji = random.choice(emojis)
                try:
                    # React with the selected emoji to the latest message in the group
                    await app.send_chat_action(dialog.chat.id, "typing")
                    await app.send_reaction(dialog.chat.id, dialog.messages[0].message_id, emoji)
                except Exception as e:
                    print(f"Error: {e}")
        # Wait for 60 seconds before reacting again
        await asyncio.sleep(60)

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

# Run the bot and react with random emojis
app.run(react_with_random_emojis())
