TOKEN = "YOUR TOKEN"
import urllib.request
import json
import random
from ia.m import MarkovChain

global mm
global model
model = MarkovChain([""])
mm = MarkovChain([""])

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command(name="hola")
async def ping(ctx):
    await ctx.send('pong')
@bot.command("random-text")
async def markov_gen(ctx, seed, numw, a):
    global model
    first = a.replace("_", " ")
    corpus = first.split(";")
    model.corpus = corpus
    model.train(True)
    response = "".join(model.ultigen(seed, int(numw)))
    print(response)
    await ctx.send(response)
@bot.command("rtext")
async def better_markov_gen(ctx, seed, numw, a):
    global mm
    first = a.replace("_", " ")
    corpus = first.split(";")
    mm.corpus = corpus
    mm.train(False)
    response = "".join(mm.ultigen(seed, int(numw)))
    await ctx.send(response)
@bot.command("helper")
async def help_msg(ctx):
    await ctx.send("COMMANDS WITH $ \n $random-text → makes a markov model to send a random message, use → $random-text [SEED] [number_of_words] [corpus, replace spaces with '_' and for separate things use ';'] \n $rtext → for do the same but in this time the system learns (no elimina el vocabulario y los datos de antes), use → the same \n $hola → Swelshiniano say's 'Pong' \n $helper → displays this message \n $reset-vocab → rests te vocabulary of the bot (at rtext) \n $save → saves the current vocab \n $load → loads the saved vocab\n$text → is the same than '$rtext' but in this you only write seed and number of words \n \n NOTA → save y load necesitan de un arguente que es el nombre del archivo")
@bot.command("reset-vocab")
async def reset(ctx):
    global mm
    mm.vocablo = []
    await ctx.send("Vocablo Reseteado Correctamente")
@bot.command("text")
async def ret_text(ctx, a, b):
    global mm
    response = "".join(mm.ultigen(a, int(b)))
    await ctx.send(response)
@bot.command("save")
async def save_vo(ctx, file):
    global mm
    mm.save_vocab(file)
    await ctx.send("Vocablo Guardado con éxito")
@bot.command("load")
async def load_vo(ctx, file):
    global mm
    mm.load_vocab(file)
    await ctx.send("Vocablo Cargado con éxito")
bot.run(TOKEN)
