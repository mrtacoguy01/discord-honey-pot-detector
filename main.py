import discord
import re

client = discord.Client()

# ---- CONFIG ---- #

SERVER_ID = 1338486040683483150

FLAGGED_BOT_IDS = [
    1450060292716494940
]

FLAGGED_IMAGE_URLS = [
    "https://honeypot.riskymh.dev/honeypot.png"
]

FLAGGED_NAME_KEYWORDS = [
    "🍯", "🐻", "🐝", "honey", "pot", "dont", "d0nt", "t2lk", "t4lk", "softban", "kick", "ban", "bot", "do-not", "banned", "kicked"
]

FLAGGED_TEXT_KEYWORDS = [
    "🍯", "🐻", "🐝", "honey", "pot", "dont", "send", "messages", "d0nt", "t2lk", "t4lk", "softban", "kick", "ban", "bot", "banned", "kicked"
]

# ---- CODE ---- #

def contains_text_keyword(text, keyword):
    text = text.lower()
    keyword = keyword.lower()

    return re.search(
        rf"(?<!\w){re.escape(keyword)}(?!\w)",
        text
    ) is not None

def matches_text_keyword(text, keywords):
    return any(
        contains_text_keyword(text, keyword)
        for keyword in keywords
    )

@client.event
async def on_ready():
    guild = client.get_guild(SERVER_ID)

    if not guild:
        await client.close()
        return

    text_channels = guild.text_channels

    for index, channel in enumerate(text_channels):
        score = 0
        instant_flag = False

        # Rule 1
        matched_name_kws = [
            kw for kw in FLAGGED_NAME_KEYWORDS
            if kw in channel.name.lower()
        ]

        if matched_name_kws:
            instant_flag = True

        # Rule 5
        if index == 0:
            score += 1

        # Retrieve past 25 messages
        messages = []
        try:
            async for msg in channel.history(limit=25):
                messages.append(msg)
        except Exception:
            pass

        # Rule 2
        if len(messages) < 25:
            score += 1

        if messages:

            # Rule 3
            latest_msg = messages[0]

            if latest_msg.author.id in FLAGGED_BOT_IDS:
                instant_flag = True

            # Rule 4 & Rule 6
            for msg in messages:

                # Rule 4
                for embed in msg.embeds:
                    embed_text = (
                        f"{embed.title or ''} "
                        f"{embed.description or ''}"
                    )

                    if matches_text_keyword(
                        embed_text,
                        FLAGGED_TEXT_KEYWORDS
                    ):
                        instant_flag = True

                # Rule 6
                for att in msg.attachments:
                    if att.url in FLAGGED_IMAGE_URLS:
                        instant_flag = True

                # Rule 6
                for embed in msg.embeds:
                    img_url = (
                        (embed.image and embed.image.url)
                        or
                        (embed.thumbnail and embed.thumbnail.url)
                    )

                    if img_url in FLAGGED_IMAGE_URLS:
                        instant_flag = True

        # Rule 7
        channel_perms = channel.permissions_for(guild.me)

        rule_broken = instant_flag or score > 0

        if rule_broken and channel_perms.send_messages:
            score += 1

        is_honeypot = instant_flag or score >= 3

        if is_honeypot:
            print(channel.name)

    await client.close()

client.run("ADD TOKEN HERE")