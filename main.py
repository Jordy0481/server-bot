import os
import discord
from discord.ext import commands
from discord import app_commands

# ---------------- CONFIG ----------------
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = 1463903186665341052  # jouw server ID

# ---------------- ROLES ----------------
roles = [
    {"name": "🆕 Nieuw Lid", "color": discord.Color.blue()},
    {"name": "👤 Lid", "color": discord.Color.green()},
    {"name": "⭐ Actief Lid", "color": discord.Color.gold()},
    {"name": "🏆 Veteran", "color": discord.Color.purple()},
    {"name": "🎖️ Event Winner", "color": discord.Color.orange()},
    {"name": "🚓 FiveM", "color": discord.Color.dark_blue()},
    {"name": "⛏️ Minecraft", "color": discord.Color.teal()},
    {"name": "🪂 Fortnite", "color": discord.Color.red()},
    {"name": "⚽ FIFA / FC", "color": discord.Color.dark_green()},
    {"name": "🛡️ Moderator", "color": discord.Color.dark_red()},
    {"name": "🛡️ Senior Moderator", "color": discord.Color.red()},
    {"name": "👑 Admin", "color": discord.Color.dark_gold()},
    {"name": "😂 Meme Master", "color": discord.Color.light_grey()},
    {"name": "🏗️ Builder", "color": discord.Color.dark_teal()},
    {"name": "🎥 Streamer", "color": discord.Color.gold()},
]

# ---------------- CATEGORIES ----------------
categories = {
    "📌 START / INFO": [
        {"name": "👋│welcome", "type": "text"},
        {"name": "👋│welcome-en", "type": "text"},
        {"name": "📜│rules", "type": "text"},
        {"name": "📜│rules-en", "type": "text"},
        {"name": "❓│faq", "type": "text"},
        {"name": "❓│faq-en", "type": "text"},
        {"name": "📘│server-info", "type": "text"},
        {"name": "📘│server-info-en", "type": "text"},
        {"name": "🎭│roles", "type": "text"},
        {"name": "🎭│roles-en", "type": "text"},
        {"name": "🔔│ping-rollen", "type": "text"},
        {"name": "🔔│ping-roles-en", "type": "text"},
        {"name": "📢│announcements", "type": "text"},
        {"name": "📢│announcements-en", "type": "text"},
        {"name": "📢│aankondigingen", "type": "text"},
    ],

    "💬 CHAT": [
        {"name": "💬│algemeen", "type": "text"},
        {"name": "💬│general-en", "type": "text"},
        {"name": "🗣️│praat", "type": "text"},
        {"name": "🗣️│chat-en", "type": "text"},
        {"name": "😂│memes", "type": "text"},
        {"name": "😂│memes-en", "type": "text"},
        {"name": "📸│clips", "type": "text"},
        {"name": "📸│clips-en", "type": "text"},
        {"name": "🎶│muziek", "type": "text"},
        {"name": "🎶│music-en", "type": "text"},
    ],

    "🚓 FiveM": [
        {"name": "fivem-chat", "type": "text"},
        {"name": "fivem-lfg", "type": "text"},
        {"name": "fivem-clips", "type": "text"},
        {"name": "🚓 FiveM VC", "type": "voice"},
    ],

    "⛏️ Minecraft": [
        {"name": "minecraft-chat", "type": "text"},
        {"name": "minecraft-builds", "type": "text"},
        {"name": "⛏️ Minecraft VC", "type": "voice"},
    ],

    "🪂 Fortnite": [
        {"name": "fortnite-chat", "type": "text"},
        {"name": "fortnite-lfg", "type": "text"},
        {"name": "🪂 Fortnite VC", "type": "voice"},
    ],

    "⚽ FIFA / FC": [
        {"name": "fifa-chat", "type": "text"},
        {"name": "ultimate-team", "type": "text"},
        {"name": "⚽ FIFA VC", "type": "voice"},
    ],

    "🔊 Voice Lounge": [
        {"name": "🔊 Lounge", "type": "voice"},
        {"name": "🎮 Gaming 1", "type": "voice"},
        {"name": "🎮 Gaming 2", "type": "voice"},
        {"name": "😴 AFK", "type": "voice"},
    ],

    "🛡️ Staff / Logs": [
        {"name": "🔒│mod-chat", "type": "text"},
        {"name": "📄│chat-logs", "type": "text"},
        {"name": "🚨│automod-logs", "type": "text"},
        {"name": "⛔│ban-logs", "type": "text"},
        {"name": "🤖│bot-logs", "type": "text"},
        {"name": "⚙️│server-instellingen", "type": "text"},
    ],
}

# ---------------- BOT SETUP ----------------
intents = discord.Intents.default()
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync(guild=discord.Object(id=GUILD_ID))
    print(f"✅ Ingelogd als {bot.user}")

# ---------------- COMMAND ----------------
@bot.tree.command(
    name="server",
    description="Maak alle rollen en kanalen aan",
    guild=discord.Object(id=GUILD_ID)
)
@app_commands.checks.has_permissions(administrator=True)
async def server_setup(interaction: discord.Interaction):
    await interaction.response.send_message("🚀 Server setup gestart...", ephemeral=True)

    guild = interaction.guild

    # Rollen maken
    for role in roles:
        if not discord.utils.get(guild.roles, name=role["name"]):
            await guild.create_role(
                name=role["name"],
                color=role["color"],
                reason="Server setup"
            )

    # Categorieën + kanalen
    for category_name, channels in categories.items():
        category = await guild.create_category(category_name)

        for ch in channels:
            if ch["type"] == "text":
                await guild.create_text_channel(ch["name"], category=category)
            elif ch["type"] == "voice":
                await guild.create_voice_channel(ch["name"], category=category)

    await interaction.followup.send("✅ Server setup voltooid!")

bot.run(TOKEN)
