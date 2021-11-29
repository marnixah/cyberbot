import discord
import os
import requests

client = discord.Client()


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
	if message.webhook_id is not None:
		return
	webhook = await message.channel.create_webhook(name=message.author.name)
	# Post message.content to https://cyberify.marnixah.com/cyberify and get the response
	response = requests.post(
		'https://cyberify.marnixah.com/cyberify', json={"text": message.content})
	await webhook.send(str(response.content.decode('utf-8')), username=message.author.name, avatar_url=message.author.avatar_url)
	await webhook.delete()
	await message.delete()

client.run(os.environ['TOKEN'])
