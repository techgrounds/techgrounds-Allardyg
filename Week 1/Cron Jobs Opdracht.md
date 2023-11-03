# Cron Jobs
Maak een cron job voor een script wat elke minuut draait en de datum schrijft naar een bestand, 

en maak een cron job voor een script wat elke week draait en de beschikbare dist ruimte schrijft naar een bestand in /var/logs

## Key-terms

**Cron** - a service running in the background that will execute commands (jobs) at a specified time, or at a regular interval.

**Cron Job** - standard method of scheduling tasks to run on your server.

**Crontab** - a file with the defined schedules of cron jobs

**Jobs** - and their schedules are defined in a configuration file called a crontab.


## Opdracht
### Gebruikte bronnen
https://www.cyberciti.biz/faq/linux-display-date-and-time/

https://www.baeldung.com/linux/create-crontab-script

https://help.dreamhost.com/hc/en-us/articles/215767047-Creating-a-custom-Cron-Job

https://www.hostinger.com/tutorials/vps/how-to-check-and-manage-disk-space-via-terminal

https://www.loggly.com/ultimate-guide/linux-logging-basics/


### Ervaren problemen
Ik was niet in staat om te schrijven naar de /var/logs directory, en dit is waar ik het meeste moeite mee had. 

De oplossing hiervoor was het dubbelchecken van de permissions, toen ik dit eenmaal had aangepast werkte alles naar behoren.


### Resultaat

Ik heb de opdracht aangepakt door het onder te verdelen in 3 gedeeltes.Het eerste is natuurlijk het script wat de beschikbare disk space schrijft naar de terminal.
Het tweede onderdeel is de cron job correct instellen. En het derde onderdeel is het kunnen schrijven naar de /var/logs directory

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/2f31a60c-51b0-4be9-9497-8a6b2708d366)

Eerste cron job, een script maken wat de datum schrijft naar een bestand.

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/bdeb6d01-465e-4538-a07f-ff5be77e0489)


het bewijs dat mijn script automatisch elke minuut draait

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/8d2861e9-e87f-492e-bbf3-541dba0e304b)

Tweede cronjob, hier is te zien hoe ik een script heb wat via een cronjob elke minuut de datum en beschikbare disk space schrijft naar /var/logs/weeklyLog.txt (om te bewijzen dat het script en de cronjob werkt)

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/ac524ea4-e014-48d3-a417-f7e176897d6e)

Dit is mijn cronjob, nu met @weekly zodat hij wekelijks runt

