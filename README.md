![Send homework for tomorrow GH Action badge](https://github.com/bortox/discord-classeviva-domani-webhook/actions/workflows/send-homework.yml/badge.svg)


# discord-classeviva-domani-webhook

![Foto per presentare il prodotto](/cover.png)
Compiti per domani con uno webhook di Discord che scannerizza attraverso l'API di classeviva i compiti.

## Come utilizzare lo webhook

* 1) Per prima cosa, puoi **forkare la repo**

* 2) Controlla l'orario in cui sarà eseguita la GitHub Action, che invierà i compiti

  Per fare questo, apri il [file dell'azione](.github/workflows/send-homework.yml) e modifica le linee:
```
  on:
    schedule:
      - cron: "42 12 * * *"
```
   La sintassi è: ore, minuti, giorni del mese, mesi, giorni della settimana, ed è la sintassi di cron, comando per pianificare l'esecuzione di comandi su Linux con una sorta di "tabella di pianificazione". Per saperne di più sulla sintassi, puoi visitare crontab.guru

  In questo caso, l'asterisco significa "tutti i valori possibili", quindi lo script verrà eseguito ogni giorno della settimana di ogni mese alle 12:42 UTC, che corrispondono alle 14:42 Italiane. 

  Modifica questo valore a tuo piacimento, sarà appunto quando verrà inviato il messaggio attraverso uno Webhook.

* 3) Crea uno Webhook da Discord e copiane l'url, se vuoi imoposta un nome e un'immagine per quello.

* 4) Aggiungi le variabili d'ambiente alla repo GitHub:

  Questo bot per funzionare usa tre variabili memorizzate come environment secrets della repo GitHub: 

  * `USERNAME` (email per accedere al registro classeviva)
  * `PASSWORD` (password per accedere al registro classeviva)
  * `DISCORD_WEBHOOK_URL` (url dello webhook creato per pubblicare messaggi in un canale)

