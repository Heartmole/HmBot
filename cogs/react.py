from discord.ext import commands

from .utils import HmBotCommand

class HmBotReact(HmBotCommand):
    """HmBot command to mass react to messages from a specific user."""

    @commands.Cog.listener()
    async def on_message(self, message):
        # print("HmBotReact", message)
        pass
    
    @commands.command()
    async def react(self, ctx, emote=None, user=None):
        """Massively reacts to messages from a specific user."""
        await self.send_message("react_usage", ctx)
