import json
import logging
import os

import psycopg2
import psycopg2.extras
from discord.ext import commands
from dotenv import load_dotenv

from features import *

load_dotenv()
# Initialize logger
logger = logging.getLogger("HmBot")
handler = logging.FileHandler("bot.log")
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter("[%(levelname)s %(asctime)s] %(name)s: %(message)s"))
logger.addHandler(handler)
"""
logging.basicConfig(filename="bot.log",
                    format="[%(levelname)s %(asctime)s] %(name)s: %(message)s",
                    level=logging.INFO)
"""
# Initialize database
database = psycopg2.connect(cursor_factory=psycopg2.extras.DictCursor,
                            dbname=os.getenv("DB_NAME", "hmbot"),
                            user=os.getenv("DB_USER", "hmbot"),
                            password=os.getenv("DB_PASS"),
                            host=os.getenv("DB_HOST"))
# Initialize messages
messages = {}
for filename in os.listdir("lang"):
    code = os.path.splitext(filename)[0]
    with open("lang/" + filename, "r") as file:
        messages[code] = json.load(file)

# Generate the bot
bot = commands.Bot(command_prefix=os.getenv("BOT_PREFIX", "hm!"))
# Add the commands
bot.add_cog(HmBotUtils(bot, database, logger, messages))
# bot.add_cog(HmBotShitpost(bot, database, logger, messages))
# Run the bot until a keyboard interrupt
print("Starting HmBot...")
bot.run(os.getenv("BOT_TOKEN"))
# Clean all resources
database.close()
print("Finished HmBot.")
