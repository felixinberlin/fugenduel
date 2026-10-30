# 💻 Fugenduel Digitale Simulation & Wetterjahr-Modus

> **„Echte historische NASA-POWER-Wetterdaten treffen auf asynchronen Battle-Simulator und Sukzessions-Evolution.“**

Die **Digitale Simulation** ist ein datengestützter Auto-Battler und Jahres-Simulator. Sie simuliert das Überleben zweier Pflanzen-Gemeinschaften in realen Großstädten über ein komplettes 12-Monats-Wetterjahr.

---

## 🎯 Kern-Konzepte der Simulation

* **Reale Wetterjahre (NASA POWER):** 12 Monatskarten von März bis Februar. Hitze, Dürre, Starkregen, Frost und Stürme basieren auf historischen Messdaten für Städte wie Berlin, Frankfurt, Madrid, Tokyo, Shanghai und Ciudad de México.
* **Sichtbare Battle-Pipeline:**  
  `EREIGNIS ➔ TEST ➔ TAKTIK ➔ RECHNUNG ➔ ERGEBNIS ➔ DRAMA`  
  Keine Blackbox: Jeder Deckungsverlust und jede Resistenz kann im Replay mathematisch nachvollzogen werden.
* **Der Deckungsbalken (Tug-of-War Board):** Beide Pflanzen starten mit 50 % / 50 % Deckung in der Ritze. Die Deckung schwankt zwischen 5 % und 95 % (kein unbarmherziger Sofort-K.O.).
* **Standort-Einfluss (Orte zählen):** Ob Bernauer Straße (Berliner Mauer), Römerberg-Pflaster oder Shibuya Crossing – der Standort entscheidet über Sieger und Verlierer.
* **Mikroevolution & Sukzession:** Pflanzen, die eine Saison überleben, akkumulieren Biomasse, bilden Humus und vererben stärkere Resistenzen an das Folgejahr.

---

## 📂 Dokumente in diesem Ordner

* [**`design-vision.md`**](design-vision.md) — Die fundamentale Design-Vision für Agenten und Entwickler: Balance-Gate, 6 Städte, 24 Orte, HP- und Resistenzmodelle.
* [**`asphalt-arena.md`**](asphalt-arena.md) — Das Konzept der Asphalt-Arena: Rundenaufbau, 6 saisonale Prüfungen und Replay-Mechanik.
* [**`wetterjahr-modus.md`**](wetterjahr-modus.md) — Der Kern-Modus: 12 Monate, relative Schwellenwerte, Watch-View und Engine-Architektur.
* [**`battle-mechanik.md`**](battle-mechanik.md) — Detaillierte Spezifikation der Battle-Pipeline, Deckungsbalken, Taktiken (Wachsen, Wurzeln, Halten) und CSR-Multiplikatoren.
* [**`sukzession-und-evolution.md`**](sukzession-und-evolution.md) — Empirische Evidenz für Bodenbildung in Fugen (Manu et al. 2025) und Mikroevolution im urbanen Raum.
* [**`testspiele-und-balance.md`**](testspiele-und-balance.md) — Spielberichte aus den ersten automatisierten Duellen zwischen Agenten und Erkenntnisse für das Balancing.
* [**`skill-trees.md`**](skill-trees.md) — Ausbaustufen und RPG-Skillbäume für Pflanzenarten im Langzeit-Modus.
