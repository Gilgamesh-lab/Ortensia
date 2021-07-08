#!/usr/bin/env python
# coding: utf-8

# In[1]:


def maj(string):
    t = ""
    string = string
    t = t + string[0].upper()
    for k in range(1,len(string)): C:\Program Files\heroku        t = t + string[k]
    return t


# In[2]:


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


# In[3]:


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


# In[4]:


def find_invite_by_code(invite_list, code):
    for inv in invite_list:
        if inv.code == code:
            return inv
        


# In[5]:


def dixi(latence):
    p = ""
    latence = str(latence)
    for k in range(len(latence)):
        if latence[k] == ".":
            return p
        else:
            p += latence[k]


# In[6]:


def reaction(channel,emoji,name_role,message): # reaction(#channel,'👀','new role')
    fichier = load('données')
    lol = fichier[str(channel.guild.id)]['lol']
    lol[message.id] = [name_role,emoji]
    fichier[str(channel.guild.id)]['lol'] = lol
    save(fichier,'données')
    


# In[7]:


def get_user(message,tag):
    for member in message.author.guild.members:
        mention = f'<@{member.id}>' #m <#827204319148769370>
        mention2 = f'<@!{member.id}>'
        if tag == mention or tag == mention2:
            user = get(member.guild.members, id = member.id)
            return user


# In[8]:


def get_channel(message,tag):#<#857278947066642442>
    for channel in message.author.guild.channels:
        mention = f'<#{channel.id}>'
        if mention == tag:
            channel = get(message.author.guild.channels, id = channel.id)
            return channel


# In[9]:


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


# In[10]:


import json
def save(dico,name):
    tf = open(f"{name}.json", "w")
    json.dump(dico,tf)
    tf.close()
def load(file):
    tf = open(f"{file}.json", "r")
    new_dict = json.load(tf)
    return new_dict


# In[11]:


def search(phrase, mot):
    o = 0
    for n in range(len(phrase)):
        if phrase[n] == mot[0]:
            for k in range(len(mot)):
                try:
                    if phrase[k+n] == mot[k]:
                        o += 1 
                except IndexError:
                    return False
            if o == len(mot) :
                return True
            else:
                o = 1
    return False
    
          


# In[12]:


import youtube_dl
import discord  

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename 


# In[13]:


def name_url(url):
    ydl_opts = {'format': 'bestaudio'}
    with youtube_dl.YoutubeDL() as ydl:
        info = ydl.extract_info(str(url), download=False)
    return info['title']


# In[26]:


import asyncio
import nest_asyncio
from discord.ext import commands
from datetime import datetime
from discord.utils import get
from discord import FFmpegPCMAudio
import os
from dotenv import load_dotenv
from googletrans import Translator
import googletrans
nest_asyncio.apply()
intents = discord.Intents.all()
client = discord.Client(intents=intents, max_messages = 1000)
from discord import Webhook, RequestsWebhookAdapter
import requests
import traceback




#fichier[t] = [[load(donnée)[t][0]], [load(donnée)[t][1]] , [load(donnée)[t][2]] , [load(donnée)[t][3]]]
@client.event
async def on_ready():
    user = client.get_user(407189858755280896)
    await client.user.edit(username= 'Ortensia')
    async for guild in client.fetch_guilds(limit=150): #guild_permissions pour member
        invites = {}
        invites[guild.id] = await guild.invites()
    if os.path.exists('données.json') == True:
        async for guild in client.fetch_guilds(limit=150): #guild_permissions pour member
            fichier = load("données")
            fichier[str(guild.id)]['attente'] = []
            save(fichier,"données")
        
    else:
        fichier = {}
        async for guild in client.fetch_guilds(limit=150): #guild_permissions pour member
            t = str(guild.id)
            fichier[t] = {'lol': {} ,'invite' : {} ,'count' : {} ,'langue' : {} ,'dico' : {} , 'glo': [] , 'rappel' : {},
                         'lg' : False , 'new' : [] , 'warn' : {} ,'attente' : [] , 'registre' : []}
        fichier['TOKEN'] = "ODI2ODkyMzE0MTIyNjQ5NjQw.YGTFeg.SSjfgxgPOjfyFQMrzm8Fiz2htK0" #load("données")["TOKEN"]
        save(fichier,'données')
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name ="le serveur en action"))
    await user.send(f"**{client.user} est connecté **", delete_after = 20)
   
@client.event
async def on_raw_reaction_add(payload):
    print('nice')
    lol = load("données")[str(payload.guild_id)]['lol']
    for cle, valeur in lol.items():
        if cle == str(payload.message_id):
            if valeur[1] == str(payload.emoji):
                t = client.get_guild(payload.guild_id)
                user = get(t.members, id = payload.user_id) #user = client.get_user(int(payload.user_id))
                Role = discord.utils.get(t.roles, name = valeur[0])
                await discord.Member.add_roles(user, Role)


@client.event
async def on_raw_reaction_remove(payload):
    lol = load("données")[str(payload.guild_id)]['lol']
    for cle, valeur in lol.items():
        if cle == str(payload.message_id):
            if valeur[1] == str(payload.emoji):
                t = client.get_guild(payload.guild_id)
                user = get(t.members, id = payload.user_id) #user = client.get_user(int(payload.user_id))
                Role = discord.utils.get(t.roles, name = valeur[0])
                await discord.Member.remove_roles(user, Role)
        
        
@client.event
async def on_member_join(member):
    async for guild in client.fetch_guilds(limit=150):
        t = guild.id
        date = datetime.now()
        if member.guild.id == t:
            for channel in guild.text_channels:
                if search(channel.name,'log'):
                    lo = channel.name
                if search(channel.name,'général'):
                    ge = channel.name
            log =  discord.utils.get(client.get_all_channels(), guild__name= guild.name, name=lo)
            general =  discord.utils.get(client.get_all_channels(), guild__name= guild.name, name= ge)
            if len(new) != 0:
                role = discord.utils.get(member.guild.roles, name = new[0])
                await discord.Member.add_roles(member,role)
            await general.send(f'Bienvenue sur le serveur {member.guild.name} {member.mention}!')
            invites_before_join = invites[member.guild.id]
            invites_after_join = await member.guild.invites()
            for invite in invites_before_join:
                if invite.uses < find_invite_by_code(invites_after_join, invite.code).uses: 
                    #o = embed.set_image(url = member.avatar_url) #cover_image_url(member.avatar_url) #('{}'.format())
                    embed = discord.Embed(colour =  discord.Colour.blue())
                    r = member.avatar_url_as(format = None, static_format='webp',size = 32)
                    embed.set_author(name = f" {member.name}(id : {member.id})", icon_url= r)
                    retStr = str(f"""```css\n à {date.hour}h{date.minute} ```""")
                    if 10 > date.minute:
                        retStr = str(f"""```css\n à {date.hour}h0{date.minute}  ```""")
                    t = f" à rejoint le serveur grâce à l'invitation de {invite.inviter} :partying_face:"
                    o = f'compte crée depuis {member.created_at[:4]}' # print(f'compte crée en {t[:4]}')
                    embed.add_field(name = t , value= o   )
                    p = f'id invitation : {invite.id}'
                    embed.add_field(name = p , value=  retStr ) 
                    await log.send(embed=embed)
                    invites[member.guild.id] = invites_after_join #mise à jour cache pour nouvel arrivant 
                    invite =  fichier[str(message.guild.id)]['invite']
                    invite[invite.inviter] = [invite[invite.inviter],member]
                    fichier[str(message.guild.id)]['invite'] = invite
                    save(fichier,'données')
                    return# Nous revenons ici car nous avons déjà trouvé lequel one a été utilisé et il est inutile de 
                   # boucler quand nous avons déjà obtenu ce que nous voulions
                    # from https://medium.com/@tonite/finding-the-invite-code-a-user-used-to-
                    #join-your-discord-server-using-discord-py-5e3734b8f21f
@client.event           
async def on_member_remove (member): 
    # Met à jour le cache lorsqu'un utilisateur quitte pour s'assurer que 
    # tout est à jour 
    async for guild in client.fetch_guilds(limit=150):
        t = guild.id
        date = datetime.now()
        if member.guild.id == t:
            for channel in guild.text_channels:
                if search(channel.name,'log'):
                    lo = channel.name
                    if search(channel.name,'général'):
                        ge = channel.name
                        log =  discord.utils.get(client.get_all_channels(), guild__name= guild.name, name= lo)
                        general =  discord.utils.get(client.get_all_channels(), guild__name= guild.name, name= ge)
                        await general.send(f' {member.display_name} a quitté le serveur :cry: ')
                        r = member.avatar_url_as(format = None, static_format='webp',size = 32)
                        embed = discord.Embed(colour =  discord.Colour.blue())
                        embed.set_author(name = f"{member.display_name} (id : {member.id})", icon_url= r)
                        retStr = str(f"""```css\n à {date.hour}h{date.minute}  ```""")
                        if 10 > date.minute:
                            retStr = str(f"""```css\n à {date.hour}h0{date.minute}  ```""")
                        t = " as quitté le serveur  "
                        embed.add_field(name = t , value=retStr )
                        await log.send(embed=embed)      
                        invites[member.guild.id] = await member.guild.invites()
                        
@client.event
async def on_member_ban(guild, user):
    pass
    
@client.event
async def on_user_update(avant, après): # changement statut
    async for guild in client.fetch_guilds(limit=150):
        t = guild.id
        date = datetime.now()
        for k in range(len(après.mutual_guilds)):
            if t == après.mutual_guilds[k].id:
                for channel in guild.text_channels:
                    if search(channel.name,'log'):
                        name = channel.name
                        log =  discord.utils.get(client.get_all_channels(), guild__name= guild.name, name= name)
                        r = avant.avatar_url_as(format = None, static_format='webp',size = 32)
                        d = après.avatar_url_as(format = None, static_format='webp',size = 32)
                        retStr = str(f"""\n à {date.hour}h{date.minute}  """)
                        if 10 > date.minute:
                            retStr = str(f"""```css\n à {date.hour}h0{date.minute}  ```""")

                        if avant.avatar != après.avatar:
                            embed = discord.Embed(title = "as changé d'avatar")
                            embed.set_author(name = f" {avant.display_name} (id : {avant.id}) ", icon_url= r, colour = discord.Colour.blue())
                            o = embed.set_footer(text = "<-- nouveau avatar" , icon_url = d)
                            embed.add_field(name = retStr , value = o)
                            await log.send(embed=embed)

                        if avant.display_name != après.display_name:
                            embed = discord.Embed(title = "as changé de nom")
                            embed.set_author(name = f" {avant.display_name} (id : {avant.id}) ", icon_url= r , colour =  discord.Colour.blue())
                            embed.add_field(name = '__avant__:  ' , value = avant.display_name)
                            embed.add_field(name = '__après__: ' , value = après.display_name)
                            embed.set_footer(text = retStr , icon_url = "")
                            await log.send(embed=embed)

                    
                    

@client.event
async def on_voice_state_update( membre , avant , après ):# entrée canal vocals
    async for guild in client.fetch_guilds(limit=150):
        t = guild.id
        if membre.guild.id == t:
            r = membre.avatar_url_as(format = None, static_format='webp',size = 32)
            for channel in guild.text_channels:
                if search(channel.name,'log'):
                    name = channel.name
                    log =  discord.utils.get(client.get_all_channels(), guild__name= guild.name , name=name)
                    date = datetime.now()
                    if après.channel == None:
                        statut = "déconnecté"
                    else:
                        statut = "connecté"
                    if statut == "déconnecté":
                        canal = avant.channel
                        t = 'du'
                    else:
                        canal = après.channel
                        t = 'au'

                    retStr = str(f"""```\n à {date.hour}h{date.minute}  ```""")
                    nom = membre
                    nom = str(nom)
                    embed = discord.Embed(colour =  discord.Colour.blue())# icon_url= r, text=membre.name
                    embed.set_author(name = f" {membre.display_name} (id : {membre.id})", icon_url= r) 
                    t = f" s'est {statut} {t} canal vocal {canal}"
                    embed.add_field(name = t , value=retStr  )
                    await log.send( embed=embed)
            

@client.event
async def on_invite_create( inviter ):
    async for guild in client.fetch_guilds(limit=150):
        t = guild.id
        if inviter.guild.id == t:
            r = inviter.inviter.avatar_url_as(format = None, static_format='webp',size = 32)
            for channel in guild.text_channels:
                if search(channel.name,'log'):
                    name = channel.name
                    log =  discord.utils.get(client.get_all_channels(), guild__name= guild.name, name= name)
                    date = datetime.now()
                    retStr = str(f"""```css\n  id invitation : {inviter.id}  ```""")
                    t = f" as crée une invitation pour le salon {inviter.channel} "
                    embed = discord.Embed(colour =  discord.Colour.blue())
                    embed.set_author(name = f"{inviter.inviter.display_name} (id : {inviter.inviter.id})" , icon_url= r )
                    embed.add_field(name = t , value= retStr)
                    await log.send(embed=embed)
    
@client.event
async def on_message_edit( avant , après ):# à {date.hour}h : {date.minute}m : {date.second}s
    if avant.author != client.user:
        if  not avant.content.startswith("!play"): 
            async for guild in client.fetch_guilds(limit=150):
                t = guild.id
                if avant.guild.id == t:
                    if avant.webhook_id == None:
                        r = avant.author.avatar_url_as(format = None, static_format='webp',size = 32)
                        for channel in avant.guild.text_channels:
                            if search(channel.name,'log'):
                                nom = channel.name
                                log =  discord.utils.get(client.get_all_channels(), guild__name = guild.name, name = nom)
                                date = datetime.now()
                                if 10 > date.minute:
                                    retStr = str(f'\n à {date.hour}h0{date.minute}  ')
                                retStr = str(f'\n à {date.hour}h{date.minute}  ')
                                t = f""" \n message modifié dans le salon {avant.channel}{retStr} """
                                embed = discord.Embed(colour =  discord.Colour.blue() ,title = f'message(id : {après.id}): {après.jump_url}')
                                embed.set_author(name = f'{avant.author.display_name} (id : {après.author.id})' , icon_url= r)
                                embed.add_field(name = '__avant__:  ' , value = avant.content)
                                embed.add_field(name = '__après__: ' , value = après.content)
                                embed.set_footer(text = t , icon_url = "")
                                # embed.add_field(name = t , value= retStr))
                                await log.send(embed=embed)

print('ok')

@client.event
async def on_message_delete(message):
    async for guild in client.fetch_guilds(limit=150):
        t = guild.id
        try:
            for channel in message.guild.text_channels:
                if search(channel.name,'log'):
                    name = channel.name
            log =  discord.utils.get(client.get_all_channels(), guild__name = guild.name , name = name)
            date = datetime.now()
            if message.guild.id == t:
                if message.author != client.user :
                    r = message.author.avatar_url_as(format = None, static_format='webp',size = 32)
                    if message.content != '': #si c'est du texte et pas une image 
                        retStr = str(f"""``` message supprimé dans le salon {message.channel} \n à {date.hour}h{date.minute}   ```""")
                        nom = f" {message.author.avatar} {str(message.author)}"
                        t = str(message.created_at)
                        embed = discord.Embed(colour =  discord.Colour.blue(),
                        description = f'message(id : {message.id}) crée le {t[8]+t[9]}/{t[5]+t[6]}/{t[:4]} à {str(int(t[11] + t[12]) + 2)}h{t[14] + t[15]}')
                        embed.set_author(name = f" {message.author.display_name} (id : {message.author.id})" , icon_url= r)
                        t = f"``` contenue : {message.content} ```"
                        embed.add_field(name = t , value= retStr)
                        await log.send(embed=embed)
                    else:
                        retStr = str(f"""```css\n à {date.hour}h{date.minute}   ```""")
                        embed = discord.Embed()
                        embed.set_author(name = f" {message.author.display_name} (id : {message.author.id})", icon_url= r)
                        embed.set_image(url = message.attachments[0].url)
                        t = f"as supprimé cette image dans le salon {message.channel}"
                        embed.add_field(name = t , value=retStr)
                        await log.send(embed=embed)
                        
        except AttributeError:
            pass
            
            


@client.event
async def on_error(event, args, **kwargs):
    try:
        guild = args.guild
    except AttributeError:
        async for guild in client.fetch_guilds(limit=150):
            if guild.id == args.guild_id:
                guild = guild
    for channel in guild.text_channels:
        if search(channel.name,'log'):
            name = channel.name 
            log =  discord.utils.get(client.get_all_channels(), guild__name = guild.name , name = name)
            colour = 0xe74c3c
            embed = discord.Embed(title = f' Event Error par {args.author.name} dans le channel {args.channel.name} ', colour=colour) #Red
            embed.add_field(name=f'contenue :', value = args.content)
            embed.add_field(name='Event', value = event)
            embed.description = '```py\n%s\n```' % traceback.format_exc()
            embed.timestamp = datetime.utcnow()
            await args.reply("Une erreur as été détecté, veuillez vérifier les arguments ")
            await log.send(embed=embed)        
        
@client.event
async def on_message(message):
     async for guild in client.fetch_guilds(limit=150):
        t = guild.id
        try:
            for channel in message.guild.text_channels:
                if search(channel.name,'log'):
                    lo = channel.name
                    log =  discord.utils.get(client.get_all_channels(), guild__name= guild.name, name= lo)
                if search(channel.name,'sondage'):
                    sonda = channel.name
                    sondage =  discord.utils.get(client.get_all_channels(), guild__name= guild.name, name= sonda)
                if search(channel.name,'song'):
                    son = channel.name
                    song =  discord.utils.get(client.get_all_channels(), guild__name= guild.name, name= son)
                    
            for channel in message.guild.voice_channels:
                if search(channel.name,'Musique'):
                    mu = channel.name
                    music =  discord.utils.get(client.get_all_channels(), guild__name= guild.name, name= mu)
        
            if message.guild.id == t:
                r = message.author.avatar_url_as(format = None, static_format='webp',size = 32)
                date = datetime.now()
                fichier = load('données')
                colour = discord.Colour
                langue = fichier[str(message.guild.id)]['langue']
                attente = fichier[str(message.guild.id)]['attente']

                try:
                    count = fichier[str(message.guild.id)]['count']
                    count[str(message.author.id)] += 1
                    fichier[str(message.guild.id)]['count'] = count
                    save(fichier,'données')
                    
                except KeyError:
                    count = fichier[str(message.guild.id)]['count']
                    count[str(message.author.id)] = 1
                    fichier[str(message.guild.id)]['count'] = count
                    save(fichier,'données')

                if message.content.lower() == 'salut' or message.content.lower() == 'bonjour' or message.content == 'yo':
                    if date.hour >= 18 or date.hour <= 5:
                        b = 'Bonsoir'
                    else:
                        b = 'Bonjour'
                    await message.reply(f'{b} {message.author.display_name}') 



                elif message.content.startswith("!inviteur") and message.author.guild_permissions.administrator:
                    user = get_user((message,message.content.split()[1]))
                    inviter = fichier[str(message.guild.id)][invite]
                    a = f'{user.display_name} as invité '
                    a += inviter[user]
                    await message.reply(a)

                elif message.content.startswith("!get_user") and message.author.guild_permissions.administrator:
                    user = client.get_user(int(message.content.split()[1]))
                    if  user == None:
                        await message.reply(f"L'utilisateur n'as pas pu être trouvé, veuillez vérifier l'id")
                    else:
                        await message.reply(f"L'utilisateur correspondant à cette id se nomme {user.mention}")
                    
                            
                elif message.content.startswith("!get_msg") and message.author.guild_permissions.administrator:
                    for channel in message.guild.text_channels:
                        msg = await channel.fetch_message(int(message.content.split()[1]))
                        if  msg != None:
                            await message.reply(f"Liens vers le message : {msg.jump_url}")
                        else:
                            await message.reply(f"Le message n'as pas pu être trouvé veuillez vérifier l'id")
                            
                elif message.content.startswith("!lg") and message.author.guild_permissions.administrator:
                    if str(message.content.split()[1]) != 'True' and str(message.content.split()[1]) != 'False':
                        await message.reply("L'argument doit être un booléen")
                    else:
                        fichier[str(message.guild.id)]['lg'] = bool(message.content.split()[1])
                        save(fichier,'données')
                        if str(message.content.split()[1]) == 'True':
                            await message.reply("Modification bien prise en compte, la langue est activée")
                        else:
                            await message.reply("Modification bien prise en compte, la langue est désactivée")
                    
                
                elif message.content.startswith("!warn") and message.author.guild_permissions.administrator:
                    colour = discord.Colour
                    user = get_user(message,message.content.split()[1])
                    warn = fichier[str(message.guild.id)]['warn']
                    t = f"{date.year}/{date.month}/{date.day}"
                    try:
                        warn[str(user.id)][1] += 1
                        print('ok')
                        fichier[str(message.guild.id)]['warn'] = warn
                        save(fichier,'données')
                        nb_warn = warn[str(user.id)][1]
                    except KeyError:
                        warn[str(user.id)] = [t,1]
                        fichier[str(message.guild.id)]['warn'] = warn
                        save(fichier,'données')
                        nb_warn = 1
                    if warn[str(user.id)][0] != t:
                        nb_warn = 1
                    embed = discord.Embed(title = "**Commande d'avertissement**" , colour = colour.red())
                    embed.set_author(name = f'{message.author.display_name}(ID : {user.id})' , icon_url= r )
                    i = (f"Vous avez été alerté par {message.author.display_name} car vous avez commis une infraction"
                    f" \n Raison communiquée : {' '.join(message.content.split()[2:])}"
                    f"\n Nombre de warn actif : {nb_warn}")
                    retStr = str("```css\n La commande d'avertissement permet d'alerter un(e) membre  qu'il/elle ```"
                    "```as commis une infraction aux règles du serveur (Au bout de trois warn en une journée une commande de baîllonement ```"
                    "```seras appliqué  de manière proportionnelle aux nombres de warn du membre).```")
                    embed.add_field(name = i , value= retStr)
                    try:
                        await user.send(embed = embed)
                        embed = discord.Embed(title = f" :white_check_mark: **{user.display_name} a bien été warn**" , colour = colour.red())
                        msg = await message.channel.send(embed = embed)
                        message.author = client.user
                        await message.delete()
                    except discord.HTTPException or discord.Forbidden:
                        embed = discord.Embed(title = "**Commande d'avertissement**" , colour = colour.red())
                        embed.set_author(name = f'{message.author.display_name}(ID : {user.id})' , icon_url= r )
                        i = (f"```{user.display_name} (ID : {user.id}) as été alerté par {message.author.display_name}"
                        f" \n Raison communiquée : {' '.join(message.content.split()[2:])}"
                        f"\n Nombre de warn actif : {nb_warn}```")
                        retStr = str(f"```css\n La commande d'avertissement permet d'alerter un(e) membre  qu'il/elle```"
                        "```as commis une infraction aux règles du serveur (Au bout de trois warn en une journée une commande de baîllonement```"
                        "```seras appliqué automatiquement de manière proportionnelle aux nombres de warn du membre).```")
                        embed.add_field(name = i , value= retStr)
                        msg = await message.channel.send(user.mention,embed=embed)
                        message.author = client.user
                        await message.delete()
                        
                    if warn[str(user.id)][0] != t:# mauvaise date
                        print('s')
                        del warn[str(user.id)]
                        warn[str(user.id)] = [t,1]
                        fichier[str(message.guild.id)]['warn'] = warn
                        save(fichier,"données")
                    else:
                        print('w',warn)
                        if warn[str(user.id)][1] % 3 == 0 :
                            await message.channel.send(f"!mute  {warn[str(user.id)][1]*10} {user.mention} Récidives")
                        
                        
                   # except ValueError: # pas de dico crée
                        #print('ok')
                        #warn[user.id] = [t,1]
                        #fichier[str(message.guild.id)]['warn'] = warn
                        #save(fichier,"données")
                        
                elif message.content.startswith("!unwarn") and message.author.guild_permissions.administrator:
                    user = get_user(message,message.content.split()[1])
                    warn = fichier[str(message.guild.id)]['warn']
                    warn[user.id][1] -= 1
                    fichier[str(message.guild.id)]['warn'] = warn
                    save(fichier,"données")
                    embed = discord.Embed(title = "**Commande de révocation d'avertissement**" , colour = colour.red())
                    embed.set_author(name = f'{message.author.display_name}(ID : {user.id})' , icon_url= r )
                    t = (f"```{user.display_name} (ID : {user.id}) as été alerté par {message.author.display_name}"
                    f" \n Raison communiquée : {' '.join(message.content.split()[2:])}```")
                    retStr = str(f"""```css\n La commande de révocation d'avertissement permet de retirer une alerte à
                    "un(e) membre.```""")
                    embed.add_field(name = t , value= retStr)
                    await message.channel.send(user.mention,embed=embed)
                    if warn[user.id][1] >= 2:
                        await message.channel.send(f"!unmute {user.mention}  {message.content.split()[2:]}")

                elif message.content.startswith("!rappel") and message.author.guild_permissions.administrator:#year/month/day-hour:minute
                    channel = get_channel(message,message.content.split()[1])
                    commande = message.content.split()[3:]
                    rappel = fichier[str(message.guild.id)]['rappel']
                    rappel[message.content.split()[2]] = [commande,channel.mention]
                    print("rappel init",rappel)
                    fichier[str(message.guild.id)]['rappel'] = rappel
                    save(fichier,'données')
                    await message.reply("Le rappel as bien été enregistré")
                    end = False
                    while len(rappel) != 0 and end == False:
                        rappel = fichier[str(message.guild.id)]['rappel']
                        sup = []
                        date = datetime.now()
                        t = f"{date.year}/{date.month}/{date.day}-{date.hour}:{date.minute}"
                        if 10 > date.minute:
                            t = f"{date.year}/{date.month}/{date.day}-{date.hour}:0{date.minute}"
                            if 10 > date.minute and 10 > date.hour:
                                    t = f"{date.year}/{date.month}/{date.day}-0{date.hour}:0{date.minute}"
                        if 10 > date.hour and 10 <= date.minute :
                            t = f"{date.year}/{date.month}/{date.day}-0{date.hour}:{date.minute}"
                        for cle in rappel:
                            if len(str(cle)) == 5:
                                t = t[-5:]
                                if str(t) == str(cle):
                                    await get_channel(message,rappel[cle][1]).send(' '.join(rappel[cle][0]))
                            if str(t) == str(cle):
                                if cle not in sup:
                                    await get_channel(message,rappel[cle][1]).send(' '.join(rappel[cle][0]))
                                    sup.append(cle)

                        for k in range(len(sup)):
                            print(rappel[sup[k]],rappel)
                            del rappel[sup[k]]
                        fichier[str(message.guild.id)]['rappel'] = rappel
                        save(fichier,'données')
                        if len(rappel) == 0:
                            end = True
                            sup = []
                        else:
                            await asyncio.sleep(60)
                            for k in range(len(sup)):
                                del rappel[sup[k]]
                            sup = []
                            
                elif message.content.startswith("!del_rappel") and message.author.guild_permissions.administrator:
                    del rappel[message.content.split()[1]]
                    await message.reply("Modification bien prise en compte")
                                
                # tag date(year/month/day-hour:minute) commande    

                elif message.content.startswith("!inviter") and message.author.guild_permissions.administrator:
                    user = get_user((message,message.content.split()[1]))
                    inviter = fichier[str(message.guild.id)][invite]
                    for cle, valeur in inviter.items():
                        if valeur == user:
                            await message.reply(f'{user.display_name} as été invité par {cle}')

                elif message.content.startswith("!restart") and message.author.guild_permissions.administrator:
                    await message.channel.send("Je reviens :wave:")
                    await client.login(TOKEN, bot = True)

                elif message.content.startswith("!shutdown") and message.author.guild_permissions.administrator:
                    await message.channel.send("Déconnection en cours")
                    await client.close()

                elif message.content.startswith("!edit") and message.author.guild_permissions.administrator:
                    channel = get_channel(message,message.content.split()[1])
                    msg = await channel.fetch_message(message.content.split()[2])
                    contenue = message.content.split()[3]
                    await msg.edit(content = contenue)

                #if message.content.startswith("!sondage"):
                    #if len(message.content.split()) <= 18:
                       # sond = {}
                        #for k in range(0,len(message.content.split()[2:]),2):
                           # sond[message.content.split()[k]] = message.content.split()[k + 1]

                #if message.content.startswith("!help") and message.author.guild_permissions.administrator:   

                elif message.content == "!count":
                    t = 1
                    count = fichier[str(message.guild.id)]['count']
                    for k, v in sorted(count.items(), key=lambda x: x[1], reverse = True ):
                        if k == str(message.author.id):
                            o = t
                        else:
                            t += 1
                    if o == 1:
                        await message.reply(f'Vous êtes la personne qui a envoyé le plus de messages  avec un total de {count[str(message.author.id)]} messages :clap:')
                    else:
                        await message.reply(f'Vous êtes la {o}ème personne à avoir envoyé le plus de messages avec un total de {count[str(message.author.id)]} messages :muscle:')


                elif message.content.startswith("!gl") and message.author.guild_permissions.administrator:
                    glo = fichier[str(message.guild.id)]['glo'] 
                    glo.append(message.content.split()[1])
                    glo.append(message.content.split()[2])
                    fichier[str(message.guild.id)]['glo'] = glo
                    save(fichier,'données')
                    print(glo)
                    await message.reply("Les langues globals ont bien été enregistré")
                
                elif message.content.startswith("!del_gl") and message.author.guild_permissions.administrator:
                    glo = []
                    fichier[str(message.guild.id)]['glo'] = glo
                    save(fichier,'données')
                    await message.reply("Les langues globals ont bien été supprimé")

                elif message.content.startswith("!lang") and fichier[str(message.guild.id)]['lg'] == True:
                    if message.content.split()[1] not in googletrans.LANGUAGES:
                        await message.reply("Vous devez entrer un code, taper '!help found' pour plus d'information ")
                    else:
                        langue = fichier[str(message.guild.id)]['langue'] 
                        langue[message.author.id] = (message.content.split()[1])
                        fichier[str(message.guild.id)]['langue'] = langue
                        save(fichier,'données')
                        await message.reply("La langue as bien été enregistré")
                    
                
                elif message.content.startswith("!found") and fichier[str(message.guild.id)]['lg'] == True: #1er arg en anglais
                    for cle, valeur in googletrans.LANGUAGES.items():
                        if valeur ==  message.content.split()[1]:
                            await message.reply(f"Le code correspondant à la langue {valeur} est {cle}")
                    
                elif message.content.startswith("!code") and message.author.guild_permissions.administrator:
                    t = ''
                    for cle, valeur in googletrans.LANGUAGES.items():
                        t += f"{valeur} --> {cle} \n"
                    embed = discord.Embed(title = 'Liste des codes :' , description = t , colour = colour.gold())
                    await message.channel.send(embed=embed)


                elif message.content.startswith("!sondage"):#!sondage titre , 1er emojis,réponse1 ect.. (max 10 emojis)
                    titre =  f'{sond(message.content[8:])}'
                    t = 8 + len(sond(message.content[8:]))
                    place = []
                    while t < len(message.content):
                        titre += f"\n {sond(message.content[t:]).split()[0] + ' ' + sond(message.content[t:]).split()[1] }"
                        place.append(sans(sond(message.content[t:]).split()[0]))
                        t += len(sond(message.content[t:]))
                    try:
                        webhook = await sondage.create_webhook(name = 'sondage')
                        web = await webhook.send(str(titre), username=message.author.display_name, avatar_url=message.author.avatar_url, wait=True)
                        for k in range(len(place)):
                            await web.add_reaction(place[k])
                        await message.reply('Le sondage as bien été crée')
                        await webhook.delete()
                    except discord.errors.HTTPException:
                        await message.reply("Erreur détecté lors du processus , veuillez vérifier les émojis entré " )

                elif message.content.startswith("!detect") :
                    t = Translator()
                    lang = t.detect(message.content[1:]).lang
                    await message.reply(f'langue détecté : {googletrans.LANGUAGES[lang]}, code de la langue : {lang}')

                
                elif str(message.author.id) in langue and not message.content.startswith("!") and fichier[str(message.guild.id)]['lg'] == True:
                    t = Translator() # (t.detect('hi').lang)
                    try :
                        a = t.translate(str(message.content) , dest = str((langue[str(message.author.id)])))
                        embed = discord.Embed( description= a.text)
                        embed.set_author(name = f" {message.author.name}", icon_url= r)
                        await message.reply(embed=embed)


                    except TypeError:
                        c = (t.translate('Erreur de traduction veuillez essayer autre chose' , 
                                         dest = t.detect(message.content).lang))
                        await message.reply(f" {c.text} ")
                        # g  = t.translate('traduction' , dest = asci(langue[(message.author.id)]))
                        
                elif  message.content.startswith("!join"):
                    await music.connect(reconnect = True)
                    
                
                elif  message.content.startswith("!play"): 
                    if message.channel == song:
                        try:
                            await music.connect(reconnect = True)
                        except discord.errors.ClientException:
                            pass
                        server = message.guild
                        voice_channel = music
                        voice_client = message.guild.voice_client
                        print('a',attente)
                        registre = load("données")[str(message.guild.id)]['registre']
                        registre.append(message.author.id)
                        attente = load("données")[str(message.guild.id)]['attente']
                        attente.append(str(message.content.split()[1]))
                        attente.append(int(message.id))
                        attente.append(message.author.id)
                        fichier = load("données")
                        fichier[str(message.guild.id)]['registre'] = registre
                        fichier[str(message.guild.id)]['attente'] = attente
                        save(fichier,"données")
                        if voice_client.is_playing() or voice_client.is_paused():
                            print('n')
                            await message.reply(f"La music as été mise en file d'attente ")
                        
                            w = len(attente)
                            print(w)
                            while len(load("données")[str(message.guild.id)]['attente']) != 0:
                                if voice_client.is_playing() or voice_client.is_paused() :
                                    while voice_client.is_playing() or voice_client.is_paused() :
                                        await asyncio.sleep(2)
                                print('go')
                                async with song.typing():
                                    print('taille',len(attente),'contenue',attente)
                                    msg = await message.reply("chargement en cours...")
                                    filename = await YTDLSource.from_url(str(attente[0]), loop=client.loop)
                                    start = await song.fetch_message(int(attente[1]))
                                    voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
                                    del attente[0]
                                    del attente[0]
                                    del attente[0]
                                    fichier = load("données")
                                    fichier[str(message.guild.id)]['attente'] = attente
                                    save(fichier,"données")
                                    nom = name_url(message.content.split()[1])
                                    await start.reply(f'** {client.user.display_name} est entrain de jouer :** {nom}')
                                    print('c',attente)
                                print('fin',attente)
                                print('d',attente)
                                await msg.delete()
                                while voice_client.is_playing() or voice_client.is_paused() :
                                    await asyncio.sleep(1)
                                del registre[0]
                                fichier = load("données")
                                fichier[str(message.guild.id)]['registre'] = registre
                                save(fichier,"données")
                                os.remove(str(filename))
                                attente = load("données")[str(message.guild.id)]['attente']
                            await song.send("Fin de la diffusion")
                            await voice_client.disconnect()
                                
                                
                                
                        else:
                            w = 0
                            msg = await message.reply("Chargement en cours, veuillez patienter")
                            print('u')
                            try:
                                async with song.typing():
                                    attente = load("données")[str(message.guild.id)]['attente']
                                    print('l')
                                    del attente[0]
                                    del attente[0]
                                    del attente[0]
                                    fichier = load("données")
                                    fichier[str(message.guild.id)]['attente'] = attente
                                    save(fichier,"données")
                                    try:
                                        filename = await YTDLSource.from_url(str(message.content.split()[1]), loop=client.loop)
                                    except youtube_dl.utils.DownloadError:
                                        await message.reply("erreur de téléchargement ")
                                    voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
                                    await msg.delete()#{str(filename)[:-16]}
                                    nom = name_url(message.content.split()[1])
                                    await song.send(f'{client.user.display_name} est entrain de jouer : ** {nom} ** ')
                                print('t')
                                while voice_client.is_playing() or  voice_client.is_paused():
                                    await asyncio.sleep(5)
                                os.remove(str(filename))
                                print('g')
                                print('e')
                                del registre[0]
                                fichier = load("données")
                                fichier[str(message.guild.id)]['registre'] = registre
                                save(fichier,"données")
                                attente = fichier[str(message.guild.id)]['attente'] 
                                while len(attente) != 0:
                                    await asyncio.sleep(1)
                                print('attent',attente)
                                await song.send("Fin de la diffusion")
                                await voice_client.disconnect()
                            except FileNotFoundError:
                                attente = load("données")[str(message.guild.id)]['attente']
                                if len(attente) != 0:
                                    await message.reply("La vidéo n'as pas pu être trouvé, vérifier l'url")
                        
                        
                elif  message.content == "!pause": 
                    registre = load("données")[str(message.guild.id)]['registre']
                    voice_client = message.guild.voice_client
                    if message.channel == song:
                        if voice_client.is_playing() or  voice_client.is_paused():
                            print('pause',voice_client.is_paused())
                            if str(message.author.id) == str(registre[0]) and voice_client.is_playing():
                                print('r')
                                voice_client.pause()

                            if int(registre[0]) not in song.members.id and voice_client.is_playing():
                                print('2')
                                voice_client.pause()
                                
                            if int(registre[0])  in song.members.id and voice_client.is_playing():
                                print('test')
                                if str(message.author.id) != str(attente[2]):
                                    print('1248')
                                    await message.reply(f"Vous ne disposer pas des droits suffisants ")
                                
                            else:
                                print('nice')
                                await message.reply("La  diffusion est déjà en pause ")
                            
                        else:
                            await message.reply(f"{client.user.display_name} ne diffuse pas de vidéo en ce moment ")

                elif  message.content == "!resume":
                    if message.channel == song:
                        voice_client = message.guild.voice_client
                        if voice_client.is_paused():
                            voice_client.resume()
                        else:
                            await message.channel.send(f"{client.user.display_name} ne lit pas de vidéo en ce moment ")

                elif  message.content.startswith("!stop"):
                    if message.channel == song:
                        voice_client = message.guild.voice_client
                        if voice_client.is_playing() or voice_client.is_paused():
                            voice_client.stop()
                            await asyncio.sleep(5)
                            if not voice_client.is_playing() or not  voice_client.is_paused() or len(attente) == 0:
                                await voice_client.disconnect()
                        else:
                            await message.channel.send(f"{client.user.display_name} ne lit pas de vidéo en ce moment ")
                
                    
                    
                    
                elif  message.content.startswith("!leave"):
                    if message.channel == song:
                        voice_client = message.guild.voice_client
                        if voice_client.is_connected():
                            await voice_client.disconnect()
                    
                      
                elif not message.content.startswith("!") and message.author != client.user and len(fichier[str(message.guild.id)]['glo']) > 0 :
                    t = Translator()
                    lang = t.detect(message.content).lang
                    glo =  fichier[str(message.guild.id)]['glo']
                    if lang != glo[0]:
                        try :
                            a = t.translate(str(message.content) , dest = str(glo[0]))
                            embed = discord.Embed( description= a.text)
                            embed.set_author(name = f" {message.author.name}", icon_url= r)
                            await message.reply(embed=embed)
                        except TypeError:
                            c = (t.translate('Erreur de traduction veuillez essayer autre chose' , 
                                             dest = t.detect(message.content).lang))
                            await message.reply(f" {c.text} ")
                            
                    if lang != glo[1]:
                        try :
                            a = t.translate(str(message.content) , dest = str(glo[1]))
                            embed = discord.Embed( description= a.text)
                            embed.set_author(name = f" {message.author.name}", icon_url= r)
                            await message.reply(embed=embed)
                        except TypeError:
                            c = (t.translate('Erreur de traduction veuillez essayer autre chose' , 
                                             dest = t.detect(message.content).lang))
                            await message.reply(f" {c.text} ")
                            
                
                elif message.content.startswith("!off"):
                    langue =  fichier[str(message.guild.id)]['langue']
                    del langue[str(message.author.id)]
                    fichier[str(message.guild.id)]['langue'] = langue
                    save(fichier,'données')
                    await message.reply("Modification bien prise en compte")


                elif message.content.startswith("!tr") and fichier[str(message.guild.id)]['lg'] == True:
                    t = Translator()
                    a = t.translate(str(' '.join(message.content.split()[2:])), dest = str(message.content.split()[1]))
                    await message.reply({a.text})

                elif message.content.startswith("!del") and message.author.guild_permissions.administrator:
                    number = message.content.split()[1]
                    if number == 'all':
                        messages =  message.channel.history(limit = 200 + 1).flatten()
                    else:
                        messages = await message.channel.history(limit = int(number) + 1).flatten()
                    for each_message in messages:
                        each_message.author == client.user # (!talk,name_channel,chaine)
                        await each_message.delete()

                elif message.content.startswith("!add") and message.author.guild_permissions.administrator:# 
                    cle = str(message.content.split()[1])
                    chaine = str(message.content.split()[2])
                    dico = fichier[str(message.guild.id)]['dico']
                    dico[cle] = chaine
                    fichier[str(message.guild.id)]['dico'] = dico
                    save(fichier,'données')
                    await message.reply("La commande as bien été crée")


                elif message.content == "!ping":
                    latence = f"Le temps de latence du bot est de {dixi(round((client.latency * 1000),0))}ms "
                    await message.reply(latence)

                elif message.content.startswith("!talk") and message.author.guild_permissions.administrator:# 
                    chaine = ' '.join(message.content.split()[2:])
                    channel =  discord.utils.get(client.get_all_channels(), guild__name = guild.name, name =  message.content.split()[1])
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

                elif message.content.startswith("!file") and message.author.guild_permissions.administrator: 
                    channel = message.content.split()[1]
                    chemin = message.content.split()[2]
                    await channel.send(file=discord.File(f'{chemin}'))

                elif message.content.startswith("!mp") and message.author.guild_permissions.administrator:
                    user = get_user(message,message.content.split()[1])
                    await user.send(message.content.split()[2])

                elif message.content.startswith("!reaction") and message.author.guild_permissions.administrator:#tag_chan,emo,id,role
                    if len( message.content.split()) < 4:
                        await message.reply("Il manque un ou plusieurs arguments")
                    channel = get_channel(message, message.content.split()[1])
                    emoji = message.content.split()[2]
                    name_role = message.content.split()[4]
                    msg = await channel.fetch_message(message.content.split()[3])
                    await msg.add_reaction(str(emoji))
                    reaction(channel,emoji,name_role,msg)
                    await message.reply("Le message pour attribué des rôles as bien été crée")

                elif message.content.startswith('!mute') and message.author.guild_permissions.administrator:
                    colour = discord.Colour
                    if message.author != client.user:
                        msg =  await message.channel.fetch_message(int(message.content.split()[2]))
                        user = msg.author
                    else:
                        user = get_user(message,message.content.split()[2])
                    mute = discord.utils.get(message.author.guild.roles, name = 'mute')
                    await discord.Member.add_roles(user,mute)
                    embed = discord.Embed(title = '**Commande de bâillonement**' , colour = colour.red())
                    embed.set_author(name = f'{message.author.display_name}(ID : {message.author.id})' , icon_url= r )
                    if message.content.split()[1] == '+' and message.author != client.user :
                        t = (f"{user.display_name} (ID : {user.id}) as été rendu(e) muet(te) par {message.author.display_name}"
                        f" pour une durée d'indéfini.\n id du message mis en cause : {msg.id}"
                        f"\n Raison communiquée : {' '.join(message.content.split()[3:])}")
                        
                    if message.content.split()[1] != '+' and message.author != client.user :
                        t = (f"{user.display_name} (ID : {user.id}) as été rendu(e) muet(te) par {message.author.display_name}"
                        f" pour une durée de {message.content.split()[1]} minutes.\n id du message ayant entraîné la sanction : {msg.id}"
                        f"\n Raison communiquée : {' '.join(message.content.split()[3:])}")
                    
                    if message.author == client.user:
                        t = (f"{user.display_name} (ID : {user.id}) as été rendu(e) muet(te) par {message.author.display_name}"
                        f" pour une durée de {message.content.split()[1]} minutes"
                        f"\n Raison communiquée : {' '.join(message.content.split()[3:])}")
                    retStr = str(f"""```css\n La commande de bâillonement permet de rendre un(e) membre muet(e) (il/elle ne peut donc plus envoyer de messages). ```""")
                    embed.add_field(name = t , value= retStr)
                    await message.channel.send(user.mention,embed=embed)
                    embed = discord.Embed(title = '**Commande de bâillonement**' , colour = colour.red())
                    embed.set_author(name = f'{message.author.display_name}(ID : {user.id})' , icon_url= r )
                    
                    if message.content.split()[1] == '+':
                        t = (f"{user.display_name} (ID : {user.id}) as été rendu(e) muet(te) par {message.author.display_name}"
                        f" pour une durée d'indéfini.\n id du message mis en cause : {msg.id}"
                        f"\n Raison communiquée : {' '.join(message.content.split()[3:])}")
                    if message.content.split()[1] != '+' and message.author != client.user :
                        t = (f"{user.display_name} (ID : {user.id}) as été rendu(e) muet(te) par {message.author.display_name}"
                        f" pour une durée de {message.content.split()[1]} minutes.\n id du message mis en cause : {msg.id}"
                        f"\n Raison communiquée : {' '.join(message.content.split()[3:])}")
                    if message.author == client.user:
                        t = (f"{user.display_name} (ID : {user.id}) as été rendu(e) muet(te) par {message.author.display_name}"
                        f" pour une durée de {message.content.split()[1]} minutes"
                        f"\n Raison communiquée : {' '.join(message.content.split()[3:])}")
                    retStr = str(f"""css\n à {date.hour}h{date.minute} """)
                    if 10 > date.minute:
                        retStr = str(f"""```\n à {date.hour}h0{date.minute}  ```""")
                    embed.add_field(name = t , value= retStr)
                    await log.send(embed =embed)
                    message.author = client.user
                    await message.delete()
                    if message.content.split()[2] != '+':
                        await asyncio.sleep(int(message.content.split()[2])*60)
                        await discord.Member.remove_roles(user,mute)






                elif message.content.startswith('!unmute') and message.author.guild_permissions.administrator:
                    user = get_user(message,message.content.split()[1])
                    mute = discord.utils.get(message.author.guild.roles, name = 'mute')
                    await discord.Member.remove_roles(user,mute)
                    colour = discord.Colour
                    embed = discord.Embed(title = '**Commande de révocation du bâillonement**' , colour = colour.red())
                    embed.set_author(name = f'{message.author.display_name}(ID : {message.author.id})' , icon_url= r )
                    t = (f"{user.display_name}(ID : {user.id}) peut de nouveau parler grâce à {message.author.display_name}")
                    retStr = "css\n La révocation d'un baîllonnement (qu'on appele unmute) permet un(e) à membre de parler de nouveau."
                    embed.add_field(name = t , value= retStr)
                    message.author = client.user
                    await message.delete()
                    await message.channel.send(user.mention,embed=embed)
                    embed = discord.Embed(title = '**Commande de révocation du bâillonement**' , colour = colour.red())
                    embed.set_author(name = f'{message.author.display_name}(ID : {message.author.id})' , icon_url= r )
                    t = (f"{user.display_name}  peut de nouveau parler grâce à {message.author.display_name}"
                    f"\n Raison communiquée : {' '.join(message.content.split()[2:])}")
                    retStr = f"""```css\n à {date.hour}h{date.minute}```"""
                    if 10 > date.minute:
                        retStr = str(f"""```css\n à {date.hour}h0{date.minute}  ```""")
                        if 10 > date.hour:
                            retStr = str(f"""```css\n à 0{date.hour}h0{date.minute}  ```""")
                    if 10 > date.hour:
                        retStr = str(f"""```css\n à 0{date.hour}h{date.minute}  ```""")
                    embed.add_field(name = t , value = retStr)
                    await log.send(embed = embed)

                elif message.content.startswith('!up ') and message.author.guild_permissions.administrator:
                    user = get_user(message,message.content.split()[1])
                    role = discord.utils.get(message.author.guild.roles, name = message.content.split()[2])
                    await discord.Member.add_roles(user,role)
                    if type(role) != None and type(user) != None:
                        await message.reply(f"{user.display_name} as bien obtenue le rôle {message.content.split()[2]}")
                    #channel = message.channel


                elif message.content.startswith('!down ') and message.author.guild_permissions.administrator:
                    user = get_user(message,message.content.split()[1])
                    role = discord.utils.get(message.author.guild.roles, name = message.content.split()[2])
                    await discord.Member.remove_roles(user,role)
                    if type(role) != None and type(user) != None:
                        await message.reply(f"{user.display_name} as bien perdue le rôle {message.content.split()[2]}")
                    #channel = message.channel

                elif message.content.startswith('!all') and message.author.guild_permissions.administrator:
                    for member in message.guild.members:
                        role = discord.utils.get(message.author.guild.roles, name = message.content.split()[1])
                        await discord.Member.add_roles(member,role)
                
                elif message.content.startswith('!nobody') and message.author.guild_permissions.administrator:
                    for member in message.guild.members:
                        role = discord.utils.get(message.author.guild.roles, name = message.content.split()[1])
                        await discord.Member.remove_roles(member,role)
                        
                elif message.content.startswith('!new') and message.author.guild_permissions.administrator:
                    new = fichier[str(message.guild.id)]['new']
                    new.append(message.content.split()[1:])
                    fichier[str(message.guild.id)]['new'] = new
                    save(fichier,'données')
                    
                elif message.content.startswith('!del_new') and message.author.guild_permissions.administrator:
                    new = fichier[str(message.guild.id)]['new']
                    new = []
                    fichier[str(message.guild.id)]['new'] = new
                    save(fichier,'données')
                    
                elif message.content.startswith('!upgrade') and message.author.guild_permissions.administrator:
                    user = get_user(message,message.content.split()[1])
                    role = discord.utils.get(message.author.guild.roles, name = message.content.split()[2])
                    await discord.Member.add_roles(user,role)
                    channel = message.channel
                    await message.delete()
                    await channel.send(f"{user.mention} tu as obtenue le role '{message.content.split()[2]}' :partying_face:")
                    embed = discord.Embed(title = "**Ajout d'un role**" , colour = colour.green())
                    embed.set_author(name = f'{message.author.display_name}' , icon_url = r )
                    retStr = f"""```css\n à {date.hour}h{date.minute}```"""
                    if 10 > date.minute:
                        retStr = str(f"""```css\n à {date.hour}h0{date.minute}  ```""")
                    t = (f"```{user.display_name} (ID : {user.id}) as obtenue le role {message.content.split()[2]} ```")
                    embed.add_field(name = t , value= retStr)
                    await log.send(embed = embed)


                elif message.content.startswith('!downgrade') and message.author.guild_permissions.administrator:
                    user = get_user(message,message.content.split()[1])
                    role = discord.utils.get(message.author.guild.roles, name = message.content.split()[2])
                    await discord.Member.remove_roles(user,role)
                    channel = message.channel
                    await message.delete()
                    await message.channel.send(f" {user.mention} tu as perdu le role de {message.content.split()[2]} ")
                    embed = discord.Embed(title = "**Rétrogradation d'un role**" , colour = colour.green())
                    embed.set_author(name = f'{message.author.display_name}' , icon_url = r )
                    retStr = f"""```css\n à {date.hour}h{date.minute}```"""
                    if 10 > date.minute:
                        retStr = str(f"""```css\n à {date.hour}h0{date.minute}  ```""")
                    t = (f"```{user.display_name} (ID : {user.id})  as perdu le role {message.content.split()[2]}```")
                    embed.add_field(name = t , value= retStr)
                    await log.send(embed = embed)

                elif message.content.startswith('!nick') and message.author.guild_permissions.administrator:
                    user = get_user(message,message.content.split()[1])
                    n = user.nick
                    t = message.content.split()[2]
                    await user.edit(nick=t)
                    await message.channel.send(f"""Le nom de {user.mention} as bien été modifié \n Ancien nom : "{n}" """
                                  f"""\n Nouveau nom : "{user.nick}" """) 
             
                dico = fichier[str(message.guild.id)]['dico']
                for cle, valeur in dico.items():
                    if message.content == cle:
                        await message.reply(valeur)
                
                #else:
                   # if message.content.startswith('!'):
                        #await message.reply("Commande non reconnue taper '!help' pour plus d'information")

        except AttributeError:
            pass
                        
client.run("ODI2ODkyMzE0MTIyNjQ5NjQw.YGTFeg.SSjfgxgPOjfyFQMrzm8Fiz2htK0")#load("données")["TOKEN"] # (os.getenv("TOKEN"))


# In[ ]:


ydl_opts = {'format': 'bestaudio'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(str(message.content.split()[1]), download=False)
    URL = info['formats'][0]['url']
voice = get(client.voice_clients, guild=message.guild)
voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))


# In[21]:


def name(url):
    ydl_opts = {'format': 'bestaudio'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(str(url), download=False)
    return info['title']


# In[20]:


t = "https://www.youtube.com/watch?v=uUeqyxNUoMQ&ab_channel=Daedron12"
ydl_opts = {'format': 'bestaudio'}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(str(t), download=False)
info


# In[ ]:


import pyyoutube as youtube
help(youtube.api)


# In[ ]:


import pyyoutube
api = pyyoutube.Api(api_key="your api key")
#api.get_video_categories('fr')
api.get("https://www.googleapis.com/youtube/v3/videoCategories")


# In[ ]:





# In[ ]:


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


# In[ ]:


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


# In[ ]:


def remove_reaction(channel_id,emoji,name_role):
    intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents,command_prefix = '!')

Channel = client.get_channel(channel_id) 
        if reaction.message.channel == Channel:
            if reaction.emoji == emoji:
                Role = discord.utils.get(user.guild.roles, name= name_role)
                await discord.Member.add_roles(user, Role)


# In[ ]:


def mot(chaine):
    chaine = chaine.upper()
    j = []
    for k in range(len(chaine)):
         j.append(ord(chaine[k]))
    return j , ','


# In[ ]:


def mo(tab):
    j = ''
    for k in range(len(chaine)):
         j += (chr(chaine[k]))
    return j 


# In[ ]:


for k in range(len(a)):
    mo(a[k])
    print('#',mo(a[k]), end = '')


# In[ ]:


mot('Intrépide')


# In[ ]:


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


# In[ ]:


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


# In[ ]:


l = [<Attachment id=828378013334896670 filename='images.jpeg-47.jpg' url='https://cdn.discordapp.com/attachments/826889157078024244/828378013334896670/images.jpeg-47.jpg'>]


# In[ ]:


@client.event
async def on_reaction_add(reaction, user ):
    Channel = client.get_channel(826889157078024244) 
    if reaction.message.channel == Channel:
        print('emojis =',reaction.emoji)
        if reaction.emoji == "👀":
            Role = discord.utils.get(user.guild.roles, name= "new role")
            await discord.Member.add_roles(user, Role)


# In[ ]:


t = 826889157078024244  
m = 826889157078024244
if m == t:
    print('ok')


# In[ ]:


list1 = ['1', '2', '3']
str1 = ' '.join(list1)
str1


# In[ ]:


j = {'k' : 'lol'}
try:
    j['d'] 
except KeyError:
    print('ok')


# In[ ]:


def ju(lol): 
    return


# In[ ]:


ju(5)*if message.channel == log:
                    message.author = client.user
                    await message.delete()


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
        im2 = Image.open('/Users/fabri/Downloads/Nouveau dossier (4)/p.bmp')
        t = display(im2)
        print(t)


# In[ ]:


import googletrans
from googletrans import Translator
help(Translator)


# In[ ]:


translator = Translator()
t = translator.translate('안녕하세요.', dest = 'fr')
k = translator.translate('안녕하세요.', dest = 'fr')
print(t.text)


# In[ ]:


t = Translator()
a = t.translate('hi', dest = 'fr')
print(t.detect('hi').lang)


# In[ ]:


t = "2018-11-28 19:49:15.283000"
print(f'compte crée en {t[:4]}')


# In[ ]:


t = 'nombre'
t = maj(t)
t


# In[ ]:


t = 'Belle journée , Beau , oui'
print(sond(str(t.split())))


# In[ ]:


y = 'lol'
y.split()


# In[ ]:


names = {'carlos': 2, 'daoud': 1, 'bob': 4, 'alex': 3}
tab = {}
t = 1
for k, v in sorted(names.items(), key=lambda x: x[1], reverse = True ):
    if k == 'daoud':
        print(t)
    else:
        t += 1


# In[ ]:


help(sorted)


# In[ ]:


a = 5
b = a
a += 2
b
a


# In[ ]:


t = 'lol'
t[:1]
len(t[1:])


# In[ ]:


grille = [[0 for _ in range(8)]for _ in range(7)]
grille.append(5)
grille.append(4)
grille.append(6)
grille


# In[ ]:


tab = [[]]
tab[0].append(5)
tab[1][0].append(7)
tab


# In[ ]:


tab = ['l','m']
f'l{tab[1]}' = 5


# In[ ]:


grille = [[0 for _ in range(20)]for _ in range(7)]
tab = ['l','m']
for k in range(len(tab)):
    grille[0][k] = tab[k]
grille


# In[ ]:




