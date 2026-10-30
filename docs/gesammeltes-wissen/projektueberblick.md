# Projektüberblick

## Gemeinsamer Kern

Urbane Fugenpflanzen, ihre Lebensräume und ökologischen Eigenschaften liefern Material für ein Spiel. Mechaniken sollen nachvollziehbar sein; Arten und Lebensräume sollen einen erkennbaren Einfluss haben.

## Zwei dokumentierte Spielformen

| Aspekt | Digitaler Asphalt-Arena-Entwurf | Vorhandenes taktiles Kirchenmauer-Konzept |
| --- | --- | --- |
| Spielfläche | Deckungsbalken mit zwei Pflanzen | 10 Mikrostandorte, Prototyp Kirchenmauer Lieberose |
| Ablauf | sechs saisonale Ereignisse; asynchroner Kampf und Replay vorgeschlagen | Kinder entwickeln Regeln aus Material und Werten |
| Werte | sechs Stats; ältere Entwürfe mit 36-Punkte-Budget | Licht, Wasser und Tiefe auf Skala 1–3 |
| Pflanzen | 14 Arten im lokalen digitalen Kader | acht Pflanzen im vorhandenen Repo beschrieben |
| Verbindungen | Fähigkeiten und Combos in Entwürfen | doppelseitige Wurzel-, Pilz- und Ameisenstreifen; Moos-Patches |

Diese Varianten werden hier nebeneinander dokumentiert. Eine Zusammenführung ist noch keine belegte Projektentscheidung.

## Digitaler Ablauf als Entwurf

`Fugenduell-battle.md` schlägt einen sichtbaren Ablauf aus Ereignis, Test, Taktik, Rechnung und Ergebnis vor. Beide Pflanzen starten mit 50 Prozent Deckung. Arena, Pflanzenwerte, Taktik und Fähigkeiten beeinflussen die Runde. Ein Replay soll die Berechnung zeigen. Vorgeschlagene Grenzen sind 20 Prozentpunkte Veränderung je Runde und 5–95 Prozent Deckung.

Der Entwurf enthält Rechen- und Regelwidersprüche; siehe die offenen Entscheidungen. Er ist keine verbindliche Implementierungsspezifikation.

## Datenstand im lokalen Quellcode

Am 30.10.2026 gelesen: `src/data/fugenduellData.ts` im Amélie-Repository. Dort enthält der wissenschaftliche Kader 14 Arten. Die Wurzeltiefe wird als Messwert referenziert; die fünf weiteren Spielstats und das Gesamtbudget bleiben in diesem Kader ausdrücklich `null`. Ältere Zahlenwerte dürfen daher nicht als aktuelle wissenschaftliche Messwerte übernommen werden.

## Orientierung im Archiv

- Design: `design-vision.md`, `Mechanics.md`, `regelwerk-v0.1.md`.
- Kämpfe: `Fugenduell-battle.md`, Combo- und Spezialangriffs-Dokumente.
- Arten und Karten: Starter-Roster, Master-Card-Deck, Kartenprompts und Artporträts.
- Daten und Revision: `QUELLEN.md`, `data-flora-quellen.md`, `daten-audit-2026-10-09.md`.
- Wetter und Erprobung: `wetterjahr-modus.md`, Testspiel und Replay-Polish vom 11.10.2026.
