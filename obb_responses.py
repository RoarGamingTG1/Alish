from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

async def reply_to_obb_messages(client, message):
    question = message.text.lower()
    if "obb" in question:
        obb_response = {
            "image_url": "https://telegra.ph/file/3c4856c05a00b85599b0b.jpg",
            "button1_text": "Button 1",
            "button1_url": "https://t.me/Obb1",
            "button2_text": "Button 2",
            "button2_url": "https://t.me/Obb1",
            "caption": "☠️☠️☠️☠️☠️"
        }

        image_url = obb_response["image_url"]
        button1_text = obb_response["button1_text"]
        button1_url = obb_response["button1_url"]
        button2_text = obb_response["button2_text"]
        button2_url = obb_response["button2_url"]
        caption = obb_response["caption"]

        # Create an inline keyboard with two buttons linked to the specified URLs
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(button1_text, url=button1_url),
                    InlineKeyboardButton(button2_text, url=button2_url)
                ]
            ]
        )
        # Reply with a message containing the inline keyboard and the specified image
        sent_message = await message.reply_photo(
            photo=image_url,
            caption=caption,
            reply_markup=reply_markup
        )
        # Wait for 30 seconds before deleting the message
        await asyncio.sleep(30)

        # Delete the sent message
        await sent_message.delete()
    else:
        # If message does not contain 'obb', do nothing
        pass
