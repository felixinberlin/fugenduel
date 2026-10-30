# 🌐 Das Untergrund-Netzwerk: Streifen & Plättchen

> **Entwurfsstand:** Dieses Dokument beschreibt die physikalische und biologische Mechanik der Verbindungsstreifen und Moos-Patches im Fugenraum.

In **Fugenduel** ist die Backsteinmauer kein passives Gemälde, sondern ein **pulsierendes, lebendiges Netzwerk**. Die Spieler nutzen physische Spielsteine (doppelseitige Streifen und organische Moos-Plättchen), die sie direkt in die Mörtelfugen zwischen den Slots verlegen.

---

## 1. Die drei Streifen-Typen (Doppelseitig)

Jeder Streifen besitzt zwei Entwicklungsstufen:
* **Seite A (Level 1):** Die zarte, frische Verbindung (günstig, aber empfindlich).
* **Seite B (Level 2):** Die verholzte, dicke Autobahn (stark, wetterfest).
* **Ausbau (Upgrade):** Der Streifen wird einfach umgedreht (*Flip!*).

```
┌─────────────────────────────────┐      ┌─────────────────────────────────┐
│        SEITE A: LEVEL 1         │ ──►  │        SEITE B: LEVEL 2         │
│  (Zarter Pfad / Frischer Trieb) │      │   (Verholzt / Verdichtet)       │
└─────────────────────────────────┘      └─────────────────────────────────┘
```

### A. 🪵 Der Wurzel-Streifen (Root Connection)
* **Farbe / Aussehen:** Erdbraun mit feinen Wurzelkapillaren (Seite 1) bzw. rissiger Rinde und verholzten Pfahlwurzelknoten (Seite 2).
* **Biologie:** Kriechtriebe (Stolonen des Zimbelkrauts) oder dicke Pfahlwurzeln (Schöllkraut, Löwenzahn).
* **Seite 1 (Faserwurzel):** Erfordert Quellpflanze mit `Wurzel ≥ 1`. Schafft eine Trasse für **1 Trieb** im Nachbarfeld. Reißt bei Winterfrost ohne Moos ab.
* **Seite 2 (Holzstrang):** Erfordert `Wurzel ≥ 2`. Schafft Platz für **2 Triebe** im Nachbarfeld. Weitet die Mörtelfuge dauerhaft auf (**$+1$ Kapazität im Ziel-Slot**). Unzerstörbar bei Frost.

### B. 🍄 Der Pilz-Streifen (Fungal Connection)
* **Farbe / Aussehen:** Helles Elfenbein mit mikroskopisch feinem Hyphen-Spinnwebenmuster (Seite 1) bzw. dickes Myzel-Kabel mit Sporenknöllchen (Seite 2).
* **Biologie:** Arbuskuläre Mykorrhiza (AMF) hinter und zwischen den Ziegeln.
* **🚫 Die Kreuzblütler-Sperre:** Pflanzen mit scharfen Senfölen (*Cardamine hirsuta / Schaumkraut*) scheiden pilzabtötende Wurzelsäfte aus. Sie **können nicht an einen Pilzstreifen angeschlossen werden!**
* **Seite 1 (Hyphenfaden):** Erlaubt das Schieben von **1 Nährstoff- oder Wasserpunkt** pro Runde zwischen zwei verbundenen Pflanzen.
* **Seite 2 (Myzel-Netz):** Freier, unbegrenzter Ausgleich von Feuchtigkeit und Stickstoff zwischen beiden Nischen. Verleiht beiden Pflanzen **Dürreschild: 1** (der Pilz holt Wasser aus feinsten Gesteinsporen).

### C. 🐜 Der Ameisen-Streifen (Ant Connection)
* **Farbe / Aussehen:** Schwarz-grauer Pfad mit einzelnen Ameisensilhouetten (Seite 1) bzw. dichte Pheromon-Straße mit Nestloch (Seite 2).
* **Biologie:** Schwarze Wegameisen (*Lasius niger*), die fettreiche Samenanhängsel (*Elaiosomen*) eintragen.
* **Seite 1 (Späher-Pfad):** 50 % Chance (Münzwurf), dass im Herbst **1 Samen** in den Nachbarslot getragen wird. Kann bei Starkregen weggespült werden.
* **Seite 2 (Ameisenstraße & Erdnest):** Garantierter Transport von **1 Samen** jeden Herbst. Die unterirdische Müllkammer der Ameisen düngt beide Slots mit **$+1$ Stickstoff ($N$)**. Völlig wetterfest.

---

## 2. Das Oberflächen-Plättchen: 🟩 Moos-Patch

Im Gegensatz zu den Streifen (die *in* den Fugen liegen) wird das Moos-Plättchen **direkt auf die Steinfläche eines Slots** gelegt.

* **Biologische Rolle:** Die „Ammenpflanze“ (*Nurse Plant* nach Manu et al. 2025).
* **Wirkung auf den Slot:**
  * 💧 **Wasser:** `+1` (wirkt wie ein nasser Schwamm).
  * ☀️ **Hitzeschild:** Reflektiert UV-Strahlung, schützt Ziegel vor Überhitzung.
  * 🌱 **Keimbett:** Babypflanzen keimen mit $+1$ zusätzlichem Trieb.
* **Besonderheit:** Unverzichtbar für die Keimung von Farnen (*Mauerraute*).

---

## 3. Kreuzungsphysik an Fugenkreuzungen

An Kreuzungen (wo sich horizontale und vertikale Fugen schneiden) greifen drei einfache Naturgesetze:

### Gesetz 1: Die 3D-Schichtung (Verschiedene Typen überlagern sich)
Unterschiedliche Streifentypen blockieren sich nicht. Sie nutzen die drei Dimensionen des Mauerhohlraums:
1. **Wurzel liegt tief** im Spalt (ganz unten).
2. **Pilzmyzel umwebt** Wurzel und Gestein (mittlere Schicht).
3. **Ameisen laufen oben** auf dem Mörtelstrich (Oberfläche).  
*Regel:* Liegen z. B. Wurzel und Ameise quer übereinander, **funktionieren beide ganz normal weiter!**

### Gesetz 2: Symbiose-Kreuzungen (Allianzen am Knotenpunkt)
* 🪵 **Wurzel kreuzt 🍄 Pilz:** **Mykorrhiza-Fusion!** Zucker und Mineralien werden getauscht. Beide Streifen erhalten in dieser Runde $+1$ Reichweite.
* 🪵 **Wurzel kreuzt 🐜 Ameise:** **Das Tunneldach!** Die Ameisen nutzen den geschützten Wurzelgang als Schnellstraße. Samen reisen 1 Slot weiter.
* 🍄 **Pilz kreuzt 🐜 Ameise:** Ameisen desinfizieren ihr Revier mit Ameisensäure. Ein Level-1-Pilzstreifen wird gestoppt (außer er ist Level 2).

### Gesetz 3: Der Revierkampf (Gleicher Typ trifft auf gleichen Typ)
Wollen zwei Spieler dieselbe Fuge mit demselben Typ besetzen:
* **Höheres Level gewinnt:** Ein Level-2-Holzstrang verdrängt eine feine Level-1-Faserwurzel.
* **Gleiches Level (Level 1 vs Level 1):** Beide stoppen an der Kreuzung, bis ein Spieler seinen Streifen auf Level 2 umdreht.

---

## 4. Verbindungen entfernen oder umleiten

Das Spielfeld verstopft nie, weil Verbindungen dynamisch bewegt werden können:

1. **Natürlicher Abbau (Kompost):** Stirbt eine einjährige Pflanze im Winter, verrotten ihre Level-1-Wurzeln. Der Streifen kommt vom Brett und hinterlässt fruchtbaren Humus.
2. **Aktives Umleiten (Tropismus):** Ein Spieler kann eine Level-1-Wurzel kappen und in Richtung einer neu entdeckten Wasserstelle (z. B. Wasserspeier) neu ausrichten.
3. **Senföl-Angriff:** Pflanzt jemand ein Schaumkraut (*Cardamine*) in ein Feld, verätzen dessen Wurzelsäfte alle dort anliegenden Pilzstreifen augenblicklich (Streifen werden entfernt).
4. **Regenguss:** Spült ungeschützte Level-1-Ameisenspuren einfach fort.
