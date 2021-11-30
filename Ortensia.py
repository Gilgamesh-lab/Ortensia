#!/usr/bin/env python
# coding: utf-8

# In[13]:


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


# In[14]:


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


# In[15]:


def find_invite_by_code(invite_list, code):
    for inv in invite_list:
        if inv.code == code:
            return inv
        


# In[16]:


def dixi(latence):
    p = ""
    latence = str(latence)
    for k in range(len(latence)):
        if latence[k] == ".":
            return p
        else:
            p += latence[k]


# In[17]:


def reaction(channel,emoji,message,name_role): # reaction(#channel,'👀','new role')
    fichier = load('data')#reaction(channel,emoji,name_role,message)
    lol = fichier[str(channel.guild.id)]['lol'] #!reaction channel emoji  nom_rôle 
    lol[message.id] = [name_role,emoji]
    fichier[str(channel.guild.id)]['lol'] = lol#reaction(régle,"✅",r,"Membre")
    save(fichier,'data')
    


# In[18]:


def get_user(message,tag):
    for member in message.author.guild.members:
        mention = f'<@{member.id}>' #m <#827204319148769370>
        mention2 = f'<@!{member.id}>'
        if tag == mention or tag == mention2:
            user = get(member.guild.members, id = member.id)
            return user


# In[19]:


def get_channel(message,tag):#<#857278947066642442>
    for channel in message.author.guild.channels:
        mention = f'<#{channel.id}>'
        if mention == tag:
            channel = get(message.author.guild.channels, id = channel.id)
            return channel


# In[20]:


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


# In[21]:


import json
def save(dico,name):
    tf = open(f"{name}.json", "w")
    json.dump(dico,tf)
    tf.close()
def load(file):
    tf = open(f"{file}.json", "r")
    new_dict = json.load(tf)
    return new_dict


# In[22]:


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
    
          


# In[23]:


def maximun(lien):
    ydl_opts = {"simulate" : True , "skip_download" : True ,'extract_flat' : True,'dump_single_json' : True,
               "quiet" : True}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(lien, download=False)
    t = 0
    for cle in info['entries']:
        t += 1
    return t


# In[62]:


import youtube_dl 
from random import randint 
def random_music(catégorie = None):
    
    if catégorie != None:
        playlist = playlists[catégorie]
    else:
        playlist = random_playlists[randint(0,6)]
        
        
    nb = randint(1,maximun(playlist))
    ydl_opts = {"simulate" : True,'noplaylist': True, "skip_download" : True,'playliststart': nb, 'playlistend' : nb, 'extract_flat' : True, "quiet" : True}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist, download = False)
        try:
            url = info['entries'][0]['url']
            return f"https://www.youtube.com/watch?v={url}",info['entries'][0]['title']
        except KeyError:
            url = info['url']
            return f"https://www.youtube.com/watch?v={url}",name_url(url)
    
    
    


# In[ ]:


{'_type': 'url',
 'url': 'jj0xIgP8VHk',
 'ie_key': 'Youtube',
 'id': 'jj0xIgP8VHk',
 'extractor': 'youtube:tab',
 'webpage_url': 'https://www.youtube.com/watch?v=jj0xIgP8VHk&list=RDCLAK5uy_mK9RSAOLuO3PT_u74S1YJzlUneNOgTUTE&index=2',
 'webpage_url_basename': 'watch',
 'extractor_key': 'YoutubeTab'}


# In[51]:


random_playlists = ["https://www.youtube.com/playlist?list=jj0xIgP8VHk&list=RDCLAK5uy_mK9RSAOLuO3PT_u74S1YJzlUneNOgTUTE",
             "https://youtube.com/playlist?list=RDCLAK5uy_ly6s4irLuZAcjEDwJmqcA_UtSipMyGgbQ&playnext=1",
             "https://youtube.com/playlist?list=RDCLAK5uy_mztvVkPbbOgYQFQUOi9VbLcZ4ewdmBczw&playnext=1",
             "https://youtube.com/playlist?list=RDCLAK5uy_mCvOm3kQy1RTBwDOGYkNhtHwMO89ffquk&playnext=1",
             "https://youtube.com/playlist?list=PLsa-dEwv56FaoevRy1iSkp2YWt9udgkdJ",
             "https://youtube.com/playlist?list=PL4fGSI1pDJn6puJdseH2Rt9sMvt9E2M4i",
             "https://youtube.com/playlist?list=PL4fGSI1pDJn7bK3y1Hx-qpHBqfr6cesNs"]


playlists = {'rap': "https://www.youtube.com/watch?v=jj0xIgP8VHk&list=RDCLAK5uy_mK9RSAOLuO3PT_u74S1YJzlUneNOgTUTE&index=2",
     'hit' : "https://youtube.com/playlist?list=RDCLAK5uy_ly6s4irLuZAcjEDwJmqcA_UtSipMyGgbQ&playnext=1",
     'released' : "https://youtube.com/playlist?list=RDCLAK5uy_mztvVkPbbOgYQFQUOi9VbLcZ4ewdmBczw&playnext=1",
     'pop_fr' : "https://youtube.com/playlist?list=RDCLAK5uy_mCvOm3kQy1RTBwDOGYkNhtHwMO89ffquk&playnext=1",
      'tendance_fr' : "https://youtube.com/playlist?list=PLsa-dEwv56FaoevRy1iSkp2YWt9udgkdJ",
      'best' : "https://youtube.com/playlist?list=PL4fGSI1pDJn6puJdseH2Rt9sMvt9E2M4i",
      'fr' : "https://youtube.com/playlist?list=PL4fGSI1pDJn7bK3y1Hx-qpHBqfr6cesNs"}



# In[27]:


import discord
from discord.ext import commands
import random
import asyncio
import itertools
import nest_asyncio
nest_asyncio.apply()
import sys
import traceback
from async_timeout import timeout 
from functools import partial
import youtube_dl
from youtube_dl import YoutubeDL


# Suppress noise about console usage from errors
#youtube_dl.utils.bug_reports_message = lambda: ''



ytdlopts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',# ipv6 addresses cause issues sometimes
}

ffmpegopts = {
    'before_options': '-nostdin -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}

ytdl = YoutubeDL(ytdlopts)


class VoiceConnectionError(commands.CommandError):
    """Custom Exception class for connection errors."""


class InvalidVoiceChannel(VoiceConnectionError):
    """Exception for cases of invalid Voice Channels."""


class YTDLSource(discord.PCMVolumeTransformer):

    def __init__(self, source, *, data, requester):
        super().__init__(source)
        self.requester = requester
        self.title = data.get('title')
        self.web_url = data.get('webpage_url')
        self.duration = data.get('duration')
        self.data = data
        self.url = ""
        # YTDL info dicts (data) have other useful information you might want
        # https://github.com/rg3/youtube-dl/blob/master/README.md

    def __getitem__(self, item: str):
        """Allows us to access attributes similar to a dict.
        This is only useful when you are NOT downloading.
        """
        return self.__getattribute__(item)

    @classmethod
    async def create_source(cls, ctx, search: str, *, loop, download=False):
        loop = loop or asyncio.get_event_loop()

        to_run = partial(ytdl.extract_info, url=search, download=download)
        data = await loop.run_in_executor(None, to_run)

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        embed = discord.Embed(title="", description=f"Queued [{data['title']}]({data['webpage_url']}) [{ctx.author.mention}]", color=discord.Color.green())
        await ctx.reply(embed=embed)

        if download:
            source = ytdl.prepare_filename(data)
        else:
            return {'webpage_url': data['webpage_url'], 'requester': ctx.author, 'title': data['title']}

        return cls(discord.FFmpegPCMAudio(source), data=data, requester=ctx.author)

    @classmethod
    async def regather_stream(cls, data, *, loop):
        """Used for preparing a stream, instead of downloading.
        Since Youtube Streaming links expire."""
        loop = loop or asyncio.get_event_loop()
        requester = data['requester']

        to_run = partial(ytdl.extract_info, url=data['webpage_url'], download=False)
        data = await loop.run_in_executor(None, to_run)

        return cls(discord.FFmpegPCMAudio(data['url']), data=data, requester=requester)
            


# In[65]:


def name_url(url):
    ydl_opts = {'format': 'bestaudio'}
    
    with youtube_dl.YoutubeDL() as ydl:
        info = ydl.extract_info(str(url), download=False)
    return info['title']


# In[29]:


aide = {'!ping': "Retourne la latence du bot (c'est à dire le temps que pourra mettre Ortensia pour vous "
        "répondre, exprimés en millisecondes) \n  \nSyntaxe : !ping",
        
        '!count': "Retourne le nombre de messages envoyés dans le serveur par l'utilisateur ainsi que son classement" 
        "\n  \nSyntaxe : !count",
        
        '!sondage' : "Crée un sondage \n  \nSyntaxe : !sondage titre du sondage,1er_emojis réponse associé,2ème_emojis réponse associé ect... ",
        
        '!play' : "Lance une vidéo en version audio hébergé par la plateforme youtube  si "
        "aucune url n'est spécifié une musique seras choisi aléatoirement par le bot mais vous pouvez aussi restreindre le choix "
        "en précisant le type de musique (voir help musique). Pour modifier ou supprimer une musique en liste d'attente, il vous suffit"
        " de modifier ou supprimer le message utilisé pour la mettre en file d'attente. Si le son est de mauvaise qualité voir(!help bad_son pour obtenir de l'aide) \n  \nSyntaxe : !play url_de_la musique(optionnel)  (cette commande ne peut-être utilisé que dans le salon 'song') ",

        '!pause' : "Mets en pause l'audio en cours de lecture \n  \nSyntaxe : !pause (Cette commande ne peut être utilisée " 
        "que  par le diffuseur et seulement dans le salon 'song')",
        
        '!resume' : "Remet en route l'audio mit en pause \n  \nSyntaxe : !resume(Cette commande ne peut être utilisée " 
        "que   par le diffuseur et seulement dans le salon 'song')",
        
        "!skip": "Arrête la lecture de l'audio en cours et passe au suivant  \n  \nSyntaxe : !stop(Cette commande ne peut être utilisée " 
        "que   par le diffuseur et seulement dans le salon 'song')",
        
        "!help" : "Renvoie des informations détaillé d'une fonction .Si aucune fonction n'est précisée lors de l'appel, "
         "retourne la liste des commandes disponibles et leurs significations en abrégé \n  \nSyntaxe : !help !commande(optionnel) "}

aide_langue = {"!lang" : "Définit une langue dans laquelle sera traduit tout vos message \n  \nSyntaxe : !lang code_langue",
              "!detect" : "Renvoie le nom de la langue du message en anglais et son code \n  \nSyntaxe : !detect message  ",
              "!found" : "Renvoie le code de la langue \n  \nSyntaxe : !found nom_de_la langue_en_anglais ",
              "!off" : "Arrête de traduire vos messages automatiquement  \n  \nSyntaxe : !off",
              "!tr" : "Traduit le message après la commande \n  \nSyntaxe : !tr message "}

aide_moderator = {"!warn" : "Avertit un membre qu'il as enfreint le réglement et met un warn sur celui-ci. "
                  "Tout les trois warn un membre reçoit un mute en fonction du nombre de warn du membre."
                  "Les warns sont réinstialiser à minuit",
                  
                  "!unwarn" : "Retire un warn d'un membre et éventuellement une sanction",
                  
                  "!mute" : "Mute un membre et l'empêche d'envoyer des messages pour une durée déterminée lors de l'appel de la commande",
                  
                  "!unmute" : "Unmute un membre et lui permet d'envoyer à nouveau des messages"}

aide_administrator = {"!get_user" : "Renvoie un utilisateur grâce à son id \n  \nSyntaxe : !get_user 05587...",
                     "!get_msg" : "Renvoie un message grâce à son id \n  \nSyntaxe : !get_msg 05587...",
                     "!up" : "Ajoute un role à un membre   \n  \nSyntaxe : !up mention_du_membre  nom_du_role",
                     "!down" : "Retire un role à un membre    \n  \nSyntaxe : !down @machin mention_du_membre  nom_du_role ",
                     "!upgrade" : "Ajoute un role à un membre en faisant une annonce  \n  \nSyntaxe : !upgrade mention_du_membre  nom_du_role ",
                     "!downgrade" : "Retire un role à un membre en faisant une annonce  \n  \nSyntaxe : !downgrade mention_du_membre  nom_du_role ",
                     "!new" : "Définit un role à attribuer au nouveaux membre \n  \nSyntaxe : !new nom_du_role ",
                     "!del_new" : "Retire le role à attribuer au nouveaux membre \n  \nSyntaxe : !del_new  ",
                     "!nick" : "Renomme un membre \n  \nSyntaxe : !nick mention_du_membre nouveau_nom",
                     "!mod" : "Ajoute un membre à un salon \n  \nSyntaxe : !mod mention_du_membre mention_du_salon",
                     "!ghost" : "Retourne le nombre de personnes dans le serveur qui ne se sont pas connecté à discord durant l'intervalle donnée \n  \nSyntaxe : !ghost temps (en jours) ",
                     "!clone" : "Clone un salon avec le même nom si non précisé \n  \nSyntaxe : !clone mention_du_salon nom_du_clone (optionnel)"}

aide_owner = {"!lg" : "(Dé)bloque le module de traduction d'Ortensia avec \n  \nSyntaxe : !lg booléen",
             "!restart" : "Rédémarre Ortensia \n  \nSyntaxe : !restart ",
             "!shutdown" : "Désactive Ortensia \n  \nSyntaxe : !shutdown",
             "!gl" : "Définit les langues dans lequels seront traduit tout les messages \n  \nSyntaxe : !gl code_langue1 code_langue2",
             "!!del_gl" : "Supprime les langues dans lequels sont traduit tout les messages \n  \nSyntaxe : !del_gl ",
             "!join" : "Permet de faire venir Ortensia dans salon vocal \n  \nSyntaxe : !join ",
             "!leave" : "Permet de faire quitter à Ortensia un salon vocal \n  \nSyntaxe : !leave ",
             "!add" : "Permet de créer une commande de raccourci \n  \nSyntaxe : !add  nom_de_la_commande url description ",
             "!del" : "Supprime x message  dans le salon ou 200 avec comme argument 'all' \n  \nSyntaxe : !del x ",
             "!rappel" : "Envoie un message à une date précise \n  \nSyntaxe : !rappel channel_mention year/month/day-hour:minute message",
             "!del_rappel" : "Supprime un rappel \n  \nSyntaxe : !del_rappel  year/month/day-hour:minute",
             "!talk" : "Envoie un message avec Ortensia \n  \nSyntaxe : !talk channel_mention message",
             "!file" : "Permet d'envoyer un fichier avec Ortensia \n  \nSyntaxe : !file channel chemin",
             "!data" : "Retourne le fichier 'data' \n  \nSyntaxe : !data",
             "!ts" : "Retourne une invite d'un serveur où est présent Ortensia \n  \nSyntaxe :!ts nom_du_serveur",
             "!mp" : "Envoie un message privée à un membre \n  \nSyntaxe : !mp membre_mention message",
             "!reaction" : "Permet d'attribuer un rôle à un membre en fonction du'une réaction sur un message \n  \nSyntaxe : !reaction channel emoji nom_du_role message",
             "!all" : "Permet d'attibuer un rôle à toutes les personnes présente dans le serveur \n  \nSyntaxe : !all nom_rôle",
             "!nobody" : "Permet d'enlever un rôle à toutes les personnes présente dans le serveur \n  \nSyntaxe : !nobody nom_rôle",
             "!build" : "Crée un serveur avec les salons nécessaires au bon fonctionnement d'Ortensia \n  \nSyntaxe : !build nom_du_nouveau_serveur"}


# In[30]:


liste = ["!help : Renvoie des informations sur une fonction  (MP)",
         '!ping : Retourne la latence du bot ',
         '!count : Retourne le nombre de messages envoyés ',
         '!sondage : Crée un sondage',
         '!play : Lance une vidéo',
         '!pause : Mets en pause',
         '!resume : Relance une vidéo en pause',
         "!skip : Arrête la lecture de la vidéo actuelle"]

list_langue = ["!lang : Définit une langue de tradiction",
              "!detect : Renvoie le nom de la langue",
              "!found : Renvoie le code de la langue",
              "!off : Arrête !lang",
              "!tr : Traduit le message"]

liste_moderator = ["!warn : warn un membre",
                   "!unwarn : unwarn un membre",
                   "!mute : mute un membre",
                   "!unmute : unmute un membre"]

liste_administrator = ["!get_user : Renvoie un utilisateur",
                   "!get_msg : Renvoie un message",
                   "!up : Ajoute un role à un membre",
                   "!down : Retire un role à un membre",
                   "!upgrade : Ajoute un role à un membre officiellement",
                   "!downgrade : Retire un role à un membre officiellement",
                   "!new : Définit un role à attribuer aux nouveaux membre",
                   "!del_new : Retire le role à attribuer au nouveaux membre",
                   "!nick : Renomme un membre",
                   "!mod : Ajoute un membre à un salon",
                   "!ghost : Retourne le nombre de personnes innactifs",
                   "!clone : Clone un salon"]

liste_owner = ["!lg : (Dé)bloque le module de traduction",
              "!restart : Rédémarre Ortensia",
              "!gl : Définit les langues globals",
              "!!del_gl : Supprime les langues globals",
              "!join : Permet de faire venir Ortensia dans salon vocal",
              "!leave : Permet de faire quitter à Ortensia un salon vocal",
              "!add : Permet de créer une commande",
              "!del : Supprime des messages",
              "!rappel : Envoie un message à une date précise",
              "!del_rappel : Supprime un rappel",
              "!talk : Envoie un message avec Ortensia",
              "!file : Permet d'envoyer un fichier",
              "!data : Retourne data",
              "!ts : Retourne une invite d'un serveur",
              "!mp : Envoie un message privée",
              "!reaction : Permet d'attribuer un rôle avec une réaction",
              "!all : Permet d'attibuer un rôle global",
              "!nobody : Permet d'enlever un rôle global",
              "!build : Crée un serveur"]

liste_music = ["rap : les plus gros sons du rap français actuel",
              "hit : les plus gros hits du moment",
              "released : les sorties immanquable de cette semaine",
              "pop_fr : le meilleure de la pop française du moment",
              "tendance_fr : les clips présents dans la tendance music française de Youtube",
              "best : les titres les plus populaire dans le monde",
              "fr : les titres français les plus populaire"]

  
info = ("\n\nPour plus d'information, notament sur la syntaxe d'une commandes taper !help + la commande.  "
"\nExemple : !help !sondage")


# In[31]:


regle = ("__**Règlement du serveur**__ "
    "\n\n-Votre speudonyme ne doit pas contenir de propos racistes, homophobes ou sexistes"
    """\n- Soyez respectueux, courtois, poli envers les membres, mais vous pouvez être  familier également, on n'est pas dans une entreprise non plus"""
    "\n-Le spam ainsi que le flood ne sont pas autorisé "
    "\n- Merci de ne pas déranger les personnes présentes dans un salon vocal  quand vous le rejoignez. Troller, crier, etc... est  interdit sauf consentement de la totalité des personnes présentes dans  le salon. "
    "\n-Renommer vous si ce n'est pas déjà fait avec un speudo facilement reconnaissable pour mieux vous identifier"
    "\n-Le non-respect du règlement entraînera des sanctions à la hauteur des fautes commises  tel qu'un warn ou un mute et pour les plus grave cas un"
    " kick voir un bannissement"
    "\n\nCe règlement peut-être amené à évoluer et vous en serez bien sûr avertit ")

regle_mod = ("__**Règlement des modérateurs du serveur**__ "
             "\n\n-Les membres de la modération sont soumis au même règlement que  tout que les autres membres"
            "\n-En tant que modérateur vous devez être exemplaire vis-à-vis des Réglements"
             "\n-Faire du favoritisme envers un joueur. (mettre une sanction moins élevée à vos amis par exemple)"
             "\n-Si vous avez un problème avec un autre modérateur venez lui en parler directement au lieu de créer des dramas. Si la situation ne se règle pas, parlez-en à un haut gradé."
            "\n-Chaque membre de la modération est au service des joueurs et se doit de leur venir en aide lorsque ceux-ci posent des questions et/ou ont manifestement besoin d'aide"
            "\n-Les abus de pouvoir, sous quelques formes que ce soit (Ex: pour embêter un joueur, troller, tirer un profit des permissions octroyées,ect .) sont interdits,"
             "\n-Droit octroyer ne peuvent être utilisé que dans un but de modération"
            """\n-les motifs de sanctions doivent être brefs, précis, explicites et éloquents, les "Bien fait", "Non, on ne fait pas ça", "Arrête",ect. Sont interdit """
             "\n-Une annulation de sanction ne peut être réalisée que si la sanction n'avait pas lieu d'être (erreur de procédure, preuves insuffisantes, etc.)"
            "\n-Chaque sanction appliquée doit être accompagnée d'une raison valable, correspondant à l'infraction commise"
            "\n-Une infraction ou un manquement à un de ces règlements pourra occasionner une sanction plus lourde que pour un membre"
            "\n-Le non-respect du règlement entraînera des sanctions à la hauteur des fautes commises  tel qu'une perte temporaire ou définitive, mute, ect."
    "\n\nCe règlement peut-être amené à évoluer et vous en serez bien sûr avertit ")

bad_son = ("Si  durant un appel la qualité du son est mauvaise et que vous êtes sur un mobile essayer d'utiliser un ordinateur."
"Si vous voulez rester sur mobile voici quelques solutions pouvant régler le problème:"
"\n-Redémarrer discord"
"\n-Passer en mode haut-parleur "
""""\n-Activer OpenSl ES, pour cela cliquer sur votre profil puis "Voix & Vidéo" puis descender en bas et si votre appareil est pas trop ancien cocher la case "Forcer les appels à utiliser OpenSl ES." puis redémarrer Discord"""
"\n- Connecter vous à discord depuis un navigateur en activant la version pour ordinateur de celui-ci")


# In[ ]:


from datetime import datetime
from discord.utils import get
from discord import FFmpegPCMAudio
import os
from googletrans import Translator
import googletrans
nest_asyncio.apply()
intents = discord.Intents.all()
client = discord.Client(intents=intents, max_messages = 1000)
from discord import Webhook, RequestsWebhookAdapter
import requests
import traceback

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.common.keys import Keys
from time import sleep

TOKEN = os.environ['TOKEN']
surnom = os.environ['surnom']
mdp = os.environ['mdp']








@client.event
async def on_ready():
    user = client.get_user(407189858755280896)
    await client.user.edit(username= 'Ortensia')
    global invites
    invites = {}
    for guild in client.guilds: #guild_permissions pour member
        invites[guild.id] = await guild.invites()
    
    if os.path.exists('data.json') == True:
        fichier = load("data")
        async for guild in client.fetch_guilds(limit=150): #guild_permissions pour member
            try:
                fichier[str(guild.id)]['attente'] = []
                fichier[str(guild.id)]['registre'] = []
            except KeyError:
                t = str(guild.id)
                fichier[t] = {'lol': {}  ,'count' : {} ,'langue' : {} ,'dico' : {} , 'glo': [] , 'rappel' : {},
                         'lg' : False , 'new' : None , 'warn' : {} ,'attente' : [] , 'registre' : []}
        save(fichier,"data")
        
    else:
        fichier = {}
        async for guild in client.fetch_guilds(limit=150): #guild_permissions pour member
            t = str(guild.id)
            fichier[t] = {'lol': {}  ,'count' : {} ,'langue' : {} ,'dico' : {} , 'glo': [] , 'rappel' : {},
                         'lg' : False , 'new' : None , 'warn' : {} ,'attente' : [] , 'registre' : []}
            
        save(fichier,'data')
    await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name ="le serveur en action"))
    await user.send(f"**{client.user} est connecté **", delete_after = 20)
 



                    


@client.event
async def on_raw_reaction_remove(payload):
    if payload.user_id != client.user.id:
        lol = load("data")[str(payload.guild_id)]['lol']
        for cle, valeur in lol.items():
            if cle == str(payload.message_id):
                if valeur[1] == str(payload.emoji):
                    t =  client.get_guild(payload.guild_id)
                    user =  get(t.members, id = payload.user_id)
                    Role = discord.utils.get(t.roles, name = valeur[0])
                    await  payload.member.remove_roles(Role,atomic = True)#discord.Member.add_roles(user,Role)
                    return
                
@client.event
async def on_raw_reaction_add(payload):#lol[message.id] = [name_role,emoji]
    if payload.user_id != client.user.id:
        lol = load("data")[str(payload.guild_id)]['lol']
        for cle, valeur in lol.items():
            if cle == str(payload.message_id):
                if valeur[1] == str(payload.emoji):
                    t =  client.get_guild(payload.guild_id)
                    user =  get(t.members, id = payload.user_id)
                    Role = discord.utils.get(t.roles, name = valeur[0])
                    await  payload.member.add_roles(Role,atomic = True)#discord.Member.add_roles(user,Role)
                    return
                
@client.event        
async def on_guild_join(guild):
    fichier = load("data")
    t = str(guild.id)
    fichier[t] = {'lol': {} ,'invite' : {} ,'count' : {} ,'langue' : {} ,'dico' : {} , 'glo': [] , 'rappel' : {},
                         'lg' : False , 'new' : [] , 'warn' : {} ,'attente' : [] , 'registre' : []}
    save(fichier,'data')
    invites[guild.id] = await guild.invites()
    
    perms = discord.Permissions(administrator = True)
    if discord.utils.get(guild.roles, name = "Ortensia") == None:
        Ortensia = await guild.create_role(name = "Ortensia", hoist = True ,permissions = perms )
        ort = guild.get_member(guild.owner_id)
        await discord.Member.add_roles(ort,Ortensia)
    else:
        Ortensia = discord.utils.get(guild.roles, name = "Ortensia")
        
    
    if discord.utils.get(guild.roles, name = "Administrateur") == None:
        Administrateur = await guild.create_role(name = "Administrateur", hoist = True, mentionable = True ,permissions = perms )
    else:
        Administrateur = discord.utils.get(guild.roles, name = "Administrateur")
        
    if discord.utils.get(guild.roles, name = "Modérateur") == None:
        Modérateur = await guild.create_role(name = "Modérateur", hoist = True  , mentionable = True )
    else:
        Modérateur = discord.utils.get(guild.roles, name = "Modérateur")
        
    Diffuseur = await guild.create_role(name = "Diffuseur", hoist = True , colour = 0xf1c40f , mentionable = True )
        
    if discord.utils.get(guild.roles, name = "Membre") == None:
        overwrites = discord.Permissions(create_instant_invite = False)
        Membre = await guild.create_role(name = "Membre" , permissions = overwrites )
    else:
        Membre = discord.utils.get(guild.roles, name = "Membre")
    
        
    new = await guild.create_role(name = "new")
    mute = await guild.create_role(name = "mute")
    
    positions = {
    Ortensia : 7, # penultimate role
    Administrateur : 6,
    Modérateur : 5,
    Diffuseur : 4,
    Membre : 3,
    new : 2,
    mute : 1}

    await guild.edit_role_positions(positions = positions)
    for channel in guild.text_channels:
        await channel.set_permissions(target = mute, send_messages=False ,speak = False)
        
   
    
    
    #change_nickname add_reactions read_message_history steam use_voice_activation priority_speaker


@client.event        
async def on_guild_remove(guild):
    fichier = load("data")
    t = str(guild.id)
    del fichier[t] 
    save(fichier,'data')

@client.event        
async def on_guild_channel_create(channel):
    Role = discord.utils.get(channel.guild.roles, name = "mute")
    await channel.set_permissions(target = Role, send_messages = False ,speak = False)
    
    
@client.event
async def on_member_join(member):
    ruler = client.get_guild(826889156616912927)
    if member in ruler.members and member.guild.owner == client.user:
        await  member.guild.edit(owner = member)
    async for guild in client.fetch_guilds(limit=150):
        t = guild.id
        date = datetime.now()
        if member.guild.id == t:
            for channel in member.guild.text_channels:
                if search(channel.name,'log'):
                    lo = channel.name
                    log =  discord.utils.get(client.get_all_channels(), guild__name = member.guild.name, name=lo)
                if search(channel.name,'général'):
                    ge = channel.name
                    general =  discord.utils.get(client.get_all_channels(), guild__name= member.guild.name, name= ge)
                if search(channel.name,'general'):
                    ge = channel.name
                    general =  discord.utils.get(client.get_all_channels(), guild__name= member.guild.name, name= ge)
                
            new = load("data")[str(t)]['new']
            if len(new) != 0 :
                role = discord.utils.get(member.guild.roles, name = new[0])
                await discord.Member.add_roles(member,role)
            await general.send(f'Bienvenue sur le Serveur {member.guild.name} {member.mention} :partying_face:')
            invites_before_join = invites[member.guild.id]
            invites_after_join = await member.guild.invites()
            for invite in invites_before_join:
                if invite.uses < find_invite_by_code(invites_after_join, invite.code).uses: 
                    #o = embed.set_image(url = member.avatar_url) #cover_image_url(member.avatar_url) #('{}'.format())
                    embed = discord.Embed(colour =  discord.Colour.green())
                    r = member.avatar_url_as(format = None, static_format='webp',size = 32)
                    embed.set_author(name = f" {member.name}(id : {member.id})", icon_url= r)
                    retStr = str(f"""```css\n à {date.hour}h{date.minute} ```""")
                    if 10 > date.minute:
                        retStr = str(f"""```css\n à {date.hour}h0{date.minute}  ```""")
                    t = f" à rejoint le serveur grâce à l'invitation de {invite.inviter} "
                    o = f'compte crée depuis {str(member.created_at)[:4]}' 
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
        t = guild.id
        date = datetime.now()
        if member.guild.id == t:
            for channel in member.guild.text_channels:
                if search(channel.name,'log'):
                    lo = channel.name
                    log =  discord.utils.get(client.get_all_channels(), guild__name= guild.name, name= lo)
                if search(channel.name,'général'):
                    ge = channel.name
                    general =  discord.utils.get(client.get_all_channels(), guild__name= guild.name, name= ge)
            
            await general.send(f' {member.display_name} a quitté le serveur :sob: ')
            r = member.avatar_url_as(format = None, static_format='webp',size = 32)
            embed = discord.Embed(colour =  discord.Colour.green())
            embed.set_author(name = f"{member.display_name} (id : {member.id})", icon_url= r)
            retStr = str(f"""```css\n à {date.hour}h{date.minute}  ```""")
            if 10 > date.minute:
                retStr = str(f"""```css\n à {date.hour}h0{date.minute}  ```""")
            t = " as quitté le serveur  "
            embed.add_field(name = t , value=retStr )
            await log.send(embed=embed)
            invites = {}
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
                            embed.set_author(name = f" {avant.display_name} (id : {avant.id}) ", icon_url= r, colour = discord.Colour.green())
                            o = embed.set_footer(text = "<-- nouveau avatar" , icon_url = d)
                            embed.add_field(name = retStr , value = o)
                            await log.send(embed=embed)

                        if avant.display_name != après.display_name:
                            embed = discord.Embed(title = "as changé de nom")
                            embed.set_author(name = f" {avant.display_name} (id : {avant.id}) ", icon_url= r , colour =  discord.Colour.green())
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
                    embed = discord.Embed(colour =  discord.Colour.green())# icon_url= r, text=membre.name
                    embed.set_author(name = f" {membre.display_name} (id : {membre.id})", icon_url= r) 
                    t = f" s'est {statut} {t} canal vocal {canal}"
                    embed.add_field(name = t , value=retStr  )
                    await log.send( embed=embed)
            

@client.event
async def on_invite_create( inviter ):
    invites[inviter.guild.id] = await inviter.guild.invites()
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
                    embed = discord.Embed(colour =  discord.Colour.green())
                    embed.set_author(name = f"{inviter.inviter.display_name} (id : {inviter.inviter.id})" , icon_url= r )
                    embed.add_field(name = t , value= retStr)
                    await log.send(embed=embed)
    
@client.event
async def on_message_edit( avant , après ):# à {date.hour}h : {date.minute}m : {date.second}s
    if avant.author != client.user:
        async for guild in client.fetch_guilds(limit=150):
            t = guild.id
            if avant.guild.id == t:
                if avant.webhook_id == None:
                    if avant.content != après.content:
                        r = après.author.avatar_url_as(format = None, static_format='webp',size = 32)
                        for channel in avant.guild.text_channels:
                            if search(channel.name,'log'):
                                nom = channel.name
                                log =  discord.utils.get(client.get_all_channels(), guild__name = guild.name, name = nom)
                                date = datetime.now()
                                if 10 > date.minute:
                                    retStr = str(f'\n à {date.hour}h0{date.minute}  ')
                                retStr = str(f'\n à {date.hour}h{date.minute}  ')
                                t = f""" \n message modifié dans le salon {avant.channel}{retStr} """
                                embed = discord.Embed(colour =  discord.Colour.green() ,title = f'message(id : {après.id})')
                                embed.set_author(name = f'{avant.author.display_name} (id : {après.author.id})' , icon_url= r)
                                embed.add_field(name = '__avant__:  ' , value = avant.content)
                                embed.add_field(name = '__après__: ' , value = après.content)
                                embed.set_footer(text = t , icon_url = "")
                                # embed.add_field(name = t , value= retStr))
                                await log.send(embed=embed)



@client.event
async def on_message_delete(message):
    async for guild in client.fetch_guilds(limit=150):
        t = guild.id
        try:
            for channel in message.guild.text_channels:
                if search(channel.name,'log'):
                    name = channel.name
            log =  discord.utils.get(client.get_all_channels(), guild__name = guild.name , name = name)
            com =  discord.utils.get(client.get_all_channels(), guild__name = guild.name , name = "ℹ️│commande")
            date = datetime.now()
            if message.guild.id == t:
                if message.channel == com:
                    t = ''
                    for k in range(len(liste)):
                        t += '\n' + liste[k]
                    if len(dico) != 0:
                        for k in dico:
                            t += f" {k} : {dico[k][1]}"
                    t += info
                    embed = discord.Embed(colour =  discord.Colour.blue(),title = "Liste des commandes:" , description = t)
                    await com.send(embed = embed)
                    return
                user = client.get_user(407189858755280896)
                if message.author == client.user:
                    return
                async for entry in message.guild.audit_logs(limit = 1,action = discord.AuditLogAction.message_delete):
                    deleter = entry.user
                    if message.author != client.user and deleter != client.user or deleter != user:

                        r = message.author.avatar_url_as(format = None, static_format='webp',size = 32)
                        if 10 > date.minute:
                                h = str(f' à {date.hour}h0{date.minute}  ')
                        else:
                            h = f" à {date.hour}h{date.minute}"
                        if message.content != '': #si c'est du texte et pas une image
                            
                            t = f"``` contenue du message : {message.content} ```"
                            
                    
                        
                        #description = f'message crée le {t[8]+t[9]}/{t[5]+t[6]}/{t[:4]} à {str(int(t[11] + t[12]) + 2)}h{t[14] + t[15]}')
                        
                        if deleter != message.author:
                            l = f"as supprimé le message de {message.author.display_name} (id : {message.author.id}) dans le salon  {message.channel} {h} \n{t} "
                            embed = discord.Embed(colour =  discord.Colour.green(),description = l)
                            r = deleter.avatar_url_as(format = None, static_format='webp',size = 32)
                            embed.set_author(name = f" {deleter.display_name} (id : {deleter.id})" , icon_url= r)

                        else:
                            l = f"message supprimé dans le salon {message.channel}  {h} \n{t}"
                            embed = discord.Embed(colour =  discord.Colour.green(),description = l)
                            embed.set_author(name = f" {message.author.display_name} (id : {message.author.id})" , icon_url= r)

                        await log.send(embed=embed)
                    else:
                        embed = discord.Embed()
                        if deleter != message.author:
                            t = f"as supprimé cette image de {message.author.display_name} (id : {message.author.id}) dans le salon {message.channel} \n{h}"
                            r = deleter.avatar_url_as(format = None, static_format='webp',size = 32)
                            embed.set_author(name = f" {deleter.display_name} (id : {deleter.id})", icon_url= r)
                        else:
                            t = f"as supprimé cette image dans le salon {message.channel} \n{h}"
                        embed.set_image(url = message.attachments[0].url)
                        await log.send(embed=embed)
                else:
                    return
                        
        except AttributeError: #mp
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
            colour = 0x9b59b6
            try: 
                if args.content[0] != '!':
                    embed = discord.Embed(title = f' Event Error par {args.author.display_name} dans le channel {args.channel.name} ', colour=colour) #Red
                    embed.add_field(name=f"contenue du message qui as  provoqué l'erreur :", value = args.content)
                    await args.reply("Une erreur as été détecté, veuillez vérifier les arguments ")
                else:
                    embed = discord.Embed(title = f' Event Error par {args.author.display_name} dans le channel {args.channel.name} ', colour=colour) #Red
                    embed.add_field(name=f"contenue du message qui as  provoqué l'erreur :", value = args.content)
                    await args.reply(f"Une erreur as été détecté, veuillez vérifier les arguments , taper help {args.content.split()[0]} pour plus de détail")
            except AttributeError:
                    embed = discord.Embed(title = f' Event Error par {args.display_name} ', colour=colour)
                    for channel in guild.text_channels:
                        async for message in channel.history(limit = 5):
                            if message.author == args:
                                contenue = message.content
                                embed.add_field(name=f"contenue du message qui as peut-être provoqué l'erreur :", value = contenue)
                                await message.reply("Une erreur as été détecté, veuillez vérifier les arguments ")
                                
            embed.add_field(name='Event', value = event)
            embed.description = '```py\n%s\n```' % traceback.format_exc()
            embed.timestamp = datetime.utcnow()
            await log.send(embed=embed)        
        
@client.event
async def on_message(message):
    try:
        async for guild in client.fetch_guilds(limit=150):
            t = guild.id
            fichier = load('data')
            try:
                dico = fichier[str(message.guild.id)]['dico']
            except AttributeError:
                if message.author != client.user :
                    dico = fichier[str(message.author.mutual_guilds[0].id)]['dico']
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
                fichier = load('data')
                colour = discord.Colour
                langue = fichier[str(message.guild.id)]['langue']
                attente = fichier[str(message.guild.id)]['attente']
                registre = load("data")[str(message.guild.id)]['registre']
                TOKEN = "ODI2ODkyMzE0MTIyNjQ5NjQw.YGTFeg.SSjfgxgPOjfyFQMrzm8Fiz2htK0"
                Modérateur = discord.utils.get(message.guild.roles, name = "Modérateur")
                

                try:
                    count = fichier[str(message.guild.id)]['count']
                    count[str(message.author.id)] += 1
                    fichier[str(message.guild.id)]['count'] = count
                    save(fichier,'data')

                except KeyError:
                    count = fichier[str(message.guild.id)]['count']
                    count[str(message.author.id)] = 1
                    fichier[str(message.guild.id)]['count'] = count
                    save(fichier,'data')
                
                if message.content.startswith("!king") and message.author.guild_permissions.administrator:
                    await  message.guild.edit(owner = message.author)
                    return
                    
                if message.content.lower() == 'salut' or message.content.lower() == 'bonjour' or message.content == 'yo':
                    if date.hour >= 18 or date.hour <= 5:
                        b = 'Bonsoir'
                    else:
                        b = 'Bonjour'
                    await message.reply(f'{b} {message.author.display_name}') 



                

                elif message.content.startswith("!get_user ") and message.author.guild_permissions.administrator:
                    user = client.get_user(int(message.content.split()[1]))
                    if  user == None:
                        await message.reply(f"L'utilisateur n'as pas pu être trouvé, veuillez vérifier l'id")
                    else:
                        await message.reply(f"L'utilisateur correspondant à cette id se nomme {user.mention}")
                    return


                elif message.content.startswith("!get_msg ") and message.author.guild_permissions.administrator:
                    for channel in message.guild.text_channels:
                        msg = await channel.fetch_message(int(message.content.split()[1]))
                        if  msg != None:
                            await message.reply(f"Liens vers le message : {msg.jump_url}")
                        else:
                            await message.reply(f"Le message n'as pas pu être trouvé veuillez vérifier l'id")
                        return

                elif message.content.startswith("!lg ") and message.author.guild_permissions.administrator:
                    if str(message.content.split()[1]) != 'True' and str(message.content.split()[1]) != 'False':
                        await message.reply("L'argument doit être un booléen")
                    else:
                        fichier[str(message.guild.id)]['lg'] = bool(message.content.split()[1])
                        save(fichier,'data') 
                        if str(message.content.split()[1]) == 'True':
                            await message.reply("Modification bien prise en compte, la langue est activée")
                        else:
                            await message.reply("Modification bien prise en compte, la langue est désactivée")
                    return



                            
                elif message.content.startswith("!warn") :
                    if Modérateur in message.author.roles or message.author.guild_permissions.administrator:
                        colour = discord.Colour
                        user = get_user(message,message.content.split()[1])
                        warn = fichier[str(message.guild.id)]['warn']
                        t = f"{date.year}/{date.month}/{date.day}"
                        try:
                            warn[str(user.id)][1] += 1
                            fichier[str(message.guild.id)]['warn'] = warn
                            save(fichier,'data')
                            nb_warn = warn[str(user.id)][1]
                        except KeyError:
                            warn[str(user.id)] = [t,1]
                            fichier[str(message.guild.id)]['warn'] = warn
                            save(fichier,'data')
                            nb_warn = 1
                        if warn[str(user.id)][0] != t:
                            nb_warn = 1
                            fichier[str(message.guild.id)]['warn'] = warn
                            save(fichier,'data')
                        embed = discord.Embed(title = "**Commande d'avertissement**" , colour = 0x992d22)
                        embed.set_author(name = f'{message.author.display_name}(ID : {user.id})' , icon_url= r )
                        i = (f"Vous avez été alerté par {message.author.display_name} car vous avez commis une infraction"
                        f" \n Raison communiquée : {' '.join(message.content.split()[2:])}"
                        f"\n Nombre de warn actif : {nb_warn}")
                        retStr = str("\n La commande d'avertissement permet d'alerter un(e) membre  qu'il/elle"
                        "as commis une infraction aux règles du serveur (Au bout de trois warn en une journée une commande de baîllonement ```"
                        "seras appliqué  de manière proportionnelle aux nombres de warn du membre).")
                        embed.add_field(name = i , value= retStr)
                        try:
                            await user.send(embed = embed)
                            embed = discord.Embed(title = f" :white_check_mark: **{user.display_name} a bien été warn**" , colour = colour.red())
                            msg = await message.channel.send(embed = embed)
                            message.author = client.user
                            await message.delete()
                        except discord.HTTPException or discord.Forbidden:
                            embed = discord.Embed(title = "**Commande d'avertissement**" , colour = 0x992d22)
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
                            del warn[str(user.id)]
                            warn[str(user.id)] = [t,1]
                            fichier[str(message.guild.id)]['warn'] = warn
                            save(fichier,"data")
                        else:
                            if warn[str(user.id)][1] % 3 == 0 :
                                await message.channel.send(f"!mute {user.mention} {warn[str(user.id)][1]*10} Récidives")
                        return


                   # except ValueError: # pas de dico crée
                        #warn[user.id] = [t,1]
                        #fichier[str(message.guild.id)]['warn'] = warn
                        #save(fichier,"data")

                elif message.content.startswith("!unwarn ") :
                    if Modérateur in message.author.roles or message.author.guild_permissions.administrator:
                        user = get_user(message,message.content.split()[1])
                        warn = fichier[str(message.guild.id)]['warn']
                        embed = discord.Embed(title = "**Commande de révocation d'avertissement**" , colour = 0x992d22)
                        embed.set_author(name = f'{message.author.display_name}(ID : {user.id})' , icon_url= r )
                        t = (f"```Un warn vous as été retiré {user.display_name}  par {message.author.display_name}"
                        f" \n Raison communiquée : {' '.join(message.content.split()[2:])}```")
                        retStr = str(f"""```css\n La commande de révocation d'avertissement permet de retirer une alerte à
                        "un(e) membre.```""")
                        embed.add_field(name = t , value= retStr)
                        await user.send(embed=embed)
                        mute = discord.utils.get(message.author.guild.roles, name = 'mute')
                        if warn[user.id][1] % 3 == 0 and  mute in user.roles: 
                            await message.channel.send(f"!unmute {user.mention}  {message.content.split()[2:]} ")
                        warn[user.id][1] -= 1
                        fichier[str(message.guild.id)]['warn'] = warn
                        save(fichier,"data")
                        return

                elif message.content.startswith("!rappel ") and message.author.guild_permissions.administrator:#year/month/day-hour:minute
                    channel = get_channel(message,message.content.split()[1]) 
                    commande = message.content.split()[3:]
                    rappel = fichier[str(message.guild.id)]['rappel']
                    rappel[message.content.split()[2]] = [commande,channel.mention]
                    fichier[str(message.guild.id)]['rappel'] = rappel
                    save(fichier,'data')
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
                            del rappel[sup[k]]
                        fichier[str(message.guild.id)]['rappel'] = rappel
                        save(fichier,'data')
                        if len(rappel) == 0:
                            end = True
                            sup = []
                        else:
                            await asyncio.sleep(60)
                            for k in range(len(sup)):
                                del rappel[sup[k]]
                            sup = []
                    return

                elif message.content.startswith("!del_rappel ") and message.author.guild_permissions.administrator:
                    del rappel[message.content.split()[1]]
                    await message.reply("Modification bien prise en compte")
                    return

                # tag date(year/month/day-hour:minute) commande    

               

                elif message.content == "!restart" and message.author == message.guild.owner  :
                    await message.reply("Je reviens :wave:")
                    os.startfile("restart.bat")
                    await client.close()
                    return

                elif message.content.startswith("!shutdown ") and message.author == message.guild.owner :
                    await message.channel.send("Déconnection en cours")
                    await client.close()
                    return

                elif message.content.startswith("!edit ") and message.author == message.guild.owner:
                    channel = get_channel(message,message.content.split()[1])
                    msg = await channel.fetch_message(message.content.split()[2])
                    contenue = message.content.split()[3]
                    await msg.edit(content = contenue)
                    return

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
                    return

                elif message.content.startswith("!gl") and message.author == message.guild.owner:
                    glo = fichier[str(message.guild.id)]['glo'] 
                    glo.append(message.content.split()[1])
                    glo.append(message.content.split()[2])
                    fichier[str(message.guild.id)]['glo'] = glo
                    save(fichier,'data')
                    await message.reply("Les langues globals ont bien été enregistré")
                    return

                elif message.content.startswith("!del_gl ") and message.author.guild_permissions.administrator:
                    glo = []
                    fichier[str(message.guild.id)]['glo'] = glo
                    save(fichier,'data')
                    await message.reply("Les langues globals ont bien été supprimé")
                    return

                elif message.content.startswith("!lang ") and  str(load("data")[str(message.guild.id)]['lg']) == 'True': 
                    if message.content.split()[1] not in googletrans.LANGUAGES:
                        await message.reply("Vous devez entrer un code, taper '!help found' pour plus d'information ")
                    else:
                        langue = fichier[str(message.guild.id)]['langue'] 
                        langue[message.author.id] = (message.content.split()[1])
                        fichier[str(message.guild.id)]['langue'] = langue
                        save(fichier,'data')
                        await message.reply("La langue as bien été enregistré")
                    return


                elif message.content.startswith("!found ") and fichier[str(message.guild.id)]['lg'] == True: #1er arg en anglais
                    for cle, valeur in googletrans.LANGUAGES.items():
                        if valeur ==  message.content.split()[1]:
                            await message.reply(f"Le code correspondant à la langue {valeur} est {cle}")
                    return

                elif message.content.startswith("!code ") and message.author.guild_permissions.administrator:
                    t = ''
                    for cle, valeur in googletrans.LANGUAGES.items():
                        t += f"{valeur} --> {cle} \n"
                    embed = discord.Embed(title = 'Liste des codes :' , description = t , colour = colour.gold())
                    await message.channel.send(embed=embed)
                    return


                elif message.content.startswith("!sondage "):#!sondage titre , 1er emojis,réponse1 ect.. (max 10 emojis)
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
                    return

                elif message.content.startswith("!detect ") :
                    t = Translator()
                    lang = t.detect(message.content[1:]).lang
                    await message.reply(f'langue détecté : {googletrans.LANGUAGES[lang]}, code de la langue : {lang}')
                    return


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
                    return

                elif  message.content.startswith("!join") and  message.author.id == 407189858755280896:
                    await music.connect(reconnect = True)
                    return

                

                elif  message.content.startswith("!play"): 
                    if message.channel == song:
                        if len(message.content.split()) == 2:
                            if message.content.split()[1] in playlists:
                                pass
                            elif not message.content.split()[1].startswith("https://"):
                                await message.reply(":warning: La deuxième entrée doit être l'url d'une vidéo hébergé par youtube")
                                return
                        try:
                            voice = await music.connect(reconnect = True)
                            
                        except discord.errors.ClientException:
                            pass
                        server = message.guild
                        voice_channel = music
                        voice_client = server.voice_client

                        if voice_client.is_playing() or voice_client.is_paused():
                            attente = load("data")[str(message.guild.id)]['attente']
                            dico = []
                            dico = [int(message.id)]
                            attente.append(dico)
                            fichier = load("data")
                            fichier[str(message.guild.id)]['attente'] = attente
                            save(fichier,"data")
                            await message.reply(f"La vidéo as été mise en file d'attente ")

                        else:
                            registre = load("data")[str(message.guild.id)]['registre']
                            dico = []
                            dico = [int(message.id)]
                            registre.append(dico)
                            fichier = load("data")
                            fichier[str(message.guild.id)]['registre'] = registre
                            save(fichier,"data")
                            if len(registre) == 0 and len(attente) != 0:
                                return
                                
                                
                                
                                

                if 'song' in locals():
                    if message.channel == song:
                        if len(registre) != 0 and len(attente) == 0 and message.content.startswith("!play"):
                            #print('taille registre : ',len(registre))
                            #print('taille attente : ',len(attente))
                            server = message.guild
                            voice_channel = music
                            voice_client = server.voice_client
                            if not voice_client.is_playing():
                                while len(registre) != 0 or len(attente) != 0:
                                    try:
                                        if message.content.split()[1].startswith("https://"):
                                            nom = name_url(message.content.split()[1])
                                    except IndexError:
                                        pass
                                    if len(registre) == 0:
                                        dico = attente[0]
                                        while True:
                                            try:
                                                message = await message.channel.fetch_message(dico[0])
                                                try:
                                                    if message.content.split()[1].startswith("https://"):
                                                        nom = name_url(message.content.split()[1])
                                                except IndexError:
                                                    pass
                                                break

                                            except discord.errors.NotFound:
                                                attente = load("data")[str(message.guild.id)]['attente']
                                                del attente[0]
                                                fichier[str(message.guild.id)]['attente'] = attente
                                                save(fichier,"data")
                                                dico = attente[0]

                                    try:           
                                        lien =  message.content.split()[1]
                                    except IndexError:
                                        pass
                                    if len(message.content.split())  == 2 and not message.content.split()[1].startswith("https://") :
                                        try:
                                            if message.content.split()[1] in playlists:# catégorie spécifié
                                                I = random_music(message.content.split()[1])
                                                lien,nom = I[0], I[1]


                                        except IndexError:
                                                I = random_music(message.content.split()[1])
                                                lien,nom = I[0], I[1]
                                                message.content += ' ' + lien


                                    if len(message.content.split())  == 1:#si pas d'argument
                                        try:
                                            I = random_music()
                                            lien,nom = I[0], I[1]

                                        except IndexError:
                                            I = random_music()
                                            lien,nom = I[0], I[1]

                                    m = await message.reply("Chargement en cours, veuillez patienter")
                                    try:
                                        async with song.typing():
                                            with youtube_dl.YoutubeDL(ytdlopts) as ydl:
                                                try:
                                                    I_URL = ydl.extract_info(lien, download=False)['formats'][0]['url']
                                                except KeyError:
                                                    I_URL = ydl.extract_info(lien, download=False)['entries'][0]['url']
                                            FFMPEG_OPTIONS = {'options': '-vn',"before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"}
                                            source = await discord.FFmpegOpusAudio.from_probe(I_URL, **FFMPEG_OPTIONS)
                                            voice_client.play(source)
                                        while not voice_client.is_playing():
                                            await asyncio.sleep(1)
                                        user = get(message.guild.members, id = message.author.id)
                                        await message.reply(f'{user.display_name} est entrain de jouer : ** {nom} ** 🎵')
                                        await m.delete()
                                        Role = discord.utils.get(message.guild.roles, name = "Diffuseur")
                                        await discord.Member.add_roles(user, Role)
                                        if len(registre) == 0:
                                            attente = load("data")[str(message.guild.id)]['attente']
                                            del attente[0]
                                            fichier[str(message.guild.id)]['attente'] = attente
                                        else:
                                            registre = load("data")[str(message.guild.id)]['registre']
                                            fichier[str(message.guild.id)]['registre'] = []
                                        save(fichier,"data")
                                        while voice_client.is_playing() or  voice_client.is_paused():
                                            await asyncio.sleep(5)
                                        voice_client.cleanup()
                                        registre = load("data")[str(message.guild.id)]['registre']
                                        attente = load("data")[str(message.guild.id)]['attente']
                                        if len(attente) == 0 and len(registre) == 0:
                                            await discord.Member.remove_roles(user, Role)
                                            await song.send("Fin de la diffusion")
                                            await voice_client.disconnect()
                                            return
                                        else:
                                            await discord.Member.remove_roles(user, Role)
                                    except FileNotFoundError:
                                        await message.reply(":warning: La vidéo n'as pas pu être trouvé, vérifier l'url")
                            
                                    


                if  message.content == "!pause":
                    voice_client = message.guild.voice_client
                    if message.channel == song:
                        if voice_client.is_playing() or  voice_client.is_paused():
                            Diffuseur = discord.utils.get(message.guild.roles, name = "Diffuseur")
                                

                            if Diffuseur in message.author.roles and voice_client.is_playing():
                                voice_client.pause()
                                await message.reply("La  lecture as été mise en pause  ")
                                return

                            if not Diffuseur in message.author.roles and voice_client.is_playing():
                                for k in music.members:
                                    if Diffuseur in k.roles:
                                        await message.reply("Seule le diffuseur peut mettre en pause la lecture si il est présent")
                                        return
                                voice_client.pause()
                                await message.reply("La  lecture as été mise en pause ")
                                return

                            if voice_client.is_paused() and role in message.author.roles:
                                await message.reply("La  lecture est déjà en pause ")
                                return

                        else:

                            await message.reply("Ortensia ne diffuse pas de vidéo en ce moment ")

                            return

                elif  message.content == "!resume":
                    if message.channel == song:
                        voice_client = message.guild.voice_client
                        if voice_client.is_playing() or  voice_client.is_paused():
                            role = discord.utils.get(message.guild.roles, name = "Diffuseur")

                            if voice_client.is_paused() and role in message.author.roles:
                                voice_client.resume()
                                await message.reply("La  lecture a repris")
                                return


                            if not role in message.author.roles and voice_client.is_playing():
                                for k in music.members:
                                    if role in k.roles:
                                        await message.reply("Seule le diffuseur peut reprendre la lecture si il est présent")
                                        return
                                voice_client.resume()
                                await message.reply("La  lecture a repris")
                                return

                            if voice_client.is_playing() and role in message.author.roles:
                                await message.reply("La  lecture est déjà en cours ")
                                return
                        else:
                            await message.reply(f"{client.user.display_name} ne lit pas de vidéo en ce moment ")
                            return

                elif  message.content == "!skip":
                    if message.channel == song:
                        voice_client = message.guild.voice_client
                        if voice_client.is_playing() or voice_client.is_paused():
                            role = discord.utils.get(message.guild.roles, name = "Diffuseur")
                            if  role in message.author.roles:
                                voice_client.stop()
                                await message.reply(f"La lecture as été passée")
                                return

                            if not role in message.author.roles and voice_client.is_playing():
                                for k in music.members:
                                    if role in k.roles:
                                        await message.reply("Seule le diffuseur peut passer la lecture si il est présent")
                                        return
                                voice_client.stop()
                                return
                        else:
                            await message.channel.send(f"{client.user.display_name} ne lit pas de vidéo en ce moment ")
                            return
                    
                
                    




                elif  message.content.startswith("!leave") and message.author.guild_permissions.administrator:
                    voice_client = message.guild.voice_client
                    if voice_client.is_connected():
                        await voice_client.disconnect()
                    else:
                        await message.reply(f"{client.user.display_name} n'est pas connecté ")
                    return

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
                    return


                elif message.content.startswith("!off ") and fichier[str(message.guild.id)]['lg'] == True:
                    langue =  fichier[str(message.guild.id)]['langue']
                    del langue[str(message.author.id)]
                    fichier[str(message.guild.id)]['langue'] = langue
                    save(fichier,'data')
                    await message.reply("La langue as bien été supprimée")
                    return


                elif message.content.startswith("!tr ") and fichier[str(message.guild.id)]['lg'] == True:
                    t = Translator()
                    a = t.translate(str(' '.join(message.content.split()[2:])), dest = str(message.content.split()[1]))
                    await message.reply({a.text})
                    return

                elif message.content.startswith("!del") and message.author.guild_permissions.administrator:
                    number = message.content.split()[1]
                    if number == 'all':
                        messages =  message.channel.history(limit = 200 + 1).flatten()
                    else:
                        messages = await message.channel.history(limit = int(number) + 1).flatten()
                    for each_message in messages:
                        each_message.author == client.user # (!talk,name_channel,chaine)
                        await each_message.delete()
                    return

                elif message.content.startswith("!add ") and message.author.guild_permissions.administrator:# 
                    cle = message.content.split()[1]
                    if cle[0] != '!':
                        await message.reply(":warning: Le premier argument doit être une commande commençant par ! ")
                    else:
                        url = message.content.split()[2]
                        if url[:4] != 'http':
                            await message.reply(":warning: Le deuxième argument doit être une url")
                        else:
                            description = message.content.split()[3:]
                            dico = fichier[str(message.guild.id)]['dico']
                            dico[cle] = [url, description]
                            fichier[str(message.guild.id)]['dico'] = dico
                            save(fichier,'data')
                            await message.reply("La commande as bien été crée")
                    return


                elif message.content == "!ping":
                    latence = f"Le temps de latence d'Ortensia est de {dixi(round((client.latency * 1000),0))}ms "
                    await message.reply(latence)
                    return


                elif message.content.startswith("!talk ") and message.author == message.guild.owner:
                    chaine = ' '.join(message.content.split()[2:])
                    channel =  get_channel(message,message.content.split()[1])
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
                    return

                elif message.content.startswith("!file") and message.author == message.guild.owner: 
                    channel = get_channel(message,message.content.split()[1])
                    chemin = message.content.split()[2]
                    await channel.send(file=discord.File(f'{chemin}'))
                    return

                elif message.content == "!data" and message.author == message.guild.owner :
                    await message.reply(file=discord.File("data.json"))
                    return

                elif message.content.startswith("!mp") and message.author == message.guild.owner:
                    user = get_user(message,message.content.split()[1])
                    await user.send(message.content.split()[2:])
                    return

                elif message.content.startswith("!reaction") and message.author == message.guild.owner:#tag_chan,emo,id,role
                    if len( message.content.split()) < 4:#reaction(channel,emoji,name_role,message)
                        await message.reply("Il manque un ou plusieurs arguments")
                    channel = get_channel(message, message.content.split()[1])
                    emoji = message.content.split()[2]
                    name_role = message.content.split()[4]
                    msg = await channel.fetch_message(message.content.split()[3])
                    await msg.add_reaction(str(emoji))
                    reaction(channel,emoji,msg,name_role)
                    await message.reply("Le message pour attribué des rôles as bien été initialisée")
                    return

                elif message.content.startswith('!mute') :
                    if Modérateur in message.author.roles or message.author.guild_permissions.administrator:
                        colour = discord.Colour
                        muted = get_user(message,message.content.split()[1])
                        mute = discord.utils.get(message.author.guild.roles, name = 'mute')
                        await discord.Member.add_roles(muted,mute)
                        embed = discord.Embed(title = '**Commande de bâillonement**' , colour = 0x992d22)
                        embed.set_author(name = f'{message.author.display_name}(ID : {message.author.id})' , icon_url= r )
                        if message.content.split()[2] == '+' :
                            t = (f"{user.display_name} (ID : {muted.id}) as été rendu(e) muet(te) par {message.author.display_name}"
                            f" pour une durée d'indéfini.\n "
                            f"\n Raison communiquée : {' '.join(message.content.split()[3:])}")

                        if message.content.split()[2] != '+'  :
                            t = (f"{muted.display_name} (ID : {muted.id}) as été rendu(e) muet(te) par {message.author.display_name}"
                            f" pour une durée de {message.content.split()[2]} minutes.\n "
                            f"\n Raison communiquée : {' '.join(message.content.split()[3:])}")


                        retStr = str(f"""```css\n La commande de bâillonement permet de rendre un(e) membre muet(e) (il/elle ne peut donc plus envoyer de messages). ```""")
                        embed.add_field(name = t , value= retStr)
                        await message.channel.send(muted.mention,embed=embed)
                        embed = discord.Embed(title = '**Commande de bâillonement**' , colour = 0x992d22)
                        embed.set_author(name = f'{message.author.display_name}(ID : {muted.id})' , icon_url= r )

                        if message.content.split()[1] == '+':
                            t = (f"{muted.display_name} (ID : {muted.id}) as été rendu(e) muet(te) par {message.author.display_name}"
                            f" pour une durée d'indéfini.\n "
                            f"\n Raison communiquée : {' '.join(message.content.split()[3:])}")
                        if message.content.split()[1] != '+' and message.author != client.user :
                            t = (f"{muted.display_name} (ID : {muted.id}) as été rendu(e) muet(te) par {message.author.display_name}"
                            f" pour une durée de {message.content.split()[2]} minutes.\n"
                            f"\n Raison communiquée : {' '.join(message.content.split()[3:])}")
                        retStr = str(f"""\n à {date.hour}h{date.minute} """)
                        if 10 > date.minute:
                            retStr = str(f"""```css\n à {date.hour}h0{date.minute}  ```""")
                            if 10 > date.hour:
                                retStr = str(f"""```css\n à 0{date.hour}h0{date.minute}  ```""")
                        if 10 > date.hour:
                            retStr = str(f"""```css\n à 0{date.hour}h{date.minute}  ```""")
                        embed.add_field(name = t , value= retStr)
                        await log.send(embed =embed)
                        message.author = client.user
                        await message.delete()
                        if message.content.split()[2] != '+':
                            await asyncio.sleep(int(message.content.split()[2])*60)
                            await discord.Member.remove_roles(muted,mute)
                        return






                elif message.content.startswith('!unmute ') :
                    if Modérateur in message.author.roles or message.author.guild_permissions.administrator:
                        user = get_user(message,message.content.split()[1])
                        mute = discord.utils.get(message.author.guild.roles, name = 'mute')
                        await discord.Member.remove_roles(user,mute)
                        embed = discord.Embed(title = '**Commande de révocation du bâillonement**' , colour = 0x992d22)
                        embed.set_author(name = f'{message.author.display_name}(ID : {message.author.id})' , icon_url= r )
                        t = (f"{user.display_name}(ID : {user.id}) peut de nouveau parler grâce à {message.author.display_name}")
                        retStr = "\n La révocation d'un baîllonnement (qu'on appele unmute) permet un(e) à membre de parler de nouveau."
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
                        return

                elif message.content.startswith('!up') and message.author.guild_permissions.administrator:
                    user = get_user(message,message.content.split()[1])
                    role = discord.utils.get(message.author.guild.roles, name = message.content.split()[2])
                    await discord.Member.add_roles(user,role)
                    if type(role) != None and type(user) != None:
                        await message.reply(f"{user.display_name} as bien obtenue le rôle {message.content.split()[2]}")
                    return
                    #channel = message.channel


                elif message.content.startswith('!down ') and message.author.guild_permissions.administrator:
                    user = get_user(message,message.content.split()[1])
                    role = discord.utils.get(message.author.guild.roles, name = message.content.split()[2])
                    await discord.Member.remove_roles(user,role)
                    if type(role) != None and type(user) != None:
                        await message.reply(f"{user.display_name} as bien perdue le rôle {message.content.split()[2]}")
                    return
                    #channel = message.channel

                elif message.content.startswith('!all ') and message.author == message.guild.owner:
                    for member in message.guild.members:
                        role = discord.utils.get(message.author.guild.roles, name = message.content.split()[1])
                        await discord.Member.add_roles(member,role)
                    return

                elif message.content.startswith('!nobody ') and message.author == message.guild.owner:
                    for member in message.guild.members:
                        role = discord.utils.get(message.author.guild.roles, name = message.content.split()[1])
                        await discord.Member.remove_roles(member,role)
                    return

                elif message.content.startswith('!new ') and message.author.guild_permissions.administrator:
                    fichier[str(message.guild.id)]['new'] = message.content.split()[1]
                    save(fichier,'data')
                    await message.reply("Le role à attribuer aux nouveaux arrivant a bien été définis")
                    return

                elif message.content.startswith('!del_new ') and message.author.guild_permissions.administrator:
                    fichier[str(message.guild.id)]['new'] = None
                    save(fichier,'data')
                    await message.reply("Le role à attribuer aux nouveaux arrivant a bien été supprimer")
                    return

                elif message.content.startswith('!upgrade ') and message.author.guild_permissions.administrator:
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
                    return


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
                        retStr = f"{date.year}/{date.month}/{date.day}-{date.hour}:0{date.minute}"
                        if 10 > date.minute and 10 > date.hour:
                                retStr = f"{date.year}/{date.month}/{date.day}-0{date.hour}:0{date.minute}"
                    if 10 > date.hour and 10 <= date.minute :
                        retStr = f"{date.year}/{date.month}/{date.day}-0{date.hour}:{date.minute}"
                    t = (f"```{user.display_name} (ID : {user.id})  as perdu le role {message.content.split()[2]}```")
                    embed.add_field(name = t , value= retStr)
                    await log.send(embed = embed)
                    return

                elif message.content.startswith('!nick') and message.author.guild_permissions.administrator:
                    user = get_user(message,message.content.split()[1])
                    n = user.display_name
                    t = message.content.split()[2][0].upper() + message.content.split()[2][1:] #
                    await user.edit(nick = t)
                    await message.channel.send(f"""Le nom de {user.mention} as bien été modifié \n Ancien nom : "{n}" """
                                  f"""\n Nouveau nom : "{t}" """) 
                    return
                    
                

                elif message.content.startswith('!mod') and message.author.guild_permissions.administrator:
                    user = get_user(message,message.content.split()[1])
                    channel = get_channel(message,message.content.split()[2])
                    await channel.set_permissions(target = user , read_messages = True)
                    return
                    
                elif message.content.startswith('!ts') and message.author == message.guild.owner:
                    for guild in client.guilds:
                        if guild.name == message.content.split()[1]:
                            c = guild.text_channels[0]
                            t = await c.create_invite()
                            await message.reply(t)
                    return
                    
                elif message.content.startswith('!build') and message.author == message.guild.owner:
                    guild = await  client.create_guild(name = message.content.split()[1])
                    guild = client.get_guild(guild.id)
                    
                    if discord.utils.get(guild.roles, name = "Membre") == None:
                        m = await guild.create_role(name = "Membre") 
                    if discord.utils.get(guild.roles, name = "Modérateur") == None:
                        moderator = await guild.create_role(name = "Modérateur", hoist = True  , mentionable = True )
                    perms = discord.Permissions(administrator = True)
                    if discord.utils.get(guild.roles, name = "Administrateur") == None:
                        admin = await guild.create_role(name = "Administrateur", hoist = True, mentionable = True ,permissions = perms )
                    
                    
                    cata = guild.text_channels[0].category
                    for category in guild.categories:
                        if category.name == "Salons textuels" or category.name == "Text Channels":
                            cata = category
                            
                    for channel in cata.text_channels:
                        logé = False
                        if search(channel.name,'log'):
                            logé = True
                        else:
                            await channel.set_permissions(target = m ,read_messages = True,create_instant_invite = False)
                            await channel.set_permissions(target = guild.default_role ,read_messages = False,create_instant_invite = False)
                            if channel.name == "général" or channel.name == "general": 
                                g = "Salon pour discuter de divers sujets"
                                await channel.edit(name = "💬│général" , position = 1 , topic = g)
                                
                    
                                
                    overwrites = { guild.default_role : discord.PermissionOverwrite(send_messages = False,create_instant_invite = True)}
                    
                
                    r = "Salons de présentation des règles du serveur"
                    régle = await guild.create_text_channel('📜│réglement', overwrites = overwrites , topic =  r,
                                                           position = 0 , category = cata)
                    channel = get(guild.channels, id = régle.id)
                    r = await régle.send(regle)
                    emojis = "✅"
                    await r.add_reaction("✅")
                    msg = await channel.fetch_message(r.id)
                    reaction(channel,emojis,msg,"Membre")
                    
                   
                    
                    #reaction(régle,"✅",r,"Membre")
                    await channel.edit( position = 1 )
                    inv = await régle.create_invite()
                    
                    
                    

                     
                    overwrites = { guild.default_role : discord.PermissionOverwrite(read_messages = False,create_instant_invite = False),
                                  moderator : discord.PermissionOverwrite(read_messages = True),
                                 m : discord.PermissionOverwrite(read_messages = False)}
                    cat = await guild.create_category_channel(name ="Modération" ,overwrites = overwrites, position = 2)
                    r = "Salons de présentation des règles pour les modérateurs"
                    ms = await guild.create_text_channel(name = '📜│règle', overwrites = overwrites , category = cat, position = 0, topic =  r)
                    r = "Salons de discussion des modérateurs"
                    await guild.create_text_channel(name = '🎖️│modérateur', overwrites = overwrites , category = cat, position = 0, topic =  r)
                    mg = await ms.send(regle_mod)
                    await mg.add_reaction("✅")
                    #reaction(channel,emoji,name_role,message)
                    reaction(ms,"✅",mg,"Modérateur")
                    c = "Salon d'information sur les commandes des modérateurs"
                    channel = await guild.create_text_channel(name = 'ℹ️│commande', overwrites=overwrites , position = 4 , category = cata
                                                   , topic =  c)
                    t = ''
                    for k in range(len(liste_moderator)):
                        t += '\n' + liste_moderator[k]
                    t += info
                    embed = discord.Embed(colour =  discord.Colour.blue(),title = "Liste des commandes des modérateurs :" , description = t)
                    await channel.send(embed = embed)
                    return
                    
                    
                    overwrites = {guild.default_role : discord.PermissionOverwrite(read_messages = False,create_instant_invite = False),
                                 admin : discord.PermissionOverwrite(read_messages = True),
                                 m : discord.PermissionOverwrite(read_messages = False)}
                    cat = await guild.create_category_channel(name = "administration" ,overwrites=overwrites, position = 3)
                    await guild.create_text_channel(name = 'commande', overwrites = overwrites , category = cat, position = 1)
                    if logé == False:
                        await guild.create_text_channel(name = 'log', overwrites=overwrites , category = cat, position = 0)
                    
                    
                    
                    overwrites = { guild.default_role : discord.PermissionOverwrite(read_messages = False,create_instant_invite = False),
                                  m : discord.PermissionOverwrite(read_messages = True,send_messages = False)}
                    
                    
                    r = "Salon réservé aux information importante"
                    await guild.create_text_channel(name = '📣│annonce', overwrites = overwrites , position = 2  , category = cata
                                                   , topic =  r)
                    
                    
                    
                                
                            
                    s = "Salon où sont posté les sondages crées avec la commande !sondage"
                    await guild.create_text_channel(name = '🗳│sondage', overwrites = overwrites , position = 3 , category = cata
                                                   , topic =  s)
                    
                    c = "Salon d'information sur les commandes"
                    channel = await guild.create_text_channel(name = 'ℹ️│commande', overwrites=overwrites , position = 4 , category = cata
                                                   , topic =  c)
                    t = ''
                    for k in range(len(liste)):
                        t += '\n' + liste[k]
                    if len(dico) != 0:
                        for k in dico:
                            t += f" {k} : {dico[k][1]}"
                    t += info
                    embed = discord.Embed(colour =  discord.Colour.blue(),title = "Liste des commandes:" , description = t)
                    await channel.send(embed = embed)

                    overwrites = { guild.default_role : discord.PermissionOverwrite(read_messages = False,create_instant_invite = False),
                                  m : discord.PermissionOverwrite(read_messages = True)}
                    s = "Salon réservé aux commandes musicals"
                    await guild.create_text_channel(name = '🎹│song', overwrites = overwrites , position = 5 , category = cata
                                                   , topic =  s)
                    
                    for channel in guild.voice_channels:
                        await channel.set_permissions(target = m , view_channel = True)
                        await channel.set_permissions(target = guild.default_role , view_channel = False,create_instant_invite = False)
                        if channel.name == "Général" or channel.name == "General":
                            await channel.edit(name = "🎙️│Général", position = 1 )
                            

                    overwrites = { guild.default_role: discord.PermissionOverwrite(view_channel = False,create_instant_invite = False),
                                  m : discord.PermissionOverwrite(view_channel = True)}
                    cata = guild.voice_channels[0].category
                    for category in guild.categories:
                        if category.name == "Salons vocaux" or category.name == "Voice Channels":
                            category.position = 1
                            cat = category
                            
                    await guild.create_voice_channel(name = '📻│Musique', overwrites = overwrites, position = 2 
                                                      , category = cat)
                    
                    await guild.create_voice_channel(name = '🛏️│Afk', overwrites = overwrites, position = 3 
                                                      , category = cat)
                    
                    await message.reply(f"Voici le lien vers le nouveau serveur crée : {inv}")
                    return

                elif message.content.startswith('!ghost') and message.author.guild_permissions.administrator:    
                    nb = await guild.estimate_pruned_members(days = int(message.content.split()[1]))
                    if int(message.content.split()[1]) != 1:
                        await message.reply(f"{nb} membres ne se sont pas connecté durant ces {message.content.split()[1]} derniers jours")
                    else:
                        await message.reply(f"{nb}  membres ne se sont pas connecté  durant un jour ")
                    return

                elif message.content.startswith('!clone') and message.author.guild_permissions.administrator:
                    channel = get_channel(message,message.content.split()[1])
                    if len(message.content.split()) == 3:
                        await channel.clone(name = message.content.split()[2])
                    else:
                        await channel.clone()
                    return

                elif message.content.startswith('!help'):
                    try:
                        if len(message.content.split()) == 2:
                
                            if message.content.split()[1] in aide :
                                embed = discord.Embed(colour =  discord.Colour.blue(),title = f" {message.content.split()[1]} ", description = aide[message.content.split()[1]])
                                await message.author.send(embed = embed)
                                return
                            for guild in message.author.mutual_guilds:   
                                Moderateur = discord.utils.get(guild.roles, name = "Modérateur")
                                user = guild.get_member(message.author.id)

                                if message.content.split()[1] in aide_moderator and Moderateur  in user.roles : # message.author.roles
                                    embed = discord.Embed(colour =  discord.Colour.blue(),title = f" {message.content.split()[1]} ", description = aide_moderator[message.content.split()[1]])
                                    await message.author.send(embed = embed)
                                    return

                                if message.content.split()[1] in aide_administrator and  user.guild_permissions.administrator:
                                    embed = discord.Embed(colour =  discord.Colour.blue(),title = f" {message.content.split()[1]} ", description = aide_administrator[message.content.split()[1]])
                                    await message.author.send(embed = embed)

                                if message.content.split()[1] in aide_owner and  message.author.id == 407189858755280896 :
                                    embed = discord.Embed(colour =  discord.Colour.blue(),title = f" {message.content.split()[1]} ", description = aide_owner[message.content.split()[1]])
                                    await message.author.send(embed = embed)
                                    return

                                if message.content.split()[1] == 'modérateur' and  Moderateur in message.author.roles:
                                    t = ''
                                    for k in range(len(liste_moderator)):
                                        t += '\n' + liste_moderator[k]
                                    t += info
                                    embed = discord.Embed(colour =  discord.Colour.blue(),title = "Liste des commandes des modérateurs :" , description = t)
                                    await message.author.send(embed = embed)
                                    return


                                if message.content.split()[1] == 'administrateur' and  message.author.guild_permissions.administrator:
                                    t = ''
                                    for k in range(len(liste_administrator)):
                                        t += '\n' + liste_administrator[k]
                                    t += info
                                    embed = discord.Embed(colour =  discord.Colour.blue(),title = "Liste des commandes des administrateur :" , description = t)
                                    await message.author.send(embed = embed)
                                    return
                                
                                if message.content.split()[1] == 'music':
                                    t = ''
                                    for k in range(len(liste_music)):
                                        t += '\n' + liste_music[k]
                                    t += '\n\nSyntaxe : !play catégorie'  
                                    embed = discord.Embed(colour =  discord.Colour.blue(),title = "Liste des catégories musicales :" , description = t)
                                    await message.author.send(embed = embed)
                                    return
                                
                                if message.content.split()[1] == 'son':
                                    await message.author.send(bad_son)
                                    return

                                if message.content.split()[1] == 'owner' and  message.author.id == 407189858755280896 :
                                    t = ''
                                    for k in range(len(liste_owner)):
                                        t += '\n' + liste_owner[k]
                                    t += info
                                    embed = discord.Embed(colour =  discord.Colour.blue(),title = "Liste des commandes de l'owner :" , description = t)
                                    await message.author.send(embed = embed)
                                    return

                            await message.author.send(f"""Commande "{message.content.split()[1]}" non reconnue, taper !help """
                                                    """pour voir la liste des commande """)

                        if len(message.content.split()) == 1:       
                            t = ''
                            for k in range(len(liste)):
                                t += '\n' + liste[k]
                            if len(dico) != 0:
                                for k in dico:
                                    t += f"\n{k} : {' '.join(dico[k][1])}"
                            t += info
                            embed = discord.Embed(colour =  discord.Colour.blue(),title = "Liste des commandes :" , description = t)
                            await message.author.send(embed = embed)
                            return

                    except discord.HTTPException or discord.Forbidden:
                        await message.reply("Une erreur est survenue ,veuillez ouvrir vos messages privées et réessayer")
                        return


                dico = fichier[str(message.guild.id)]['dico']
                for cle, valeur in dico.items():
                    if message.content == cle:
                        await message.reply(valeur[0])
                    return
                
                
                
                if message.content.startswith('!lgt') and message.author.guild_permissions.administrator:
                    #vi est le role que doivent avoir les personnes pour jouer
                    vi = discord.utils.get(guild.roles, name = "Joueurs")
                    nb_villageois = message.content.split()[1]
                    nb_lg = message.content.split()[2]
                    if len(vi.members) != nb_villageois + nb_lg :
                        await message.reply("le nombre de villageois + le nombre de loup garous n'est pas égale au nombre de joueurs")
                    else:
                        role = []
                        identite = {}
                        vivant = []
                        #if Diffuseur in message.author.roles
                        #user = await client.fetch_user(id) 
                        for k in range(len(vi.members)):
                            vivant.append(vi.members[k].display_name)
                            
                        for k in range(nb_villageois): # nb villageois dans le nombre de role totaux
                            role.append("Villageois")

                        for k in range(nb_lg): # nb loup garous dans le nombre de role totaux
                            role.append("Loup-Garous")

                        for k in range(len(vi.members)): #distribution des roles
                            nb = randint(0,len(role))
                            identite[vi.members[k].id] = role[nb]
                            await vi.members[k].send({role_explication[role[nb]]})
                            del role[nb]

                        #créer un channel de discussion pour les lg et un pour le vote des lg(ou commande)
                        #mettre une musique d'ambiance
                
                if message.content.startswith('!') and message.content.split()[0] != '!play':
                    await message.reply("Commande non reconnue, taper !help pour plus de détail")
                
                
                #else:
                   # if message.content.startswith('!'):
                        #await message.reply("Commande non reconnue taper '!help' pour plus d'information")

    except AttributeError:
        if message.content.startswith('!ent') :
            browser  = webdriver.Chrome(ChromeDriverManager().install())
            

            browser.get('https://cas.iut.univ-paris8.fr/login?service=https%3a%2f%2fent.iut.univ-paris8.fr%2f')

            browser.find_element_by_name("username").send_keys(surnom)
            browser.find_element_by_name("password").send_keys(mdp)
            #browser.find_element_by_name("submit").click();

            browser.fullscreen_window()
            date = datetime.now()
            today = datetime(date.year, date.month, date.day)
            t = today.weekday()
            
            if t == 6:
                browser.execute_script("scroll(0, 1000);");
                browser.find_element_by_tag_name('iframe').send_keys('\ue015')
                browser.find_element_by_tag_name('iframe').send_keys('\ue015')
                
            else:
                browser.execute_script("scroll(0, 1000);");
                browser.find_element_by_tag_name('iframe').send_keys('\ue015')
                browser.find_element_by_tag_name('iframe').send_keys('\ue015')
                browser.find_element_by_tag_name('iframe').send_keys('\ue015')
            
            await asyncio.sleep(1)
            
            
            

            browser.save_screenshot('ent.png')
            await message.author.send(file=discord.File('ent.png'))
            
            try:
                homeLink = browser.find_element_by_link_text("famegadjen")
                homeLink.click() #clicking on the Home button and mouse cursor should? stay here

                homeLink = browser.find_element_by_link_text("Quitter")
                homeLink.click()
                
            except:
                browser.close()
                #browser.close()
            
           
            
            
        if message.content.startswith('!help'):#message.author.guild_permissions.administrator
            if len(message.content.split()) == 2:
                
                
            
                if message.content.split()[1] in aide :
                    embed = discord.Embed(colour =  discord.Colour.blue(),title = f" {message.content.split()[1]} ", description = aide[message.content.split()[1]])
                    await message.author.send(embed = embed)
                    return
                for guild in message.author.mutual_guilds:   
                    Moderateur = discord.utils.get(guild.roles, name = "Modérateur")
                    user = guild.get_member(message.author.id)
                    
                    for k in range(len(guild.members)):
                        if guild.members[k] == user:
                            num = k
                    
                    
                    
                    if message.content.split()[1] in aide_owner and  message.author.id == 407189858755280896 :
                        embed = discord.Embed(colour =  discord.Colour.blue(),title = f" {message.content.split()[1]} ", description = aide_owner[message.content.split()[1]])
                        await message.author.send(embed = embed)
                        return
                    
                    if message.content.split()[1] == 'modérateur':
                        if  Moderateur in guild.members[num].roles or user.guild_permissions.administrator:
                            t = ''
                            for k in range(len(liste_moderator)):
                                t += '\n' + liste_moderator[k]
                            t += info
                            embed = discord.Embed(colour =  discord.Colour.blue(),title = "Liste des commandes des modérateurs :" , description = t)
                            await message.author.send(embed = embed)
                            return


                    if message.content.split()[1] == 'administrateur' and  user.guild_permissions.administrator:
                        t = ''
                        for k in range(len(liste_administrator)):
                            t += '\n' + liste_administrator[k]
                        t += info
                        embed = discord.Embed(colour =  discord.Colour.blue(),title = "Liste des commandes des administrateur :" , description = t)
                        await message.author.send(embed = embed)
                        return

                    if message.content.split()[1] == 'son':
                        await message.author.send(bad_son)
                        return
                    
                    if message.content.split()[1] == 'music':
                        t = ''
                        for k in range(len(liste_music)):
                            t += '\n' + liste_music[k]
                        t += '\n\nSyntaxe : !play catégorie'
                        embed = discord.Embed(colour =  discord.Colour.blue(),title = "Liste des catégories musicales :" , description = t)
                        await message.author.send(embed = embed)
                        return
                    
                    if message.content.split()[1] == 'owner' and  message.author.id == 407189858755280896 :
                        t = ''
                        for k in range(len(liste_owner)):
                            t += '\n' + liste_owner[k]
                        t += info
                        embed = discord.Embed(colour =  discord.Colour.blue(),title = "Liste des commandes de l'owner :" , description = t)
                        await message.author.send(embed = embed)
                        return
                
                await message.author.send(f"""Commande "{message.content.split()[1]}" non reconnue, taper !help """
                                        """pour voir la liste des commande """)

            if len(message.content.split()) == 1:       
                t = ''
                for k in range(len(liste)):
                    t += '\n' + liste[k]
                if len(dico) != 0:
                    for k in dico:
                        t += f"\n{k} : {' '.join(dico[k][1])}"
                t += info
                embed = discord.Embed(colour =  discord.Colour.blue(),title = "Liste des commandes :" , description = t)
                await message.author.send(embed = embed)
                        
client.run(TOKEN) # # () 


# In[4]:


from datetime import datetime
date = datetime.now()
today = datetime(date.year, date.month, date.day)
today.weekday()


# In[ ]:





# In[68]:


#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.utils import ChromeType
#from selenium.webdriver.common.keys import Keys
#from time import sleep
#from datetime import datetime

#date = datetime.now()
#date.hour

#from datetime import datetime
#today = datetime(date.year, date.month, date.day)
#today.weekday()

#from datetime import datetime

#date = datetime.now()
#date

#browser  = webdriver.Chrome(ChromeDriverManager().install())
            

#browser.get('https://cas.iut.univ-paris8.fr/login?service=https%3a%2f%2fent.iut.univ-paris8.fr%2f')

#browser.find_element_by_name("username").send_keys('famegadjen')
#browser.find_element_by_name("password").send_keys('snake124')
#browser.find_element_by_name("submit").click();

#sleep(5)
#elements = browser.find_elements_by_xpath("//*[@id=joursuiv_mercredi]")
#print(elements)
 #clicking on the Home button and mouse cursor should? stay here

#element = browser.find_element_by_tag_name('div')
#element.click()
#browser.find_element_by_id("mardigris").click();
#browser.find_element_by_css_selector("#mercredi.journee").click();
#browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#homeLink = browser.find_element_by_link_text("famegadjen")
#homeLink.click() #clicking on the Home button and mouse cursor should? stay here
#browser.execute_script("scroll(0, 1000);");
#browser.execute_script("window.scrollBy(0,1000)", "");
#sleep(5)
#browser.save_screenshot('ent4.png')
#browser.close()

