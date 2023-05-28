
import requests 
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#NAME -> YOUR BOTS FILE NAME 
from camellia import pbot as app


def call_back_in_filter(data):
    return filters.create(lambda flt, _, query: flt.data in query.data,
                          data=data)



@app.on_callback_query(call_back_in_filter('quote'))
async def callback_quotek(_, query):
    if query.data.split(":")[1] == "change":
        #         query.message.delete()
        kk = requests.get('https://animechan.vercel.app/api/random').json()
        anime = kk['anime']
        quote = kk['quote']
        character = kk['character']
        caption = f"""
** ANIME:** `{anime}`

** CHARACTER:** `{character}`

** QUOTE:** `{quote}`"""
        await query.message.edit(caption,
                           reply_markup=InlineKeyboardMarkup([
                               [
                                   InlineKeyboardButton(
                                       "CHANGE 🔄", callback_data="quotek:change")
                               ],
                           ]))


@app.on_message(filters.command('aniquote'), group=91)
async def quote(_, message):
    kk = requests.get('https://animechan.vercel.app/api/random').json()
    anime = kk['anime']
    quote = kk['quote']
    character = kk['character']
    caption = f"""
** ANIME:** `{anime}`

** CHARACTER:** `{character}`

** QUOTE:** `{quote}`"""
    await message.reply(caption, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("CHANGE 🔄", callback_data="quotek:change")]]))")
