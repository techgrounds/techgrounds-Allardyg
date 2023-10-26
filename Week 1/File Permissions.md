# File Permissions
Elke bestand in Linux heeft rechten voor de eigenaar, groepen, en andere gebruikers.
In deze opdracht leer ik om de rechten aan te passen

## Key-terms
**permissions** - rechten, wat een gebruiker of groep wel of niet mag doen met het bestand

**reading files** - de inhoud van bestanden inzien

**writing files** - de inhoud van bestanden aanpassen

**executing files** - een bestand uitvoeren


## Opdracht
### Gebruikte bronnen
https://www.pluralsight.com/blog/it-ops/linux-file-permissions
https://www.alibabacloud.com/blog/changing-file-and-directory-permissions-with-chmod_594187

### Ervaren problemen
Het verschil tussen het toevoegen en verwijderen van rechten (permissions) had ik eerst niet goed door, waardoor ik bijvoorbeeld -rwx gebruikte in plaats van +rwx.
Verder zijn chown, chgrp, en chmod allemaal aparte commando's, terwijl ik eerst aannam dat het een commando zou zijn met verschillende modifiers.

### Resultaat
Hier is te zien hoe ik een bestand aanmaak en kan lezen, en er een executable van maak. 
ervolgens verander ik de permissions zodat alleen de eigenaar het kan lezen.
en tot slot verander ik de groep en de eigenaar van het bestand zodat mijn huidige gebruiker \(allard_) het niet meer kan lezen behalve met het sudo commando

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/7d5614a6-984a-45f9-ae73-7ce275c486e1)
