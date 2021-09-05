#Program jest reakcyjnym botem do platformy discord
#Korzystam z bazy danych i uruchamiam bota ( polaczenie Flask'iem ) w serwisie replit.com
#Bot jest bardzo łatwo rozszerzalny

import discord
import os
import requests
import json
import random

from replit import db
from keep_alive import keep_alive

client = discord.Client()

sad_words = ["smutno", "zdołowany", "zdołowana",
             "nie mam siły", "zmęczony", "nie mogę już", "zmęczona"]                   # prosty slownik reakcji, ktory mozna rozszerzac za pomoca ponizszej funkcji update


cheer = ["nie przejmuj się!", "trzymaj się!", "głowa do góry!",                        # reakcje bota, rowniez rozszerzalne
         "jesteś cudowny/a!"]

if "responding" not in db.keys():                                                     # db. - > baza danych serwisu replit.com
    db["responding"] = True


def get_quote():
    response = requests.get(
        "http://zenquotes.io/api/random")                                            # funkcja do komendy inspire, pobieranie ( za pomoca json)
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


def update_reactions(reacting_message):  # aktualizacja slownika reakcji
    if "reactions" in db.keys():
        reactions = db["reactions"]
        reactions.append(reacting_message)
        db["reactions"] = reactions
    else:
        db["reactions"] = [reacting_message]


def delete_reaction(index):                                                             # usuwanie reakcji
    reactions = db["reactions"]
    if len(reactions) > index:
        del reactions[index]
        db["reactions"] = reactions


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event                                                                               # reakcja na slowa w formie funkcji
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("$hi"):
        if str(message.author) == "TomekW#0225":                                             # spersonifikowana reakcja
            await message.channel.send("hi " + str(message.author) + "!")
        else:
            await message.channel.send("hi, I am a bot, bip bop 01011000.")

    msg = message.content

    if msg.startswith('$inspire'):                                                      # reakcja na polecenie 'inspire'
        quote = get_quote()
        await message.channel.send(quote)

    if db["responding"]:                                                                # podstawowa baza reakcji
        options = cheer
        if "reactions" in db.keys():
            options = options + db["reactions"]

        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(options))

    if msg.startswith("$new"):                                                      # polecenie 'new' rozszerza baze reakcji
        reacting_message = msg.split("$new", 1)[1]
        update_reactions(reacting_message)
        await message.channel.send("New reacting message was added.")

    if msg.startswith("$del"):                                                      # usuwanie reakcji
        reactions = []
        if "reactions" in db.keys():
            index = int(msg.split("$del", 1)[1])
            delete_reaction(index)
            reactions = db["reactions"]
            await message.channel.send(reactions)

    if msg.startswith("$list"):                                                     # lista reakcji
        reactions = []
        if "reactions" in db.keys():
            reactions = db["reactions"]
        await message.channel.send(reactions)

    if msg.startswith("$responding"):                                               # wlaczanie / wylaczanie responsywnosci
        value = msg.split("$responding ", 1)[1]

        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Responding is on.")
        else:
            db["responding"] = False
            await message.channel.send("Responding is off.")

    if msg.startswith("$help"):                                                     # lista prostych komend
        await message.channel.send("```diff\n"
                                   "- Commands:\n"
                                   "+      $help - lista komend\n"
                                   "+      $list - lista odpowiedzi dodanych do bazy danych bota\n"
                                   "+      $inspire - losowy insirujący cytat\n"
                                   "+      $new - dodaj nową reakcję do bazy danych bota\n"
                                   "+      $del - usuń nową reakcję, posługując się indeksami, począwszy od 0\n"
                                   "+      $responding true/false - włącz/wyłącz reaktywność bazy danych bota\n"
                                   "+      $hi - powitaj bota\n"
                                   "```")


keep_alive()
client.run(os.getenv('TOKEN'))
