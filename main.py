from discord.ext import commands
import discord
from dotenv import load_dotenv
from downloader import download_tiktok
import os


load_dotenv()

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="!", help_command=None)


@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(f"Error syncing commands: {e}")

    print(f"{bot.user.name} is ready!")


@bot.event
async def on_message(ctx: discord.Message):
    if ctx.content.startswith("https://www.tiktok.com/") or ctx.content.startswith(
        "https://vm.tiktok.com/"
    ):
        await ctx.delete()
        download_tiktok(ctx.content)
        with open("tiktok.mp4", "rb") as f:
            await ctx.channel.send(file=discord.File(f))


bot.run(os.getenv("BOT_TOKEN"))
