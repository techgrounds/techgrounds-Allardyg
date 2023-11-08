# Detection, Response & Analysis

Hoe ga je om met een cybersecurity aanval?

## Key-terms

Social Engineering - Het richten van een cybersecurity aanval op de persoon zelf door te rekenen op menselijke fouten. Denk hierbij aan het overtuigen van Tech Support dat je iemand bent met een hoge status binnen het bedrijf

IDS

IPS

Hack response strategies

System hardening

RPO

RTO


## Onderzoek

### IDS and IPS.

### Hack response strategies.

### The concept of systems hardening.

### Different types of disaster recovery options.


    
## Opdracht

    A Company makes daily backups of their database. 
    The database is automatically recovered when a failure happens using the most recent available backup. 
    The recovery happens on a different physical machine than the original database,
    and the entire process takes about 15 minutes. What is the RPO of the database?

The RPO, or recovery point objective, will be the accumulutive data of the past 24h (or 24h and 15min) at most. If the attack happens one minute before the scheduled daily backup, it will have been 23 hours and 59 minutes. From that point on, it still takes 15 minutes to restore the system. However, if the attack happens 5 minutes  after the scheduled backup, there will be 20min worth of lost database data. How much data this actually is will depend on the type of company, and what they decide to store in their database.


    An automatic failover to a backup web server has been configured for a website.
    Because the backup has to be powered on first and has to pull the newest version 
    of the website from GitHub, the process takes about 8 minutes.
    What is the RTO of the website?


The amount of time it will take to be back online will about be 8 minutes, this is also the RTO (recovery time objective).


### Gebruikte bronnen
https://www.juniper.net/nl/nl/research-topics/what-is-ids-ips.html

https://en.wikipedia.org/wiki/Failover

https://www.beyondtrust.com/resources/glossary/systems-hardening

https://www.csoonline.com/article/574649/data-breaches-some-of-the-best-and-worst-among-recent-responses.html

https://www.impactmybiz.com/blog/what-should-company-do-after-data-breach/#assess-damage

https://www.msp360.com/resources/blog/how-to-respond-to-cyberattacks/

https://dynamixsolutions.com/types-disaster-recovery-plans/



### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat
[Omschrijf hoe je weet dat je opdracht gelukt is (gebruik screenshots waar nodig).]
