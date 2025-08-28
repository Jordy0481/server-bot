
import os
import discord
from discord.ext import commands
from discord import app_commands

# ---------------- CONFIG ----------------
TOKEN = os.getenv("DISCORD_TOKEN")  # <--- Zet hier je bot token
GUILD_ID = 1410623409863393302  # <--- Server ID waar je dit wilt doen

# Rollen die moeten worden aangemaakt
roles = [
    {"name": "👑 Owner", "color": discord.Color.red(), "permissions": discord.Permissions.all()},
    {"name": "🛠️ Admin", "color": discord.Color.orange(), "permissions": discord.Permissions.all()},
    {"name": "👮 Politie", "color": discord.Color.blue()},
    {"name": "🎖️ KMAR", "color": discord.Color.dark_blue()},
    {"name": "🚑 EMS", "color": discord.Color.red()},
    {"name": "🚒 ANWB", "color": discord.Color.orange()},
    {"name": "💣 Crimineel", "color": discord.Color.dark_red()},
    {"name": "👤 Burger", "color": discord.Color.light_grey()},
    {"name": "🤖 Bot", "color": discord.Color.teal()},
]

# Categorieën en kanalen
categories = [
   
 {
      "name": "👤 Speler Logs",
      "channels": [
        "⚡・join-leave-logs",
        "🕵️・name-change-logs",
        "⏱️・playtime-logs",
        "📍・location-logs",
        "🎯・kill-logs",
        "❤️・revive-logs",
        "💉・heal-logs",
        "🍔・status-logs",
        "👥・interaction-logs",
        "🎮・animation-logs",
        "🗣️・voice-logs"
      ]
    },
    {
      "name": "🛠️ Admin Logs",
      "channels": [
        "👮・admin-actions",
        "🔨・ban-logs",
        "❌・kick-logs",
        "⚠️・warn-logs",
        "🎁・giveitem-logs",
        "💎・giveweapon-logs",
        "💵・givemoney-logs",
        "🚀・teleport-logs",
        "👀・spectate-logs",
        "📢・report-handling-logs",
        "📋・announcement-logs",
        "🛠️・admin-repair-logs"
      ]
    },
    {
      "name": "🚓 Politie & KMAR Logs",
      "channels": [
        "🚓・arrest-logs",
        "🔫・seize-logs",
        "📋・ticket-logs",
        "📝・fine-logs",
        "⛓️・jail-logs",
        "🕵️・search-logs",
        "👮‍♂️・police-duty-logs",
        "🎖️・kmar-duty-logs",
        "🎖️・kmar-border-logs",
        "🪖・kmar-raid-logs",
        "🪪・id-check-logs"
      ]
    },
    {
      "name": "🚑 EMS & ANWB Logs",
      "channels": [
        "🚑・ems-duty-logs",
        "💊・ems-treatment-logs",
        "❤️・ems-revive-logs",
        "🚒・anwb-duty-logs",
        "🔧・anwb-repair-logs",
        "⛽・anwb-fuel-logs",
        "🪝・anwb-tow-logs",
        "🚑・medkit-logs"
      ]
    },
    {
      "name": "💰 Economie / Koop & Verkoop",
      "channels": [
        "💰・money-logs",
        "🎲・blackmoney-logs",
        "🛒・shop-buy-logs",
        "🛍️・shop-sell-logs",
        "🔫・weapon-buy-logs",
        "💎・weapon-sell-logs",
        "🌿・drug-buy-logs",
        "🌱・drug-sell-logs",
        "🏚️・house-buy-logs",
        "🏘️・house-sell-logs",
        "🏢・apartment-buy-logs",
        "🏬・apartment-sell-logs",
        "🚗・car-buy-logs",
        "🏁・car-sell-logs",
        "🚤・boat-buy-logs",
        "✈️・plane-buy-logs",
        "🛳️・property-rent-logs",
        "📦・stash-logs",
        "🏪・inventory-logs",
        "🏦・society-logs",
        "🎰・casino-logs",
        "🍷・alcohol-buy-logs",
        "🍺・alcohol-sell-logs",
        "🐟・fishing-logs",
        "🌾・farming-logs"
      ]
    },
    {
      "name": "🚗 Voertuig Logs",
      "channels": [
        "🚗・vehicle-spawn-logs",
        "🅿️・garage-logs",
        "🛠️・vehicle-mod-logs",
        "⛽・fuel-logs",
        "🏁・vehicle-theft-logs",
        "💥・vehicle-damage-logs",
        "🔑・vehicle-lockpick-logs",
        "🚓・vehicle-impound-logs",
        "🪛・vehicle-upgrade-logs",
        "🛞・tire-change-logs"
      ]
    },
    {
      "name": "🏠 Appartement / Woning Logs",
      "channels": [
        "🏠・apartment-enter-logs",
        "🚪・apartment-exit-logs",
        "🗝️・apartment-key-logs",
        "🛋️・apartment-storage-logs",
        "🏚️・house-key-logs",
        "🏠・house-raid-logs",
        "🔑・house-lockpick-logs"
      ]
    },
    {
      "name": "💣 Criminele Logs",
      "channels": [
        "💣・robbery-logs",
        "🏦・bank-heist-logs",
        "🚚・truck-heist-logs",
        "💼・money-launder-logs",
        "🧪・drug-production-logs",
        "🌿・drug-harvest-logs",
        "🔫・gang-war-logs"
      ]
    },
    {
      "name": "⚙️ Systeem Logs",
      "channels": [
        "🐛・error-logs",
        "🔧・resource-logs",
        "📡・anticheat-logs",
        "🌐・connection-logs",
        "📊・performance-logs",
        "🔒・security-logs",
        "💻・command-logs",
        "🕹️・script-event-logs"
      ]
    },
    {
      "name": "🤖 Discord ↔ Server Sync",
      "channels": [
        "🔗・discord-link-logs",
        "🎫・ticket-logs",
        "📨・report-logs",
        "🤖・bot-logs",
        "🛡️・role-change-logs",
        "📢・discord-announcement-logs"
      ]
    }
  ]
# ---------------- BOT SETUP ----------------
intents = discord.Intents.default()
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Ingelogd als {bot.user}")

@bot.tree.command(name="server", description="Maak alle rollen, categorieën en kanalen aan")
@app_commands.checks.has_permissions(administrator=True)
async def server_setup(interaction: discord.Interaction):
    await interaction.response.send_message("🚀 Server setup wordt gestart...", ephemeral=True)

    # Rollen maken
    for role in roles:
        await interaction.guild.create_role(
            name=role["name"],
            color=role.get("color", discord.Color.default()),
            permissions=role.get("permissions", discord.Permissions.none()),
            reason="Server setup rol aanmaak"
        )

    # Categorieën + kanalen maken
    for cat in categories:
        category = await interaction.guild.create_category(cat["name"])
        for ch in cat["channels"]:
            await interaction.guild.create_text_channel(ch, category=category)

    await interaction.followup.send("✅ Server setup voltooid!")

bot.run(TOKEN)
