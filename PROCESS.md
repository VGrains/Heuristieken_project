# PROCESS - Programmeertheorie
### Robin Laponder (11892439), Dido Verstegen (11871288), Kay Brouwers (12906948)


<b> Maandag 6 januari 2020 </b>
- Explorerend onderzoek gedaan naar de casus.
- Verschillende algorithmes opgezocht en besproken.
- GitHub repository opgezet (Gekozen voor 1 master branch waar iedereen naar pushed).
- Presentatie voorbereid.
- Onderzocht wat Manhattan Distance is.
- Koffie gedronken om elkaar wat beter te leren kennen.

<b> Dinsdag 7 januari 2020 </b>
- Eerste werkgroep gehad en tijdens die werkgroep de eerste presentatie gegeven.
- Voortgangsgesprek met Quinten gehad. 
- Nagedacht over de datastructuur. Hoe willen we de data gaan inladen en gebruiken in Python.
    - CSV reader schrijven voor het inladen van de data. 
    - Data opslaan in verschillende dictionaries.
    - Probleem: Coördinaten hebben in de wiskunde een andere betekenis dan in Python. 
- Google heeft ons bij een algoritme 'A*' gebracht. Wellicht kunnen we dit gebruiken.

<b> Woensdag 8 januari 2020 </b>
- Het is gelukt om met het A* algoritme een route te krijgen tussen twee punten op een 2D grid.
    - Probleem: Wanneer er te veel obstakels worden geplaatst, lijkt de code in een loop te blijven hangen.
- Er is een csv reader geschreven, waardoor we niet meer handmatig de coördinaten hoeven in te voeren.

<b> Donderdag 9 januari 2020 </b>


<b> Vrijdag 10 januari 2020 </b>
- We lopen tegen problemen aan met de code van het A* algoritme. Hij lijkt niet altijd tot een goede oplossing te komen en soms komt er helemaal geen oplossing. 
    - De code is nog eens kritisch bekeken en herschreven. Deze nieuwe code hebben we nog niet geïmplementeerd in chips.py
- Begin gemaakt aan het toevoegen van extra lagen op de chip. 

<b> Maandag 13 januari 2020 </b>
- Groot deel van de dag is gewerkt aan het maken van de tweede presentatie. De eerste presentatie was niet volgens de indeling van een wetenschappelijk onderzoek en dat hebben we voor de tweede presentatie nu wel gedaan.
- We hebben ontdekt dat er een bug zit in de code van het A* algoritme, waardoor de code soms vast blijft zitten in een loop en niet tot een oplossing komt. Dit vermoeden hadden we al, maar is vandaag bevestigd door een ander groepje dat dezelfde code gebruikte.
- We lopen tegen het probleem aan dat een gate soms volledig wordt ingebouwd door nets van andere gates, waardoor het algoritme niet tot een oplossing kan komen.
    - We gaan proberen om de netlist anders te sorteren, om dit probleem op te lossen.
- Door middel van 'pipreqs' hebben we requirements.txt bijgewerkt.

<b> Dinsdag 14 januari 2020 </b>
- 's Ochtends nog wat laatste dingen aangepast aan de presentatie.
- Eerder liepen we aan tegen het probleem dat gates na een tijdje helemaal worden ingebouwd door wires, waardoor de netlist niet kan worden afgewerkt. 
    - Heuristiek om het op te lossen: Netlist opnieuw sorteren na vastlopen. Route waar op vastgelopen wordt, verplaatsen naar de voorkant van de netlist.
    - Algoritme:
        - Open de netlist.
        - Zoek op volgorde van boven naar beneden voor elke combinatie de snelste route tussen de gates d.m.v. A*.
        - Wanneer een route is gevonden tussen twee punten, voeg deze toe aan de lijst met routes.
        - Wanneer er geen route kan worden gevonden tussen twee gates:
            - Maak de lijst met routes leeg.
            - Plaats de combinatie van gates bovenaan de netlist en begin opnieuw.
    - Resultaat: Succes
        - Deze heuristiek zorgt voor een oplossing. Het is natuurlijk nog niet bekend of dit een goede oplossing is.

<b> Woensdag 15 januari 2020 </b>
- Een begin gemaakt aan het herschrijven van de code in classes en functies.
- Functies geschreven voor het schrijven van outputfiles.

<b> Donderdag 16 januari 2020 </b>
- Verder gegaan met het testen van de bedachte heuristiek (vooraan plaatsen van de route waar op wordt vastgelopen).
    - Het blijkt dat dit niet altijd voor een oplossing zorgt. Netlist 2 en 3 kunnen hier niet mee opgelost worden (netlist 4 t/m 6 zijn niet geprobeerd). Dit komt doordat er een loop ontstaat van steeds dezelfde combinatie vooraan de netlist zetten. 
