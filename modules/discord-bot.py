from imports import load_dotenv, os, asyncio, datetime, commands, timezone
from linked_in_bot import messages

# Set Timezone
date = datetime.datetime.now()
time = date.astimezone(timezone("US/Pacific"))

# Secure personal key
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

# Initiate discord bot
bot = commands.Bot(command_prefix="$")

# Send messages to discord
async def schedule_daily_message() -> None:
    await bot.wait_until_ready()
    channel = await bot.fetch_channel(GUILD)
    msg_sent = False
    while True:
        if time.hour == 8 and time.minute == 0:
            if not msg_sent:
                while messages != []:
                    await channel.send(messages.pop())
                    msg_sent = True
        else:
            msg_sent = False

        await asyncio.sleep(1)


if __name__ == "__main__":
    bot.loop.create_task(schedule_daily_message())
    bot.run(TOKEN)
