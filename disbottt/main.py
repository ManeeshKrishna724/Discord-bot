import discord
import datetime
import time
import json
from discord.ext import commands
import random
import pytz
import requests
from bs4 import BeautifulSoup
import os
from web import keep_alive
from bing_image_urls import bing_image_urls



bot = discord.Client()
client = commands.Bot(command_prefix=('!'))

def _start():
  @client.event
  async def on_ready(ctx):
    await ctx.send('Started')

def dog_gen():
  r = requests.get('https://dog.ceo/api/breeds/image/random'). json()
  ppen = r['message']
  return ppen


def fact():
  qer = requests.get('https://catfact.ninja/fact?max_length=100').json()
  ft = qer['fact']
  return ft

def cat_gen ():
  req = requests.get('http://aws.random.cat/meow').json()
  pen = req['file']
  return pen


responses = ["I see it, yes.", "Ask again later.", "Better not tell you now.","Cannot predict now.", "Concentrate and ask again.","Don’t count on it.", "It is certain.", "It is decidedly so.","Most likely.", "My reply is no.","My sources say no.","Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.","Yes.", "Yes – definitely.","You may rely on it."]

@client.event
async def on_ready():
  print(f"{client.user} Started...")


def _8_ball():
  rply = random.choice(responses)
  return rply

@client.command()
async def start(ctx):
  _start()

@client.command()
async def about(ctx):
  await ctx.reply('https://c.tenor.com/-z2KfO5zAckAAAAC/hello-there-baby-yoda.gif')
  name = 'VOLT MaX'
  discriminator = '#8246'
  final = '@'+name+discriminator
  await ctx.send(f'Language : Python 3.0  \nDeveloper : {final } ')

rply = random.choice(responses)

@client.command(aliases=['8ball'])
async def opinion(ctx,*, question):
  await ctx.send(f"Question : {question} \nMy Opinion : {_8_ball()}")

@client.command()
async def clear(ctx, amount = 3):
  if int(amount) > 30 and ctx.author.name != 'VOLT MaX':
    await ctx.send('Only Max can delete more than 30 messages.')
  else:
    await ctx.channel.purge(limit=amount)
    time.sleep(1)
    await ctx.send(f'{amount} message deleted 👽')



@client.command()
async def commands(ctx):
  await ctx.send('commands - \n1 | !about - To know more about me. \n2 | !8ball - To play Magic 8ball(To get my opinion)  Eg - !8ball Do you think that I will pass my exam?\n3 | !clear - To clear chat message. Eg - !clear 10 - To delete 10 msg. \n4 | !time - To get present time.')

t_zone = pytz.timezone('Asia/Kolkata')
present_time = datetime.datetime.now(t_zone)
tim = present_time.strftime('Date = %d/%b/%Y  \nTime = %H : %M')

@client.command(aliases=['time'])
async def now(ctx):
  await ctx.send(tim)

@client.command()
async def kick(ctx, member:discord. Member, because=None):
  await member.kick(reason = because)
  await ctx.send(f"Successfully kicked {member.mention} \nReason : {because}")


@client.command()
async def ban(ctx, member:discord. Member, because=None):
  await member.ban(reason = because)
  await ctx.send(f"Successfully banned {member.mention} \nReason : {because}")
wrds = ['bloop']

@client. event
async def on_message(message):
  for words in wrds:
    if message.content in words:
      await message.delete()
  await client.process_commands(message)

@client.command()
async def cat(ctx):
  ct = await ctx.send(cat_gen())
  await ct.reply(f"Fact : {fact()}")

@client.command()
async def id(ctx):
  await ctx.send(f"{ctx. author. name}#{ctx.author.discriminator}")


def jdfacts():
  data = open("dfact.json")
  ld = json.load(data)
  rann = random.choice(ld)
  return rann



@client.command()
async def info(ctx):
  await ctx.send(f"Click : {ctx.author.mention}")

@client.command()
async def dog(ctx):
  f = await ctx.send(dog_gen())
  await ctx.send(jdfacts())


@client.command()
async def gen(ctx,name,*,url):
  await ctx.send(f'[{name}](buttonurl:{url})')


@client.command()
async def google(ctx,*,name):
  result = search(name,num=5,stop=5, pause=2)

  try:
    for z in result:
       await ctx.send(z)
  except Exception as a:
    print(f'Error : {a}')
    await ctx.send('Something went wrong')


@client.command()
async def calc(ctx,*,prblem):
  rslt = eval(prblem)
  await ctx.send(f'{prblem} = {rslt}')

@client.command()
async def dfp(ctx,limit,*,name):
  i = 1

  while i <= 2:
      name = name
      url = f"https://m.cfake.com/picture/{name}/{str(i)}/p{str(i)}{str(i)}".replace(' ','_')
      soup = soup = BeautifulSoup(requests.get(url).text, 'lxml')

      try:
          img_tags = soup.find_all("img")
          for img in img_tags:
              if (img['src'] == '/images/flags/United_States_of_America.png') or (img['src'] == '/images/page_precedente.gif') or (img['src'] == '/images/page_suivante.gif') or (img['src'] == '/images/tag.png'):
                  continue
              else:
                  word = img['src']
                  await ctx.send('http://m.cfake.com'+word)


          i+=1

      except  Exception as ex:
          pass






@client.command()
async def img(ctx,limit,*,name):
  if int(limit) > 100 and ctx.author.name != 'VOLT MaX':
    limit = '10'
    await ctx.send('Max have restricted to request more than 100 images at a time.Here is 10 result for your search')
  else:
    img = bing_image_urls(name,limit=int(limit),adult_filter_off=False)
    for z in img:
      await ctx.send(z)



keep_alive()
tke = 'OTE0Mzk4MTkzMjgwNzc4Mjky.YaMdrQ.gkB4L1803YX0QN7Hp-njig8aJkw'
client.run(tke)
