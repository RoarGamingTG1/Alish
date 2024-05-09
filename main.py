import os
import requests
from pyrogram import Client, filters

# Bot credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# Bot creation
Bot = Client(
    "InstagramVideoBot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

# Function to extract video URL from Instagram link
def extract_video_url(url):
    try:
        response = requests.get(url)
        html_content = response.text
        start_index = html_content.find("og:video") + 19
        end_index = html_content.find('"/>', start_index)
        video_url = html_content[start_index:end_index]
        return video_url
    except Exception as e:
        print("Error extracting video URL:", e)
        return None

# Message handler
@Bot.on_message(filters.private & filters.regex(r"(?i)https?://(www\.)?instagram\.com/.+"))
async def handle_instagram_link(bot, message):
    # Extract video URL from Instagram link
    video_url = extract_video_url(message.text)
    if video_url:
        # Download the video
        video_file = f"{message.chat.id}_video.mp4"
        try:
            with requests.get(video_url, stream=True) as r:
                r.raise_for_status()
                with open(video_file, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
            # Send the video file to the user
            await bot.send_video(message.chat.id, video_file)
        except Exception as e:
            print("Error downloading or sending video:", e)
            await message.reply_text("Error downloading or sending video. Please try again later.")
        finally:
            # Delete the video file
            os.remove(video_file)
    else:
        await message.reply_text("Sorry, unable to extract video URL from the provided link.")

# Bot start message
@Bot.on_message(filters.command(["start"]))
async def start(bot, message):
    await message.reply_text("Welcome to Instagram Video Downloader Bot! Send me an Instagram video link and I'll download it for you.")

# Run the bot
Bot.run()
