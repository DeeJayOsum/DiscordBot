import discord
import asyncio
import os
import random
import datetime
from discord.ext import commands

client= commands.Bot(command_prefix ='.')

@client.command()
async def ping(ctx):
    await ctx.send(f'nalla ping {round(client.latency * 1000)}ms')

@client.event
async def on_member_join(member):
    if member.id == bot.id:
        return
    channel = discord.utils.get(bot.guilds[0].channels, name="general")
    response = f"Welcome to Oreo, {member.name}."
    await channel.send(response)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    keywords = ["kim","kowlaski","kowlaski#0283"]
    abc=["link"]
    channel = message.channel
    for keyword in keywords:
        if keyword.lower() in message.content.lower():
            response = f"Kochu kallan"
            await channel.send(response)
    for keyword in abc:
        if keyword.lower() in message.content.lower():
            response = f"Thanne Kandpidi"
            await channel.send(response)

        

@client.event
async def on_member_remove(member):
    print(f'{member} why you leave server')

@client.event
async def reminder():
    while(True):
        await client.wait_until_ready()
        online_members = []
        for member in client.get_all_members():
            if member.status !=discord.Status.offline and member.id != client.user.id:
                online_members.append(member.id)
        if len(online_members) > 0:
            user = random.choice(online_members)
            current_time = int(datetime.datetime.now().strftime("%I"))
            channel = discord.utils.get(client.guilds[0].channels, name = "general")
            message = f"Poyi Padikkeda <@{user}> samayam {current_time} ayi"
            await channel.send(message)
        await asyncio.sleep(3600)

client.loop.create_task(reminder())


client.run("NzU2MzczOTI3NTE2ODMxNzg0.X2Q6HQ.g3nibFiOnOaspaC7TH96O9xL0Xw")
