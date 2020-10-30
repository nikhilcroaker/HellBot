import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, hellversion
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"
PM_IMG = "https://telegra.ph/file/643ce03c1e9dc3f73938a.mp4"
pm_caption = "🔥🔥**Nɪᴛʀɪᴄ Bᴏᴛ Is Oɴ Tᴀʙᴀʜɪ🔥🔥\n\n\n"

pm_caption += f"🎌 Bᴏᴛ Pᴏᴡᴇʀᴇᴅ ʙʏ        : {DEFAULTUSER}\n\n"

pm_caption += "🎌 Tᴇʟᴇᴛʜᴏɴ               : 1.15.0 \n\n"

pm_caption += f"🎌 Vᴇʀsɪᴏɴ               : `{hellversion}`\n\n"

pm_caption += "🌐 Cʜᴀɴɴᴇʟ                : Jᴏɪɴ(https://t.me/NoobCheats)\n\n"

pm_caption += "🌠 Gʀᴏᴜᴘ                  : Jᴏɪɴ(https://t.me/NoobCheatSupport)\n\n"

pm_caption += "🎫 Lɪᴄᴇɴsᴇ                : Lɪᴄᴇɴsᴇ(https://github.com/HellBoy-OP/HellBot/blob/master/LICENSE)\n\n"

pm_caption += "🎭 Cʀᴇᴀᴛᴏʀ                : Bᴏᴛ Oᴡɴᴇʀ(https://t.me/Its_Nitric)\n\n"


#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
