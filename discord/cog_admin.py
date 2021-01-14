import discord
from discord.ext import commands


class Admin (commands.Cog) :
    def __init__ (self, bot) :
        self.bot = bot

    @commands.command(description = "Le moment où vous avez rejoint ce serveur.")
    async def rejoint(self, ctx, member: discord.Member):
        await self.bot.clean(ctx, 1)
        await self.bot.Admin(ctx)
        await ctx.send('{0.mention} à rejoint le serveur le : {0.joined_at}'.format(member))


    @commands.command(description = "Changer le statut du bot")
    async def changeBotStatus(self, ctx, statut : discord.Game) :
        await self.bot.clean(ctx, 1)
        await self.bot.Admin(ctx)
        await self.bot.change_presence(status=discord.Status.online, activity = statut)
        await ctx.send ("Votre bot à bien changé de statut.")
        return

    @commands.command(description = "Commande de bannissement.")
    async def ban (self, ctx, membre : discord.Member, raison : str) :
        user = self.bot.get_user (membre.id)
        await self.bot.clean(ctx, 1)
        await self.bot.Admin (ctx)
        await self.bot.roles(ctx, membre)
        Bannissement = "Vous êtes banni " + membre.mention +  ". Pourquoi : " + raison
        await self.bot.tableau (ctx, "Bannissement", Bannissement, discord.Colour.blue(), 'https://media.giphy.com/media/3orifbI12fKrcTgYbS/giphy.gif')
        await user.send ("Vous êtes banni du serveur " + ctx.guild.name + " : " + membre.mention + " \n " + raison)
        await membre.ban(reason=raison)


    @commands.command(description = "Commande d'expulsion")
    async def kick (self, ctx, membre : discord.Member, raison : str) :
        user = self.bot.get_user (membre.id)
        await self.bot.clean(ctx, 1)
        await self.bot.Admin (ctx)
        await self.bot.roles(ctx, membre)
        Expulsion = "Vous êtes expulsé " + membre.mention +  ". Pourquoi : " + raison
        await self.bot.tableau (ctx, "Expulsion", Expulsion, discord.Colour.dark_purple(), 'https://media1.tenor.com/images/e4e4730bdc422c5f75b1126926077485/tenor.gif?itemid=4838544')
        await user.send ("Vous êtes banni du serveur " + ctx.guild.name + " : " + membre.mention + " \n " + raison)
        await membre.kick(reason=raison)

    @commands.command (hidden=True, description = "pour les rôles")
    async def roles (self, ctx) :
            await self.bot.Admin(ctx)
            channel = self.bot.get_channel(705450503823163482)
            x = " "
            for i in range (2, 6) :
                x = x + str(i - 1) + " pour le role "  + ctx.guild.roles[i].mention + "\n"
            await self.bot.clean (ctx,1)
            await channel.send(x)
            msg = discord.utils.get(await channel.history(limit = 1).flatten(), author = self.bot.user) # Récuperer le dernier message envoyé par le bot.
            await msg.add_reaction ('<:1_:770017095176945694>')
            await msg.add_reaction ('<:2_:770017132180144158>')
            await msg.add_reaction ('<:3_:770017437218373672>')
            await msg.add_reaction ('<:4_:770017179386118165>')
