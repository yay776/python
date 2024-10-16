import discord
from discord.ext import commands
import random
import os
classify_residuos = {
    "botles": "Las botellan van en la caneca negra.",
     
}
def clasificar_residuos(objeto):
    return classify_residuos.get(objeto.lower(), "No tengo informacion sobre este objeto")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.command('clasificar')
async def clasificar(ctx, *, objeto:str):
    respuesta = clasificar_residuos(objeto)
    await ctx.send(f"Clasificacion: {respuesta}")
    
bot.run("MTI5NTkyMDc1NzgyNTg2Nzc3Ng.G1aKYC.h_De_svfAev5fuVhys0hEA0a7SL21GLLJlIWN4")
