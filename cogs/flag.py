from discord.ext import commands

from .utils import HmBotCommand

class HmBotFlag(HmBotCommand):
    """HmBot command to apply a flag filter to an image."""
    
    @commands.command(name="flag")
    async def manage_flags(self, ctx, name=None, url=None):
        """Adds a flag filter to an image from an attachment or a URL."""
        if name is None:
            await self.send_message("flag_usage", ctx)
            return
        # TODO: Search through all assets
        await ctx.send("TODO: Search through all assets")
    
    def get_flag_list(self):
        # TODO: Get the list of flags from the assets folder
        flags = ["pe", "us", "ve", "ec", "ch", "todos los de ISO bla bla bla", "lgbt flags", "etc"]
