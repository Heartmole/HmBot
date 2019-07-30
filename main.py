import logging
import os

import psycopg2
import psycopg2.extras
from discord.ext import commands
from dotenv import load_dotenv

from cogs import *

load_dotenv()
# Initialize logger
logging.basicConfig(filename="bot.log",
                    format="[%(levelname)s %(asctime)s] %(name)s: %(message)s",
                    level=logging.INFO)
# Initialize database
conn = psycopg2.connect(cursor_factory=psycopg2.extras.DictCursor,
                        dbname="hmbot",
                        user=os.getenv("DB_USERNAME"),
                        password=os.getenv("DB_PASSWORD"),
                        host=os.getenv("DB_HOST"))
# Generate the bot
bot = commands.Bot(command_prefix="hm!")
# Add the commands
bot.add_cog(HmBotFlag(bot, conn))
bot.add_cog(HmBotLang(bot, conn))
bot.add_cog(HmBotPing(bot, conn))
bot.add_cog(HmBotReact(bot, conn))
# Run the bot until a keyboard interrupt
print("Starting HmBot...")
bot.run(os.getenv("BOT_TOKEN"))
# Clean all resources
conn.close()
print("Finished HmBot.")
