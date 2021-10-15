# Avvio, import delle dipendenze necessarie

import json,datetime
from dotenv import load_dotenv
from os import getenv
from discord_webhook import DiscordWebhook
import classeviva
# Caricamento delle variabili private dal file .env, se esiste.
load_dotenv()
USERNAME= getenv('USERNAME')
PASSWORD= getenv('PASSWORD')
DISCORD_WEBHOOK_URL= getenv('DISCORD_WEBHOOK_URL')

# Definisci date di oggi e domani, per i compiti

oggi = datetime.date.today()
if oggi.weekday() == 6: # Se è sabato il bot elencherà i compiti per la prossima settimana.
    domani = oggi + datetime.timedelta(days=7)
    target = 'la prossima settimana'
else:
    domani = oggi + datetime.timedelta(days=1)
    target = 'domani'
dopodomani = domani + datetime.timedelta(days=1)

# Accesso a classeviva

registro = classeviva.Session()
registro.login(USERNAME,PASSWORD)

# Estrazione dei compiti

compiti = registro.agenda(domani,dopodomani)
compiti_json = json.loads(json.dumps(compiti))
compiti_list = compiti_json['agenda']
print(compiti_list)
# Ora, minuti e secondi in cui sono stati estratti i compiti
ora_compiti = datetime.datetime.now()
ora_compiti_str = ora_compiti.strftime('%H:%M')

# Lista con i messaggi che il bot invierà

messaggi = []
messaggi.append(f'📆 Compiti ed annotazioni per {target} ({domani.strftime("%d/%m")}), estratti alle {ora_compiti_str}\n----------------------------------------\n')
messaggio_compiti = []
for nota in compiti_list:
    compito_emoji = "▫️" if nota['evtCode'] == "AGNT" else "🔸"
    datetime_object = datetime.datetime.fromisoformat(nota['evtDatetimeBegin'])
    if datetime_object.hour != 0:
        strtime = datetime_object.strftime('%d/%m (%H:%M)')
    else:
        strtime = datetime_object.strftime('%d/%m')
    messaggio_compiti.append('🗣️ ' + nota['authorName'].title() + '\n' +  '⌛ ' + strtime + '\n' + compito_emoji +' ' + nota['notes'])
b = registro.lessons(oggi,oggi)
messaggi.append('\n-------------\n'.join(messaggio_compiti))
for messaggio in messaggi: #Invia ogni messaggio
    webhook = DiscordWebhook(url=DISCORD_WEBHOOK_URL, content=messaggio)
    response = webhook.execute()
    pass

print('All done! Homeworks updated!')
