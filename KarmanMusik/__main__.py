import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from KarmanMusik import LOGGER, app, userbot
from KarmanMusik.core.call import Karman 
from KarmanMusik.plugins import ALL_MODULES
from KarmanMusik.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
        and not config.STRING6
        and not config.STRING7
        and not config.STRING8
        and not config.STRING9
        and not config.STRING10
    ):
        LOGGER("KarmanMusik").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("KarmanMusik").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("KarmanMusik.plugins" + all_module)
    LOGGER("KarmanMusik.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await Karman.start()
    karman = await app.get_me()
    KarmanMusik = karman.username
    await userbot.one.send_message("obrolansuar", f"@{KarmanMusik}")
    try:
        await Karman.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("KarmanMusik").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    except:
        pass
    await Karman.decorators()
    LOGGER("KarmanMusik").info("Karman Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("KarmanMusik").info("Stopping Karman Music Bot! GoodBye")
