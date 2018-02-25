import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from discord.voice_client import VoiceClient

Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "?") #Initialise client bot
react = ":cookie:"
everyone = discord.User()
gen = discord.Channel


if discord.opus.is_loaded():
    print("Voice is on")        #Confirm voice is okay
else:
    print("nope")    

@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server


@client.event
async def joinVoiceChannel():
    channel = client.get_channel('416383115947147268')
    await client.join_voice_channel(channel)

class Music:
    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id] = state

        return state

    async def create_voice_client(self, channel):
        voice = await self.bot.join_voice_channel(channel)
        state = self.get_voice_state(channel.server)
        state.voice = voice

    def __unload(self):
        for state in self.voice_states.values():
            try:
                state.audio_player.cancel()
                if state.voice:
                    self.bot.loop.create_task(state.voice.disconnect())
            except:
                pass

    @commands.command(pass_context=True, no_pm=True)
    async def joe(self, ctx, channel: discord.Channel):
        voice = await bot.join_voice_channel(channel)
        player = voice.create_ffmpeg_player('peter.mp3')
        player.start()


    

@client.event
async def on_message(message):
    if message.content == "hey joe":
        await client.send_message(message.channel, "HEY PETER") 
    if message.content == "joe":
        await joinVoiceChannel()
        
        await client.send_message(message.channel, ":HeyBeter:")
    if message.content == "test":
        await client.send_message(message.channel, 'Hey Peter', tts=True)




    
client.run("NDE2MzgyMjA5MzY5MzA5MjA4.DXEfGw.BImCIMhgcWEGW7J7a_-YDESzcUc") #Replace token with your bots token
