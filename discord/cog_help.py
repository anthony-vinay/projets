import discord
from discord.ext import commands
import math
import random

couleurs = [0, 0x3498db, 0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xe67e22, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a, 0x7289da, 0x99aab5, 0x36393F]

class Help (commands.Cog) :
    def __init__ (self, bot) :
        self.bot = bot

    @commands.command (aliases = ['a'])
    async def aide (self, ctx):
        await self.bot.clean(ctx, 1)
        help = discord.Embed (
            title = "Voici les commandes !  ",
            color = random.choice(couleurs)
            )

        categories = [c for c in self.bot.cogs.keys()]

#Admin
        categories.remove ('Help')
        if ctx.author.guild_permissions.administrator == False :
            categories.remove('Admin')

        for cog in categories : #pour chaque catégorie
            liste = ""
            for commandes in self.bot.get_cog(cog).walk_commands() : # pour chaque commande présente dans "categories"
                liste = liste + f"**{commandes.name}** - *{commandes.description}* " + "\n"

            help.add_field(name = cog, value = liste, inline = False ) # ajout de la commande et de sa description dans un tableau
            
        await ctx.send (embed = help)
