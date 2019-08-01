from discord.ext import commands

from .utils import HmBotCommand

class HmBotReact(HmBotCommand):
    """HmBot command to mass react to messages from a specific user."""

    EMOTE_MAX = 10
    
    @commands.command(name="react")
    @commands.guild_only()
    async def manage_mass_reacts(self, ctx, action=None, user=None, emote=None):
        """Massively reacts to messages from a specific user."""
        print(ctx.invoked_subcommand)
        # If no action is provided, print usage
        if action is None:
            await self.send_message("react_usage", ctx)
            return
        # Get needed variables
        reacts = self.get_react_list(ctx.message)
        # If action provided is "list", print the supported languages
        if action == "list":
            await self.send_message("react_list", ctx, user=ctx.message.author, reacts=reacts)
            return
        emotes = self.get_reacts(ctx.message)
        if len(emotes) > self.EMOTE_MAX:
            return await ctx.send("TODO: NO MORE MESSAGES")
        print("react 1", ctx)
        print("react 2", ctx.guild.id)
        print("react 3", ctx.message)
        print("react 4", emote)
        print("react 5", user)
        await self.send_message("TODO: CONFIRM EMOTES")
    
    @commands.Cog.listener()
    async def on_message(self, message):
        # Check if react commands are in the database
        emotes = self.get_reacts(message)
        for emote in emotes:
            print(emote)
    
    def get_react_list(self, message):
        with self.conn as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT emote_id FROM hm_react WHERE guild_id = %s AND user_id = %s",
                            (message.guild.id, message.author.id))
                return cur.fetchall()
