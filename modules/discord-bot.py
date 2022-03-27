from dotenv import load_dotenv
import os, asyncio, datetime, pytz
from discord.ext import commands
from pytz import timezone

#Set Timezone
date = datetime.datetime.now()
time = date.astimezone(timezone('US/Pacific'))

#Secure personal key
load_dotenv() 
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#Initiate discord bot
bot = commands.Bot(command_prefix="$")

#Main Function
async def schedule_daily_message():
  await bot.wait_until_ready()
  channel = await bot.fetch_channel(GUILD)
  msg_sent = False
  print("start")
  while True:
    if time.hour == 18 and time.minute == 40:
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