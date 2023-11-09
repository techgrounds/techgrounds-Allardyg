# Assymmetric Encryption Opdracht

Assymetric Encryption werkt door middel an public keys en private keys. Met de ene key versleutel (encrypt) je de tekst, en met de andere sleutel open (decrypt) je het bericht.


## Key-terms

Encryption - Het veranderen van een rij karakters naar een nieuwe rij onbegrijpelijke karakters, dit kan ongedaan worden gemaakt door decryption

Decryption - Het terugveranderen van een rij onbegrijpelijke karakters naar wat er origineel stond.



## Opdracht

Verstuur een encrypted message naar een klasgenoot via het publieke slack kanaal.


### Gebruikte bronnen en tools

https://www.devglan.com/online-tools/rsa-encryption-decryption

https://www.youtube.com/watch?v=ZPXVSJnDA_A


### Ervaren problemen

Een observatie door een klasgenoot was dat de resulterende string tekst telkens anders is, zelfs als je alle parameters hetzelfde houdt.


### Resultaat
Public key:

    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCawsk4HS2IQ/
    ZwseNheFkRB0ttwvCmSvLgj0cvtW/SZIDa6j5dJ01DrvhH3FeL
    cz8UgyLWNNUCj+1QNKNBjVQmwfQL1yiu5HcltSZIiaaEJlhSiP
    TFhV4jplUcqWljTiPGone756o3tZ3oElehaz53lwf+D8X1WFY8
    H1u4AezWlQIDAQAB

Private key:

    MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAJr
    CyTgdLYhD9nCx42F4WREHS23C8KZK8uCPRy+1b9JkgNrqPl0nTU
    Ou+EfcV4tzPxSDItY01QKP7VA0o0GNVCbB9AvXKK7kdyW1JkiJp
    oQmWFKI9MWFXiOmVRypaWNOI8aid7vnqje1negSV6FrPneXB/4P
    xfVYVjwfW7gB7NaVAgMBAAECgYEAgLnkhTg/10gwhCxy5XAlJXT
    b2MB9StSskPycSaKxEF9ojq6okPNP4Sx4d81fRC7oGTe6klH/m9
    H7ousloDDd/MyAtozV8gTHfmY2kc4iF5CDPgifV+DfvZlHbc1zK
    6szpyDbFFlrf/WrCT194FK5XxtVhRhM4uA2fem8FwycYUECQQD1
    lnzM0ynFW9w/N93fr9CS15J+0DzD/HcHyERTyjwMC4enpEj1M35
    TGIREy5gRHtZRdfA1XGLWwRG0JUmtVxYfAkEAoVJ/uTMvybQbCQ
    ftKLSgjb3YZ3pqjF9aJic5Ko/ur5N2tknYI4fP2JatUwlN4Fonr
    JCf2/sj1uWmGONStqA0ywJBAKRTybYUJYMVcE4sx52BOwLGlBOe
    qspJCCyA6JdYXs2AeYjG+Lp5djGL2hVeVaY/CBEB5XUPGGOyVHJ
    B8Qa3mukCQFzhBrA2DDlw/G/CpIRfGmEBAGrzTAztiRWWV49ttt
    pXaG2jLlGmi8ADYF8CaFfXECiGS8N3YDcFmQ+TMbf7nOkCQHVCy
    vyYp17T20odd+PxaQnpgZzr8TMkJ4tbTNjcXBDZPXeA2PQLe8/b
    PwAFGKrmJkFAmdzCbh/Ge1gNJA90Pgo=

Public key van klasgenoot Deniz:

    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCoW7x25IzWYF1
    bUQfhtYTNFTiW+TY3qc5lFm3/JFu+MPufQz+w0JMjLdBeZRSzVe
    QVKPOvlrRtnrLhKMhg9GPh93hCXRoxeUVNV3qVmh26XHvM5ZgeO
    Y3UJheYnLONmgGDmR8f1CulZ5evyCFN92M3/5IEVNldiDQtGGxx
    fiT/owIDAQAB

Bovenstaande informatie plaatsen we in de website, wat resulteert in het volgende resultaat:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/c5154af9-4a2c-45bd-b4d1-d814346b395d)

Encrypted message van mij naar Deniz:

    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCoW7x25IzWYF1
    bUQfhtYTNFTiW+TY3qc5lFm3/JFu+MPufQz+w0JMjLdBeZRSzVe
    QVKPOvlrRtnrLhKMhg9GPh93hCXRoxeUVNV3qVmh26XHvM5ZgeO
    Y3UJheYnLONmgGDmR8f1CulZ5evyCFN92M3/5IEVNldiDQtGGxx
    fiT/owIDAQAB

Dit delen we in het Slack kanaal:

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/ae4a3601-857f-4315-aa2a-e759738e33b2)



Deniz heeft ons ook een bericht gestuurd.
Encrypted message van Deniz naar mij:

    WFxsErD5xwG2RhC+dcClVmIX05s20cDDE2r1gvgch38nCiaco8x
    RfcnbDoOuxsJJ/8vhtLoYnyXQ057v9TA8i9L5SvHo1JcQp3jYGA
    7FfMgv2Z9Kp+tOkayBguQBkcARyitE+7yJGOvL8m6k8li0e/l0p
    OPkIodapvGLfobM2CI=

![afbeelding](https://github.com/techgrounds/techgrounds-Allardyg/assets/132412310/835ce368-c50e-4123-9460-5d2283ed5fdd)

De inhoud van deze berichten kan alleen worden gelezen door mij en Deniz, en de lezer van deze opdrachten. Om het te lezen heb je dus de private key nodig.


