import discord
from discord.ext import commands
from discord import Webhook, RequestsWebhookAdapter
import random
import os
import requests


class CommandesFun (commands.Cog) :
    def __init__ (self, bot) :
        self.bot = bot

    @commands.command(description = "Le bot choisira entre les différentes possibilités que vous allez lui soumettre." )
    async def aleatoire(self, ctx, *choices: str):
        await self.bot.clean(ctx, 1)
        await ctx.send("Parmi les différents choix qui m'ont été proposés, j'ai choisi celui ci -> " + random.choice(choices))
        return


    @commands.command(description ="Êtes vous un bot ? Nous allons le savoir avec cette commande" )
    async def bot(self, ctx) :
        x = ctx.author.bot
        if x == 1 :
            await ctx.send ("Vous êtes un bot")
            return
        else :
            await ctx.send("Vous n'êtes pas un bot")
            return

    @commands.command (description = "Pour récupérer l'emploi du temps sous format .ics")
    async def edt (self, ctx) :
        webhook = Webhook.partial(788179383717855302, '5OkXG1x5EjlLoOWzRkROGwgOSzGWuX4mIHrMFKJ0eh11bMuk_5onyohH0MTnWAYlod6V', adapter=RequestsWebhookAdapter())
        webhook.send("https://ent.univ-paris13.fr/ics/8aCFD", username='Le livreur de la LP MRIT')
