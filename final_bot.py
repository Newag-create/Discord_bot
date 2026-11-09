import discord
from discord.ext import commands
from bot_logic import coin_toss 
from bot_logic import gen_pas
from bot_logic import emoi
from bot_logic import random_fact
from bot_logic import get_duck_image_url
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')
    channel = bot.get_channel(1498365960153989284)  # ID kanału
    
    if channel:
        await channel.send(
            f'Cześć👋, jestem {bot.user}!\n'
            'PL:Jeśli chcesz wygenerować hasło to napisz $password. '
            'Albo możesz wylosować emotkę😉. Wystarczy, że napiszesz $emoj. '
            'Jeżeli chcesz rzucić monetą🪙, to napisz $toss.' 
            'Mogę również wylosować coś o zmianach klimatycznych (czym są, jakie są ich przyczyny, co można robić). Po prostu napisz $fact  '
            'EN: Hello👋! '
            'If you want to generate a password, type $password. '  
            'Or you can pick a random emoji😉. Just type $emoj. '  
            'If you want to flip a coin🪙, type $toss. '
            'I can also draw something about climate changes (what they are, what their causes are, what can we do about them). Just type $fact')
@bot.command()
async def toss(ctx):
    await ctx.send("Co wypadło|What came out: " + coin_toss())
@bot.command()
async def emoj(ctx):
    await ctx.send(emoi())
@bot.command()
async def password(ctx):
    await ctx.send("Twoje hasło|Your password: " + gen_pas(10))
@bot.command()
async def fact(ctx):
    await ctx.send(random_fact())
@bot.command()
async def duck(ctx):
    await ctx.send(get_duck_image_url())
bot.run("TOKEN")
