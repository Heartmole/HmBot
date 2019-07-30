from discord.ext import commands

class HmBotCommand(commands.Cog):
    """Base class for HmBot commands. Includes utilities to access database info and send messages."""
    
    MSG_LANG_DEF = 1 # ID for English
    MSG_LANG_ERROR = "ERROR: Could not find message `{code}` for language ID `{lang}`."
    
    def __init__(self, bot, conn):
        self.bot = bot
        self.conn = conn
    
    async def send_message(self, code, ctx, **kwargs):
        """Localizes a message based on the id, the Discord bot context, and the selected language."""
        # Get the message in the current language defined in the guild information
        with self.conn as conn:
            with conn.cursor() as cur:
                lang = self.get_selected_language(cur, ctx)
                message = self.get_message(cur, code, lang)
                if message is None:
                    message = self.get_message(cur, code, self.MSG_LANG_DEF)
                    if message is None:
                        # Print error message
                        kwargs["code"] = code
                        kwargs["lang"] = lang
                        message = self.MSG_LANG_ERROR
        # Parse message and send it through the bot
        kwargs["prefix"]  = ctx.prefix
        kwargs["command"] = ctx.prefix + ctx.invoked_with
        return await ctx.send(message["message"].format(**kwargs))
    
    def get_selected_language(self, cur, ctx):
        """Get the selected language for the current guild."""
        cur.execute("SELECT * FROM hm_guild WHERE id = %s LIMIT 1", (ctx.guild.id,))
        guild = cur.fetchone()
        return guild["lang_id"] if guild else self.MSG_LANG_DEF
    
    def get_message(self, cur, code, lang):
        cur.execute("SELECT message FROM hm_message WHERE code = %s AND lang_id = %s LIMIT 1",
                    (code, lang))
        message = cur.fetchone()
        return message["message"] if message else None
