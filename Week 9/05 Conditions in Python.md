## Opdracht

### Exercise 1

Gebruik de input() functie, en print verschillende soorten tekst op basis van de gegeven input.

Resultaat:
![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/a8df647e-2190-4fe5-86d8-64c91048cced)

### Exercise 2

Maak een script waarbij de gebruiker om een getal wordt gevraagd, geef een reactie op basis van het antwoord.
Geef het aan als het lager is dan 100, en geef het aan als het hoger is dan 100. Laat dit script pas stoppen wanneer de gebruiker 100 invult als input.

Resultaat:

    print ("Guess a number between 1 and 101")

    Guessed_number = int (input())

    while Guessed_number != 100:

            if Guessed_number <= 100:
                print("too low, try again")

            if Guessed_number >= 101:
                print("I said between 1 and 101, that's too high. try again:")
            Guessed_number = int (input())

    if Guessed_number == 100:
        print("Good job, you got it!")

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/08884bcd-3fe6-439f-a4b2-26df3601b4b4)
