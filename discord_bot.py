import discord
from discord.ext import commands
import urllib.parse
import requests

# Deine Tokens und Repository Informationen
DISCORD_BOT_TOKEN = "MTMyNzI1MzM4NTQ4OTE1NDE3MA.GT29Jn.bwrmJBxSRgacJzNKSivck0FJU5kXCOpzJicbZA"

intents = discord.Intents.default()  # Standard Intents aktivieren
intents.message_content = True       # Berechtigung zum Lesen von Nachrichteninhalten

bot = commands.Bot(command_prefix="!", intents=intents) # Intents übergeben

# Neuer Event Handler für Befehlsvorschläge
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "!":
        commands_list = [command.name for command in bot.commands]
        embed = discord.Embed(
            title="📝 Verfügbare Befehle",
            description="Hier sind alle verfügbaren Befehle:",
            color=discord.Color.green()
        )
        
        for cmd in commands_list:
            command = bot.get_command(cmd)
            embed.add_field(
                name=f"!{cmd}",
                value=command.help or "Keine Beschreibung verfügbar",
                inline=False
            )
            
        await message.channel.send(embed=embed)
    
    await bot.process_commands(message)

#bot commands
@bot.command()
async def hilfe(ctx):
    """Zeigt die Hilfe für den Bot an."""
    embed = discord.Embed(title=":question: Mr.Issues :question:", description="So benutzt du den Bot:", color=discord.Color.blue())
    embed.add_field(name=":link: Befehl:", value="`!issue Benutzername/Repositoryname Titel des Issues`", inline=False)
    embed.add_field(name=":pencil: Beschreibung:", value="Erstellt einen Link zum Erstellen eines neuen Issues auf GitHub. ", inline=False)
    embed.add_field(name=":bulb: Beispiel:", value="`!issue NADOOIT/NADOO-Launchpad Problem mit dem Editor`  ➡️  Öffnet ein neues Issue im vscode Repository mit dem Titel Problem mit dem Editor", inline=False)
    embed.set_footer(text="Bei Fragen wende dich an den Entwickler: Majd Almotaem.") # Optional: Footer hinzufügen
    await ctx.send(embed=embed)

@bot.command()
async def issue(ctx, repo_name: str, *, issue_title: str):
    """Erstellt einen Link zum "New Issue" Tab eines öffentlichen GitHub Repositories.

    Usage: !issue Benutzername/Repositoryname "Titel des Issues"
    """
    try:
        encoded_title = urllib.parse.quote_plus(issue_title) # Korrekte URL-Kodierung
        new_issue_url = f"https://github.com/{repo_name}/issues/new?title={encoded_title}"
        await ctx.send(f"Erstelle ein neues Issue hier: {new_issue_url}")
    except Exception as e:
        await ctx.send(f"Fehler: {e}")



@bot.command()
async def show_issues(ctx, repo_name: str):
    """Zeigt die offenen Issues eines GitHub Repositories an.
    
    Usage: !show_issues Benutzername/Repositoryname
    """
    try:
        # GitHub API URL für Issues
        api_url = f"https://api.github.com/repos/{repo_name}/issues"
        
        # API Anfrage senden
        response = requests.get(api_url)
        issues = response.json()
        
        if response.status_code == 200:
            # Erstelle ein Embed für die Ausgabe
            embed = discord.Embed(
                title=f"📋 Issues für {repo_name}",
                color=discord.Color.blue()
            )
            
            if not issues:
                embed.description = "Keine offenen Issues gefunden!"
            else:
                # Zeige die ersten 10 Issues an
                for issue in issues[:10]:
                    embed.add_field(
                        name=f"#{issue['number']} - {issue['title']}",
                        value=f"Status: {issue['state']}\n"
                              f"[Link zum Issue]({issue['html_url']})",
                        inline=False
                    )
            
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"Fehler beim Abrufen der Issues. Statuscode: {response.status_code}")
            
    except Exception as e:
        await ctx.send(f"Fehler beim Abrufen der Issues: {str(e)}")



bot.run(DISCORD_BOT_TOKEN)

