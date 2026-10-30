# 🎲 Fugenduel Brettspiel — Wertetabellen & Spielkomponenten

> **Leitprinzip:**  
> *„Die Kinder erfinden die Regeln — wir machen Werte und Material nachvollziehbar.“*  
> Alle Spielwerte bewegen sich intuitiv auf einer Skala von **1 bis 3** (oder eindeutigen Symbolen). Keine großen Zahlen, kein Rechnen mit Kommastellen.

---

## 1. Die Werte des Spielbretts (Arena: Kirchenmauer Lieberose)

Das Spielfeld besteht aus 10 Mikrostandorten (Slots). Die oberen 5 Slots (01–05) bilden die sonnige, trockene Mauerkrone; die unteren 5 Slots (06–10) bilden den kühlen, feuchteren Sockel.

| Slot-Nr. | Name der Nische | ☀️ Licht | 💧 Wasser | 🪴 Wurzel / Tiefe | Nischen-Tag / Besonderheit | Max. Triebe |
|:---:|---|:---:|:---:|:---:|---|:---:|
| **01** | **Mauerkrone (Süd)** | `3` (Volle Sonne) | `1` (Trocken) | `1` (Flach) | 🌬️ Starkwind (hohe Verdunstung) | 2 |
| **02** | **Wasserspeier-Spur** | `2` (Halbsonne) | `3` (Feucht) | `2` (Mittel) | 💧 Dauertropf nach jedem Regen | 2 |
| **03** | **Fenstersims-Maßwerk**| `1` (Schatten) | `2` (Mäßig) | `2` (Mittel) | 🪟 Wind- und wettergeschützt | 3 |
| **04** | **Kragstein / Taubensitz** | `3` (Volle Sonne) | `1` (Trocken) | `2` (Mittel) | 🕊️ Guano-Zone: **$+2$ Stickstoff ($N$)** | 2 |
| **05** | **Ziegelspalt (Mürbe)** | `2` (Halbsonne) | `1` (Trocken) | `3` (Tief) | 🧱 Weicher Ziegel (leichtes Wurzeln) | 2 |
| **06** | **Kalkmörtel-Spalt** | `1` (Schatten) | `2` (Mäßig) | `2` (Mittel) | 🧪 **Kalkreich ($pH > 7{,}5$):** Ideal für Farne | 2 |
| **07** | **Normale Mauerfuge** | `2` (Halbsonne) | `1` (Trocken) | `1` (Flach) | 🧱 Standard-Fuge | 1 |
| **08** | **Mäusegang / Höhle** | `1` (Schatten) | `2` (Mäßig) | `3` (Tief) | 🕳️ **Bunker:** Frost- und Hitzegeschützt | 3 |
| **09** | **Nord-Ecke (Moosbett)**| `1` (Schatten) | `3` (Feucht) | `1` (Flach) | 🟩 **Moos-Startplatz:** Natürliches Keimbett | 2 |
| **10** | **Sockelkante (Boden)** | `2` (Halbsonne) | `2` (Mäßig) | `2` (Mittel) | 👣 **Bodenkontakt:** Tritt & Spritzwasser | 2 |

*Hinweis zu Abweichungen zwischen Bild und Tabelle:* Siehe [Status und offene Punkte](status-und-offene-punkte.md).

---

## 2. Die Werte der Verbindungs-Streifen (Doppelseitig)

Jeder Streifen hat zwei Stufen: **Seite A = Level 1** und **Seite B = Level 2**.  
Wird eine Verbindung ausgebaut, wird der Streifen einfach auf die Rückseite umgedreht (*Flip!*).

```
┌─────────────────────────────────┐      ┌─────────────────────────────────┐
│        SEITE A: LEVEL 1         │ ──►  │        SEITE B: LEVEL 2         │
│  (Zarter Pfad / Frischer Trieb) │      │   (Verholzt / Verdichtet)       │
└─────────────────────────────────┘      └─────────────────────────────────┘
```

### 🪵 Wurzel-Streifen (Brauner Kartonstreifen)
| Seite / Level | Name | Voraussetzung an Pflanze | Transfer-Wirkung | Haltbarkeit / Modifikator |
|---|---|---|---|---|
| **Seite A (Lvl 1)** | **Zarte Faserwurzel** | Pflanze mit Wurzel $\ge 1$ | ➡️ Schafft Trasse für **1 Trieb** im Nachbarslot | ❄️ *Frostgefahr:* Reißt bei Winterfrost ohne Moos ab |
| **Seite B (Lvl 2)** | **Holzstrang** *(Flip!)* | Pflanze mit Wurzel $\ge 2$ | ➡️ Schafft Trasse für **2 Triebe** im Nachbarslot | 🧱 **$+1$ Fugenplatz** im Ziel-Slot · 🛡️ **Frostfest** |

---

### 🍄 Pilz-Streifen (Elfenbeinfarbener Myzelstreifen)
| Seite / Level | Name | Voraussetzung an Pflanze | Transfer-Wirkung | Haltbarkeit / Modifikator |
|---|---|---|---|---|
| **Seite A (Lvl 1)** | **Hyphenfaden** | Beide = `Mykorrhiza: Ja`<br>*(🚫 Kreuzblütler gesperrt!)* | 🔄 Tauscht **1 Wasser** oder **1 Nährstoff** pro Runde | ⚠️ Stirbt ab, wenn Nachbarpflanze Senföle ausscheidet |
| **Seite B (Lvl 2)** | **Myzel-Netz** *(Flip!)* | Beide = `Mykorrhiza: Ja` | 🔄 **Freier Ausgleich:** Wasser und Nahrung fließen frei | 🛡️ **Dürreschild: $-1$** (kühlt beide Pflanzen) |

---

### 🐜 Ameisen-Streifen (Schwarzer Pheromonstreifen)
| Seite / Level | Name | Voraussetzung an Pflanze | Transfer-Wirkung | Haltbarkeit / Modifikator |
|---|---|---|---|---|
| **Seite A (Lvl 1)** | **Späher-Pfad** | Quellpflanze hat Samen | 🎲 **50 % Chance** auf 1 Samentransport (Münzwurf) | 🌧️ *Wegwaschbar:* Wird bei Starkregen weggespült |
| **Seite B (Lvl 2)** | **Ameisenstraße** *(Flip!)* | Pflanze bietet Ameisenbrot (Elaiosom) | 📦 **100 % Samentransport:** Jeden Herbst wandert 1 Samen | 🕊️ **$+1$ Stickstoff ($N$)** für beide Nischen · 🛡️ **Wetterfest** |

---

### 🟩 Das Oberflächen-Plättchen: Moos-Patch (Green Cushion Tile)
Das Moos ist ein unregelmäßiges grünes Plättchen, das direkt auf einen beliebigen Slot gelegt werden kann.

* 💧 **Wasser:** `+1` *(wirkt wie ein Feuchtigkeitsschwamm)*
* ☀️ **Hitzeschild:** `1` *(reflektiert Sonnenstrahlung, schützt vor Verbrennung)*
* 🌱 **Keimbett:** `+1` *(Samen keimen mit $+1$ zusätzlichem Trieb)*
* 🛡️ **Besenschutz:** Flache Moospolster sind immun gegen Straßenbesen.

---

## 3. Die Werte der Pflanzenkarten (Level I und II)

Die beiden Seiten zeigen junge und etablierte Pflanzen. Botanische Artwerte bleiben gleich; Wurzelraum und Triebe sind Spielwerte. Licht und Feuchte werden aus den tschechischen **Pladias**-Werten in drei Kategorien eingeteilt: **1–3 → 1, 4–6 → 2, 7–9 → 3**.

| Pflanze | ☀️ Licht I / II | 💧 Wasser I / II | 🪴 Wurzelraum I / II | 🌿 Triebe I / II | Eigenschaft I (Jung) | Eigenschaft II (Erwachsen) | Botanische Akte |
|---|:---:|:---:|:---:|:---:|---|---|:---:|
| **Zimbelkraut** | 2 / 2 | 2 / 2 | 1 / 2 | 1 / 2 | Zarter Kriechtrieb | Samenkapseln in Mauerspalten | [Akte](../../pflanzen/arten/zimbelkraut/) |
| **Mauerraute** | 3 / 3 | 1 / 1 | 1 / 1 | 1 / 2 | Jungfarn im feuchten Spalt | Reife Wedel mit Sporenlagern | [Akte](../../pflanzen/arten/mauerraute/) |
| **Schöllkraut** | 2 / 2 | 2 / 2 | 2 / 3 | 1 / 3 | Junger krautiger Trieb | Reife Samen mit Ameisenbrot | [Akte](../../pflanzen/arten/schoellkraut/) |
| **Behaartes Schaumkraut** | 2 / 2 | 2 / 2 | 1 / 1 | 1 / 1 | Kleine Blattrosette | Reife Schoten schleudern Samen | [Akte](../../pflanzen/arten/behaartes-schaumkraut/) |
| **Breitwegerich** | 3 / 3 | 2 / 2 | 1 / 2 | 1 / 2 | Junge bodennahe Rosette | Breite Rosette mit Blütenähren | [Akte](../../pflanzen/arten/breitwegerich/) |
| **Sommer-Portulak** | 3 / 3 | 2 / 2 | 1 / 1 | 1 / 3 | Junge sukkulente Pflanze | Reife Pflanze mit gelben Blüten | [Akte](../../pflanzen/arten/sommer-portulak/) |
| **Einjähriges Rispengras** | 3 / 3 | 2 / 2 | 1 / 1 | 1 / 2 | Junger Grasbüschel | Lockere Rispen mit Ährchen | [Akte](../../pflanzen/arten/einjaehriges-rispengras/) |
| **Silber-Birnmoos** | 1–3 / 1–3 | 1 / 1 | 0 / 0 | 1 / 2 | Junge Mooskolonie | Dichtes Polster mit Sporenkapseln | [Akte](../../pflanzen/arten/silber-birnmoos/) |

---

## 4. Alternative A4-PDF-Spielvariante

Im beiliegenden Druckbogen [`material/Fugenduell-Verbindungen-A4-v1.pdf`](material/Fugenduell-Verbindungen-A4-v1.pdf) existiert eine erweiterte Testvariante mit **Energie- (E)** und **Nährstoff-Token (N)**:

* **Wurzelzugang I/II:** Speichert 1 bzw. 2 Wasser-Vorrat; kostet 1 E Ausbau.
* **Kriechtrasse I/II:** Ermöglicht 0 bzw. 1 Neupflanzung in Nachbarslots; kostet 1 E Ausbau.
* **Pilzverbindung I/II:** Transferiert 1 bzw. 2 N-Token; Aktion kostet 1 E.
* **Ameisenroute I/II:** Transportiert 1 bzw. 2 geeignete Samen; Aktion kostet 1 E.
* **Moos-Patches:** Feuchte $+1$, max. 1 Patch pro Slot, kein Stapeln.
