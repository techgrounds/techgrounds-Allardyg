# Users & Groups
Maak een admin gebruiker aan met sudo rechten en een wachtwoord. 
Zoek vervolgens het bestand waar de gebruiker informatie (namen, wachtwoorden, groepen) staat opgeslagen 
en laat zien dat de nieuwe gebruiker in dit bestand staat.


## Key-terms

**Users** - een gebruiker op het systeem, kan met wachtwoord beveiligd worden.

**Group** - een groep waar een gebruiker deel van kan zijn. Afhankelijk van de groep kan de gebruiker bepaalde rechten hebben.


## Opdracht
### Gebruikte bronnen
https://linuxize.com/post/how-to-create-users-in-linux-using-the-useradd-command/#creating-a-user-and-assign-multiple-groups

https://unix.stackexchange.com/questions/272715/what-does-the-cd-etc-command-do

https://tldp.org/LDP/sag/html/etc-fs.html

### Ervaren problemen

Ik had moeite om het bestand in /etc/ te vinden, dit kwam omdat ik een forward slash vergat en etc/ schreef in plaats van /etc/


### Resultaat
In de screenshot is te zien hoe ik een admin gebruiker heb aangemaakt met wachtwoord.
De gebruiker heeft sudo rechten, en ik kan het bestand /etc/passwd openen waar de informatie van de gebruiker in staat.
Tot slot open ik het /etc/group bestand en laat ik zien dat de gebruiker deel is van de admin groep.

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/e5edf19e-deb3-4fb5-961b-3f2e7541caed)
![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/e3d7d2b6-ccd2-4ce5-a729-249f3853a019)

