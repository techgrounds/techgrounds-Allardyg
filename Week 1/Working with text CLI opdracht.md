# Working with text (CLI)

    1. Use the echo command and output redirection to write a new sentence into your text file using the command line.
    The new sentence should contain the word ‘techgrounds’.
    
    2. Use a command to write the contents of your text file to the terminal.
    Make use of a command to filter the output so that only the sentence containing ‘techgrounds’ appears.
    
    3. Read your text file with the command used in the second step, once again filtering for the word ‘techgrounds’. 
    This time, redirect the output to a new file called ‘techgrounds.txt’.

## Key-terms
**Output redirection** - het resultaat van een linux commando verwerken in een nieuw commando of bestand.

**grep**, een linux commando wat staat voor global regular expression print.

**echo**, een linux commando om de waarden van een variable weer te geven.

**cat**, een linux commando om de inhoud van een bestand weer te geven

**logical operators** - het uitbreiden van een linux commando door middel van extra tekens.  

## Opdracht

### Gebruikte bronnen
https://www.linuxjournal.com/content/how-search-and-find-files-text-strings-linux

https://www.geeksforgeeks.org/echo-command-in-linux-with-examples/


### Ervaren problemen
Tijdens de opdracht heb ik een aantal keer > gebruikt in plaats van >>, in het eerste geval wordt het document overschreven en in het tweede geval wordt de tekst toegevoegd.
Verder heeft grep ook veel logical operators, en er was wat trial and error voor nodig om erachter te komen welke ik precies nodig had.

### Resultaat
![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/f80f3835-673e-40ad-b943-61440ffe4d96)

In de screenshot is te zien hoe ik een tekstbestand (txt.txt) heb met twee zinnen tekst, vervolgens het echo commando gebruik om een zin toe te voegen, en hoe ik grep gebruik om de zin weer te geven met "techgrounds" in de zin.

Tot slot gebruik ik output redirection om het resultaat van de zoekopdracht te schrijven naar een bestand genaamd "techgrounds.txt", en bewijs ik dat door de inhoud van het bestand te laten zien.
