## Opdracht

### Exercise 1

Maak een script, import de random package, en print 5 getallen tussen 0 en 100. 

Resultaat:

    import random

    for i in range(5):
        print(random.randrange(0,101))

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/35bfd9e3-b45b-4ff6-b9dd-539b70e3db98)

Iets waar ik tegenaan liep is dat bij het testen van het programma met een kleinere range (1-5, en daarna 1-2) ik merkte dat de 5 en de 2 nooit als resultaat gegeven werden. 
Dit is de reden dat ik 101 gebruik in plaats van 100

### Exercise 2

Maak een script met een custom function dat Hello, World! print naar de terminal.

Resultaat:

    def myfunction():
        print ("Hello, World!")

    myfunction()

Herschrijf het script zodat het een string tekst neemt als argument.

    def myfunction(Name):
    print ("Hello,", Name+"!")

    myfunction("Allard")

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/ff08c4e2-2243-4d61-9a85-d2318bbb67d2)

Iets waar ik tegenaan liep is het uitroepteken, er kwam automatisch een spatie bij. Dit heb ik opgelost door geen Name, "!" te gebruiken maar Name+"!"

### Exercise 3

Maak een nieuw script met deze code:

    def avg():
    # write your code here
    # you are not allowed to edit any code below here

    x = 128
    y = 255
    z = avg(x,y)

    print("The average of",x,"and",y,"is",z)

Pas de bovenstaande code aan zodat het gemiddelde van x en y in de terminal geprint wordt. Je mag de laatste paar regels code niet aanpassen, alleen het begin.


Resultaat:

De code die ik heb veranderd of toegevoegd is als volgt:

    def avg(num1,num2):
    num = num1+num2
    return num/2
    # write your code here

num1 num2 zijn mijn argumenten, en door middel van de return functie geef ik een waarde terug wanneer de functie geroepen wordt. Dit deel je door 2 om het gemiddelde te krijgen.

Dit kan zelfs efficienter door:

    def avg(num1,num2):
    return (num1+num2)/2

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/6e8230bc-780e-4d42-abe1-831067f7cf52)

En hier tot slot de volledige uitwerking.


#### Bronnen

https://www.w3schools.com/python/module_random.asp

https://www.datacamp.com/tutorial/functions-python-tutorial

https://www.programiz.com/python-programming/function
