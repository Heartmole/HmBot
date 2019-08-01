from discord.ext import commands

from .utils import HmBotCommand

class HmBotLang(HmBotCommand):
    """HmBot command to manage bot language changes."""

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO hm_guild (id, lang_id) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING",
                            (guild.id, self.MSG_LANG_DEF))
    
    @commands.command(name="lang")
    @commands.guild_only()
    async def manage_languages(self, ctx, action=None):
        """Changes the bot language, or shows the list of supported languages."""
        # If no action is provided, print usage
        if action is None:
            await self.send_message("lang_usage", ctx)
            return
        # If action provided is "list", print the supported languages
        if action == "list":
            languages = self.get_language_list()
            await self.send_message("lang_list", ctx, languages=languages)
            return
        # Get the language information from database
        lang = self.get_language_info(action)
        if lang is None:
            await self.send_message("lang_unknown", ctx, lang=action)
            return
        # Change the language based on current guild information
        self.change_language(ctx, lang["id"])
        # Show message in the new language
        await self.send_message("lang_selected", ctx)
    
    def get_language_list(self):
        """Get the list of languages from the database and format them to be sent."""
        # Get language list
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM hm_lang WHERE active = true")
                languages = cur.fetchall()
        # Format language list
        return "\n".join(map(format_language, languages))
    
    def format_language(lang):
        return "- {code} ({name})".format(code=lang["code"], name=lang["name"])
    
    def get_language_info(self, lang_code):
        """Get the language information based on its code."""
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM hm_lang WHERE code = %s AND active = true LIMIT 1", (lang_code,))
                return cur.fetchone()
    
    def change_language(self, ctx, lang_id):
        """Change the selected language in the current guild information."""
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE hm_guild SET lang_id = %s WHERE id = %s", (lang_id, ctx.guild.id))
