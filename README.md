# Fugenduel 🌿🧱

> **„Die realen Werte der Pflanzen sind das unveränderliche Fundament — jedes Spiel wählt daraus die Werte, die es braucht. Und die Kinder erfinden die Regeln.“**

Willkommen im aufgeräumten und neu strukturierten Repository zu **Fugenduel**. Dieses Projekt erforscht urbane Fugenökosysteme als modulares Spielsystem: vom physischen, taktilen Brettspiel mit echten Ziegeln bis zum digitalen Wetterjahr-Simulator.

---

## 🌟 Schnell-Navigation

```
                                      🌿 FUGENDUEL
                                           │
         ┌─────────────────────────────────┴─────────────────────────────────┐
         ▼                                                                   ▼
  🌿 pflanzen/                                                        🎲 spiele/
  (Botanische Wahrheit,                                               (5 Spielsysteme)
   einheitliche JSON- & MD-Akten,                                            │
   Goodies & Kiez-Apotheke)                                  ┌───────────────┼───────────────┬───────────────┐
                                                             ▼               ▼               ▼               ▼
                                                       ⭐ 01-brettspiel  02-kartenspiel  03-simulation  04-patenschaft & 05-mobile
                                                      (UNSER FOKUS!)
```

---

## 🌿 1. [`pflanzen/`](pflanzen/) — Die Pflanzen-Schatzkiste

Alle Pflanzen besitzen eine **vollkommen einheitliche Datenstruktur** – sowohl maschinenlesbar als [`plant.json`](pflanzen/arten/breitwegerich/plant.json) für automatische Parser als auch ausführlich als [`README.md`](pflanzen/arten/breitwegerich/README.md).

### Schnellzugriff auf die Pflanzen-Dossiers:
* 🍃 [**Breitwegerich** (*Plantago major*)](pflanzen/arten/breitwegerich/) — *Trittkönig, Wiesenpflaster & Panzerblatt* *(inkl. 2 Bildkarten)*
* 🌸 [**Zimbelkraut** (*Cymbalaria muralis*)](pflanzen/arten/zimbelkraut/) — *Mauerkletterer, Mauerblümchen & Mauerrückzug* *(inkl. 2 Bildkarten)*
* 🌿 [**Mauerraute** (*Asplenium ruta-muraria*)](pflanzen/arten/mauerraute/) — *Steinfarn, Kalkspezialist & Poikilohydrie* *(inkl. 1 Bildkarte)*
* 🌼 [**Schöllkraut** (*Chelidonium majus*)](pflanzen/arten/schoellkraut/) — *Warzenkraut, oranger Ätzsaft & Ameisenbrot*
* 🚀 [**Behaartes Schaumkraut** (*Cardamine hirsuta*)](pflanzen/arten/behaartes-schaumkraut/) — *Springkresse, 2 m Katapult & scharfe Senföle*
* 🥗 [**Sommer-Portulak** (*Portulaca oleracea*)](pflanzen/arten/sommer-portulak/) — *Bürzelkraut, C4/CAM-Hitze-Turbo & Omega-3-Gourmetgemüse*
* 🌾 [**Einjähriges Rispengras** (*Poa annua*)](pflanzen/arten/einjaehriges-rispengras/) — *Vogelgras, 12-Monats-Dauerblüher & Trittpolster*
* 🟩 [**Silber-Birnmoos** (*Bryum argenteum*)](pflanzen/arten/silber-birnmoos/) — *Silberfilz, Sonnenspiegel-UV-Schild & Ammenpflanze*
* ☀️ [**Gewöhnlicher Löwenzahn** (*Taraxacum officinale*)](pflanzen/arten/loewenzahn/) — *Pusteblume, 1 m Pfahlwurzel & Pappus-Fallschirme*

### Goodies & Botanische Quellen:
* 💊 [**Kiez-Apotheke & Wildküche**](pflanzen/goodies/kiez-apotheke-und-kueche.md) — Heilwirkungen, Hausrezepte, aktive Inhaltsstoffe und Outdoor-Tipps.
* 💥 [**Tag-Team-Combos & Finisher**](pflanzen/goodies/combos-und-spezialangriffe.md) — Kiez-Combos, chemische Abwehr und botanische Ultimates.
* 🔬 [**Botanische Trait-Datenbanken**](pflanzen/quellen/data-flora-quellen.md) — Quellenverzeichnis (Pladias, UNDERPLOT, TRY, LEDA).
* 📋 [**Daten-Audit & Methodik**](pflanzen/quellen/daten-audit.md) — Grundregeln zur Trennung von Messwerten und Spielregeln.

---

## 🎲 2. [`spiele/`](spiele/) — Die fünf Spielwelten

Jedes Spielsystem greift auf die zentrale Pflanzendatenbank zu und wählt die Parameter, die es benötigt:

### ⭐ [01-Brettspiel (Taktile Kirchenmauer & Fugen-Netzwerk)](spiele/01-brettspiel/)
> **AKTUELLER ARBEITSFOKUS:** Hier setzen wir gemeinsam an!
* **Konzept:** Vertikales Spielfeld (*Kirchenmauer Lieberose*) mit 10 Mikro-Nischen entlang eines Höhen- und Sonnengradienten (Z-Achse).
* **Physisches Material:** Doppelseitige Fugenstreifen (Wurzel, Pilzmyzel, Ameisenstraße), Moos-Patches und 2-Level-Pflanzenkarten.
* **Werte:** Intuitiv auf einer Skala von **1 bis 3** für Licht, Wasser und Tiefe.
* **Dateien:** [Wertetabellen](spiele/01-brettspiel/regeln-und-werte.md) · [Arena Lieberose](spiele/01-brettspiel/arena-lieberose.md) · [Untergrund-Netzwerk](spiele/01-brettspiel/untergrund-netzwerk.md) · [Status & Offene Punkte](spiele/01-brettspiel/status-und-offene-punkte.md) · [Druckmaterial (PDF/Bilder)](spiele/01-brettspiel/material/).

### [02-Kartenspiel (Taktischer Deckbuilder & Duell)](spiele/02-kartenspiel/)
* 3 Fugen-Abschnitte (Marvel Snap), 6 Runden = 1 Wetterjahr, Enemy Intents (Slay the Spire), Samenbank als Friedhof.
* [Regelwerk v0.1](spiele/02-kartenspiel/regelwerk-v0.1.md) · [Master-Deck](spiele/02-kartenspiel/master-deck.md) · [Starter-Kader](spiele/02-kartenspiel/starter-roster.md).

### [03-Digital-Simulation (Asphalt-Arena & Auto-Battler)](spiele/03-digital-simulation/)
* Reale NASA-POWER-Wetterjahre für 6 Weltstädte, 50/50-Deckungsbalken, sichtbare Replay-Mathematik.
* [Design-Vision](spiele/03-digital-simulation/design-vision.md) · [Wetterjahr-Modus](spiele/03-digital-simulation/wetterjahr-modus.md) · [Battle-Mechanik](spiele/03-digital-simulation/battle-mechanik.md).

### [04-Kiez-Patenschaft (Beobachtungsposten & Tamagotchi)](spiele/04-kiez-patenschaft/)
* Friedliche Citizen-Science-App (*„Mama, der pH-Wert von meinem Löwenzahn ist gesunken!“*).
* [Pflege-Mechanik](spiele/04-kiez-patenschaft/pflege-mechanik.md) · [Stadt-Stellen](spiele/04-kiez-patenschaft/stadt-stellen.md).

### [05-Mobile-Economy (Fugenpacht & Samenmarkt)](spiele/05-mobile-economy/)
* Live-Ops-Mechaniken, Fugenpacht-Reviere und städteübergreifender Samenhandel.
* [Samenmarkt](spiele/05-mobile-economy/samen-markt.md) · [Retention-Loops](spiele/05-mobile-economy/retention-mechanik.md).

---

## 🛠️ 3. [`scripts/`](scripts/) — Entwickler-Tools

* [`scripts/build_all_plant_dossiers.py`](scripts/build_all_plant_dossiers.py): Baut und validiert die standardisierten `plant.json` und `README.md` Dossiers für jede Art.
* [`scripts/render-pflanzen.py`](scripts/render-pflanzen.py): Generiert gemeinsame Wertetabellen und Bild-Prompts für alle Arten.
