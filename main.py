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
        "ab tera time khatam! 💣💥",
        "tere liye special surprise hai mere pass! 🎁🔥",
        "Love is not just a feeling, it's an endless journey ❤️",
"In the chaos of life, love is the calm harbor 🌊❤️",
"A true love story never ends, it evolves 💫❤️",
"Love is the language that every heart understands 💌❤️",
"Every moment with you is a precious memory ✨❤️",
"Love is the key that unlocks the door to happiness 🗝️❤️",
"With you, every day feels like Valentine's Day 🌹❤️",
"Love is the melody our hearts dance to 🎶❤️",
"You are the missing piece that completes my puzzle 🧩❤️",
"In your arms, I've found my home 🏡❤️"
"Love is the art of being with someone who makes you feel alive 🎨❤️",
"In your eyes, I see my reflection and the future we'll build together 👀❤️",
"Love is not about finding the perfect person, but about seeing an imperfect person perfectly 👫❤️",
"Every love story is beautiful, but ours is my favorite 📖❤️",
"With you, I've found my happily ever after 🏰❤️",
"Your love is the melody that plays in my heart, day and night 🎵❤️",
"Love is the strongest force in the universe, binding hearts together across time and space 💫❤️",
"With your love, I am stronger, braver, and happier 💪❤️",
"You are the sunshine that brightens my darkest days ☀️❤️",
"Love is not just a word, it's a feeling that fills every part of my being 🌟❤️",
"With every beat of my heart, I love you more ❤️",
"Being deeply loved by someone gives you strength; loving someone deeply gives you courage 💖",
"Love is the answer to every question the heart asks 💭❤️",
"With you, I've found my soulmate, my partner, and my best friend 👫❤️",
"Love is the greatest adventure, and I'm glad to have you by my side 🌍❤️",
"Your love is the anchor that keeps me grounded in the stormiest seas ⚓❤️",
"With you, every moment is a treasure to cherish forever 🎁❤️",
"Love is the light that guides me through the darkest nights 🕯️❤️",
"You are my today and all of my tomorrows 📆❤️",
"Love is not about how much you say 'I love you,' but how much you prove that it's true 💖",
"In your arms, I've found my safe haven 🏠❤️",
"You are the missing piece I never knew I needed until I found you 🧩❤️",
"Love is like a flower; it needs care, attention, and nurturing to bloom 🌹❤️"
"With you, I've learned that love is not just a noun, but a verb—an action we choose every day 💞❤️",
"You are my heart's home, the place where I truly belong 🏡❤️",
"Love is not about finding perfection, but about embracing imperfection with open arms 💖",
"With your love, even the ordinary moments become extraordinary ✨❤️",
"Your love is the sweetest melody that plays in the symphony of my life 🎶❤️",
"Love is the bridge that connects two hearts, no matter the distance 🌉❤️",
"In a world full of chaos, your love is my calm oasis 🌊❤️",
"With you, I've found the true meaning of love—a journey of growth, understanding, and unwavering support 💑❤️",
"You are my sunshine on the darkest days, my light in the endless night ☀️🌙❤️"
"Love is the greatest gift of all, and I'm grateful to have you as mine 🎁❤️",
"With your love, I am whole, complete, and utterly content 🧩❤️",
"In your arms, I've found solace, peace, and endless joy 🕊️❤️",
"Love is the thread that weaves together the fabric of our lives, creating a beautiful tapestry of memories 💞🧵❤️"
"With you, every moment feels like a fairytale come true 🏰❤️",
"Your love is the anchor that keeps me grounded amidst life's storms ⚓❤️",
"Love is not just a feeling; it's a commitment, a promise to stand by each other through thick and thin 💍❤️",
"In your eyes, I see a reflection of my soul, and I'm endlessly captivated by its beauty 👁️❤️",
"With you, I've found a love that transcends space and time, a love that is eternal and unbreakable ⏳❤️",
"Love is the language that every heart speaks, the universal bond that connects us all 🗣️❤️",
"Your love is the compass that guides me through life's journey, pointing me towards true north 🧭❤️",
"With you, every day is Valentine's Day, filled with love, laughter, and cherished moments 🌹❤️",
"Love is the greatest adventure, and I'm grateful to have you as my partner in crime 🚀❤️",
"Your love is my greatest treasure, worth more than all the riches in the world 💰❤️",
"With you, I've learned that love is not about finding someone perfect, but about loving someone perfectly flawed 💖",
"Love is the song that my heart sings, a melody that echoes through eternity 🎶❤️",
"In your eyes, I see my past, present, and future, all intertwined in the beautiful tapestry of our love 👁️❤️",
"With you, every day feels like a dream come true, a fairytale romance that never fades 🌌❤️",
"Your love is the anchor that keeps me grounded, the wind beneath my wings, lifting me higher and higher ⚓✈️❤️"
"Love is not about grand gestures, but the 🌹💒",
"Khudi ko kar buland itna ke har taqdeer se pehle, Khuda bande se khud pooche, bata teri raza kya hai. 🌟❤️.",
"Sitaron se aage jahan aur bhi hain, abhi ishq ke imtihan aur bhi hain. ✨❤️.",
"Hai tair-e-lahooti, rang-o-bu se baaz aa ja, ke khoon-e-dil mein dubo lia hai ungliyon ne. 🌊❤️.",
"Kuch baat hai ki hasti mit-ti nahi hamari, sadiyon raha hai dusman daur-e-zaman hamara. 💪❤️.",
"Himmat e marda toh madad e Khuda, naseeb e mardan toh peshwa e taqdeer hota hai. 💖.",
"Bura waqt bhi ho, aur badal bhi guzar jaye, Khuda ke bandon ko kabhi na ghabrana chahiye. ☔❤️.",
"Hazaron saal nargis apni benoori pe roti hai, bari mushkil se hota hai chaman mein dedawar paida. 🌹🌱.",
"Girti hui deewaron ke aarzon se sarkashiyaan, bahut nikat hai dariya lekin rasta nahi dekhte. 🏞️❤️.",
"Na samjho ke tujh se koi shikayat nahi hai, teri aankhon mein bhi koi raaz chhupa hota hai. 🤔❤️.",
"Ae rah-e-haq ke shaheedo, wafa ki tasveero, tumhe watan ki hawain salam kehti hain. 🇵🇰❤️.",
"Tu shaheen hai, basera kar paharon ki chatano mein, is chaman ki jis ki khatir, jino ne qurbaan ho jaana hai. 🦅🏔️."
"Na thha kuch toh Khuda tha, kuch na hota toh Khuda hota, duboya mujh ko hone ne, na hota main toh kya hota. 🙏❤️.",
"Tu shayar hai, par woh qatra-e-sharab bhi hai, tu mehshar hai, par shabnam bhi hai, mahtab bhi hai. 🌧️📝.",
"Sitaron se aage jahan aur bhi hain, abhi ishq ke imtihan aur bhi hain. 🌌❤️."
"Khud ko kar buland itna ki har taqdeer se pehle, Khuda bande se khud pooche, bata teri raza kya hai. 🌟❤️.",
"Ae rah-e-haq ke shaheedo, wafa ki tasveero, tumhe watan ki hawain salam kehti hain. 🇵🇰❤️.",
"Tu shaheen hai, basera kar paharon ki chatano mein, is chaman ki jis ki khatir, jino ne qurbaan ho jaana hai. 🦅🏔️."
"Sitaron se aage jahan aur bhi hain, abhi ishq ke imtihan aur bhi hain. 🌌❤️.",
"Na thha kuch toh Khuda tha, kuch na hota toh Khuda hota, duboya mujh ko hone ne, na hota main toh kya hota. 🙏❤️.",
"Tu shayar hai, par woh qatra-e-sharab bhi hai, tu mehshar hai, par shabnam bhi hai, mahtab bhi hai. 🌧️📝.",
"Sitaron se aage jahan aur bhi hain, abhi ishq ke imtihan aur bhi hain. 🌌❤️."
"Khud ko kar buland itna ki har taqdeer se pehle, Khuda bande se khud pooche, bata teri raza kya hai. 🌟❤️.",
"Ae rah-e-haq ke shaheedo, wafa ki tasveero, tumhe watan ki hawain salam kehti hain. 🇵🇰❤️.",
"Tu shaheen hai, basera kar paharon ki chatano mein, is chaman ki jis ki khatir, jino ne qurbaan ho jaana hai. 🦅🏔️.",
"Sitaron se aage jahan aur bhi hain, abhi ishq ke imtihan aur bhi hain. 🌌❤️.",
"Na thha kuch toh Khuda tha, kuch na hota toh Khuda hota, duboya mujh ko hone ne, na hota main toh kya hota. 🙏❤️.",
"India, the land of diversity, where cultures weave a vibrant tapestry together. 🇮🇳❤️"
"The majestic Himalayas stand tall in the north, guarding the nation like silent sentinels. 🏔️🙌",
"Ganges, the sacred river, flows through the heart of the nation, bestowing blessings upon all. 🌊🕉️",
"From the bustling streets of Mumbai to the serene backwaters of Kerala, India offers experiences for every soul. 🌆🌴",
"Taj Mahal, a symbol of eternal love, stands as a testament to India's rich history and architectural marvels. 🕌💖"
"The aroma of spices fills the air in bustling markets, tantalizing taste buds and igniting the senses. 🌶️🍛",
"Diwali, the festival of lights, illuminates the night sky, spreading joy and warmth in every corner. ✨🪔",
"Holi, the festival of colors, paints the nation in a kaleidoscope of hues, celebrating unity amidst diversity. 🎨🎉",
"India's rich heritage is reflected in its art, dance, music, and literature, captivating hearts worldwide. 🎶📚",
"The roar of the Bengal tiger echoes in the dense forests of India's national parks, a symbol of the nation's wildlife conservation efforts. 🐅🌳",
"Yoga, an ancient practice, finds its roots in India, promoting physical, mental, and spiritual well-being. 🧘‍♂️☯️",
"Unity in diversity is India's mantra, where people of various religions, languages, and cultures coexist harmoniously. 🤝🌐",
"The Indian Railways, a lifeline connecting the nation, embarks on journeys that traverse mountains, plains, and deserts. 🚂🛤️",
"India's space program reaches for the stars, symbolizing the nation's aspirations for scientific excellence and exploration. 🚀🌌",
"The aroma of freshly brewed chai wafts through the streets, bringing people together for conversations and camaraderie. 🍵👥",
"Indian cuisine, with its myriad flavors and spices, tantalizes taste buds and satisfies culinary cravings. 🍲🌶️",
"From Bollywood blockbusters to regional cinema gems, Indian cinema captivates audiences with its storytelling prowess. 🎬🌟",
"Indian weddings, extravagant affairs filled with rituals and celebrations, unite families and communities in joyous union. 💒🎊",
"PUBG's competitive scene has grown rapidly, with tournaments and esports leagues attracting top players and teams from around the world. 🏆🌎",
"Strategic planning and decision-making are crucial in PUBG, as players must carefully manage their resources and prioritize objectives to survive and succeed. 📊🎯",
"Each match in PUBG offers a unique experience, with no two games playing out exactly the same, thanks to the game's dynamic environment and player interactions. 🔄🎮",
"The thrill of a chicken dinner, earned by outlasting all other players and emerging as the sole survivor, is one of PUBG's most satisfying achievements. 🍗🎉",
"PUBG Mobile, a version of the game optimized for smartphones and tablets, has expanded the game's reach to millions of players worldwide, making it accessible anytime, anywhere. 📱🌍",
"The game's intuitive controls and streamlined gameplay mechanics make PUBG Mobile easy to pick up for players of all skill levels, from beginners to seasoned veterans. 🎮📈",
"PUBG's vibrant community of players and content creators share strategies, tips, and memorable moments, fostering a sense of camaraderie and excitement within the game's community. 👥🎥",
"From intense firefights to heart-pounding escapes, PUBG offers adrenaline-fueled action and unforgettable moments that keep players coming back for more. 💥😱",
"Players can customize their characters with a variety of outfits, skins, and emotes, allowing them to express their personality and style in-game. 👕🎭"
"PUBG's replay feature enables players to review their matches, analyze their gameplay, and learn from their mistakes, helping them improve and grow as players. 🎥📈",
"The game's ranking system rewards skilled players with higher ranks and exclusive rewards, encouraging players to strive for improvement and mastery. 🏅🎁"
"PUBG's anti-cheat measures and fair play policies ensure a level playing field for all players, maintaining the integrity and competitiveness of the game. 🔒⚖️",
"The game's seasonal battle passes offer a variety of challenges and rewards for players to unlock, providing a sense of progression and accomplishment throughout the season. 📜🎁",
"PUBG's training mode allows players to hone their skills, test out weapons, and practice strategies in a safe and controlled environment, preparing them for the rigors of battle. 🎯🎮",
"Community events and in-game challenges offer players opportunities to earn exclusive rewards and engage with the PUBG community, fostering a sense of belonging and excitement. 🎉🎮",
"PUBG's immersive gameplay experience and high-stakes encounters make it a favorite among streamers and content creators, who entertain audiences with their epic plays and hilarious moments. 📺😂",
"The game's dedicated development team listens to player feedback and regularly implements changes and improvements based on community suggestions, ensuring that PUBG remains a dynamic and evolving experience. 👂🛠️",
"PUBG's vibrant modding community creates custom game modes, maps, and content, expanding the game's creative possibilities and keeping gameplay fresh and exciting. 🛠️🌟",
"From intense close-quarters combat to epic long-range sniping, PUBG offers a variety of playstyles and strategies for players to explore and master. 🔫🎯",
"The game's intuitive ping system allows players to communicate and coordinate with teammates without relying on voice chat, making teamwork more accessible and inclusive. 🗣️🤝",
"PUBG's seasonal updates and themed events introduce new content, challenges, and experiences for players to enjoy, keeping the game's community engaged and entertained. 🌟🎉",
"The game's realistic ballistics and bullet physics add depth and complexity to gunplay, rewarding precision and skillful marksmanship. 🔫🎯",
"PUBG's expansive map offers countless opportunities for exploration and discovery, with hidden loot, secret locations, and unexpected encounters waiting to be uncovered. 🗺️🔍",
"The game's evolving lore and backstory, set in a post-apocalyptic world ravaged by conflict, add depth and immersion to the PUBG universe, sparking the imagination of players. 📖🌍",
"PUBG's seasonal events and limited-time modes offer unique twists on the classic battle royale formula, introducing new challenges and gameplay mechanics for players to experience and enjoy. 🎉🔄",
"The game's robust spectating and replay features allow players to relive their favorite moments, share highlights with friends, and learn from the strategies and tactics of top players. 🎥📺",
"PUBG's immersive audio design and realistic soundscapes enhance the gameplay experience, allowing players to pinpoint enemy locations and react to threats with split-second precision. 🎶👂",
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
            "caption": "Caption for Mod",
            "button1_text": "Button 1",
            "button1_url": "https://t.me/Mod1",
            "button2_text": "Button 2",
            "button2_url": "https://t.me/Mod2",
            "image_url": "https://telegra.ph/file/0c5cab3ac6f9543497959.jpg"
        },
        "obb": {
            "caption": "Caption for Obb",
            "button1_text": "Button 1",
            "button1_url": "https://t.me/Obb1",
            "button2_text": "Button 2",
            "button2_url": "https://t.me/Obb2",
            "image_url": "https://telegra.ph/file/8710c559a915747a6622a.jpg"
        },
        "ali": {
            "caption": "Caption for Key",
            "button1_text": "Button 1",
            "button1_url": "https://t.me/Mod1",
            "button2_text": "Button 2",
            "button2_url": "https://t.me/Mod1",
            "image_url": "https://telegra.ph/file/f6be52baa496065e85862.jpg"
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
    elif message.text.lower() == "who created you?":
        sent_message = await message.reply_text("I was created by a team of developers at OpenAI.")
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
