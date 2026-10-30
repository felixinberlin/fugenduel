# 🔍 Fugenduel Brettspiel — Statusreview & Offene Punkte

> Stand: 30.10.2026. Zusammenfassung aller Konsistenzprüfungen, offenen Diskrepanzen und Prioritäten für den nächsten Arbeitsschritt.

---

## 1. Was bereits steht und trägt

1. **Starke Identität & Taktiles Spielmaterial:** Die vertikale Kirchenmauer mit 10 Mikro-Nischen macht Standortwahl unmittelbar begreifbar.
2. **Umdrehbare Doppel-Elemente (*Flip!*):** Sowohl die Pflanzenkarten (Level 1 & 2) als auch die Verbindungsstreifen (Level 1 & 2) funktionieren ohne Token-Türme durch einfaches Umdrehen.
3. **Gemeinsame Datenbasis der Pflanzen:** Alle Pflanzenwerte wurden konsolidiert und mit echten Messwerten aus Pladias und UNDERPLOT v39 verknüpft.
4. **Das Leitprinzip:** Kinder erfinden eigene Spielregeln anhand klarer, ehrlicher Zahlen (1 bis 3) und verständlicher Icons.

---

## 2. Die drei offenen Diskrepanzen

### Diskrepanz 1: Brettgrafik vs. Wertetabelle in 7 von 10 Slots

Ein genauer Vergleich des gedruckten Entwurfs [`material/lieberose-kirchenmauer.png`](material/lieberose-kirchenmauer.png) mit der Wertetabelle in [`regeln-und-werte.md`](regeln-und-werte.md) zeigt folgende Abweichungen (Reihenfolge: **Licht / Wasser / Wurzelraum**):

| Slot | Auf dem Brettbild | In der Tabelle | Empfohlene Lösung für den Druck |
|:---:|:---:|:---:|---|
| **01** | **3 / 1 / 1** | **3 / 1 / 1** | ✅ **Übereinstimmend** (Mauerkrone Süd) |
| **02** | 2 / 2 / 1 | 2 / 3 / 2 | Tabelle bevorzugen: Wasserspeier braucht Wasser 3! |
| **03** | 1 / 3 / 2 | 1 / 2 / 2 | Tabelle bevorzugen: Fenstersims ist mäßig feucht (W2). |
| **04** | **3 / 1 / 2** | **3 / 1 / 2** | ✅ **Übereinstimmend** (Kragstein / Taubensitz) |
| **05** | 2 / 3 / 3 | 2 / 1 / 3 | Tabelle bevorzugen: Mürber Ziegel ist oben, daher trocken (W1). |
| **06** | 1 / 2 / 1 | 1 / 2 / 2 | Tabelle bevorzugen: Kalkspalt hat mittlere Tiefe (Wurzel 2). |
| **07** | 2 / 1 / 3 | 2 / 1 / 1 | Tabelle bevorzugen: Normale Fuge ist eng und flach (Wurzel 1). |
| **08** | 3 / 2 / 2 | 1 / 2 / 3 | Tabelle bevorzugen: Mäusehöhle ist schattig (L1) und tief (Wurzel 3). |
| **09** | 1 / 3 / 3 | 1 / 3 / 1 | Tabelle bevorzugen: Moosbett ist flach auf dem Stein (Wurzel 1). |
| **10** | **2 / 2 / 2** | **2 / 2 / 2** | ✅ **Übereinstimmend** (Sockelkante Boden) |

*Fazit:* Die Werte der Tabelle sind ökologisch schlüssiger als das ursprüngliche KI-generierte Brettbild. Für den nächsten Grafik-Export sollte das Brett auf die Tabellenwerte aktualisiert werden.

---

### Diskrepanz 2: Zwei unterschiedliche Verbindungs-Systeme

Im Projekt existieren zwei verschiedene Ausarbeitungen der Streifen:

| Aspekt | Standard-System (Wertetabelle) | A4-PDF Druckbogen v1 |
|---|---|---|
| **Ressourcen** | Keine Währung; Werte direkt aufgedruckt | Verwendet **Energie- (E)** und **Nährstoff-Token (N)** |
| **Wurzel** | Schafft Trassen für 1 bzw. 2 Triebe; Level 2 gibt $+1$ Fugenplatz | Speichert Wasser-Vorrat (1 bzw. 2); kein neuer Slot |
| **Ausbreitung** | Teil der Wurzelverbindung | Eigene „Kriechtrasse“ (Neupflanzen 0 bzw. 1) |
| **Pilz** | Tauscht 1 Wasser/Nährstoff; freier Ausgleich auf Level 2 | Transfer von 1 bzw. 2 N-Token; Aktion kostet 1 E |
| **Ameise** | 50 % / 100 % Samentransport im Herbst; $+1$ Stickstoff | Transport 1 bzw. 2 Samen; Aktion kostet 1 E |

*Entscheidung:* Für das Spiel mit Kindern bleibt das **Standard-System ohne Token-Währung** die primäre, einfachere Variante. Das PDF-System wird als Experten-Variante („Fugenduel Taktik“) geführt.

---

### Diskrepanz 3: Vorhandene vs. fehlende Kartenmotive

* **Vorhanden als hochauflösende Bilddateien:**
  * Breitwegerich: Datenkarte + Level 2 Karte (`breitwegerich-level-2.jpg`)
  * Zimbelkraut: Level 1 (`zimbelkraut-level-1.jpg`) + Level 2 (`zimbelkraut-level-2.jpg`)
  * Mauerraute: Level 1 (`mauerraute-level-1.jpg`)
* **Noch zu generieren:**
  * Schöllkraut (Level 1 & 2)
  * Behaartes Schaumkraut (Level 1 & 2)
  * Sommer-Portulak (Level 1 & 2)
  * Einjähriges Rispengras (Level 1 & 2)
  * Silber-Birnmoos (Level 1 & 2)
  * Breitwegerich (Level 1)
  * Mauerraute (Level 2)
* Die vollständigen Prompts liegen fertig in [`../../pflanzen/bild-prompts/alle-prompts.txt`](../../pflanzen/bild-prompts/alle-prompts.txt).

---

## 3. Prioritäten für die nächsten Schritte

1. 🎯 **Entscheidung über das Brett-Layout treffen:** Wollen wir das Bild an die Tabelle anpassen oder die Tabelle an das bestehende Bild? *(Empfehlung: Bild an Tabelle anpassen).*
2. 🎯 **Die restlichen 11 Kartenmotive generieren** mit den einheitlichen Layout-Prompts.
3. 🎯 **Ersten begleiteten Spieltest vorbereiten:** Ein kleines Set ausdrucken, ausschneiden und mit Testspielern/Kindern erproben.
