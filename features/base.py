from discord.ext import commands

class HmBotFeature(commands.Cog):
    """Base feature class for HmBot commands. Includes utilities to access database info and send messages."""

    MSG_LANG_DEF = "en"
    MSG_LANG_ERROR = "ERROR: Could not find message with code `{code}`."

    def __init__(self, bot, database, logger, messages):
        self.bot = bot
        self.database = database
        self.logger = logger
        self.messages = messages

    async def send_message(self, ctx, code, **kwargs):
        """Localize and send a message based on the selected language in the guild information."""
        lang = self.get_language(ctx)
        message = self.localize_message(ctx, code, lang, **kwargs)
        return await ctx.send(message)

    def get_language(self, ctx):
        """Get the selected language in the guild information, or the default language if none was found."""
        try:
            with self.database as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT lang FROM hm_guild WHERE guild_id = %s LIMIT 1", (ctx.guild.id,))
                    result = cur.fetchone()
            return result[0] if result else self.MSG_LANG_DEF
        except:
            self.logger.exception("Could not find language due to a database error")
            return self.MSG_LANG_DEF

    def localize_message(self, ctx, code, lang, **kwargs):
        """Localize a message based on the selected language."""
        try:
            message = self.messages[lang][code]
        except KeyError:
            message = self.messages[self.MSG_LANG_DEF][code]
        except KeyError:
            message = self.MSG_LANG_ERROR
        kwargs["command"] = ctx.prefix + ctx.invoked_with
        return message.format(**kwargs)
