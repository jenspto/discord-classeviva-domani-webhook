# Webhook Discord con compiti Classeviva

Invia ogni giorno ad un'ora impostata (in questo caso 14:30, modificabile nel file [send-homework.yml](/.github/workflows/send-homework.yml) in un dato canale la lista dei compiti sul Registro Elettronico Classeviva per il giorno seguente, come **embed** Discord.

![Send homework for tomorrow GH Action badge](https://github.com/bortox/discord-classeviva-domani-webhook/actions/workflows/send-homework.yml/badge.svg)


Questo Webhook sfrutta [ClassevivaAPI](https://github.com/MarcoBuster/ClasseVivaAPI ) di [@MarcoBuster](https://github.com/MarcoBuster)

## Feature:

* Compiti inviati in ordine cronologico
* Se è Sabato, invia i compiti per la prossima settimana
* Username e Password di Classeviva, ed anche l'url dello Webhook, sono conservati come [ENCRYPTED SECRETS](https://docs.github.com/en/actions/security-guides/encrypted-secrets) nella repo, in modo sicuro.
* Orario d'invio dei compiti personalizzabile facilmente
* Riprova ad inviare il messaggio se trova rate-limiting da Discord, grazie al modulo discord-webhook che ha reso tutto più semplice.




![Foto per presentare il prodotto](/cover.png)

## Come utilizzare lo webhook, forkando la repo

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

