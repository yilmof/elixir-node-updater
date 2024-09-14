import discord
import subprocess
import re
import logging
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

# Set up logging to a file
logging.basicConfig(
    filename=os.path.join(os.getcwd(), 'bot.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID")

if not TOKEN:
    raise EnvironmentError("Missing required environment variable: DISCORD_TOKEN")

if not CHANNEL_ID:
    raise EnvironmentError("Missing required environment variable: DISCORD_CHANNEL_ID")

SCRIPT_PATH = os.path.join(os.getcwd(), 'update_elixir.sh')

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

async def execute_bash_script(channel):
    try:
        logging.info("Executing the update script...")
        process = subprocess.Popen([SCRIPT_PATH], shell=True, executable='/bin/bash', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            logging.info("Script executed successfully.")
            await channel.send("✅ The validator update was successful!")
        else:
            error_message = stderr.decode('utf-8')
            logging.error(f"Script failed with error: {error_message}")
            await channel.send(f"❌ The validator update failed with the following error:\n```{error_message}```")
    except Exception as e:
        logging.error(f"An error occurred while executing the script: {e}")
        await channel.send(f"❌ An error occurred while trying to run the update script:\n```{e}```")

@client.event
async def on_ready():
    logging.info(f'Bot has logged in as {client.user}')
    print(f'Bot has logged in as {client.user}')

@client.event
async def on_message(message):
    print(message.content)
    if message.channel.id == int(CHANNEL_ID) and ("validator version" in message.content.lower()) and ("priority" in message.content.lower()):
        logging.info("Detected a new update message in the channel.")

        version = re.search(r'Validator version (\d+\.\d+\.\d+)', message.content)
        if version:
            logging.info(f"New version detected: {version.group(1)}")

        # Wait 90 seconds before proceeding with the update
        await message.channel.send(" ⏳Waiting 90 seconds before starting the update...")
        await asyncio.sleep(90)

        # After waiting, execute the bash script and send success or error message to the channel
        await execute_bash_script(message.channel)

# Run the client
client.run(TOKEN)