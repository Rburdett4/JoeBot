import asyncio
import discord
import random
from discord.ext import commands
import time

if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

class Music:

    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}

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
        player.stop()

    @commands.command(pass_context=True, no_pm=True)
    async def rockthatworld(self, ctx, channel: discord.Channel):
        voice = await bot.join_voice_channel(channel)
        player = voice.create_ffmpeg_player('rockthatworld.mp3')
        player.start()
        player.stop()
            
bot = commands.Bot(command_prefix='.', description='hey peter')
bot.add_cog(Music(bot))
@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user)) 

@bot.event
async def on_message(message):
    if message.content == "hey joe":
            await bot.send_message(message.channel, "HEY PETER") 
    if message.content == "joe":        
            await bot.send_message(message.channel, ":HeyBeter:")
    if message.content == "test":
            await bot.send_message(message.channel, 'Hey Peter', tts=True)
    await bot.process_commands(message)
    

bot.run("KEY")
    
