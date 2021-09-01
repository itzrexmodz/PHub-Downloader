from phub import bot
from telethon import events

@bot.on(events.NewMessage(pattern="^[!/]start$"))
async def phub_start(e):
 if not e.is_private:
   return
 
