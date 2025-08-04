import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.dm_messages = True

class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # Sync global commands so they work in guilds and DMs
        await self.tree.sync()

bot = MyBot()

# Create a slash command that works in both DMs and guilds
@bot.tree.command(name="hello", description="Say hello!")
async def hello(interaction: discord.Interaction):
    location = "DMs" if isinstance(interaction.channel, discord.DMChannel) else f"guild: {interaction.guild.name}"
    await interaction.response.send_message(f"Hello, {interaction.user.name}! You are using this in {location}.")

bot.run("YOUR_BOT_TOKEN")
