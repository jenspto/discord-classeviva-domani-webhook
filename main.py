# Avvio, import delle dipendenze necessarie

import json,datetime
from dotenv import load_dotenv
from os import getenv
from discord_webhook import DiscordWebhook, DiscordEmbed
import classeviva
# Caricamento delle variabili private dal file .env, se esiste.
load_dotenv()
USERNAME= getenv('USERNAME')
PASSWORD= getenv('PASSWORD')
DISCORD_WEBHOOK_URL= getenv('DISCORD_WEBHOOK_URL')

# Definisci date di oggi e domani, per i compiti

oggi = datetime.date.today()
domani = oggi + datetime.timedelta(days=1)
if oggi.weekday() == 5: # Se è sabato il bot elencherà i compiti per la prossima settimana.
    dopodomani = domani + datetime.timedelta(days=7)
    target = 'la prossima settimana'
else:
    dopodomani = domani + datetime.timedelta(days=1)
    target = 'domani'

# Accesso a classeviva

registro = classeviva.Session()
registro.login(USERNAME,PASSWORD)

# Estrazione dei compiti

compiti = registro.agenda(domani,dopodomani)
compiti_json = json.loads(json.dumps(compiti))
compiti_list = compiti_json['agenda']
# Ora, minuti e secondi in cui sono stati estratti i compiti
ora_compiti = datetime.datetime.now()
ora_compiti_str = ora_compiti.strftime('%H:%M')

# Crea webhook
messaggio = f'✏️ Compiti ed annotazioni per {target} ({domani.strftime("%d/%m")}-{dopodomani.strftime("%d/%m")})'
webhook = DiscordWebhook(url=DISCORD_WEBHOOK_URL, username=messaggio)
n_embeds = 0
for nota in compiti_list:
    compito_ora = datetime.datetime.fromisoformat(nota['evtDatetimeBegin']).timestamp()
    compito_color = "0000ff" if nota['evtCode'] == "AGNT" else "ff00ff"
    embed = DiscordEmbed(
        title=nota['notes'],
        color=compito_color
    )
    embed.set_image(url='https://raw.githubusercontent.com/bortox/discord-classeviva-domani-webhook/main/line.png')
    embed.set_timestamp(compito_ora)
    embed.set_author(name=nota['authorName'].title())
    embed.set_footer(text=nota['classDesc'])
    if n_embeds % 10 == 0 and n_embeds > 0:
        response = webhook.execute(remove_embeds=True)
    webhook.add_embed(embed)
    n_embeds += 1

response = webhook.execute()
print('All done! Homeworks updated!')
