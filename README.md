# Chips & Circuits - str(group_name)
## De case
Een chip, of een geïntegreerde schakeling, is een siliconen plaatje met daarop zogenaamde 'gates' en 'nets'. Gates zijn poortjes die met elkaar worden verbonden door middel van draden of nets. Welke gates met elkaar moeten verbinden, staat in een netlist. Dit is een lijst met op iedere regel een start-gate en een eind-gate. Bij het verbinden van de gates, is het belangrijk dat de nets elkaar niet raken of kruisen. Wanneer dit gebeurt, is er sprake van een 'collision' en zal de hele chip niet meer werken. Daarnaast is het belangrijk om de nets zo kort mogelijk te houden, zodat de chip sneller werkt en de productiekosten laag worden gehouden.
Bij deze case horen twee chips van verschillend formaat, met voor elke chip drie netlists. Aan ons was de taak om een programma te schrijven dat door middel van algoritmes en heuristieken de nets van de verschillende netlists legt.

## Aan de slag (Getting Started)
### Vereisten (Prerequisites)
Deze codebase is volledig geschreven in Python3.7.5. In requirements.txt staan alle benodigde packages om de code succesvol te runnen. Deze packages zijn gemakkelijk te installeren via pip door middel van de volgende instructie:
```
pip install -r requirements.txt
```

### Structuur (Structure)
Alle Python scripts staan in de folder 'code'. In de map 'data' zitten alle inputwaarden en in de map 'resultaten' worden alle resultaten opgeslagen door de code.

### Test(Testing)
Om de code te draaien, gebruik de instructie:
```
python main.py
```
In de terminal zul je meerdere malen worden gevraagd om een keuze te maken:
- Allereerst zul je moeten kiezen welke netlist je wilt gebruiken. Je kunt hier kiezen tussen netlist 1 tot en met 6, waarbij 1 tot en met 3 bij chip 1 horen, en 4 tot en met 6 bij chip 2.
- Vervolgens moet je kiezen welke heuristiek je wilt toepassen. Je keuzes zijn hier:
    - Regular - Er wordt een A* algoritme gebruikt om het kortste pad tussen twee gates te vinden. Wanneer een net niet gelegd kan worden, doordat een gate volledig is omsloten door andere nets, wordt het grid leeggemaakt, zal deze combinatie van start- en eindgate bovenaan de netlist worden geplaatst en begint het algoritme opnieuw tot alle nets gelegd kunnen worden.
    - Neighbours - Om meer ruimte rond de gates te bewaren, krijgen de directe verticale en horizontale buren van een gate een hogere prijs om een net doorheen te leggen. Deze heuristiek wordt gecombineerd met de 'regular' heuristiek.
    - Extended neighbours - Om meer ruimte rond de gates te bewaren, krijgen naast de directe horizontale en verticale buren, ook de directe diagonale buren van een gate een hogere prijs om een net doorheen te leggen. Het is hierbij belangrijk om de directe horizontale en verticale buren een hogere prijs te geven dan de directe diagonale buren. Deze heuristiek wordt gecombineerd met de 'regular' heuristiek. 
    - Upstairs neighbours - Om meer ruimte boven de gates te bewaren, krijgen de nodes in een rechte lijn boven een gate een hogere prijs om een net doorheen te leggen. Deze heuristiek wordt gecombineerd met de 'regular' heuristiek.
    - Extended upstairs neighbours - Om meer ruimte rondom en boven de gates te bewaren, krijgen de directe horizontale, verticale en diagonale buren van een gate een hogere prijs om een net doorheen te leggen. Daarnaast krijgen de nodes in een rechte lijn boven een gate een hogere prijs. Het is hierbij belangrijk dat de directe horizontale en verticale buren en de nodes boven een gate een hogere prijs krijgen dan de directe diagonale buren en de nodes die boven de directe diagonale buren liggen. Deze heuristiek wordt gecombineerd met de 'regular' heuristiek.
    - Lava - Voor deze heuristiek worden alle nets met 'constraint relaxation' gelegd. Vervolgens wordt bekeken hoeveel nets door elke node liggen en dit aantal bepaalt hoeveel hoger de prijs van die node wordt om een net overheen te leggen. Wanneer er bijvoorbeeld 5 nets door eenzelfde node liggen, wordt de prijs van deze node met 5 verhoogd. De gebruiker kan er voor kiezen om deze prijs met een factor x te verhogen. Deze heuristiek wordt gecombineerd met de 'regular' heuristiek.
    - Elevator - 
    - N.B. Bij (Extended) (Upstairs) Neighbours raden wij aan om de kosten te verhogen met een waarde tussen de 2 en 25. Een te lage waarde zal namelijk als nog geen ruimte overhouden rondom een gate en een te hoge waarde zal het algoritme langzamer maken.
    - N.B. bij Lava raden wij aan om de kosten te verhogen met maximaal factor 5. Een hogere factor zal het algoritme langzamer maken.
- Na het kiezen van een heuristiek, moet een keuze gemaakt worden voor de sortering van de netlist. De keuzes hiervoor zijn:
    - No sorting - De netlist wordt niet gesorteerd en wordt gebruikt zoals die in het csv-bestand staat.
    - Manhattan distance - Alle nets worden gelegd met 'constraint relaxation'. Vervolgens wordt de lengte van iedere net bepaald. De netlist wordt gesorteerd op de afstand die tussen een start- en eindgate ligt, met bovenaan de start- en eindgate met de korte afstand en onderaan de langste afstand.
    - Collisions - Alle nets worden gelegd met 'constraint relaxation'. Vervolgens wordt bekeken hoeveel collisions iedere net heeft met andere nets. De netlist wordt gesorteerd op volgorde van het aantal collisions dat een net heeft, met de net met de meeste collisions bovenaan en de net met de minste collisions onderaan.
- Vervolgens kan gekozen worden voor een extra heuristiek.
    - Nothing - Er wordt geen extra heuristiek toegepast.
    - Countdown (alleen bij lava en neighbours) - De door de gebruiker gekozen verhoogde prijs van een node, wordt bij het leggen van de nets steeds goedkoper.
    - Turned up - Een net tussen start- en eindgate wordt steeds van start naar eind en van eind naar start gelegd. Het kortste pad wordt behouden.
- Nadat een oplossing is gevonden en dus alle nets zijn gelegd, moet je aangeven of je de gevonden oplossing wilt opslaan in twee csv-bestanden.
    - Een bestand slaat de volgorde van de netlist op waarmee uiteindelijk een oplossing is gevonden.
    - Een bestand slaat de coördinaten van alle gelegde nets op.
- Door middel van Matplotlib wordt een 3D-weergave van de gelegde nets gemaakt en weergegeven.

## Auteurs (Authors)
* Kay Brouwers
* Dido Verstegen
* Robin Laponder

## Dankwoord (Acknowledgments)
* minor programmeren van de UvA