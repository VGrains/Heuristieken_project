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