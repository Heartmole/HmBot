from discord.ext import commands

from .utils import HmBotCommand

class HmBotPing(HmBotCommand):
    @commands.command()
    async def ping(self, ctx):
        # TODO: Edit this with another command
        await self.send_message("ping_first", ctx)
