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

## Botanische Referenzen und Spielverbindungen

### Zimbelkraut — *Cymbalaria muralis*

Botanik (Artwerte): L 6 | F 4 | N 5; Höhe 0.1–0.4 m; CSR % 37.3 / 0 / 62.7; maximale Wurzeltiefe k. A. m; Wurzelradius k. A. m; Knospenbank 15.

Quelle: [Artprofil](https://pladias.cz/en/taxon/data/Cymbalaria%20muralis). Untergrund: [UNDERPLOT v39](https://doi.org/10.25829/idiv.3610-56acy9); Originalzeile im [Datenauszug](data/underplot-v39-auszug.csv).

Phänologie im tschechischen Pladias-Datensatz: May–September (Artspanne, keine Garantie für jede Pflanze).

Spielentwurf: Pilzverbindung als Test freigegeben; keine verifizierte Mykorrhiza-Aussage. Kriechtrassen I/II: 1/3 als Sonderfähigkeit; keine Wurzeltiefen. UNDERPLOT führt die Art als nicht klonal, daher ist das Ausbreitungsnetz eine Spielabstraktion. Eine Verbindung wird unabhängig von der Pflanze umgedreht; Pflanzen-Level II bedeutet weder verholzt noch frostfest.

### Mauerraute — *Asplenium ruta-muraria*

Botanik (Artwerte): L 8 | F 3 | N 3; Höhe 0.05–0.2 m; CSR % 12.6 / 54.6 / 32.8; maximale Wurzeltiefe k. A. m; Wurzelradius k. A. m; Knospenbank 10.

Quelle: [Artprofil](https://pladias.cz/en/taxon/data/Asplenium%20ruta-muraria). Untergrund: [UNDERPLOT v39](https://doi.org/10.25829/idiv.3610-56acy9); Originalzeile im [Datenauszug](data/underplot-v39-auszug.csv).

Ein Farn bildet Sporen. Das im Quellfeld „Flowering period“ genannte Zeitfenster darf nicht als Blüte eines Farns beschriftet werden. Feuchte Keimbedingungen sind kein Beleg für zwingende Moosbindung oder Dürre-Immunität.

Spielentwurf: Pilzverbindung als Test freigegeben; keine verifizierte Mykorrhiza-Aussage. Eine Verbindung wird unabhängig von der Pflanze umgedreht; Pflanzen-Level II bedeutet weder verholzt noch frostfest.

### Schöllkraut — *Chelidonium majus*

Botanik (Artwerte): L 6 | F 5 | N 8; Höhe 0.3–0.9 m; CSR % 54.7 / 6.6 / 38.8; maximale Wurzeltiefe k. A. m; Wurzelradius k. A. m; Knospenbank 20.

Quelle: [Artprofil](https://pladias.cz/en/taxon/data/Chelidonium%20majus). Untergrund: [UNDERPLOT v39](https://doi.org/10.25829/idiv.3610-56acy9); Originalzeile im [Datenauszug](data/underplot-v39-auszug.csv).

Phänologie im tschechischen Pladias-Datensatz: May–September (Artspanne, keine Garantie für jede Pflanze).

Spielentwurf: Pilzverbindung als Test freigegeben; keine verifizierte Mykorrhiza-Aussage. Ameisen-Samentransport im Spiel freigegeben; Elaiosomen sind botanisch belegt, garantierte Transporte sind Spielregeln. Eine Verbindung wird unabhängig von der Pflanze umgedreht; Pflanzen-Level II bedeutet weder verholzt noch frostfest.

### Behaartes Schaumkraut — *Cardamine hirsuta*

Botanik (Artwerte): L 6 | F 5 | N 6; Höhe 0.1–0.25 m; CSR % 22.5 / 0 / 77.5; maximale Wurzeltiefe 0.37 m; Wurzelradius 0.155 m; Knospenbank 2.5.

Quelle: [Artprofil](https://pladias.cz/en/taxon/data/Cardamine%20hirsuta). Untergrund: [UNDERPLOT v39](https://doi.org/10.25829/idiv.3610-56acy9); Originalzeile im [Datenauszug](data/underplot-v39-auszug.csv).

Phänologie im tschechischen Pladias-Datensatz: April–June (Artspanne, keine Garantie für jede Pflanze).

Spielentwurf: Pilzverbindung im Basistest nicht freigegeben; keine verifizierte Mykorrhiza-Aussage. Eine Verbindung wird unabhängig von der Pflanze umgedreht; Pflanzen-Level II bedeutet weder verholzt noch frostfest.

### Breitwegerich — *Plantago major*

Botanik (Artwerte): L 7 | F 5 | N 6; Höhe 0.1–0.4 m; CSR % 82.3 / 0 / 17.7; maximale Wurzeltiefe 0.497 m; Wurzelradius 0.33 m; Knospenbank 20.

Quelle: [Artprofil](https://pladias.cz/en/taxon/data/Plantago%20major). Untergrund: [UNDERPLOT v39](https://doi.org/10.25829/idiv.3610-56acy9); Originalzeile im [Datenauszug](data/underplot-v39-auszug.csv).

Phänologie im tschechischen Pladias-Datensatz: June–October (Artspanne, keine Garantie für jede Pflanze).

Spielentwurf: Pilzverbindung als Test freigegeben; keine verifizierte Mykorrhiza-Aussage. Eine Verbindung wird unabhängig von der Pflanze umgedreht; Pflanzen-Level II bedeutet weder verholzt noch frostfest.

### Sommer-Portulak — *Portulaca oleracea*

Botanik (Artwerte): L 8 | F 4 | N 7; Höhe 0.05–0.3 m; CSR % 0.3 / 0 / 99.7; maximale Wurzeltiefe 0.25 m; Wurzelradius 0.12 m; Knospenbank 1.2.

Quelle: [Artprofil](https://pladias.cz/en/taxon/data/Portulaca%20oleracea). Untergrund: [UNDERPLOT v39](https://doi.org/10.25829/idiv.3610-56acy9); Originalzeile im [Datenauszug](data/underplot-v39-auszug.csv).

Phänologie im tschechischen Pladias-Datensatz: June–October (Artspanne, keine Garantie für jede Pflanze).

Spielentwurf: Pilzverbindung im Basistest nicht freigegeben; keine verifizierte Mykorrhiza-Aussage. Eine Verbindung wird unabhängig von der Pflanze umgedreht; Pflanzen-Level II bedeutet weder verholzt noch frostfest.

### Einjähriges Rispengras — *Poa annua*

Botanik (Artwerte): L 7 | F 6 | N 8; Höhe 0.05–0.25 m; CSR % 6.8 / 35 / 58.2; maximale Wurzeltiefe 0.17 m; Wurzelradius 0.11 m; Knospenbank 4.2.

Quelle: [Artprofil](https://pladias.cz/en/taxon/data/Poa%20annua). Untergrund: [UNDERPLOT v39](https://doi.org/10.25829/idiv.3610-56acy9); Originalzeile im [Datenauszug](data/underplot-v39-auszug.csv).

Phänologie im tschechischen Pladias-Datensatz: January–December (Artspanne, keine Garantie für jede Pflanze).

Spielentwurf: Pilzverbindung als Test freigegeben; keine verifizierte Mykorrhiza-Aussage. Eine Verbindung wird unabhängig von der Pflanze umgedreht; Pflanzen-Level II bedeutet weder verholzt noch frostfest.

### Silber-Birnmoos — *Bryum argenteum*

Botanik: Rhizoide, keine echten Wurzeln; Sporen statt Samen. L/F/N, CSR und Messmaße: k. A. Spielwerte vorläufig.

Quelle: [Artprofil](https://www.britishbryologicalsociety.org.uk/learning/species-finder/bryum-argenteum/).

Moos bildet Sporen und besitzt Rhizoide. Die vorliegenden Gefäßpflanzendaten belegen keine L/F/N- oder CSR-Zahlen für diese Art. Keine garantierte Wiederbelebung in exakt 20 Minuten aufdrucken.

Spielentwurf: Pilzverbindung im Basistest nicht freigegeben; keine verifizierte Mykorrhiza-Aussage. Eine Verbindung wird unabhängig von der Pflanze umgedreht; Pflanzen-Level II bedeutet weder verholzt noch frostfest.

## Quellenumfang

Pladias: abgerufen am 30.10.2026, tschechische Artprofile; nicht mit regional abweichenden FloraWeb-Werten vermischen. UNDERPLOT: Portalversion v39 / Version 7196, DOI und Download-Prüfsumme in data/pflanzen.json. RDepth ist die aggregierte maximale Wurzeltiefe, LRExtent der maximale Radius; keine Messung an der dargestellten Pflanze. Fehlende Werte wurden nicht ergänzt. Knospenbankwerte aus UNDERPLOT und einzelnen CLO-PLA/Pladias-Profilen können durch Aggregation voneinander abweichen. Der Originaldatenauszug bleibt erhalten.
