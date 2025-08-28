import os
import discord
from discord.ext import commands
from discord import app_commands

# ---------------- CONFIG ----------------
TOKEN = os.getenv("DISCORD_TOKEN")  # Zet je bot token in Render → Environment → DISCORD_TOKEN
GUILD_ID = 1410623409863393302  # Zet hier je server ID

# Rollen
staff_roles = [
    {"name": "Owner", "color": discord.Color.red(), "permissions": discord.Permissions.all()},
    {"name": "Hoge Raad", "color": discord.Color.dark_red()},
    {"name": "Hogeop", "color": discord.Color.orange()},
    {"name": "Management", "color": discord.Color.gold()},
    {"name": "Admin", "color": discord.Color.blue()},
    {"name": "Noorderveen Staff", "color": discord.Color.teal()}
]

# Logcategorieën + alle kanalen APART
categories = [
    {
        "name": "👤 Speler Logs",
        "channels": [
            "⚡・join-logs", "⚡・leave-logs", "🕵️・name-change-logs",
            "🖼️・avatar-change-logs", "⏱️・playtime-logs", "📍・location-logs",
            "🎯・kill-logs", "❤️・revive-logs", "💉・heal-logs",
            "🍔・status-logs", "👥・interaction-logs", "🎮・animation-logs",
            "🎤・voice-join-logs", "🔇・voice-leave-logs", "🔊・voice-mute-logs",
            "🎧・voice-deafen-logs", "📢・voice-move-logs"
        ]
    },
    {
        "name": "🛠️ Admin Logs",
        "channels": [
            "👮・admin-actions", "🔨・ban-logs", "❌・kick-logs", "⚠️・warn-logs",
            "🎁・giveitem-logs", "💎・giveweapon-logs", "💵・givemoney-logs",
            "🚀・teleport-logs", "👀・spectate-logs", "📢・report-handling-logs",
            "📋・announcement-logs", "🛠️・admin-repair-logs", "📌・pin-logs",
            "🗑️・delete-message-logs", "✏️・edit-message-logs"
        ]
    },
    {
        "name": "🚓 Politie & KMAR Logs",
        "channels": [
            "🚓・arrest-logs", "🔫・seize-logs", "📋・ticket-logs", "📝・fine-logs",
            "⛓️・jail-logs", "🕵️・search-logs", "👮‍♂️・police-duty-logs",
            "🎖️・kmar-duty-logs", "🎖️・kmar-border-logs", "🪖・kmar-raid-logs", "🪪・id-check-logs"
        ]
    },
    {
        "name": "🚑 EMS & ANWB Logs",
        "channels": [
            "🚑・ems-duty-logs", "💊・ems-treatment-logs", "❤️・ems-revive-logs",
            "🚒・anwb-duty-logs", "🔧・anwb-repair-logs", "⛽・anwb-fuel-logs",
            "🪝・anwb-tow-logs", "🚑・medkit-logs"
        ]
    },
    {
        "name": "💰 Economie / Koop & Verkoop",
        "channels": [
            "💰・money-logs", "🎲・blackmoney-logs", "🛒・shop-buy-logs", "🛍️・shop-sell-logs",
            "🔫・weapon-buy-logs", "💎・weapon-sell-logs", "🌿・drug-buy-logs", "🌱・drug-sell-logs",
            "🏚️・house-buy-logs", "🏘️・house-sell-logs", "🏢・apartment-buy-logs", "🏬・apartment-sell-logs",
            "🚗・car-buy-logs", "🏁・car-sell-logs", "🚤・boat-buy-logs", "✈️・plane-buy-logs",
            "🛳️・property-rent-logs", "📦・stash-logs", "🏪・inventory-logs", "🏦・society-logs",
            "🎰・casino-logs", "🍷・alcohol-buy-logs", "🍺・alcohol-sell-logs", "🐟・fishing-logs", "🌾・farming-logs"
        ]
    },
    {
        "name": "🚗 Voertuig Logs",
        "channels": [
            "🚗・vehicle-spawn-logs", "🅿️・garage-logs", "🛠️・vehicle-mod-logs",
            "⛽・fuel-logs", "🏁・vehicle-theft-logs", "💥・vehicle-damage-logs",
            "🔑・vehicle-lockpick-logs", "🚓・vehicle-impound-logs",
            "🪛・vehicle-upgrade-logs", "🛞・tire-change-logs"
        ]
    },
    {
        "name": "🏠 Appartement / Woning Logs",
        "channels": [
            "🏠・apartment-enter-logs", "🚪・apartment-exit-logs", "🗝️・apartment-key-logs",
            "🛋️・apartment-storage-logs", "🏚️・house-key-logs", "🏠・house-raid-logs",
            "🔑・house-lockpick-logs"
        ]
    },
    {
        "name": "💣 Criminele Logs",
        "channels": [
            "💣・robbery-logs", "🏦・bank-heist-logs", "🚚・truck-heist-logs",
            "💼・money-launder-logs", "🧪・drug-production-logs", "🌿・drug-harvest-logs",
            "🔫・gang-war-logs"
        ]
    },
    {
        "name": "⚙️ Systeem Logs",
        "channels": [
            "🐛・error-logs", "🔧・resource-logs", "📡・anticheat-logs",
            "🌐・connection-logs", "📊・performance-logs", "🔒・security-logs",
            "💻・command-logs", "🕹️・script-event-logs", "🔑・role-change-logs",
            "👤・permission-change-logs", "📂・channel-create-logs",
            "🗑️・channel-delete-logs", "✏️・channel-edit-logs"
        ]
    },
    {
        "name": "🤖 Discord ↔ Server Sync",
        "channels": [
            "🔗・discord-link-logs", "🎫・ticket-logs", "📨・report-logs",
            "🤖・bot-logs", "🛡️・role-change-logs", "📢・discord-announcement-logs",
            "📋・discord-message-logs"
        ]
    }
]

# ---------------- BOT SETUP ----------------
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync(guild=discord.Object(id=GUILD_ID))
    print(f"✅ Ingelogd als {bot.user} en commands gesynct in {GUILD_ID}")

@bot.tree.command(name="server", description="Maak rollen, categorieën en ALLE log-kanalen aan")
@app_commands.checks.has_permissions(administrator=True)
async def server_setup(interaction: discord.Interaction):
    await interaction.response.send_message("🚀 Server setup gestart...", ephemeral=True)

    # Staffrollen maken
    created_roles = {}
    for role in staff_roles:
        r = await interaction.guild.create_role(
            name=role["name"],
            color=role.get("color", discord.Color.default()),
            permissions=role.get("permissions", discord.Permissions.none()),
            reason="Server setup rol aanmaak"
        )
        created_roles[role["name"]] = r

    # Permissions: alleen staff ziet logs
    overwrites = {
        interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False)
    }
    for r in created_roles.values():
        overwrites[r] = discord.PermissionOverwrite(view_channel=True, send_messages=True)

    # Categorieën + kanalen maken
    for cat in categories:
        category = await interaction.guild.create_category(cat["name"], overwrites=overwrites)
        for ch in cat["channels"]:
            await interaction.guild.create_text_channel(ch, category=category, overwrites=overwrites)

    await interaction.followup.send("✅ Server setup voltooid! Alle logs zijn nu apart gezet.")

bot.run(TOKEN)
