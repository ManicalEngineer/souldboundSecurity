import config
import discord
import random
import json
import time
import socket
import asyncio
from web3 import Web3
import requests
from hexbytes import HexBytes
from eth_account.messages import encode_defunct
from discord import app_commands
from discord.ext import commands
from discord.utils import get

web3 = Web3(Web3.HTTPProvider("https://goerli.infura.io/v3/8cd7704fa37449e1a9561223908decb2"))

contract_address = "0x431B560E36C33df109Fd0F07053A9a3d83F4e7e1"
contract_abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_fromTokenId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_toTokenId","type":"uint256"}],"name":"BatchMetadataUpdate","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"MetadataUpdate","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"projectName","type":"string"}],"name":"ProjectAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"_token","type":"address"}],"name":"allowToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"allowTokens","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"projectName","type":"string"},{"internalType":"address","name":"ownerAddr","type":"address"}],"name":"changeProjectOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"projectName","type":"string"},{"internalType":"address","name":"projectOwner","type":"address"}],"name":"createProject","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"},{"internalType":"uint256","name":"_amt","type":"uint256"},{"internalType":"string","name":"projectName","type":"string"}],"name":"makePayment","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"string","name":"projectName","type":"string"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"","type":"string"}],"name":"projects","outputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"bool","name":"active","type":"bool"},{"internalType":"uint256","name":"nextPaymentDue","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_token","type":"address"}],"name":"removeToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_fee","type":"uint256"}],"name":"setFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"tokenProjects","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"projectName","type":"string"},{"internalType":"bool","name":"active","type":"bool"}],"name":"updateProjectStatus","outputs":[],"stateMutability":"nonpayable","type":"function"}]')

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

API_KEY = config.api_key
url = "https://eth-goerli.g.alchemy.com/nft/v2/VxLAorRx1UVFlBV4Y5kTWcRHO1YT9d5q/getNFTs?{}"


async def waitForSignature():
	try:
		s = socket.socket()
		port = 65432
		ip = "127.0.0.1"
		s.bind((ip, port))
		s.listen(5)
		data = None
		print(f"Socket is listening on port {port}")
		while True:
			c, addr = s.accept()
			print(f"Connected to {c} - {addr}")
			data = json.loads(c.recv(1024).decode())
			print(data)
			if data is not None:
				s.close()
				break
			await asyncio.sleep(0.1)
	except:
		s.close()

	return data

def confirmToken(address):
	print(f'Holder address: {address}')
	url = f"https://eth-goerli.g.alchemy.com/nft/v2/VxLAorRx1UVFlBV4Y5kTWcRHO1YT9d5q/getNFTs?owner={address}"
	nfts = requests.get(url, allow_redirects=True).json()
	for nft in nfts["ownedNfts"]:
		if nft["contract"]["address"].upper() == contract_address.upper():
			tokenID = int(nft["id"]["tokenId"],0)
			print(nft)
			project_name = contract.functions.tokenProjects(tokenID).call()
			project = contract.functions.projects(project_name).call()
			return project[2]

	return False

def recoverAddress(sig, msg):
	message = encode_defunct(text=msg)
	address = web3.eth.account.recover_message(message, signature=sig)
	return address

guild=discord.Object(id="1088599429981945957")

class SoulBound(discord.Client):

	def __init__(self, intents: discord.Intents):
	    super().__init__(intents=intents)
	    self.tree = app_commands.CommandTree(self)

	async def setup_hook(self):
		self.tree.copy_global_to(guild=guild)
		await self.tree.sync(guild=guild)



intents = discord.Intents.default()
intents.message_content = True
client = SoulBound(intents=intents)

#bot = commands.Bot()

msg_dict = {}

wordLst = ["dog", "puppy", "kitten", "son", "daughter", "father", "mother", "grand", "great", "life", "sleep", "house", "truck", "garden", "soda", "pop"]

@client.event
async def on_ready():
	#await self.tree.sync(guild=discord.Object(id="1088599429981945957"))
	print("Ready!")
	print(f'Logged on as {client.user}!')

@client.event
async def on_message(message):
	print(f'Message from {message.author}: {message.content}')
	#print(message.channel.category_id)
	#if message.author.id != 1141505607216681053:
	#	content = message.content
	#	await message.delete()
	#	await message.channel.send(content)
	#await interaction.response.send_message(f'Hi {message.author}! Nice to see you here!')

@client.tree.command(name="post-message", description = "Post message through SBS verification")
@app_commands.describe(msg="Enter Message Here")
@app_commands.describe(sig="Enter Signature")
async def postMessage(interaction: discord.Interaction, msg: str, sig: str):

	print(f'{interaction.user.name}: {msg_dict[interaction.user.name]}')
	
	if confirmToken(address):
		await interaction.response.send_message(f"{interaction.user.name} posted: {msg}")
	else:
		await interaction.response.send_message(f"{interaction.user.name} authorization failed")

async def revoke_role(user, role, window):
	await asyncio.sleep(window)
	await user.remove_roles(role)
	await user.send(content=f'{role} was revoked after {window} seconds')
	print(f'{role} removed')


async def add_role(interaction: discord.Interaction):
	role = get(interaction.guild.roles, name="verified")
	window = 30
	await interaction.user.add_roles(role)
	#await interaction.response.send_message(f'{role} added for {interaction.user} for {window} seconds', ephemeral=True)
	#threading.Timer(30, revoke_role, args=[interaction.user, role])
	await revoke_role(interaction.user, role, window)



@client.tree.command(name="authorize", description = "SBS verification")
async def auth(interaction: discord.Interaction):
	verificationMsg = ""

	for i in range(3):
		verificationMsg += random.choice(wordLst)

	msg_dict[interaction.user.name] = verificationMsg
	user = interaction.user
	await user.send(f"visit http://www.animatenetur.com/soulboundsecurity/verify/?message={verificationMsg}&userID={user}")
	await interaction.response.defer(ephemeral=True, thinking=True)
	data = await waitForSignature()
	address = recoverAddress(data['signature'], msg_dict[user.name])
	if confirmToken(address):
		print("Confirmed")
		await add_role(interaction)
		#http://maniacalengineer.com/soulboundsecurity/verify/?message=sodatrucksleep&userID=.maniacalengineer
		await interaction.followup.send("Authorized", ephemeral=True)
	else:
		print("Denied")
		#interaction.user.send(content="Authorization Failed")
		await interaction.followup.send("Failed", ephemeral=True)
#@client.tree.command(name="temp_role", description="Temporary Role")
#async def role(interaction: discord.Interaction):
	#member = interaction.user
	#role = get(member.server.roles, name="Test")
	#await bot.add_roles(member, role)
	#time.sleep(30)
	#await bot.


API_token = config.discord_api_token

client.run(API_token)
