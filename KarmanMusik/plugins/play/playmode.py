from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

from config import BANNED_USERS
from strings import get_command
from KarmanMusik import app
from KarmanMusik.utils.database import (get_playmode, get_playtype,
                                       is_nonadmin_chat)
from KarmanMusik.utils.decorators import language
from KarmanMusik.utils.inline.settings import playmode_users_markup

### Commands
PLAYMODE_COMMAND = get_command("PLAYMODE_COMMAND")


@app.on_message(
    filters.command(PLAYMODE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def playmode_(client, message: Message, _):
    playmode = await get_playmode(message.chat.id)
    Direct = True if playmode == "Direct" else None
    is_non_admin = await is_nonadmin_chat(message.chat.id)
    Group = True if not is_non_admin else None
    playty = await get_playtype(message.chat.id)
    Playtype = None if playty == "Everyone" else True
    buttons = playmode_users_markup(_, Direct, Group, Playtype)
    response = await message.reply_text(
        _["playmode_1"].format(message.chat.title),
        reply_markup=InlineKeyboardMarkup(buttons),
    )
