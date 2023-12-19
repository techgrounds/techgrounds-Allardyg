## Opdracht

### Exercise 1

Maak een dictionary aan in Python met de volgende key-value pairs:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/7ad12b73-eb2e-43ce-9f94-0c1df8c6ef0e)

Loop hier overheen in print elke key-value pair.

Resultaat:

    TechyData = {
        "First Name": "Casper",
        "Last name": "Velzen" ,
        "Job title": "Learning coach",
        "Company": "Techgrounds"
    }

    for x, y in TechyData.items():
        print(x,y)


![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/1a02be3b-2325-4fe6-a926-cc65296a6ee3)


### Exercise 2

Resultaat:

    import csv
    from csv import DictWriter

    field_names = ["first name", "last name", "job title", "company"]

    infodict = {
    }

    print("Hey there. Could you please fill in your first name?")
    infodict.update({"first name":input()})

    print("Could you please fill in your last name?")
    infodict.update({"last name":input()})

    print("Could you please fill in your job title?")
    infodict.update({"job title":input()})

    print("Could you please fill in your company name?")
    infodict.update({"company":input()})

    print("Thank you. That is everything i need, here's a list of your answers:")
    for x, y in infodict.items():
            print(x,y)


    with open('Techyinfo.csv', 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = field_names)
        writer.writeheader()
        writer.writerow(infodict)
        csvfile.close()

  De dictionary wordt naar Techyinfo.csv geschreven, en omdat er in de regel
  
      with open('Techyinfo.csv', 'a') as csvfile:
  
een 'a' staat in plaats van 'w' wordt er tekst bijgeschreven in plaats van overschreven.


![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/b927acd3-0ea4-40ea-a910-816bb07bb7f3)

En het tot slot het resulterende .csv bestand met meerdere dictionaries:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/cb5aadee-f6f7-4cf4-b1fe-5e790a386ed9)

#### Bronnen

https://www.w3schools.com/python/python_dictionaries.asp

https://www.w3schools.com/python/python_dictionaries_loop.asp

https://www.w3schools.com/python/python_dictionaries_add.asp

https://www.geeksforgeeks.org/how-to-save-a-python-dictionary-to-a-csv-file/

https://www.sololearn.com/en/Discuss/2672086/python-how-can-i-append-data-to-a-csv-file-without-overwriting-other-colums
