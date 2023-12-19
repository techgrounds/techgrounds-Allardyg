## Opdracht

### Exercise 1

Maak een nieuw script en een variabele met vijf namen, loop over de namen waarbij elke naam op een nieuwe lijn in de terminal wordt geprint.

Resultaat:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/b3a4b676-d9b2-4ca0-96b4-1301490e42f4)

### Exercise 2

Maak een nieuw script met vijf integers, gebruik een for loop om elk getal + het volgende getal in de lijst te printen, behalve het laatste getal.
Het laatste getal moet geprint worden + het eerste getal.

Resultaat:

    newlist = [29,1800,7,264, 2023]

    i = 0

    while i < len(newlist)-1:
        print(newlist[i]+newlist[i+1])
        i = i+1
    else:
        print(newlist[i]+newlist[0])

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/96a78206-c46e-4eb7-9475-bc575d1cc1ab)

Ik gebruik een while loop om door de lijst te gaan, de while loop stopt net voor het laatste getal in de lijst.
Waarna het door gaat naar het volgende stukje code waarbij ik het eerste getal en het laatste getal combineer.


#### Bronnen

https://www.w3schools.com/python/python_lists.asp
