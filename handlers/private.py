from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgIAAx0CVtdbKgACib1g8ue6OWf2UMw7Bw8JkoseIpuzJgACIgADG-__NsuqcnFmC0PBHgQ")
    await message.reply_text(
        f"""**Salam, Mən {bn} 🎵

Mən səslidə musiqi oxuyuram. Developed by [彡𝚕𝚌𝚓𝚗🎴](https://t.me/elcjn).

yalnız @oldBMB üçün!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠Kanal🛠", url="https://t.me/BMBMMC")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/oldBMB"
                    ),
                    InlineKeyboardButton(
                        "🔊 Dəstəkçi", url="https://t.me/BrendUserBot"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕Dəstək qrupu", url="https://t.me/BrendSUP"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Music Bot Online✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/BMBmmc")
                ]
            ]
        )
   )


