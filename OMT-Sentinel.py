import discord
import asyncio
import random
import re
import sys
import json
import os
from datetime import datetime
from discord.ext import commands

# ================= CONFIGURATION SYSTEM =================
def load_config():
    config_file = 'config.json'
    if not os.path.exists(config_file):
        default_config = {
            "TOKEN": "YOUR_DISCORD_TOKEN_HERE",
            "WELCOME_CHANNEL_ID": 1478042966626140160,
            "MY_USER_ID": 989347262025060352
        }
        with open(config_file, 'w') as f:
            json.dump(default_config, f, indent=4)
        print("--------------------------------------------------")
        print("❌ CONFIG ERROR: 'config.json' nahi mili.")
        print("✅ Maine ek nayi 'config.json' bana di hai.")
        print("👉 Isme apna Token aur User ID check karein.")
        print("--------------------------------------------------")
        input("Press Enter to exit...")
        sys.exit()
    with open(config_file, 'r') as f:
        return json.load(f)

config_data = load_config()
TOKEN = config_data["TOKEN"]
WELCOME_CHANNEL_ID = int(config_data["WELCOME_CHANNEL_ID"])
MY_USER_ID = int(config_data["MY_USER_ID"])

INFO_BOT_ID = 874910942490677270 
POKETWO_ID = 716390085896962058

stats = {"total_caught": 0}

# ================= UTILITY FUNCTIONS =================
def log_to_file(pokemon):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("catch_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] Caught: {pokemon}\n")

def print_status(msg, status_type="INFO"):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] [{status_type}] {msg} | Total: {stats['total_caught']}")

# ================= NAME FIXES =================
EXTRA_FIXES = {
    "MR-MIME": "Mr. Mime", "MR-RIME": "Mr. Rime", "MIME-JR": "Mime Jr.",
    "FARFETCHD": "Farfetch'd", "SIRFETCHD": "Sirfetch'd", "HO-OH": "Ho-Oh",
    "PORYGON-Z": "Porygon-Z", "PORYGON2": "Porygon2", "TYPE-NULL": "Type: Null",
    "NIDORAN-F": "Nidoran-f", "NIDORAN-M": "Nidoran-m",
    "IRON-VALIANT": "Iron Valiant", "ROARING-MOON": "Roaring Moon",
    "FLABEBE": "Flabébé", "SUNNY-CASTFORM": "Sunny Castform"
}

bot = commands.Bot(command_prefix="!", self_bot=True, chunk_guilds_at_startup=False)

def deep_clean(name):
    name = re.split(r'[<【(\[]', name)[0] 
    name = name.replace('##', '').replace('*', '').strip()
    check_name = name.upper().replace(' ', '-')
    return EXTRA_FIXES.get(check_name, name)

@bot.event
async def on_ready():
    print_status(f"GLUMBOT ONLINE as {bot.user}", "SYSTEM")
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        try:
            await channel.send(f"This Glumbot is created by omt_god <@{MY_USER_ID}>")
            print_status("Welcome message sent!", "SUCCESS")
        except: pass

@bot.event
async def on_message(message):
    # Stop Command
    if message.author.id == bot.user.id and message.content.lower() == "!stop":
        await message.channel.send("Glumbot stopping...")
        await bot.close()
        return

    # ================= CAPTCHA AUTO-SHUTDOWN =================
    if message.author.id == POKETWO_ID:
        msg_low = message.content.lower()
        if "whoa there" in msg_low or "captcha" in msg_low or "verify" in msg_low:
            print_status("🚨 CAPTCHA DETECTED! ALERTING USER...", "CRITICAL")
            
            # Alerting on Discord
            channel = bot.get_channel(WELCOME_CHANNEL_ID)
            if channel:
                await channel.send(f"⚠️ **CAPTCHA ALERT!** <@{MY_USER_ID}> please verify fast! Bot is shutting down for safety.")
            
            await bot.close()
            sys.exit()

    # Catching Logic
    if message.author.id == INFO_BOT_ID:
        content = message.content or (message.embeds[0].description if message.embeds else "")
        if content:
            match = re.search(r'##\s*(?:<.*?>\s*)?([^【<\n\s]+(?:\s+[^【<\n\s]+)*)', content)
            if match:
                pokemon_name = deep_clean(match.group(1).strip())
                
                # Anti-Ban Delays
                wait_time = random.uniform(0.5, 1.0) 
                print_status(f"Target: {pokemon_name} | Waiting {wait_time:.2f}s", "TARGET")
                
                await asyncio.sleep(wait_time)
                async with message.channel.typing():
                    type_delay = len(pokemon_name) * random.uniform(0.1, 0.2)
                    await asyncio.sleep(type_delay)
                    
                    await message.channel.send(f"<@{POKETWO_ID}> c {pokemon_name}")
                    stats["total_caught"] += 1
                    log_to_file(pokemon_name)
                    print_status(f"Caught {pokemon_name}", "SUCCESS")

bot.run(TOKEN)