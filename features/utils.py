import time

from discord.ext import commands

from .base import HmBotFeature

class HmBotUtils(HmBotFeature, name="Utilities"):
    """Utility commands for HmBot."""

    @commands.command()
    async def ping(self, ctx):
        """HmBot command to send a test message to check if the bot is properly working."""
        lang = self.get_language(ctx)
        # Send first message and record time
        message = self.localize_message(ctx, "ping_first", lang)
        start = time.time()
        result = await ctx.send(message)
        end = time.time()
        # Send second message
        seconds = round(1000*(end-start), 2)
        message = self.localize_message(ctx, "ping_second", lang, seconds=seconds)
        await result.edit(content=message)

    @commands.group()
    @commands.guild_only()
    async def lang(self, ctx):
        """HmBot command to set the bot language, or show the list of supported languages."""
        if ctx.invoked_subcommand is None:
            return await self.send_message(ctx, "lang_usage")

    @lang.command(name="list")
    async def lang_list(self, ctx):
        """Show the list of supported languages."""
        selected = self.get_language(ctx)
        # Prepare language list
        languages = [self.localize_message(ctx, "lang_list", selected)]
        for key, value in self.messages.items():
            languages.append("- {0} ({1})".format(key, value["name"]))
        # Send message
        await ctx.send("\n".join(languages))

    @lang.command(name="set")
    async def lang_set(self, ctx, code=None):
        """Change the bot language."""
        if code is None:
            return await self.send_message(ctx, "lang_usage")
        # Check that the language code is valid
        result = self.messages.get(code)
        if result is None:
            return await self.send_message(ctx, "lang_invalid", language=code)
        try:
            # Save language code to database
            sql = """INSERT INTO hm_guild (guild_id, lang) VALUES (%(guild)s, %(lang)s)
                ON CONFLICT (guild_id) DO UPDATE SET lang = %(lang)s"""
            with self.database as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, {"guild": ctx.guild.id, "lang": code})
            # Send confirmation message
            await self.send_message(ctx, "lang_selected")
        except:
            self.logger.exception("Could not save language due to a database error")
            await self.send_message(ctx, "lang_error")
