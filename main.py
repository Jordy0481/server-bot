import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

GUILD_ID = 1463903186665341052  # vervang door je server ID
STAFF_ROLES = ["🛡️ Moderator", "🛡️ Senior Moderator", "👑 Admin"]

# Rollen met emoji
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

# Categorieën en kanalen (NL + EN)
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
        {"name": "🎥│video", "type": "text"},
        {"name": "🎥│videos-en", "type": "text"},
        {"name": "🎶│muziek", "type": "text"},
        {"name": "🎶│music-en", "type": "text"},
        {"name": "📢│ping", "type": "text"},
        {"name": "📢│pings-en", "type": "text"},
        {"name": "😴│late-night", "type": "text"},
        {"name": "🌙│late-night-en", "type": "text"},
        {"name": "🔥│hot-takes", "type": "text"},
        {"name": "🔥│hot-takes-en", "type": "text"},
        {"name": "💀│rage", "type": "text"},
        {"name": "💀│rage-en", "type": "text"},
        {"name": "🤡│random", "type": "text"},
        {"name": "🤡│random-en", "type": "text"},
    ],
    # Games: elke game een categorie
    "🚓 FiveM": [
        {"name": "fivem-chat", "type": "text"},
        {"name": "fivem-lfg", "type": "text"},
        {"name": "fivem-clips", "type": "text"},
        {"name": "fivem-updates", "type": "text"},
        {"name": "fivem-vragen", "type": "text"},
        {"name": "fivem-mods", "type": "text"},
        {"name": "fivem-bugs", "type": "text"},
        {"name": "🚓 FiveM VC", "type": "voice"},
        {"name": "fivem-chat-en", "type": "text"},
        {"name": "fivem-lfg-en", "type": "text"},
        {"name": "fivem-clips-en", "type": "text"},
        {"name": "fivem-updates-en", "type": "text"},
        {"name": "fivem-questions-en", "type": "text"},
        {"name": "fivem-mods-en", "type": "text"},
        {"name": "fivem-bugs-en", "type": "text"},
        {"name": "🚓 FiveM VC-en", "type": "voice"},
    ],
    "⛏️ Minecraft": [
        {"name": "minecraft-chat", "type": "text"},
        {"name": "minecraft-lfg", "type": "text"},
        {"name": "minecraft-builds", "type": "text"},
        {"name": "minecraft-redstone", "type": "text"},
        {"name": "minecraft-survival", "type": "text"},
        {"name": "minecraft-creative", "type": "text"},
        {"name": "minecraft-seeds", "type": "text"},
        {"name": "⛏️ Minecraft VC", "type": "voice"},
        {"name": "minecraft-chat-en", "type": "text"},
        {"name": "minecraft-lfg-en", "type": "text"},
        {"name": "minecraft-builds-en", "type": "text"},
        {"name": "minecraft-redstone-en", "type": "text"},
        {"name": "minecraft-survival-en", "type": "text"},
        {"name": "minecraft-creative-en", "type": "text"},
        {"name": "minecraft-seeds-en", "type": "text"},
        {"name": "⛏️ Minecraft VC-en", "type": "voice"},
    ],
    "🪂 Fortnite": [
        {"name": "fortnite-chat", "type": "text"},
        {"name": "fortnite-lfg", "type": "text"},
        {"name": "fortnite-clips", "type": "text"},
        {"name": "fortnite-loadouts", "type": "text"},
        {"name": "fortnite-updates", "type": "text"},
        {"name": "fortnite-customs", "type": "text"},
        {"name": "🪂 Fortnite VC", "type": "voice"},
        {"name": "fortnite-chat-en", "type": "text"},
        {"name": "fortnite-lfg-en", "type": "text"},
        {"name": "fortnite-clips-en", "type": "text"},
        {"name": "fortnite-loadouts-en", "type": "text"},
        {"name": "fortnite-updates-en", "type": "text"},
        {"name": "fortnite-customs-en", "type": "text"},
        {"name": "🪂 Fortnite VC-en", "type": "voice"},
    ],
    "⚽ FIFA / FC": [
        {"name": "fifa-chat", "type": "text"},
        {"name": "fifa-potjes", "type": "text"},
        {"name": "fifa-packs", "type": "text"},
        {"name": "fifa-rage", "type": "text"},
        {"name": "ultimate-team", "type": "text"},
        {"name": "career-mode", "type": "text"},
        {"name": "⚽ FIFA VC", "type": "voice"},
        {"name": "fifa-chat-en", "type": "text"},
        {"name": "fifa-matches-en", "type": "text"},
        {"name": "fifa-packs-en", "type": "text"},
        {"name": "fifa-rage-en", "type": "text"},
        {"name": "ultimate-team-en", "type": "text"},
        {"name": "career-mode-en", "type": "text"},
        {"name": "⚽ FIFA VC-en", "type": "voice"},
    ],
    "🔊 Voice Lounge": [
        {"name": "🔊 Lounge", "type": "voice"},
        {"name": "🔊 Lounge-en", "type": "voice"},
        {"name": "🎮 Gaming 1", "type": "voice"},
        {"name": "🎮 Gaming 1-en", "type": "voice"},
        {"name": "🎮 Gaming 2", "type": "voice"},
        {"name": "🎮 Gaming 2-en", "type": "voice"},
        {"name": "🎮 Gaming 3", "type": "voice"},
        {"name": "🎮 Gaming 3-en", "type": "voice"},
        {"name": "🎤 Talk", "type": "voice"},
        {"name": "🎤 Talk-en", "type": "voice"},
        {"name": "😴 AFK", "type": "voice"},
        {"name": "😴 AFK-en", "type": "voice"},
    ],
    "🎉 Events": [
        {"name": "📅│events", "type": "text"},
        {"name": "📅│events-en", "type": "text"},
        {"name": "🏆│toernooien", "type": "text"},
        {"name": "🏆│tournaments-en", "type": "text"},
        {"name": "🎁│giveaways", "type": "text"},
        {"name": "🎁│giveaways-en", "type": "text"},
        {"name": "🧩│challenges", "type": "text"},
        {"name": "🧩│challenges-en", "type": "text"},
        {"name": "📸│event-clips", "type": "text"},
        {"name": "📸│event-clips-en", "type": "text"},
    ],
    "🛡️ Staff / Logs": [
        # NL-only
        {"name": "🔒│mod-chat", "type": "text"},
        {"name": "🧠│staff-overleg", "type": "text"},
        {"name": "📣│staff-aankondigingen", "type": "text"},
        {"name": "🗂️│cases", "type": "text"},
        {"name": "🎯│doelen", "type": "text"},
        {"name": "📥│reports-in", "type": "text"},
        {"name": "🧾│ticket-open", "type": "text"},
        {"name": "🧾│ticket-gesloten", "type": "text"},
        {"name": "🧾│appeals", "type": "text"},
        # Logs
        {"name": "📄│chat-logs", "type": "text"},
        {"name": "📄│voice-logs", "type": "text"},
        {"name": "🚨│automod-logs", "type": "text"},
        {"name": "👮│warn-logs", "type": "text"},
        {"name": "⛔│ban-logs", "type": "text"},
        {"name": "🔁│mute-logs", "type": "text"},
        {"name": "⏳│timeout-logs", "type": "text"},
        {"name": "📤│message-delete-logs", "type": "text"},
        {"name": "✏️│message-edit-logs", "type": "text"},
        {"name": "👤│join-leave-logs", "type": "text"},
        {"name": "🔄│role-update-logs", "type": "text"},
        {"name": "🔧│channel-logs", "type": "text"},
        {"name": "🤖│bot-logs", "type": "text"},
        {"name": "📊│activity-logs", "type": "text"},
        {"name": "🗃️│archief", "type": "text"},
        # Admin
        {"name": "⚙️│server-instellingen", "type": "text"},
        {"name": "🔐│permissions", "type": "text"},
        {"name": "📈│statistieken", "type": "text"},
        {"name": "🧪│test-kanaal", "type": "text"},
    ],
}

@bot.event
async def on_ready():
    print(f"Bot is online! Logged in as {bot.user}")
    guild = bot.get_guild(GUILD_ID)

    # Rollen aanmaken
    for role in roles:
        if not discord.utils.get(guild.roles, name=role["name"]):
            await guild.create_role(name=role["name"], color=role["color"])
            print(f"Role created: {role['name']}")

    # Categorieën en kanalen aanmaken
    for cat_name, chans in categories.items():
        category = discord.utils.get(guild.categories, name=cat_name)
        if not category:
            category = await guild.create_category(cat_name)
            print(f"Category created: {cat_name}")

        for ch in chans:
            if ch["type"] == "text":
                if not discord.utils.get(guild.text_channels, name=ch["name"]):
                    overwrites = {}
                    # Alleen staff kan Staff/Logs zien
                    if cat_name == "🛡️ Staff / Logs":
                        for role_name in STAFF_ROLES:
                            role = discord.utils.get(guild.roles, name=role_name)
                            if role:
                                overwrites[role] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
                        overwrites[guild.default_role] = discord.PermissionOverwrite(view_channel=False)
                    await guild.create_text_channel(ch["name"], category=category, overwrites=overwrites)
                    print(f"Text channel created: {ch['name']}")
            elif ch["type"] == "voice":
                if not discord.utils.get(guild.voice_channels, name=ch["name"]):
                    await guild.create_voice_channel(ch["name"], category=category)
                    print(f"Voice channel created: {ch['name']}")

os.getenv("DISCORD_TOKEN")
