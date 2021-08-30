from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgIAAx0CVtdbKgACwP9hLUNLBjE8B98QPApKGixyHEx-lAACbgwAAo1DiUolFuOVLYr4th4E")
    await message.reply_text(
        f"""**Salam, Mən {bn} 🎵

Mən səslidə musiqi oxuyuram. Developed by [彡𝚕𝚌𝚓𝚗🎴](https://t.me/elcjn).

 @oldzona üçün**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠Kanal🛠", url="https://t.me/BrendBots")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/oldzona"
                    ),
                    InlineKeyboardButton(
                        "Sahib", url="https://t.me/shirnovff"
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
                        "🔊 Qrup", url="https://t.me/oldzona")
                ]
            ]
        )
   )


