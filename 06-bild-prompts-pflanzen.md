# Fugenduel — Pflanzen in zwei Leveln

Stand: 30.10.2026. Gemeinsame Quelle: [data/pflanzen.json](data/pflanzen.json). Neu erzeugen: `python3 scripts/render-pflanzen.py`.

Die beiden Seiten zeigen junge und etablierte Pflanzen. Botanische Artwerte bleiben gleich; Wurzelraum und Triebe sind vorgeschlagene Spielwerte, keine gemessenen Entwicklungsstufen. Licht und Feuchte werden für die sieben Gefäßpflanzen aus **Pladias** in drei Kategorien zusammengefasst: **1–3 → 1, 4–6 → 2, 7–9 → 3**. Diese Einteilung ist eine Designentscheidung. Die Pflanzenwerte sind Standortpräferenzen; passende Felder und zulässige Toleranzen vereinbaren die Kinder. Wurzelraum ist der Platzbedarf im Spiel und wird nicht aus Metern errechnet. Beim Moos sind Licht 1–3 und Wasser 1 vorläufige Spielwerte ohne hier verifizierte Zeigerwerte. Fehlende Messwerte bleiben `k. A.`; Wurzelraum 0 bezeichnet Rhizoide.

| Pflanze | Licht I / II | Wasser I / II | Wurzelraum I / II | Triebe I / II |
|---|---|---|---|---|
| Zimbelkraut | 2 / 2 | 2 / 2 | 1 / 2 | 1 / 2 |
| Mauerraute | 3 / 3 | 1 / 1 | 1 / 1 | 1 / 2 |
| Schöllkraut | 2 / 2 | 2 / 2 | 2 / 3 | 1 / 3 |
| Behaartes Schaumkraut | 2 / 2 | 2 / 2 | 1 / 1 | 1 / 1 |
| Breitwegerich | 3 / 3 | 2 / 2 | 1 / 2 | 1 / 2 |
| Sommer-Portulak | 3 / 3 | 2 / 2 | 1 / 1 | 1 / 3 |
| Einjähriges Rispengras | 3 / 3 | 2 / 2 | 1 / 1 | 1 / 2 |
| Silber-Birnmoos | 1–3 / 1–3 | 1 / 1 | 0 / 0 | 1 / 2 |

## Verwendung

Die vollständigen Prompts stehen getrennt in [Level 1](PROMPTS-LEVEL-1.txt) und [Level 2](PROMPTS-LEVEL-2.txt), gesammelt in [Copy/Paste](PROMPTS-COPY-PASTE.txt). Sie enthalten exakte deutsche Kartenbeschriftungen und Quellenwerte. Jeder Prompt funktioniert ohne Anbieterparameter; das Seitenverhältnis im Generator auf 2:3 stellen. Eine Layoutreferenz kann zusätzlich mitgegeben werden.

Bei schlechter Schriftwiedergabe nur das Motiv generieren und die Beschriftungen anschließend unverändert im Layout setzen. Vor dem Druck Artname, Level, Zahlen und Symbole am Katalog prüfen. Jede Rückseite hat denselben Rahmen und dieselben Artwerte wie ihre Vorderseite.

## Korrigierte Angaben

Portulak: Wasser 2 statt 1 nach der angegebenen Pladias-Kategorisierung; Wurzelraum II bleibt 1 statt der zuvor widersprüchlichen 2. Rispengras: Licht 3 und Wasser 2 statt 2/3. Pflanzen-Level, Wurzelraum, Streifenanzahl und gemessene Tiefe werden getrennt geführt. Keine pauschale Datenbank-Bestätigung für Spielkräfte, keine erfundenen Jugendmesswerte. Für drei Arten fehlt RDepth in UNDERPLOT.
