from discord.ext import commands

from .base import HmBotFeature

class HmBotShitpost(HmBotFeature, name="Shitpost"):
    """Shitpost commands for HmBot."""

    @commands.group()
    @commands.guild_only()
    async def flag(self, ctx):
        """HmBot command to apply a flag filter to an image."""
        if ctx.invoked_subcommand is None:
            return await self.send_message("flag_usage", ctx)

    @flag.command(name="list")
    async def flag_list(self, ctx):
        # TODO: Get the list of flags from the assets folder
        flags = ["pe", "us", "ve", "ec", "ch", "todos los de ISO bla bla bla", "lgbt flags", "etc"]
        await ctx.send(", ".join(flags))

    @flag.command(name="apply")
    async def flag_apply(self, ctx):
        """Adds a flag filter to an image from an attachment or a URL."""
        await ctx.send("TODO")
