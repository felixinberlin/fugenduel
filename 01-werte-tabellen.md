# Fugenduel — Wertetabellen für den Prototyp

> **Leitprinzip:**
> *„Die Kinder erfinden die Regeln — wir machen Werte und Material nachvollziehbar.“*
> Alle Werte bewegen sich intuitiv auf einer Skala von **1 bis 3** (oder speziellen klaren Icons). Keine großen Zahlen, kein Rechnen mit Kommastellen.

**Prüfstand 30.10.2026:** Abschnitt 3 und die Pflanzenprompts werden gemeinsam aus [data/pflanzen.json](data/pflanzen.json) erzeugt. Die Brett- und Verbindungswerte in Abschnitt 1–2 sind ältere Spielentwürfe; Bilder und PDF weichen davon ab. Sie sind keine gemessenen Standortwerte oder bestätigten Naturgesetze. [Statusreview](07-status-review.md).

---

## 1. Die Werte des Spielbretts (Arena: Kirchenmauer Lieberose)

Das Spielfeld besteht aus 10 Mikrostandorten (Slots). Die oberen 5 Slots bilden die sonnige, trockene Mauerkrone; die unteren 5 Slots bilden den kühlen, feuchteren Sockel.

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

---

## 2. Die Werte der Verbindungs-Streifen (Doppelseitig)

Jeder Streifen hat zwei Seiten: **Seite A = Level 1** und **Seite B = Level 2**.
Wird eine Verbindung ausgebaut, wird der Streifen einfach auf die Rückseite umgedreht (*Flip!*).

### 🪵 Wurzel-Streifen (Brauner Kartonstreifen)
| Seite / Level | Name | Voraussetzung an Pflanze | Transfer-Wirkung | Haltbarkeit / Modifikator |
|---|---|---|---|---|
| **Seite A (Lvl 1)** | **Zarte Faserwurzel** | Pflanze mit Wurzel $\ge 1$ | ➡️ Schafft Trasse für **1 Trieb** | ❄️ *Frostgefahr:* Reißt bei Winterfrost ohne Moos ab |
| **Seite B (Lvl 2)** | **Holzstrang** *(Flip!)* | Pflanze mit Wurzel $\ge 2$ | ➡️ Schafft Trasse für **2 Triebe** | 🧱 **$+1$ Fugenplatz** im Ziel-Slot · 🛡️ **Frostfest** |

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
| **Seite B (Lvl 2)** | **Ameisenstraße** *(Flip!)* | Pflanze bietet Ameisenbrot | 📦 **100 % Samentransport:** Jeden Herbst wandert 1 Samen | 🕊️ **$+1$ Stickstoff ($N$)** für beide Nischen · 🛡️ **Wetterfest** |

---

### 🟩 Das Oberflächen-Plättchen: Moos-Patch (Green Cushion Tile)
Das Moos ist ein unregelmäßiges grünes Plättchen, das direkt auf einen beliebigen Slot gelegt werden kann.

* 💧 **Wasser:** `+1` *(wirkt wie ein Feuchtigkeitsschwamm)*
* ☀️ **Hitzeschild:** `1` *(reflektiert Sonnenstrahlung, schützt vor Verbrennung)*
* 🌱 **Keimbett:** `+1` *(Samen keimen mit $+1$ zusätzlichem Trieb)*
* 🛡️ **Besenschutz:** Flache Moospolster sind immun gegen Straßenbesen.

---

## 3. Die Werte der Pflanzenkarten — Level I und II

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

Quellen und Artwerte: [Pflanzenkatalog](04-pflanzen-katalog.md). Fertige Prompts: [Level 1](PROMPTS-LEVEL-1.txt), [Level 2](PROMPTS-LEVEL-2.txt).
