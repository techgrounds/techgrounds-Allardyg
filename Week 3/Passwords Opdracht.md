# Passwords

Linux slaat wachtwoorden hashed op, dit houdt in dat ze omgezet worden naar een nieuwe rij tekens. In deze opdracht kijken we daar wat meer naar.


## Key-terms

Hashing - het transformeren van een rij tekst of karakters naar iets anders, 
het is beter voor het opslaan van wachtwoorden. Hashes worden opgeslagen, en op deze manier kan een bedrijf kijken of een ingevuld wachtwoord correct is. De hash wordt vergeleken met de opgeslagen hash.

Symmetrische encryptie - Een andere manier van beveiligen, maar meer bedoeld voor informatie wat al in transit is.

Rainbow Table - Een grote tabel vol makkelijke wachtwoorden en de resulterende hashes.


## Opdracht en resultaat

We hebben hier twee MD5 wachtwoord hashes. Een is een zwak wachtwoord, het andere is een rij van 16 willekeurig generereerde karakters. Zoek beide hashes op in een online rainbow table.

    03F6D7D1D9AAE7160C05F71CE485AD31

    03D086C9B98F90D628F2D1BD84CFA6CA

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/e3b2ba25-6c72-44ff-8f01-08f0ce823982)


We zie hier dat het eerste wachtwoord "Welldone!" is, maar het tweede wachtwoord nog onbekend.

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/b1f9d94b-033b-45ef-8b92-cc638b219543)

Hier maak ik een nieuwe user "Elephant" aan.

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/3650be2f-32f6-40af-aa0a-418ba0711042)

En hier kijk ik in het /etc/shadow bestand voor het hashed wachtwoord

    Create a new user in Linux with the password 12345. Look up the hash in a Rainbow Table.

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/78b24bf9-3b2f-4a05-b7f3-93df618166e7)

Hier zoek ik het hashed wachtwoord op in een online rainbow table. Ondanks het zwakke wachtwoord geeft de rainbow table geen match, dit komt omdat het wachtwoord salted is. Om te begrijpen hoe dit werkt vergelijk ik mijn hash met dat van een peer. We hebben allebei hetzelfde wachtwoord gekozen.
    
Hier vergelijk ik mijn hashed wachtwoord met dat van Bas, we zien dat er aan het begin en aan het eind wat karakters overeen komen, maar dat alles daartussenin compleet anders is. Dit komt omdat de bestanden salted waren voordat ze werden gehashed, wat voor zorgt dat er willekerige data toegevoegd wordt voordat het verandert naar het resulterende hash bestand. Omdat de willekeurige data verschilt voor mij en Bas, hebben wij een andere hash.

    $6$  Qn.HX4XmpYck092S$AbZHVH/Ld5wQe2NoiQ52PklcwaTlviWLrgkr8fKuu5VgdgtbIVmcAJUGUXvAsMsGKXHFxDMSc5AzqK8mZqc5k1  :19668:0:99999:7:::
    $6$  cpww45knJsT9o0Ao$hOHpGpXtXJBsgaxuhfbXmgZ5PwWW9RH53V.D3gQ66xShHxOizuuCn7NnHz5ZLvvwZ/gHbHotj8QTNOZ8tchML1  :19668:0:99999:7:::


### Gebruikte bronnen

https://www.techtarget.com/searchdatamanagement/definition/hashing

https://www.encryptionconsulting.com/education-center/encryption-vs-hashing/

https://www.youtube.com/watch?v=PR7aG8OzRR8


### Ervaren problemen

Ik heb geen problemen ervaren met deze opdracht.
