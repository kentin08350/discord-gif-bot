import discord

TOKEN = os.getenv("TOKEN")

PHRASES = [
    "joue quoi",
    "joues quoi",
    "quoi jouer",
    "quoi joué",
    "joué quoi",
    "jouer quoi"
]

GIF_URL = "https://media.discordapp.net/attachments/1136648685883756655/1476512481714372629/image0.gif?ex=69a164e7&is=69a01367&hm=6b80ef306f911406afb4b348580b5539ee7a0d6a4ff23d12d91cabde18688138&=&width=275&height=276"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Connecté en tant que {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    contenu = message.content.lower().strip()

    print("Message normalisé :", contenu)  # debug

    for phrase in PHRASES:
        if phrase.lower() in contenu:
            print("Phrase détectée :", phrase)  # debug
            await message.channel.send(GIF_URL)
            break

client.run(TOKEN)