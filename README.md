> **See a mistake or want to add anything?** <br>
> Contact me on Discord **@t_a3c**, **write an issue**, or **make a PR**.

## Channels must follow these rules, if broken it might be a honey pot

Output:  
```
2026-09-25 22:20:55 INFO     discord.client Logging in using static token.
2026-09-25 22:20:55 INFO     discord.http Found user agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36", build number 621195.
2026-09-25 22:20:55 INFO     discord.http Found TLS fingerprint target "chrome150".
2026-09-25 22:20:56 INFO     discord.gateway Connected to Gateway (session ID: x).
honeypot
2026-09-25 22:21:00 INFO     discord.gateway Gateway received close code 1000 and reason 'Connection closed'.
```
In the output under ``` 2026-09-25 22:20:56 INFO     discord.gateway Connected to Gateway (session ID: x). ``` are the detected channels   
In this case its ```honeypot```


## Rules
Rule 1 (Instant Flag)  
If channel name contains any of the following TEXT:  
"🍯", "🐻", "🐝", "honey", "pot", "dont", "d0nt", "t2lk", "t4lk", "softban", "kick", "ban", "bot", "do-not"  

Rule 2 (+1 Score)  
Has under 25 messages sent in the channel total  

Rule 3 (Instant Flag)  
Latest Message by one of these user ids (bot ids):  
1450060292716494940  

Rule 4 (Instant Flag)  
If theres an embed message in the channel (bot) that contains any of the following WORDS:  
"🍯", "🐻", "🐝", "honey", "pot", "dont", "send", "messages", "d0nt", "t2lk", "t4lk", "softban", "kick", "ban", "bot"  

Rule 5 (+1 Score)  
Is the first channel in the channel list  

Rule 6 (Instant Flag)  
If this image is in the channel (past 25 messages) (including embeds)  
https://honeypot.riskymh.dev/honeypot.png  

Rule 7 (+1 Score IF breaks rule 1, 2, 3, 4, 5, 6)  
Can talk in the channel  