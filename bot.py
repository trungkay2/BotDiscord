# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
import asyncio

load_dotenv()
TOKEN = 'ODg5NDQ1NzkzNTc5MzAyOTIz.YUhW8g.K5xHpFmk3E74GQ8_T_6PZ3YHGqo'
GUILD = 'km10NguyenTrai'




#2
bot = commands.Bot(command_prefix='!')

@bot.command(name='cmsn')
async def cmsn(ctx):
    await ctx.send('Happy Birthday! 🎈🎉')
    

@bot.command(name='ptit', help='Trash talk')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'Hello guys',
        'Oke!!!',
        'Khỏe bạn ơi',
        'Bye bye',
        'Bạn là nhất',
        'Anh Tuấn đẹp trai',
        'Hoàng nghiện',
        'Lâm Bùi đẹp trai',
        'Vua Việt',
        'Đức chúa',
        'Duy duong ngáo vl',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='random', help='Simulates rolling dice with two parameters(output, range).')
async def roll(ctx, number_of_dice:int, number_of_sides:int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

#đang sai
# @bot.command(name='join')
# async def join(ctx):
#     channel = ctx.author.voice.channel
#     await channel.connect()
# @bot.command(name='leave')
# async def leave(ctx):
#     await ctx.voice_client.disconnect()
# bot.run(TOKEN)