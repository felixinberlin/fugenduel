# 🌿 Pflanzen-Katalog & Botanische Schatzkiste

> **„Die realen Werte der Pflanzen sind das unveränderliche Fundament. Jedes Spiel wählt daraus die Werte, die es braucht.“**

Willkommen in der zentralen Pflanzen-Datenbank von **Fugenduel**. Jede Art in diesem Verzeichnis besitzt eine einheitliche, standardisierte Datenstruktur – sowohl maschinenlesbar als [`plant.json`](arten/breitwegerich/plant.json) für Parser und Generatoren als auch ausführlich formatiert als [`README.md`](arten/breitwegerich/README.md) für menschliche Spieler, Spieldesigner und Pädagogen.

---

## 📂 Einheitliche Struktur je Pflanze

Jede Art lebt in ihrem eigenen Unterordner unter `pflanzen/arten/<art-id>/`:

```
pflanzen/arten/<art-id>/
├── README.md       # Vollständige Akte: Botanik, Goodies, Spielwerte aller Systeme, Prompts
├── plant.json      # Standardisiertes JSON: Einheitliche Keys für Parser & Spiel-Engines
├── prompts.txt     # Copy/Paste Prompts für Level 1 & 2 (2:3 Bildgenerierung)
└── bilder/         # Finale Spielkarten, botanische Datenkarten und Bildassets
```

### JSON-Schema für Entwickler & Parser

Alle `plant.json`-Dateien teilen die identische Top-Level-Struktur:
* `id` & `name` & `scientific_name`: Eindeutige Bezeichner und botanische Nomenklatur.
* `botany`: Reale wissenschaftliche Daten (**Ellenberg-Zeigerwerte**, **CSR-Strategie**, **Wuchshöhe**, **UNDERPLOT-Wurzelmaße**, **Knospenbank**, **Phänologie**, **Quellen**).
* `goodies`: Kulturelles Wissen (**Volksmund**, **Kiez-Apotheke**, **Wildkräuterküche & Geschmack**, **Aktive Inhaltsstoffe**, **Spiel-Heileffekt**, **Draußen-Tipp für Kinder**).
* `game_adaptations`: Vorkonfigurierte Parameter für die verschiedenen Spielsysteme:
  * `board_game`: Werte auf Skala 1–3 für Level 1 & Level 2 (Licht, Wasser, Wurzelraum, Triebe, Superkraft, Netzwerk-Affinitäten).
  * `card_game`: 0–10 RPG-Statblock (WURZEL, TRITT, DÜRRE, SAAT, TEMPO, CHEMIE) und Signatur-Skills.
* `media`: Verknüpfte Bilddateien und Prompts.

---

## 📊 Schnellübersicht aller Arten

| Artname | Wissenschaftlicher Name | CSR-Klasse | ☀️ L | 💧 F | 🧪 R | 🥩 N | Max. Wurzel | Blütezeit | Besondere Stärke |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|---|---|
| [**Breitwegerich**](arten/breitwegerich/) | *Plantago major* | CR | 7 | 5 | 7 | 6 | 0,50 m | Jun–Okt | Trittfeste Rosette mit elastischen Zugfasern |
| [**Zimbelkraut**](arten/zimbelkraut/) | *Cymbalaria muralis* | R / SR | 6 | 4 | 7 | 5 | k. A. | Mai–Sep | Kriechtriebe; Mauerrückzug in finstere Ritzen |
| [**Mauerraute**](arten/mauerraute/) | *Asplenium ruta-muraria* | S | 8 | 3 | 8 | 3 | k. A. | Jul–Sep (Sporen) | Austrocknungsstarre (Poikilohydrie); Kalkfugen |
| [**Schöllkraut**](arten/schoellkraut/) | *Chelidonium majus* | CR | 6 | 5 | 7 | 8 | Pfahlwurzel | Mai–Sep | Oranger Ätzsaft; Ameisensamen mit Elaiosomen |
| [**Behaartes Schaumkraut**](arten/behaartes-schaumkraut/) | *Cardamine hirsuta* | R | 6 | 5 | 6 | 6 | 0,37 m | Apr–Jun (Winter) | Schleuderfrüchte (2 m Katapult); scharfe Senföle |
| [**Sommer-Portulak**](arten/sommer-portulak/) | *Portulaca oleracea* | R | 8 | 4 | 7 | 7 | 0,25 m | Jun–Okt | Sukkulenter C4/CAM-Turbo bei > 35 °C; Omega-3 |
| [**Einjähriges Rispengras**](arten/einjaehriges-rispengras/) | *Poa annua* | R / SR | 7 | 6 | 6 | 8 | 0,17 m | Jan–Dez | Blüht 12 Monate; unzerstörbares Fugenpolster |
| [**Silber-Birnmoos**](arten/silber-birnmoos/) | *Bryum argenteum* | S | 7 | 4 | 7 | 6 | 0,00 m (Rhizoide) | Herbst–Frühjahr | Sonnenspiegel-Blattspitzen; Ammenpflanze |
| [**Gewöhnlicher Löwenzahn**](arten/loewenzahn/) | *Taraxacum officinale* | RC | 7 | 5 | 7 | 6 | 1,00 m | Mär–Nov | 1 m Pfahlwurzel; Pappus-Fallschirme bis 500 m |

---

## 🎁 Weiterführende Inhalte & Goodies

* [**Kiez-Apotheke & Wildküche**](goodies/kiez-apotheke-und-kueche.md) — Ausführlicher Heilkräuter- und Foraging-Guide für alle Pflanzen mit Inhaltsstoffen und Rezepten.
* [**Tag-Team-Combos & Finisher**](goodies/combos-und-spezialangriffe.md) — Kiez-Combos, botanische Spezialangriffe und Kettenreaktionen.
* [**Botanische Quellen & Trait-Datenbanken**](quellen/data-flora-quellen.md) — TRY, LEDA, Pladias, UNDERPLOT und wissenschaftliche Literatur.
* [**Daten-Audit & Methodik**](quellen/daten-audit.md) — Grundregeln zur Trennung von Messwerten und Spielregeln.
* [**Bild-Prompts (Gesamtübersicht)**](bild-prompts/alle-prompts.txt) — Alle 16 Kopiervorlagen für KI-Bildgeneratoren.
