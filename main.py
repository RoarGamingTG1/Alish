import telebot
import random

# Telegram bot token
TOKEN = 'apna_telegram_bot_token_yahan_dalen'

# Create a bot instance
bot = telebot.TeleBot(TOKEN)

# Function to handle incoming messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Function to generate random response
    response = generate_response()
    bot.reply_to(message, response)

# Function to generate random response
def generate_response():
    responses = [
        "تمہیں لعنت دی گئی ہے! امید کرو کہ جہاں بھی جاؤ، نحوستی تمہارا پیچھا کرے گی۔",
        "مبارک ہو! تم نے ایک سفری بوائے کی ٹکٹ جیت لی ہے جوزاہنم میں پہنچنے کا آرام کریں۔ اپنی دائمی عذاب کا لطف اٹھائیں!",
        "خبردار! سایہ تمہیں دیکھ رہا ہے...",
        "تمہارے سیاہ خفیہ اسرار میرے حوالے میں ہیں۔ آج رات اچھی طرح سونا...",
        "تمہارا وقت ختم ہو رہا ہے...",
        "ختم ہونے والا ہے...",
        "میں تمہیں دیکھ رہا ہوں...",
        "تمہارا مقدر بچ نہیں سکتا...",
        "تمہاری مصیبت مجھے خوشی دیتی ہے... 😈",
        "میں وہ تارا ہوں جو لوگوں کے دلوں میں چھپا ہے...",
        "آپ کی خوابوں کا کھیل میں ہوں...",
        "رات کو آپ کو سننے والے اسراری گپشپ وہ میں ہوں...",
        "آپ صرف میرے بڑے منصوبے کا ایک پیشہ ہیں...",
        "ہر قدم آپ کو اپنی تباہی کے قریب لاتا ہے...",
        "روشنی نہیں ہے، صرف تاریکی ہے... 😈",
        "خوش آمدید! میں آپ کو دوزخ کی مدد گار ہوں۔ آپ کا خیر مقدم ہے ۔ 😈",
        "تیار ہو جاؤ! آپ کا مقدر میں لا رہا ہوں... 😈",
        "کیا آپ کو بھی مجھ سے ڈر لگتا ہے؟ اچھا لگتا ہے! 😈",
        "آپ کو کیا لگتا ہے؟ کوئی بچا پایے گا؟ بہت مضبوط! 😈"
    ]
    return random.choice(responses)

# Start the bot
bot.polling()
