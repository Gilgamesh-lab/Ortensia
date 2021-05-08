#!/usr/bin/env python
# coding: utf-8

# In[9]:


def copier(chaine):
    import win32clipboard
    # set clipboard data
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()    
    win32clipboard.SetClipboardText(chaine)
    win32clipboard.CloseClipboard()


# In[1]:


def maj(string):
    t = ""
    string = string
    t = t + string[0].upper()
    for k in range(1,len(string)):
        t = t + string[k]
    return t


# In[54]:


def sans(phrase):
    if type(phrase) != str:
        raise TypeError('le paramètre doit être une chaîne de caractères')
    nouvelle_phrase = ''
    for lettre in phrase:
        if lettre == ' ':
            pass
        else:
            nouvelle_phrase += lettre       
    return nouvelle_phrase


# In[2]:


def asci(phrase, r = False):
    """
    Transforme une chaîne de caractères en enlevant majuscules et accents.
    - Entrée : phrase (chaîne de caractères)
    - Sortie : nouvelle_phrase (chaîne de caractères)
    """
    if type(phrase) != str:
        raise TypeError('le paramètre doit être une chaîne de caractères')
    nouvelle_phrase = ''
    for lettre in phrase:
        if r == False:
            if lettre == '[':
                nouvelle_phrase += ' '
            elif lettre == ']':
                nouvelle_phrase += ' '
            elif lettre == "'":
                nouvelle_phrase += ' '
            elif lettre == ',':
                nouvelle_phrase += ' '
        if r == True:
            if lettre == '{':
                nouvelle_phrase += ' '
            elif lettre == '}':
                nouvelle_phrase += ' '
            elif lettre == "'":
                nouvelle_phrase += ' '
        else:
            nouvelle_phrase += lettre
            
    
    return nouvelle_phrase


# In[3]:


def find_invite_by_code(invite_list, code):
    for inv in invite_list:
        if inv.code == code:
            return inv
        


# In[4]:


def dixi(latence):
    p = ""
    latence = str(latence)
    for k in range(len(latence)):
        if latence[k] == ".":
            return p
        else:
            p += latence[k]


# In[5]:


def reaction(channelid,emoji,name_role,message_id = None): # reaction(826889157078024244,'👀','new role')
    lol[emoji] = name_role
    @client.event
    async def on_raw_reaction_add(payload):
        Channel = channelid
        if str(payload.channel_id) == str(Channel):
            if  message_id == payload.message_id or  message_id == None:
                for cle, valeur in lol.items():
                    if str(payload.emoji) == cle:
                        t = client.get_guild(payload.guild_id)
                        user = get(t.members, id = payload.user_id) #user = client.get_user(int(payload.user_id))
                        Role = discord.utils.get(t.roles, name = valeur)
                        await discord.Member.add_roles(user, Role)
                    
    @client.event
    async def on_raw_reaction_remove(payload):
        Channel = channelid
        if str(payload.channel_id) == str(Channel):
            if  message_id == payload.message_id or  message_id == None:
                for cle, valeur in lol.items():
                    if str(payload.emoji) == cle:
                        t = client.get_guild(payload.guild_id)
                        user = get(t.members, id = payload.user_id) #user = client.get_user(int(payload.user_id))
                        Role = discord.utils.get(t.roles, name = valeur)
                        await discord.Member.remove_roles(user, Role)


# In[6]:


def get_user(message,tag):
    for member in message.author.guild.members:
        mention = f'<@{member.id}>'
        if mention == tag:
            user = get(member.guild.members, id = member.id)
            return user


# In[7]:


def get_channel(message,tag):
    for channel in message.author.guild.channels:
        mention = f'#{channel.name}'
        print(channel.name,tag,)
        if mention == tag:
            channel = get(member.guild.channels, id = channel.id)
            return channel


# In[58]:


def sond(phrase):
    """
    Transforme une chaîne de caractères en enlevant majuscules et accents.
    - Entrée : phrase (chaîne de caractères)
    - Sortie : nouvelle_phrase (chaîne de caractères)
    """
    if type(phrase) != str:
        raise TypeError('le paramètre doit être une chaîne de caractères')
    nouvelle_phrase = ' '
    t = 0
    for lettre in phrase:
        if lettre == ',':
            t += 1
        else:
            nouvelle_phrase += lettre
            
        if t == 1:
            return nouvelle_phrase
    return nouvelle_phrase


# In[82]:


import discord # get_user( id )
import asyncio
import nest_asyncio
from discord.ext import commands
from datetime import datetime
from discord.utils import get
import os
from dotenv import load_dotenv
from googletrans import Translator
nest_asyncio.apply()
intents = discord.Intents.all()
client = discord.Client(intents=intents) 
dico = {} #enregistre commande site 
invites = {} # enregistre
langue = {} # enregistre la langue des utilisateurs
lol = {} # enregistre réaction / role
count = {}# enregistre nb message

if os.path.getsize("token.txt") != 0:
    with open('token.txt', 'r', encoding = 'utf-8') as fichier:
        TOKEN = fichier.read()


@client.event
async def on_ready():
    user = client.get_user(407189858755280896)
    await user.send(f"**{client.user} est connecté **", delete_after = 10)
    async for guild in client.fetch_guilds(limit=150): #guild_permissions pour member
        t = guild.name
        log =  discord.utils.get(client.get_all_channels(), guild__name= t, name='log')
        invites[guild.id] = await guild.invites()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="le serveur en action"))
    
        
        
       
@client.event
async def on_member_join(member):
    async for guild in client.fetch_guilds(limit=150):
        t = guild.name
        date = datetime.now()
        if member.guild.name == t:
            log =  discord.utils.get(client.get_all_channels(), guild__name= t, name='log')
            general =  discord.utils.get(client.get_all_channels(), guild__name= t, name='général')
            await general.send(f'Bienvenue sur le serveur {member.guild.name} {member.mention}!')
            invites_before_join = invites[member.guild.id]
            invites_after_join = await member.guild.invites()
            for invite in invites_before_join:
                if invite.uses < find_invite_by_code(invites_after_join, invite.code).uses: 
                    #o = embed.set_image(url = member.avatar_url) #cover_image_url(member.avatar_url) #('{}'.format())
                    embed = discord.Embed()
                    r = member.avatar_url_as(format = None, static_format='webp',size = 32)
                    embed.set_author(name = f" {member.name}(id : {member.id})", icon_url= r)
                    retStr = str(f"""```css\n à {date.hour}h {date.minute} ```""")
                    t = f" à rejoint le serveur grâce à l'invitation de {invite.inviter}"
                    o = f'compte crée depuis {member.created_at[:4]}' # print(f'compte crée en {t[:4]}')
                    embed.add_field(name = t , value= o   )
                    p = f'id invitation : {invite.id}'
                    embed.add_field(name = p , value=  retStr ) 
                    await log.send(embed=embed)
                    invites[member.guild.id] = invites_after_join #mise à jour cache pour nouvel arrivant 
                    return# Nous revenons ici car nous avons déjà trouvé lequel one a été utilisé et il est inutile de 
                   # boucler quand nous avons déjà obtenu ce que nous voulions
                    # from https://medium.com/@tonite/finding-the-invite-code-a-user-used-to-
                    #join-your-discord-server-using-discord-py-5e3734b8f21f
@client.event           
async def on_member_remove (member): 
    # Met à jour le cache lorsqu'un utilisateur quitte pour s'assurer que 
    # tout est à jour 
    async for guild in client.fetch_guilds(limit=150):
        t = guild.name
        date = datetime.now()
        if member.guild.name == t:
            log =  discord.utils.get(client.get_all_channels(), guild__name= t, name='log')
            general =  discord.utils.get(client.get_all_channels(), guild__name= t, name='général')
            await general.send(f' {member.name} a quitté le serveur :( ')
            r = member.avatar_url_as(format = None, static_format='webp',size = 32)
            embed = discord.Embed()
            embed.set_author(name = f"{member.name} (id : {member.id})", icon_url= r)
            retStr = str(f"""```css\n à {date.hour}h {date.minute}  ```""")
            t = " as quitté le serveur  "
            embed.add_field(name = t , value=retStr )
            await log.send(embed=embed)      
            invites[member.guild.id] = await member.guild.invites()
    
@client.event
async def on_user_update(avant, après): # changement statut
    async for guild in client.fetch_guilds(limit=150):
        t = guild.name
        date = datetime.now()
        if avant.guild.name == t:
            log =  discord.utils.get(client.get_all_channels(), guild__name= t, name='log')
            if avant.avatar != après.avatar:
                embed = discord.Embed(title = {avant.name} )
                d = embed.set_image(url = avant.avatar_url)
                e = embed.set_image(url = après.avatar_url)
                t = f" as changé d'avatar {d} --> {e} "
                embed.add_field(name = t , value=retStr , )
                await log.send(embed=embed)

            if avant.name != après.name:
                embed = discord.Embed(title = {avant.name} )
                embed.set_image(url = avant.avatar_url)
                t = f" as changé de nom {avant.name} --> {après.name} "
                embed.add_field(name = t , value=retStr , )
                await log.send(embed=embed)

            if avant.discriminator != après.discriminator:
                embed = discord.Embed(title = {avant.name} )
                embed.set_image(url = avant.avatar_url)
                t = f" as changé de discriminator  {avant.discriminator} --> {après.discriminator} "
                embed.add_field(name = t , value=retStr , )
                await log.send(embed=embed)

@client.event
async def on_voice_state_update( membre , avant , après ):# entrée canal vocals
    async for guild in client.fetch_guilds(limit=150):
        t = guild.name
        if membre.guild.name == t:
            r = membre.avatar_url_as(format = None, static_format='webp',size = 32)
            log =  discord.utils.get(client.get_all_channels(), guild__name= t, name='log')
            date = datetime.now()
            if après.channel == None:
                statut = "déconnecté"
            else:
                statut = "connecté"
            if statut == "déconnecté":
                canal = avant.channel
            else:
                canal = après.channel
            if statut == "déconnecté":
                t = 'du'
            else:
                t= 'au'
            retStr = str(f"""```css\n à {date.hour}h {date.minute}  ```""")
            nom = membre
            nom = str(nom)
            embed = discord.Embed()# icon_url= r, text=membre.name
            embed.set_author(name = f" {membre.name} (id : {membre.id})", icon_url= r) 
            t = f" s'est {statut} {t} canal vocal {canal}"
            embed.add_field(name = t , value=retStr  )
            await log.send( embed=embed)
            

@client.event
async def on_invite_create( inviter ):
    async for guild in client.fetch_guilds(limit=150):
        t = guild.name
        if inviter.guild.name == t:
            r = inviter.inviter.avatar_url_as(format = None, static_format='webp',size = 32)
            log =  discord.utils.get(client.get_all_channels(), guild__name= t, name='log')
            date = datetime.now()
            retStr = str(f"""```css\n  id invitation : {inviter.id}  ```""")
            t = f" as crée une invitation pour le salon {inviter.channel} "
            embed = discord.Embed()
            embed.set_author(name = f"{inviter.inviter.name} (id : {inviter.inviter.id})" , icon_url= r )
            embed.add_field(name = t , value= retStr)
            await log.send(embed=embed)
    
@client.event
async def on_message_edit( avant , après ):# à {date.hour}h : {date.minute}m : {date.second}s
    if avant.author != client.user:
        async for guild in client.fetch_guilds(limit=150):
            t = guild.name
            if avant.guild.name == t:
                r = avant.author.avatar_url_as(format = None, static_format='webp',size = 32)
                log =  discord.utils.get(client.get_all_channels(), guild__name= t, name='log')
                date = datetime.now()
                retStr = str(f'\n à {date.hour}h {date.minute}  ')
                t = f"""\n  message modifié dans le salon {avant.channel}{retStr} """
                embed = discord.Embed( )
                embed.set_author(name = f'{avant.author.name} (id : {après.author.id})' , icon_url= r)
                embed.add_field(name = '__avant__:  ' , value = avant.content)
                embed.add_field(name = '__après__: ' , value = après.content)
                embed.set_footer(text = t , icon_url = "")
                # embed.add_field(name = t , value= retStr)
                await log.send(embed=embed)

@client.event
async def on_message_delete(message):
    async for guild in client.fetch_guilds(limit=150):
        t = guild.name
        log =  discord.utils.get(client.get_all_channels(), guild__name= t, name='log')
        date = datetime.now()
        if message.guild.name == t:
            if message.author != client.user :
                r = message.author.avatar_url_as(format = None, static_format='webp',size = 32)
                if message.content != '': #si c'est du texte et pas une image 
                    retStr = str(f"""``` message supprimé dans le salon {message.channel} \n à {date.hour}h {date.minute}   ```""")
                    nom = f" {message.author.avatar} {str(message.author)}"
                    embed = discord.Embed()
                    embed.set_author(name = f" {message.author.name} (id : {message.author.id})" , icon_url= r)
                    t = f" {message.content} "
                    embed.add_field(name = t , value= retStr)
                    await log.send(embed=embed)
                else:
                    retStr = str(f"""```css\n à {date.hour}h {date.minute}   ```""")
                    embed = discord.Embed()
                    embed.set_author(name = f" {message.author.name} (id : {message.author.id})", icon_url= r)
                    embed.set_image(url = message.attachments[0].url)
                    t = f"as supprimé cette image dans le salon {message.channel}"
                    embed.add_field(name = t , value=retStr)
                    await log.send(embed=embed)
            
            
        
        
@client.event
async def on_message(message):
    async for guild in client.fetch_guilds(limit=150):
        t = guild.name
        log =  discord.utils.get(client.get_all_channels(), guild__name= t, name= 'log')
        if message.author != client.user :
            if message.guild.name == t:
                sondage =  discord.utils.get(client.get_all_channels(), guild__name= t, name= 'sondage')
                r = message.author.avatar_url_as(format = None, static_format='webp',size = 32)
                date = datetime.now()
                try:
                    count[message.author.id] += 1
                except KeyError:
                    count[message.author.id] = 1
                if message.content.lower() == 'salut' or message.content.lower() == 'bonjour' or message.content == 'yo':
                    if date.hour >= 19 or date.hour <= 5:
                        b = 'Bonsoir'
                    else:
                        b = 'Bonjour'
                    await message.reply(f'{b} {message.author.name}') 
                    
                if message.content.startswith("!imo") and message.author.guild_permissions.administrator:
                    print(message.content.split()[1])  
                    
                #if message.content.startswith("!sondage"):
                    #if len(message.content.split()) <= 18:
                       # sond = {}
                        #for k in range(0,len(message.content.split()[2:]),2):
                           # sond[message.content.split()[k]] = message.content.split()[k + 1]
                            
                #if message.content.startswith("!help") and message.author.guild_permissions.administrator:   
                    
                if message.content.startswith("!count"):
                    t = 1
                    for k, v in sorted(count.items(), key=lambda x: x[1], reverse = True ):
                        if k == message.author.id:
                            o = t
                        else:
                            t += 1
                    if o == 1:
                        await message.reply(f'Vous avez envoyé le plus de messages  avec un total de {count[message.author.id]} messages')
                    else:
                        await message.reply(f'Vous êtes {o}ème as avoir envoyé le plus de message avec un total de {count[message.author.id]} messages')
                    
        
                if message.content.startswith("!lang"):
                    langue[message.author.id] = (message.content.split()[1])
                    
                if message.content.startswith("!sondage"):#!sondage titre , 1er emojis,réponse1 ect.. (max 10 emojis)
                    titre =  f'{sond(message.content[8:])}'
                    t = 8 + len(sond(message.content[8:]))
                    place = []
                    while t < len(message.content):
                        titre += f'\n{sond(message.content[t:])} {sond(message.content[t + len(sond(message.content[t:])):])}'
                        place.append(sans(sond(message.content[t:])))
                        t += len(sond(message.content[t:])) + len(sond(message.content[t + len(sond(message.content[t:])):]))
                    titre = await sondage.send(titre)
                    for k in range(len(place)):
                        print(place[k])
                        await titre.add_reaction(place[k])
                
                if message.author.id in langue and not message.content.startswith("!") :
                    t = Translator() # (t.detect('hi').lang)
                    try :
                        a = t.translate(str(message.content) , dest = str((langue[(message.author.id)])))
                        embed = discord.Embed( description= a.text)
                        embed.set_author(name = f" {message.author.name}", icon_url= r)
                        await message.reply(embed=embed)
                        
                    except TypeError:
                        c = (t.translate('Erreur de traduction veuillez essayer autre chose' , 
                                         dest = t.detect(message.content).lang))
                        await message.reply(f" {c.text} ")
                        # g  = t.translate('traduction' , dest = asci(langue[(message.author.id)]))
                if message.content.startswith("!off"):
                    del langue[message.author.id]
                    
                if message.content.startswith("!tr"):
                    t = Translator()
                    a = t.translate(str(' '.join(message.content.split()[2:])), dest = str(message.content.split()[1]))
                    await message.reply({a.text})
                    
                if message.content.startswith("!del") and message.author.guild_permissions.administrator:
                    number = message.content.split()[1]
                    if number == 'all':
                        messages =  message.channel.history(limit = 200 + 1).flatten()
                    else:
                        messages = await message.channel.history(limit = int(number) + 1).flatten()
                    for each_message in messages:
                        each_message.author == client.user # (!talk,name_channel,chaine)
                        await each_message.delete()

                if message.content.startswith("!add") and message.author.guild_permissions.administrator:# 
                    cle = str(message.content.split()[1])
                    chaine = str(message.content.split()[2])
                    dico[cle] = chaine
                
                if message.content.startswith("!ping"):
                    latence = f"Le temps de latence du bot est de {dixi(round((client.latency * 1000),0))}ms"
                    await message.reply(latence)

                if message.content.startswith("!talk") and message.author.guild_permissions.administrator:# 
                    chaine = ' '.join(message.content.split()[2:])
                    channel =  discord.utils.get(client.get_all_channels(), guild__name = t, name =  message.content.split()[1])
                    if chaine != '' and  len(message.attachments) == 0:
                        await channel.send(chaine)
                    if len(message.attachments) != 0:
                        if chaine != '':
                            n = chaine
                        else:
                            n = ''
                        embed = discord.Embed(title= n)
                        for k in range(len(message.attachments)):
                            embed.set_image(url = message.attachments[k].url)
                            await channel.send(embed=embed)
                    message.author = client.user 
                    await message.delete()
                    
                if message.content.startswith("!file") and message.author.guild_permissions.administrator: 
                    channel = message.content.split()[1]
                    chemin = message.content.split()[2]
                    await channel.send(file=discord.File(f'{chemin}'))

                if message.content.startswith("!mp") and message.author.guild_permissions.administrator:
                    user = get_user(message,message.content.split()[1])
                    await user.send(message.content.split()[2])
                    
                if message.content.startswith("!reaction") and message.author.guild_permissions.administrator:
                    channel_id = message.content.split()[1]
                    emoji = message.content.split()[2]
                    name_role = message.content.split()[3]
                    if len( message.content.split()) > 4:
                        message_id = message.content.split()[4]
                    reaction(channel_id,emoji,name_role,message_id = None)
                    
                if message.content.startswith('!mute') and message.author.guild_permissions.administrator:
                    user = get_user(message,message.content.split()[1])
                    mute = discord.utils.get(message.author.guild.roles, name = 'mute')
                    await discord.Member.add_roles(user,mute)
                    if str(message.content.split()[2])  != '+':
                        await asyncio.sleep(int(message.content.split()[2])*60)
                        await discord.Member.remove_roles(user,mute)
                    
                if message.content.startswith('!unmute') and message.author.guild_permissions.administrator:
                    user = get_user(message,message.content.split()[1])
                    mute = discord.utils.get(message.author.guild.roles, name = 'mute')
                    await discord.Member.remove_roles(user,mute)
                    
                if message.content.startswith('!nick') and message.author.guild_permissions.administrator:
                    user = get_user(message,message.content.split()[1])
                    n = user.nick
                    t = message.content.split()[2]
                    await user.edit(nick=t)
                    await message.channel.send(f"""Le nom de {user.mention} as bien été modifié \n Ancien nom : "{n}" """
                                  f"""\n Nouveau nom : "{user.nick}" """) 
                    
                for cle, valeur in dico.items():
                    if message.content == cle:
                        await message.reply(valeur)
                        
client.run(TOKEN) # (os.getenv("TOKEN"))
print('yes')


# In[3]:


import asyncio
help(asyncio.sleep)


# In[2]:


a = [[65, 76, 71, 79, 82, 73, 84, 72, 77, 73, 81, 85, 69, 77, 69, 78, 84],# ALGORITHMIQUEMENT
[76, 79, 83, 65, 78, 71, 69], # LOSANGE
[80, 79, 85, 86, 79, 73, 82], # POUVOIR
[82, 69, 78, 201, 71, 65, 84], # RENÉGAT
[79, 88, 89, 71, 200, 78, 69], # OXYGÈNE
[83, 89, 77, 80, 84, 212, 77, 69], # SYMPTÔME
[85, 84, 79, 80, 73, 81, 85, 69], # UTOPIQUE
[71, 79, 84, 72, 73, 81, 85, 69], # GOTHIQUE
[66, 82, 79, 85, 72, 65, 72, 65], # BROUHAHA
[66, 65, 67, 67, 65, 76, 65, 85, 82, 201, 65, 84], # BACCALAURÉAT
[65, 66, 82, 65, 67, 65, 68, 65, 66, 82, 65], # ABRACADABRA
[77, 201, 84, 65, 77, 79, 82, 80, 72, 79, 83, 69], # MÉTAMORPHOSE
[70, 82, 65, 78, 67, 79, 80, 72, 73, 76, 69], # FRANCOPHILE
[81, 85, 65, 76, 73, 70, 73, 67, 65, 84, 73, 79, 78], # QUALIFICATION
[67, 79, 78, 81, 85, 73, 83, 84, 65, 68, 79, 82], # CONQUISTADOR
[67, 79, 78, 83, 80, 73, 82, 65, 84, 69, 85, 82],
[81, 85, 65, 68, 82, 73, 76, 65, 84, 200, 82, 69],
[83, 79, 82, 67, 69, 76, 76, 69, 82, 73, 69],
[67, 79, 78, 84, 82, 79, 86, 69, 82, 83, 69],
[65, 80, 79, 67, 65, 76, 89, 80, 83, 69],
[66, 79, 85, 73, 76, 76, 79, 84, 84, 69],
[67, 73, 84, 82, 79, 85, 73, 76, 76, 69],
[70, 76, 73, 66, 85, 83, 84, 73, 69, 82],
[68, 73, 83, 83, 73, 77, 85, 76, 69, 82],
[76, 65, 66, 89, 82, 73, 78, 84, 72, 69],
[80, 82, 85, 68, 69, 77, 77, 69, 78, 84],
[81, 85, 65, 68, 82, 73, 67, 69, 80, 83],
[83, 85, 66, 74, 69, 67, 84, 73, 86, 69],
[86, 69, 83, 84, 73, 65, 73, 82, 69],
[84, 65, 77, 66, 79, 85, 82, 73, 78],
[81, 85, 201, 77, 65, 78, 68, 69, 82],
[80, 82, 73, 78, 84, 69, 77, 80, 83],
[80, 79, 80, 85, 76, 65, 73, 82, 69],
[80, 201, 82, 73, 80, 201, 84, 73, 69], # Péripétie
[78, 65, 82, 82, 65, 84, 69, 85, 82],
[77, 201, 84, 65, 80, 72, 79, 82, 69],
[77, 65, 83, 67, 65, 82, 65, 68, 69],
[75, 76, 65, 88, 79, 78, 78, 69, 82], 
[73, 78, 84, 82, 201, 80, 73, 68, 69]]
def random(a):
    from random import randint
    return a[randint(0,len(a))]


# In[159]:


def pendu(message2):    
    mot_liste = random(a)
    reponse_liste = [45] * len(mot_liste)
    mot = '-' * len(mot_liste)
    await message.channel.send(f'Mot à deviner : {mot}')
    coups = 0
    while reponse_liste != mot_liste:
        await message.channel.send('Choisissez une lettre : ')
        async def on_message(message):
            if len(str(message.contain)) == 1:
                lettre = message.contain.upper()
        coups = coups + 1
        for k in range(len(mot_liste)):
            if mot_liste[k] == ord(lettre):
                reponse_liste[k] = ord(lettre)
        mot = ''
        for k in range(len(reponse_liste)):
            mot = mot + str(chr(reponse_liste[k]))
        await message.channel.send(f'Mot à deviner : {mot}')
    await message.channel.send(f'Vous avez trouvé le mot en {coups} coups.')


# In[ ]:


help(discord.message)


# In[ ]:


import logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


# In[ ]:


from datetime import datetime
date = datetime.now()
date.hour


# In[ ]:


t = 'Lol'
t = t.lower()
t


# In[ ]:


def durée (h,m,s,statut,membre):
    tab = []
    if statut == 'connecte':
        tab.append(membre , h,m,s)
    if statut == 'deconnecte':
        for k in range(len(tab)):
            if membre == tab[k]:
                h = h - tab[k+1]
                m = m - tab[k+2]
                s = s - tab[k+3]
                for n in range(k,k+3):
                    del tab[n]
                    
        return int((int(h),int(m),int(s)))


# In[ ]:


help(discord.embed)


# In[ ]:


t = 'https://cdn.discordapp.com/avatars/407189858755280896/9f862240d29803a4ac95223c5bd0d782.webp?size=1024'
print(t)


# In[1]:


def remove_reaction(channel_id,emoji,name_role):
    intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents,command_prefix = '!')

Channel = client.get_channel(channel_id) 
        if reaction.message.channel == Channel:
            if reaction.emoji == emoji:
                Role = discord.utils.get(user.guild.roles, name= name_role)
                await discord.Member.add_roles(user, Role)


# In[90]:


def mot(chaine):
    chaine = chaine.upper()
    j = []
    for k in range(len(chaine)):
         j.append(ord(chaine[k]))
    return j , ','


# In[93]:


def mo(tab):
    j = ''
    for k in range(len(chaine)):
         j += (chr(chaine[k]))
    return j 


# In[104]:


for k in range(len(a)):
    mo(a[k])
    print('#',mo(a[k]), end = '')


# In[139]:


mot('Intrépide')


# In[128]:


tab =  ['ALGORITHMIQUEMENT' ,'LOSANGE', 'POUVOIR', 'RENÉGAT', 'OXYGÈNE', 'SYMPTÔME', 'UTOPIQUE', 'GOTHIQUE', 'BROUHAHA',
        'BACCALAURÉATABRACADABRA', 'MÉTAMORPHOSE', 'FRANCOPHILE', 'QUALIFICATION', 'CONQUISTADOR', 'CONSPIRATEUR'
        'QUADRILATÈRE', 'SORCELLERIE', 'CONTROVERSE',  'APOCALYPSE', 'BOUILLOTTE', 'CITROUILLE', 'FLIBUSTIER','DISSIMULER',
        'LABYRINTHE', 'PRUDEMMENT' ,'QUADRICEPS', 'SUBJECTIVE' , 'VESTIAIRE', 'TAMBOURIN' ,'QUÉMANDER', 'PRINTEMPS',
        'POPULAIRE', 'PÉRIPÉTIE','Métaphore','Narrateur','Mascarade','Klaxonner','Intrépide']
def search(chaine,tab):
    chaine = chaine.upper()
    for k in range(len(tab)):
        if tab[k] == chaine:
            return True
    return False


# In[138]:


search('Intrépide',tab)


# In[ ]:





# In[ ]:


if message.content == '!pendu':
            mot_liste = random(a)
            reponse_liste = [45] * len(mot_liste)
            mot = '-' * len(mot_liste)
            await message.channel.send(f'Mot à deviner : {mot}')
            coups = 0
            u = True
            while reponse_liste != mot_liste:
                if message.author != client.user :
                    await message.channel.send('Choisissez une lettre : ')
                    while u:
                        @client.event
                        async def on_message(message1):
                            print(message1.contain)
                            if message.contain == type(str):
                                u = False
                    print('ok')
                    if message.author != client.user :
                        if len(str(message.contain)) == 1:
                            lettre = message.contain.upper()
                            coups = coups + 1
                            for k in range(len(mot_liste)):
                                if mot_liste[k] == ord(lettre):
                                    reponse_liste[k] = ord(lettre)
                                    mot = ''
                                    for k in range(len(reponse_liste)):
                                        mot = mot + str(chr(reponse_liste[k]))
                                    await message.channel.send(f'Mot à deviner : {mot}')
            await message.channel.send(f'Vous avez trouvé le mot en {coups} coups.')


# In[26]:


l = [<Attachment id=828378013334896670 filename='images.jpeg-47.jpg' url='https://cdn.discordapp.com/attachments/826889157078024244/828378013334896670/images.jpeg-47.jpg'>]


# In[1]:


@client.event
async def on_reaction_add(reaction, user ):
    Channel = client.get_channel(826889157078024244) 
    if reaction.message.channel == Channel:
        print('emojis =',reaction.emoji)
        if reaction.emoji == "👀":
            Role = discord.utils.get(user.guild.roles, name= "new role")
            await discord.Member.add_roles(user, Role)


# In[38]:


t = 826889157078024244  
m = 826889157078024244
if m == t:
    print('ok')


# In[14]:


list1 = ['1', '2', '3']
str1 = ' '.join(list1)
str1


# In[6]:


j = {'k' : 'lol'}
try:
    j['d'] 
except KeyError:
    print('ok')


# In[6]:


def ju(lol): 
    return


# In[8]:


ju(5)*if message.channel == log:
                    message.author = client.user
                    await message.delete()


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
        im2 = Image.open('/Users/fabri/Downloads/Nouveau dossier (4)/p.bmp')
        t = display(im2)
        print(t)


# In[1]:


import googletrans
from googletrans import Translator
help(Translator)


# In[ ]:


translator = Translator()
t = translator.translate('안녕하세요.', dest = 'fr')
k = translator.translate('안녕하세요.', dest = 'fr')
print(t.text)


# In[46]:


t = Translator()
a = t.translate('hi', dest = 'fr')
print(t.detect('hi').lang)


# In[41]:


t = "2018-11-28 19:49:15.283000"
print(f'compte crée en {t[:4]}')


# In[91]:


t = 'nombre'
t = maj(t)
t


# In[19]:


t = 'Belle journée , Beau , oui'
print(sond(str(t.split())))


# In[22]:


y = 'lol'
y.split()


# In[45]:


names = {'carlos': 2, 'daoud': 1, 'bob': 4, 'alex': 3}
tab = {}
t = 1
for k, v in sorted(names.items(), key=lambda x: x[1], reverse = True ):
    if k == 'daoud':
        print(t)
    else:
        t += 1


# In[32]:


help(sorted)


# In[47]:


a = 5
b = a
a += 2
b
a


# In[2]:


t = 'lol'
t[:1]
len(t[1:])


# In[73]:


grille = [[0 for _ in range(8)]for _ in range(7)]
grille.append(5)
grille.append(4)
grille.append(6)
grille


# In[67]:


tab = [[]]
tab[0].append(5)
tab[1][0].append(7)
tab


# In[65]:


tab = [[]]
tab[0][1].append(5)
tab


# In[ ]:




