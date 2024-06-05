import discord
import os
import random
from dotenv import load_dotenv
from ec2_metadata import ec2_metadata  # Import the ec2_metadata module

# Load the environment variables from the .env file
load_dotenv()

# Define intents to control what events the bot will listen to
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Create a client instance with the specified intents
client = discord.Client(intents=intents)

# Retrieve the bot token from the environment variable
token = os.getenv('TOKEN')

# Print the bot token for debugging purposes
print("token:", token)

# Print EC2 metadata
print('This is my Ec2_metadata.region:', ec2_metadata.region)
print('This is my Ec2_metadata.instance.id:', ec2_metadata.instance_id)

# Event handler: called when the bot is ready and connected to Discord
@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

# Event handler: called whenever a message is sent in any server the bot is in
@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]  # Extract the username from the message author's name
    channel = str(message.channel.name)  # Get the name of the channel where the message was sent
    user_message = str(message.content)  # Get the content of the message sent by the user

    # Print information about the message to the console
    print(f'Message "{user_message}" by {username} on {channel}')

    # Ignore messages sent by the bot itself to avoid infinite loops
    if message.author == client.user:
        return

    # Check if the message was sent in the "general" channel
    if channel == "general":
        # Respond to certain messages with predefined replies
        if user_message.lower() in ["hello", "hi"]:
            await message.channel.send(f'Hello {username} Your EC2 Data: {ec2_metadata.region}')
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}')
        elif user_message.lower() == "tell me a joke":
            jokes = [
                "Why did Luis Cross the road",
                "Why did Kevin Cross the road",
                "Why did Andrew Cross the road"
            ]
            await message.channel.send(random.choice(jokes))
            
        # Respond to the command "show me a gif" with a random GIF
        elif user_message.lower() == "show me a gif":
            gifs = [
                "https://giphy.com/gifs/looneytunesworldofmayhem-world-of-mayhem-looney-tunes-ltwom-RbDKaczqWovIugyJmW",
                "https://giphy.com/gifs/quixyofficial-coding-programming-computer-science-JCOY3YxLsEbmtaUkgZ",
                "https://giphy.com/gifs/Massivesci-robots-ai-artificial-intelligence-WxJLwDBAXDsW1fqZ3v"
            ]
            await message.channel.send(random.choice(gifs))

# Run the client with the provided token to connect to Discord
client.run(token)
