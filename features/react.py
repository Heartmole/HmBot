import typing

from discord.ext import commands

from .base import HmBotFeature

"""
TODO: REWRITE THIS
"""

class HmBotReact(HmBotFeature):
    """HmBot command to mass react to messages from a specific user."""

    EMOJI_OWN_MAX = 10
    EMOJI_GIVEN_MAX = 10

    @commands.group()
    @commands.guild_only()
    async def react(self, ctx):
        """Massively reacts to messages from a specific user."""
        # If no subcommand is provided, print usage
        if ctx.invoked_subcommand is None:
            return await self.send_message("react_usage", ctx)
        """
        print("react 1", ctx)
        print("react 2", ctx.guild.id)
        print("react 3", ctx.message)
        print("react 4", emote)
        print("react 5", user)
        await self.send_message("TODO: CONFIRM EMOTES", ctx)
        """

    @react.command(name="list")
    async def react_list(self, ctx):
        # Get both own reacts and given reacts
        with self.database as conn:
            with conn.cursor() as cur:
                own = self.get_own_reacts(ctx.message, cur)
                given = self.get_given_reacts(ctx.message, cur)
        # Format reacts
        own = "\n".join(map(self.format_own_react, own))
        given = "\n".join(map(self.format_given_react, given))
        # Send message
        await self.send_message("react_list", ctx, user=ctx.message.author, own=own, given=given)

    @react.command(name="add")
    async def react_add(self, ctx, emote: typing.Union[commands.PartialEmojiConverter, str, None],
                        user: typing.Optional[commands.MemberConverter]):
        # If a parameter was not given, show usage
        if emote is None or user is None:
            await self.send_message("react_usage", ctx)
            return
        # Check if react counts have not maxed out
        with self.database as conn:
            with conn.cursor() as cur:
                own_count = self.get_given_react_count(ctx.guild, ctx.message.author, cur)
                given_count = self.get_given_react_count(ctx.guild, user, cur)
        if own_count >= self.EMOJI_OWN_MAX:
            return await self.send_message("react_given_max", ctx, count=self.EMOJI_OWN_MAX)
        if given_count >= self.EMOJI_GIVEN_MAX:
            return await self.send_message("react_given_max", ctx, count=self.EMOJI_GIVEN_MAX, user=user)
        # Check if
        print(type(emote))
        print(type(user))
        print("add", own_count, emote, user)
        # givencount = self.get_own_react_count(cur, ctx.message)
        pass

    @react.command(name="remove")
    async def remove_mass_react(self, ctx, emote: typing.Union[commands.PartialEmojiConverter, str, None],
                                user: typing.Optional[commands.MemberConverter]):
        # If a parameter was not given, show usage
        if emote is None or user is None:
            await self.send_message("react_usage", ctx)
            return
        with self.database as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM hm_react WHERE 1 = 0")

    @commands.Cog.listener()
    async def on_message(self, msg):
        # Check if react commands are in the database
        with self.database as conn:
            with conn.cursor() as cur:
                reacts = self.get_given_reacts(cur, msg)
        # React with all given emotes
        for react in reacts:
            # Get the emote object
            print(react)

    def get_own_reacts(self, msg, cur):
        cur.execute("SELECT * FROM hm_react WHERE guild_id = %s AND owner_id = %s",
                    (msg.guild.id, msg.author.id))
        return cur.fetchall()
    
    def get_own_react_count(self, guild, owner, cur):
        cur.execute("SELECT COUNT(*) FROM hm_react WHERE guild_id = %s AND owner_id = %s",
                    (guild.id, owner.id))
        result = cur.fetchone()
        return result[0] if result else 0

    def format_own_react(self, react):
        # TODO
        return "TODO: A react you own!"

    def get_given_reacts(self, msg, cur):
        cur.execute("SELECT * FROM hm_react WHERE guild_id = %s AND user_id = %s",
                    (msg.guild.id, msg.author.id))
        return cur.fetchall()

    def format_given_react(self, react):
        # TODO
        return "TODO: A react you were given!"

    def get_given_react_count(self, guild, user, cur):
        cur.execute("SELECT COUNT(*) FROM hm_react WHERE guild_id = %s AND user_id = %s",
                    (guild.id, user.id))
        result = cur.fetchone()
        return result[0] if result else 0
