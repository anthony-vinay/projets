import discord
from discord.ext import commands
import random
import cog_commands
import cog_admin
import cog_help


intents = discord.Intents.default()
intents.members = True
intents.messages = True

#Définition du préfixe, de l'aide aux commandes et des "intents"
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)
couleurs = [0, 0x3498db, 0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xe67e22, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a, 0x7289da, 0x99aab5, 0x36393F]

@bot.event
async def time () :
    while true :
        channel = bot.get_channel(707973610744053861)
        if time.localtime[3] == "10" and time.localtime[4] == "25" and time.localtime[5] == "0" :
            await channel.send ("Bonjour ! ")
@bot.event
async def on_ready(): # Lorsque le bot se lance.
    await bot.change_presence(status=discord.Status.online, activity = discord.Game("En attente d'ordres ! ")) # Changer l'état du statut
    print ('Bot opérationnel : ')
    print(bot.user.name)
    print (bot.user.id)
    print ('-------')

@bot.event
async def on_command_error (ctx, error) :
    if isinstance (error, commands.MemberNotFound) :
        await clean (ctx, 1)
        await ctx.send(f"Le membre {error.argument} n'existe pas dans ce serveur. Veuillez vérifier l'orthographe et/ou que l'utilisateur est présent dans ce serveur.")
    if isinstance (error, commands.CommandNotFound) :
        await ctx.send ("Elle existe cette commande ?!? En tout cas pas pour moi")

@bot.event
async def on_message (ctx) : # fonction que j'utilise pour les DM's
    await bot.process_commands(ctx)
    if ctx.author == bot.user :
        return

    if isinstance (ctx.channel, discord.DMChannel) : # Si message ecrit dans les DM's du bot
        identite = ctx.author.id
        if identite != 532222326134145025 : # Seul Snooze peut envoyer des dm
            await ctx.author.send ("Tu n'as pas le droit de me DM, mon créateur a été prévenu")
            await mp (ctx, "Cette personne -> " +  ctx.author.mention + " à essayé de m'envoyer un message privé, mais pour qui il se prend !" + "\n" + "Voici le contenu du message : " + ctx.content)
        else :
            channel = bot.get_channel (772538410358800385)
            channel1 = bot.get_channel (765951389368057876)
            await channel.send (ctx.content) # envoi du contenu récupéré depuis les DM's # La Team
            await channel1.send (ctx.content) # MRIT

@bot.event
async def on_reaction_add (reaction, user) : # Se base sur les messages après lancement du bot, anciennnes réactions aux messages ignorés.
    if user.id == 765479675962195969 : # le bot
        return

    else :
        if reaction.message.channel.id != 705450503823163482 : # Si nous ne sommes pas dans le salon #roles
            pass
        else :
            emoji1 = bot.get_emoji(770017095176945694)
            role1 = discord.utils.get(user.guild.roles, name = 'Streamer')

            emoji2 = bot.get_emoji(770017132180144158)
            role2 = discord.utils.get(user.guild.roles, name = 'FORTNITE')

            emoji3 = bot.get_emoji(770017437218373672)
            role3 = discord.utils.get(user.guild.roles, name = 'ROCKET-LEAGUE')

            emoji4 = bot.get_emoji(770017179386118165)
            role4 = discord.utils.get(user.guild.roles, name = 'GENSHIN IMPACT')

            if reaction.emoji == emoji1 :
                await user.add_roles(role1)

            elif reaction.emoji == emoji2 :
                await user.add_roles(role2)

            elif reaction.emoji == emoji3 :
                await user.add_roles(role3)

            elif reaction.emoji == emoji4 :
                await user.add_roles(role4)

@bot.event
async def on_reaction_remove (reaction, user) :
    if user.id == 765479675962195969 : # le bot
        pass
    else :
        if reaction.message.channel.id != 705450503823163482 : # Si nous ne sommes pas dans le salon #roles
            pass
        else :
            emoji1 = bot.get_emoji(770017095176945694)
            role1 = discord.utils.get(user.guild.roles, name = 'Streamer')

            emoji2 = bot.get_emoji(770017132180144158)
            role2 = discord.utils.get(user.guild.roles, name = 'FORTNITE')

            emoji3 = bot.get_emoji(770017437218373672)
            role3 = discord.utils.get(user.guild.roles, name = 'ROCKET-LEAGUE')

            emoji4 = bot.get_emoji(770017179386118165)
            role4 = discord.utils.get(user.guild.roles, name = 'GENSHIN IMPACT')

            if reaction.emoji == emoji1 :
                await user.remove_roles(role1)

            elif reaction.emoji == emoji2 :
                await user.remove_roles(role2)

            elif reaction.emoji == emoji3 :
                await user.remove_roles(role3)

            elif reaction.emoji == emoji4 :
                await user.remove_roles(role4)

@bot.event
async def on_member_join(ctx): # Fonction appelé lorsqu'une personne rentre dans le serveur
    channel = bot.get_channel (ctx.guild.system_channel.id) # ID du channel sur lequel on souhaite envoyer le message
    bienvenue = "Bienvenue à " + ctx.mention + " sur le serveur !" # contenu du message de bienvenue
    embed = discord.Embed(title = "Bienvenue",description = bienvenue, color = random.choice (couleurs)) # créer un embed où intégrer les précédentes informations.
    embed.set_thumbnail (url = ctx.avatar_url) # récupération du la photo de profil (coté esthetique)
    await channel.send(embed=embed) # envoi du embed

@bot.event
async def on_member_remove(ctx): # Fonction appelé lorsqu'une personne quitte le serveur
    channel =  bot.get_channel(ctx.guild.system_channel.id) # ID du channel sur lequel on souahite envoyer le message
    bye = ctx.mention + "nous à quitté, tant pis ! " # contenu du message d'au revoir
    embed = discord.Embed(title = "Au revoir",description = bye, color = random.choice (couleurs)) #créer un embed où intégrer les précédentes informations.
    embed.set_thumbnail (url = ctx.avatar_url) # récupération du la photo de profil (coté esthetique)
    await channel.send(embed=embed) # envoi du embed

@bot.event
async def Admin(ctx): # Fonction pour éxécuter les commandes Administrateurs
    guild = ctx.author.guild

    if ctx.author.guild_permissions.administrator == True : # Es-tu administrateur ?

        if ctx.author.guild.id == 690730758297354246 : #La Team
            channel = bot.get_channel (720729893771542538)
            if ctx.channel.id != 720729893771542538  :
                await ctx.send ("Votre requête ne peut se faire que si vous êtes sur le salon textuel : " + channel.mention )
                raise Exception

        elif ctx.author.guild.id == 763686049490534420 : #MRIT
            channel1 = bot.get_channel (765951389368057876)
            if ctx.channel.id != 765951389368057876 :
                await ctx.send ("Votre requête ne peut se faire que si vous êtes sur le salon textuel : " + channel1.mention )
                raise Exception
    else :
            await ctx.send(ctx.author.mention + ", t'es pas admin mec. Aucun ordre à recevoir pour cette commande de ta part. ")
            await mp (ctx, "Cette personne" + ctx.author.mention + ", essaye d'utiliser une commande d'administrateur sans avoir les droits requis ")
            raise Exception

@bot.event
async def mp (ctx, contenu : str) :
    user = bot.get_user (532222326134145025) # récupération des ID des personnes qui recevront le mp
    user1 = bot.get_user (501027521337491467)
    user2 = bot.get_user (455785954691514399)
    adam = bot.get_user (128551356209430528)
    auteur = bot.get_user (ctx.author.id)
    if ctx.author.id == 532222326134145025 or ctx.author.id == 501027521337491467 or ctx.author.id == 455785954691514399  : # Si commande provient d'un SuperAdmin
        pass
    else : # Sinon envoi d'un mp

        await user.send (contenu) # Envoi d'un mp à Snooze

        if ctx.author.guild.id == 690730758297354246 :  # La team
            await user1.send (contenu) # Envoi d'un mp à Seyl
            #await user2.send (contenu) # Envoi d'un mp à Nat_Life

        elif ctx.author.guild.id == 763686049490534420 : # discord MRIT
            await adam.send (contenu)


@bot.event # permettre un check de différences entre deux rôles.
async def roles (ctx, role : discord.Member) :
    myrole = ctx.author.roles[-1] # dernier rôle de la liste Role : le plus élevé
    hisrole = role.roles # role du membre
    X = 0
    for i in range (0, len(hisrole)) : # Compter le nombre de roles que possède la personne.
        if myrole.position > hisrole[i].position : # Si ma position de rôle est plus élevé que celle du membre
            pass
        else :
            X = X + 1 # incrémenter X
            #print (X) #Déboggage

    if X > 0 : # Si aucun de mes rôles n'est égal ou inférieur à ceux du membre
        await ctx.send ("Vous ne pouvez pas exécuter cette commande car vous possédez le même rôle que " + role.mention + " ou que son rôle est supérieur au votre ")
        await mp(ctx, "Cette personne " + ctx.author.mention + ", n'a pas les rôles suffisants pour executer une commande sur " + role.mention )
        raise Exception

    else :
        pass

@bot.event # Permet de savoir si le membre détient le rôle DJ pour exécuter des musiques
async def rolesMusique (ctx) :
    roleDJ = ctx.guild.get_role (690904489573613590) # l'ID du rôle DJ
    X = 0

    if ctx.author.guild.id == 690730758297354246 : #La Team
        for i in range (0, len (ctx.author.roles)) : # checker tout les rôles du membre
            if ctx.author.roles[i].position == roleDJ.position : # si un des rôles du membre à la même position que celui du rôle DJ (concrêtement si il détient le rôle DJ)
                X = 1 # incrémenter X

        if X == 1  : # Si nous détenons ce rôle DJ
            channel = bot.get_channel (768821373891510322)# channel La Team - musique
            if ctx.channel.id != 768821373891510322 :
                await ctx.send ("Les commandes musicales ne peuvent s'effectuer que sur le salon " + channel.mention )
                raise Exception

        else : # Si nous ne détenons pas le rôle DJ
            await ctx.send ("T'as pas les droits pour les commandes musicales ! " + ctx.author.mention)
            await mp (ctx, "Cette personne " + ctx.author.mention +  ", essaye d'utiliser une commande musicale sans avoir les droits requis. ")
            raise Exception
    else :
        await ctx.send ("Mon créateur ne me permet pas d'effectuer des commandes musicales sur ce serveur")
        raise Exception

@bot.event
async def tableau (ctx, titre, description, color, url) :
    embed = discord.Embed (title = titre, description = description, color = random.choice (couleurs))
    embed.set_thumbnail (url = url)
    await ctx.send (embed = embed)

@bot.event # Fonction de suppression de messages
async def clean (ctx, nbr : int) :
    if nbr > 99 :
        await ctx.send ("Trop de messages à supprimer, je ne peux me le permettre. ")
        raise Exception
    else :
        await ctx.channel.purge(limit = nbr) # Sa limite maximale est de 100


#Ajouter les cogs (catégories)
bot.add_cog (cog_commands.CommandesFun(bot))
bot.add_cog (cog_admin.Admin(bot))
bot.add_cog(cog_help.Help(bot))


bot.run('NzY1NDc5Njc1OTYyMTk1OTY5.X4VagA.f2d4jpdAzmYd_-Ip8yGWkoiHl0g')
