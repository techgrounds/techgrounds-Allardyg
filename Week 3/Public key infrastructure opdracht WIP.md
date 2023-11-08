# Public Key Infrastructure
In deze opdracht leer ik meer over Self Signed Certificates, en maak ik er zelf een aan.

## Key-terms

Self Signed Certificate - Een certificaat bedoeld om de beveiliging van een website te verbeteren

## Opdracht
Maakt een Self Signed Certificate aan in je linux omgeving

Bekijk Self Signed Certificates van bekende websites en analyseer ze

Bekijk de lijst van Self Signed Certificates op je windows computer, en je linux omgeving.


### Gebruikte bronnen

https://linuxize.com/post/creating-a-self-signed-ssl-certificate/

https://resources.infosecinstitute.com/topics/operating-system-security/using-certificates-in-windows-10/

### Ervaren problemen

Het bekijken van de SSC's van bekende websites kon ik eerst niet vinden, maar dat kan blijkbaar vrij makkelijk door op het slot icoon te klikken in de URL bar.

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/492b9cb1-afae-45b9-9276-0a57277e7f51)

### Resultaat

Ik heb een SSL aangemaakt door middel van het openssl commando

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/5fcb3731-48ca-4af0-8de5-5623bc8df567)

Hier is de inhoud van het bestand:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/a5b95c2d-2a00-4ab0-84e7-7a21670cc58f)

Hier is de SSL van Github te zien:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/8ad30f2d-6242-4b19-b7ee-4a981f31bf6f)

Vergeleken met andere websites zoals Google zie ik dat het bestand minder groot is, en het lijkt er op dat het certicaat deel is van een ander certificaat, wat weer deel is van nog een ander certificaat. En aan de geldiheidsdatum te zien is de eerste ongeveer een jaar geldig, het tweede 10 jaar, en de laatste 25 jaar.

Via windows+R, en ** ben ik terecht gekomen bij de SSL's in mijn Windows omgeving:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/83ce8ac4-1a74-4422-89c3-888e1be1e565)

En via de directory /etc/ssl/certs ben ik terecht gekomen bij de SSL's in mijn Linux omgeving:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/1dab4a4c-6519-4907-9fa6-6d87317568d2)
