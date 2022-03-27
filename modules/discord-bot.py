from dotenv import load_dotenv
import os, asyncio, datetime, pytz
from discord.ext import commands
from pytz import timezone

load_dotenv() #'---.env'


TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix="$")
date = datetime.datetime.now()
time = date.astimezone(timezone('US/Pacific'))

async def schedule_daily_message():
  await bot.wait_until_ready()
  channel = await bot.fetch_channel(957136983950508072)
  msg_sent = False
  print("start")
  while True:
    if time.hour == 18 and time.minute == 17:
      if not msg_sent:
        print('success')
        await channel.send("Good test")
        msg_sent = True
    else:
      msg_sent = False

    await asyncio.sleep(1)

if __name__ == '__main__':
  bot.loop.create_task(schedule_daily_message())
  bot.run(TOKEN)