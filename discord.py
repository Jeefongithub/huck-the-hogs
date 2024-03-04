import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import score
import pig_roll
import image

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='/', intents=intents)
print('Huck the Hogs successfully initiated.')

current_games = {}

class Player:
    def __init__(self, name, total_score, current_score, is_my_turn):
        self.name = name
        self.total_score = total_score
        self.current_score = current_score
        self.is_my_turn = is_my_turn

# Handle all other errors
@bot.event
async def on_command_error(ctx, error):
    pass

@bot.command(name='huckthehogs', help='Initialize the game') # initialize the game
async def init_game(ctx):
    print(ctx.guild.id)

