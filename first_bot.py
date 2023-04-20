import discord
import openai


with open("keys.txt") as f:
	# converting our text file to a list of lines
	lines = f.read().split('\n')
	# openai api key
	openai.api_key = lines[0]
	# discord token
	DISCORD_TOKEN = lines[1]
	# close the file
f.close()

response = openai.ChatCompletion.create(
	model ="gpt-3.5-turbo",
	messages=[
	{"role": "system", "content": "You are a cute bunny and very mystery, you like to telling the history and sometimes giving words in mandarin, you love Sichuan opera and change different mask depending on your mood"},
	{"role": "user", "content": "How to make mask changing works in Sichuan Opera?"}
	]
)
print(response.choices[0].message.content)

# specifying our server
GUILD = "{beebonnie's server}"

# create an object that will control our discord bot
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
	for guild in client.guilds:
		if guild.name == GUILD:
			break
	# print out nice statment saying our bot is online (only in command prompt)
	print(f'{client.user} has connected to Discord!')

client.run(DISCORD_TOKEN)

