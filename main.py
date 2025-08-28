import { Client, GatewayIntentBits, REST, Routes, SlashCommandBuilder, PermissionFlagsBits } from "discord.js";


// ---------------- CONFIG ----------------
const TOKEN = "DISCORD_TOKEN"; // <--- Zet hier je bot token
const CLIENT_ID = "1410627256593682432"; // <--- Bot ID
const GUILD_ID = "1410623409863393302"; // <--- Server ID waar je dit wilt doen


// Rollen die moeten worden aangemaakt
const roles = [
{ name: "👑 Owner", color: 0xff0000, permissions: [PermissionFlagsBits.Administrator] },
{ name: "🛠️ Admin", color: 0xff8800, permissions: [PermissionFlagsBits.Administrator] },
{ name: "👮 Politie", color: 0x0055ff },
{ name: "🎖️ KMAR", color: 0x0033aa },
{ name: "🚑 EMS", color: 0xff3333 },
{ name: "🚒 ANWB", color: 0xffaa00 },
{ name: "💣 Crimineel", color: 0x660000 },
{ name: "👤 Burger", color: 0xaaaaaa },
{ name: "🤖 Bot", color: 0x00ffcc }
];


// Categorieën en kanalen (versimpeld voorbeeld, jouw volledige JSON kan je hier plakken)
const categories = [
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
  ];


// ---------------- BOT SETUP ----------------
const client = new Client({ intents: [GatewayIntentBits.Guilds] });


// Slash command registreren
const commands = [
new SlashCommandBuilder()
.setName("server")
.setDescription("Maak alle rollen, categorieën en kanalen aan")
.setDefaultMemberPermissions(PermissionFlagsBits.Administrator)
];


const rest = new REST({ version: "10" }).setToken(TOKEN);


(async () => {
try {
console.log("Registering slash commands...");
await rest.put(Routes.applicationGuildCommands(CLIENT_ID, GUILD_ID), {
body: commands.map(cmd => cmd.toJSON()),
});
console.log("Slash commands registered.");
} catch (error) {
console.error(error);
}
})();


// ---------------- COMMAND HANDLER ----------------
client.on("ready", () => {
console.log(`✅ Ingelogd als ${client.user.tag}`);
});


client.on("interactionCreate", async (interaction) => {
if (!interaction.isChatInputCommand()) return;


if (interaction.commandName === "server") {
await interaction.reply({ content: "🚀 Server setup wordt gestart...", ephemeral: true });


// Rollen maken
for (const role of roles) {
await interaction.guild.roles.create({
name: role.name,
color: role.color,
permissions: role.permissions || [],
reason: "Server setup rol aanmaak"
});
}


// Categorieën + kanalen maken
for (const cat of categories) {
const category = await interaction.guild.channels.create({
name: cat.name,
type: 4 // CATEGORY
});


for (const ch of cat.channels) {
await interaction.guild.channels.create({
name: ch,
type: 0, // TEXT
parent: category.id
});
}
}
client.login(TOKEN);
