# Fugenduel — Statusreview vom 30.10.2026

Fugenduel hat eine erkennbare Identität und genügend Material für einen begleiteten Versuch: urbane Pflanzen, zwei gemeinsam bespielbare Arenen, sichtbare Standortunterschiede und umdrehbare Spielteile. Ein durchgehend abgestimmtes Druckset liegt noch nicht vor. Die wichtigsten offenen Punkte sind widersprüchliche Brettwerte und zwei unterschiedliche Entwürfe der Verbindungen. Dokumentierte Spieltests fehlen im geprüften Repository.

## Was bereits trägt

Die Mauer mit zehn Nischen macht Standortwahl sichtbar. Wurzeln, Pilze, Ameisen und Moos bieten unterschiedliche Möglichkeiten zur Zusammenarbeit und Konkurrenz. Die zwei Pflanzenlevel passen zum Umdrehen der Verbindungen. Das Leitprinzip, dass Kinder Regeln erfinden, bleibt sinnvoll: Das Material muss dafür einheitlich lesbar sein; feste Siegbedingungen sind keine Voraussetzung für einen ersten Materialtest.

Vorhanden sind fünf ursprüngliche Designdokumente, Brett- und Arenabilder, eine Breitwegerich-Datenkarte, ein Zwei-Arenen-Konzept, eine Zimbelkraut-Level-1-Karte und ein zweiseitiger A4-Bogen für Verbindungen. Die Illustrationen zeigen Gestaltungsabsichten; sie belegen keinen gebauten oder getesteten physischen Prototyp.

## Bildimport und Nachvollziehbarkeit

Aus den beiden vom Nutzer angegebenen Windows-Ordnern wurden fünf PNGs geprüft. Drei fehlende Dateien wurden unverändert importiert: Breitwegerich-Datenkarte, Zwei-Arenen-Konzept und das größere Original des Lieberose-Bretts. Zwei weitere Dateien waren bereits bytegleich vorhanden. Das Arenaporträt liegt zusätzlich zweimal unter verschiedenen lokalen Dateinamen vor. Originale wurden erhalten.

Die [Bildübersicht](assets/README.md) und das [Importprotokoll mit SHA-256](assets/import-2026-10-30.json) dokumentieren die Zuordnung. Private ChatGPT-Gespräche wurden nicht abgerufen; geprüft wurden die Repository-Zusammenfassung und die bereitgestellten Bildordner. Vollständigkeit über alle Gespräche hinweg ist daher nicht bestätigt.

## Konsistenzbefunde

### 1. Brett und Tabelle weichen in sieben Slots ab

Vergleich von `lieberose-kirchenmauer.jpg` beziehungsweise dem importierten Original mit Abschnitt 1 der Wertetabelle. Reihenfolge: **Licht / Wasser / Wurzelraum**.

| Slot | Auf dem Brett | In der Tabelle |
|---|---|---|
| 02 | 2 / 2 / 1 | 2 / 3 / 2 |
| 03 | 1 / 3 / 2 | 1 / 2 / 2 |
| 05 | 2 / 3 / 3 | 2 / 1 / 3 |
| 06 | 1 / 2 / 1 | 1 / 2 / 2 |
| 07 | 2 / 1 / 3 | 2 / 1 / 1 |
| 08 | 3 / 2 / 2 | 1 / 2 / 3 |
| 09 | 1 / 3 / 3 | 1 / 3 / 1 |

01, 04 und 10 stimmen überein. Der Entwurf mit der 2018-Jahreskarte ordnet Standorte nochmals anders zu. Die Varianten sollten vor einem gemeinsamen Druck vereinheitlicht werden. Die vorhandenen Rastergrafiken wurden bei diesem Import nicht verändert.

### 2. PDF und Netzwerktexte sind unterschiedliche Spielentwürfe

| Thema | Wertetabelle / Netzwerktext | A4-PDF v1 |
|---|---|---|
| Wurzel | Trassen für Triebe, Level II mit zusätzlichem Fugenplatz | Wurzelzugang speichert Wasser; ausdrücklich kein neuer Pflanzenslot |
| Ausbreitung | Teil der Wurzelverbindung | Eigene Kriechtrasse, Neupflanzen I/II: 0/1 |
| Pilz | 1 Wasser oder Nährstoff; Level II unbegrenzter Ausgleich | Transfer I/II: 1/2 Nährstoff-Token, kostet Energie |
| Ameise | Münzwurf beziehungsweise ein garantierter Samen im Herbst | Transport I/II: 1/2 geeignete Samen, kostet Energie |
| Moos | Feuchte, Hitzeschild, zusätzliches Keimen | Lokal Feuchte +1, nicht stapelbar |

`E` bedeutet im PDF Energie; `N` bedeutet dort Nährstoff-Token. Der botanische N-Zeigerwert ist eine andere Größe. Die PDF-Werte wurden als separate Testvariante erhalten, nicht als bestätigte Fortsetzung der Tabellen behandelt. Duplexpassung und tatsächliche Lesbarkeit sind noch praktisch zu testen.

### 3. Pflanzen und Prompts wurden auf eine gemeinsame Datenquelle gebracht

Alle acht Arten besitzen jetzt genau zwei Seiten in [data/pflanzen.json](data/pflanzen.json). Daraus werden die Pflanzentabelle, der Katalog und die 16 vollständigen Prompts erzeugt. Licht und Feuchte werden aus den tschechischen Pladias-Werten in drei Kategorien eingeteilt: 1–3 → 1, 4–6 → 2, 7–9 → 3. Das ist eine dokumentierte Spielvereinfachung, keine neue Messung.

Damit ändern sich gegenüber den alten Spielzahlen Portulak-Wasser von 1 auf 2 sowie Rispengras-Licht/Wasser von 2/3 auf 3/2. Portulak-Wurzelraum II ist wieder 1; zuvor stand in den Prompts 2 und in der Ausgangstabelle 1. Botanische Artwerte bleiben auf beiden Seiten identisch. Wurzelraum, Triebe und Fähigkeiten sind Spielentwurf. Beim Moos bleiben nicht verifizierte Zeigerwerte offen; seine Kategorien sind ausdrücklich vorläufig.

Die [UNDERPLOT-Originalzeilen](data/underplot-v39-auszug.csv) bestätigen für Breitwegerich rund 0,497 m Wurzeltiefe, 0,33 m Radius und Knospenbank 20. Pladias bestätigt CSR 82,3 / 0 / 17,7 %. Für Mauerraute, Zimbelkraut und Schöllkraut fehlt RDepth in dieser UNDERPLOT-Version. Die Werte wurden nicht erfunden oder aus Spielklassen zurückgerechnet. Originalquellen und Versionsangaben stehen im [Katalog](04-pflanzen-katalog.md).

### 4. Biologische Spielkräfte sind noch keine wissenschaftliche Freigabe

Die frühere Behauptung, sämtliche Zahlen und Kräfte seien biologisch fertig geprüft, war nicht belegt. Pauschale Frostfestigkeit durch Level II, unbegrenzter Pilzaustausch, vollständige Tritt- oder Dürre-Immunität und Wiederbelebung nach exakt 20 Minuten gehören nicht als gesicherte Messwerte auf neue Pflanzenkarten. Farn und Moos bilden Sporen; die Prompts berücksichtigen das.

Pilzfreigaben werden als Testentscheidungen geführt. Eine Freigabe im Spiel belegt keine tatsächliche Partnerschaft jeder Art. Auch Kriechtrassen und Wurzeltiefe sind getrennte Merkmale: UNDERPLOT führt Zimbelkraut als nicht klonal. Seine besondere Netzwerkausbreitung bleibt eine ausdrücklich vereinfachte Spielidee.

## Nächste Schritte nach Priorität

1. Eine Brettfassung und eine Verbindungsvariante auswählen; Standortnummern, Symbole und Wirkungen dann gemeinsam setzen. Historische Jahreskarten und lokale Wetterwerte brauchen nachvollziehbare Orts- und Datumsquellen.
2. Mit den neuen Prompts beide Seiten jeder Pflanze gestalten. Vor dem Druck die generierte Schrift und alle Zahlen gegen den Katalog prüfen. Die vorhandene Zimbelkraut-Karte zeigt den richtigen Level-I-Spielwertsatz, enthält aber noch keinen Herkunftshinweis.
3. Ein kleines Materialset gemeinsam mit Kindern erproben: Erkennen sie Licht, Feuchte und Wurzelraum? Können sie Verbindungen nachvollziehen und eigene Regeln erklären? Beobachtungen und Regelentscheidungen festhalten, bevor zusätzliche Sonderkräfte hinzukommen.
4. Anschließend Druckmaße, verfügbare Verbindungsstücke, Slotkapazitäten und Kartenrückseiten abstimmen. Noch fehlen ein einheitliches vollständiges Druckset und belegte Ergebnisse aus Spieltests.

## Prüfumfang

Geprüft wurden Repository-Texte, alle vorhandenen Bilder, Text und Seitenformat des PDFs, die fünf angegebenen PNG-Quelldateien, Pladias-Artprofile und der heruntergeladene UNDERPLOT-Datensatz v39. Die Bildprüfung erfolgte visuell; der Import wurde über Dateivergleich und SHA-256 geprüft. Historische Arena-Aussagen wurden hier nicht extern verifiziert. Es wurden weder neue Bilder generiert noch Druck- oder Spieltests durchgeführt.
