# Processes

Er zijn verschillende soorten processen die binnen Linux kunnen draaien, deze zijn onververdeeld in Daemons, services, en programma's.
Eerder heb ik gebruik gemaakt van ssh, dit is een voorbeeld van een Daemon. In deze opdracht gebruiken we de telnet Daemon.
Het doel is om te leren welke processen er draaien, hoe je daar meer informatie over kan vinden, en hoe je ze afsluit.

## Key-terms

**Telnet** - een Daemon proces, een verouderde versie van SSH (Secure Shell). Telnet is minder veilig

## Opdracht
### Gebruikte bronnen

https://linuxhandbook.com/run-process-background/

https://www.geeksforgeeks.org/get-process-id-of-linux-foreground-and-background-processes/

https://www.tutorialspoint.com/10-lsquo-free-rsquo-commands-to-check-memory-usage-in-linux


### Ervaren problemen

Het eerste probleem waar ik tegenaan liep was het opstarten van Telnet, dat heb ik opgelost door te kijken naar het gebruik van het ssh proces.
Verder heb ik het programma meerdere keren opgestart omdat ik me er niet van was bewust dat je een proces meerdere keren kan laten draaien.
Tot slot is het me niet gelukt om het kill commando toe te passen, ook niet in combinatie met de PID.
Maar door middel van het fg commando is het gelukt om een achtergrondproces weer naar de voorgrond te brengen, en af te sluiten via "Telnet>quit"


### Resultaat

In de screenshots is te zien hoe ik het telnet proces opstart, 
de Process ID achterhaal en gebruik om te zien hoe veel geheugen het proces gebruikt,
en hoe ik de verschillende Telnet processen afsluit.

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/57b5c6c0-7b35-46d8-a4af-449d4cb89eeb)

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/9e5eccf5-5193-45ca-8311-0383b0bb2724)

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/e2d516e2-8d93-48cf-89e5-499f99465a79)

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/3fa0c531-ae95-43fd-9ae0-3c80b246fde8)

