# Fugenduel 🌿🧱

> **„Die Kinder erfinden die Regeln — wir machen Werte und Material nachvollziehbar.“**

Willkommen im Repository zu **Fugenduel**. Dieses Projekt erforscht ein modulares, taktiles und botanisch fundiertes Brettspiel- und Lernsystem über das verborgene Ökosystem urbaner Pflaster- und Mauerfugen.

**Stand 30.10.2026:** Ein Materialprototyp mit noch offenen Brett- und Verbindungsvarianten. Die [Statusreview](07-status-review.md) beschreibt die Unterschiede. [Bildübersicht und Import](assets/README.md) · [Prompts Level 1](PROMPTS-LEVEL-1.txt) · [Prompts Level 2](PROMPTS-LEVEL-2.txt) · [Botanische Quellen und Werte](04-pflanzen-katalog.md).

---

## 🎯 Die Kern-Idee

Fugenduel gibt Kindern und Spielern ein Set ehrlicher, naturwissenschaftlicher Werkzeuge an die Hand:
1. **Das Spielfeld (Die Arena):** Ein vertikaler Schnitt durch einen echten historischen Ort (Prototyp: *Kirchenmauer Lieberose*) mit 10 Mikro-Nischen entlang eines Höhen- und Sonnengradienten.
2. **Die Verbindungen (Das Fugen-Netzwerk):** Physische, doppelseitige Streifen (Wurzel, Pilzmyzel, Ameisenstraße), die in den Mörtelfugen zwischen den Feldern verlegt und bei Wachstum einfach umgedreht werden (*Level 1 ➔ Level 2*).
3. **Die Ammen-Plättchen (Moos-Patches):** Grüne Filz-/Papp-Inseln, die trockene Ziegel in feuchte Keimstätten verwandeln.
4. **Die Pflanzen-Karten:** 8 charakterstarke urbane Überlebenskünstler mit belegten botanischen Artwerten und getrennten Spielkategorien von **1 bis 3**, jeweils auf **zwei Leveln**.

Es gibt kein 30-seitiges Regelwerk: Die Zahlen und Symbole sind selbsterklärend auf die Steine und Karten gedruckt. Wie gewonnen, gekämpft oder kooperiert wird, bestimmen die Kinder selbst.

---

## 📂 Repository-Struktur

* [`01-werte-tabellen.md`](01-werte-tabellen.md) — **Das Herzstück:** Aktuelle Entwurfswerte für das Board (10 Slots), die 3 doppelseitigen Streifen, das Moos-Plättchen und die Pflanzenkarten.
* [`02-kirchenmauer-lieberose.md`](02-kirchenmauer-lieberose.md) — Die Prototyp-Arena im Detail: Z-Gradient, die 10 Nischen (Wasserspeier, Kalkspalt, Taubensitz) und die 4 historischen Epochen-Jahre (1945, 1947, 2018, 2024).
* [`03-untergrund-netzwerk.md`](03-untergrund-netzwerk.md) — Die Biologie und Physik der Streifen: Dickenwachstum, 3D-Schichtung an Fugenkreuzungen, Mykorrhiza-Fusion und Senföl-Angriffe.
* [`04-pflanzen-katalog.md`](04-pflanzen-katalog.md) — Die 8 Pflanzen-Pioniere im Porträt mit Werten (1–3), Netzwerk-Affinität und botanischen Superkräften.
* [`05-gespraechsprotokoll.md`](05-gespraechsprotokoll.md) — Die überlieferte Zusammenfassung des Denkprozesses; kein vollständiger Chat-Export.
* [`06-bild-prompts-pflanzen.md`](06-bild-prompts-pflanzen.md) — 16 vollständige Prompts, Leveldefinitionen und gemeinsame Datenquelle.
* [`07-status-review.md`](07-status-review.md) — Stand, Widersprüche, überprüfte Quellen und nächste Schritte.
* [`assets/`](assets/) — Grafiken und Vorlagen, inklusive des Original-Spielfeldentwurfs `lieberose-kirchenmauer.jpg`.

---

## 🛠️ Schnellübersicht der Zahlen (Skala 1–3)

```
        ☀️ LICHT          💧 WASSER          🪴 WURZEL / TIEFE
   1 = Schatten       1 = Trocken        1 = Flacher Spielraum
   2 = Wechsellicht   2 = Mäßig feucht   2 = Normaler Mörtelspalt
   3 = Volle Sonne    3 = Feucht/nass      3 = Tiefe Trümmerkluft
```

Die folgenden Streifenwirkungen sind der ursprüngliche Testentwurf und weichen vom A4-PDF ab; siehe Statusreview. Die Streifen haben **Seite 1 (Level 1)** und **Seite 2 (Level 2)** und zeigen ihre Werte direkt aufgedruckt:
* 🪵 **Wurzel-Streifen (Braun):** Etabliert Triebe, weitet Fugen auf (+1 Kapazität), wird verholzt frostfest.
* 🍄 **Pilz-Streifen (Elfenbein):** Tauscht Wasser & Nährstoffe, kühlt im Sommer (Kreuzblütler gesperrt!).
* 🐜 **Ameisen-Streifen (Schwarz):** Transportiert Samen, düngt beide Slots mit Stickstoff.
* 🟩 **Moos-Plättchen (Grün):** Spendet $+1$ Wasser, Hitzeschild und Keimbett auf dem Ziegel.
