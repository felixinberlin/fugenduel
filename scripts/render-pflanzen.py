"""Generate plant tables and copy/paste prompts from the shared, sourced data."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent.parent
DATA=json.loads((ROOT/'data/pflanzen.json').read_text())
def num(v):
    return 'k. A.' if v is None else f'{v:.3f}'.rstrip('0').rstrip('.') if isinstance(v,float) else str(v)
def facts(p):
    f=p['facts']
    if f['light'] is None:
        return 'Botanik: Rhizoide, keine echten Wurzeln; Sporen statt Samen. L/F/N, CSR und Messmaße: k. A. Spielwerte vorläufig.'
    csr=' / '.join(num(v) for v in f['csr_percent'])
    return (f"Botanik (Artwerte): L {f['light']} | F {f['moisture']} | N {f['nutrients']}; "
            f"Höhe {f['height_m']} m; CSR % {csr}; maximale Wurzeltiefe {num(f['root_depth_m'])} m; "
            f"Wurzelradius {num(f['root_radius_m'])} m; Knospenbank {num(f['bud_bank_size'])}.")
def prompt(p,l):
    f=p['facts']
    lines=[f"Create one finished FUGENDUEL botanical game card, portrait 2:3, full card visible with identical dimensions and layout across the series. "
    "Use a restrained weathered brick and dark stone frame, warm parchment panels, dark legible type, natural macro photography style and authentic urban plant anatomy. "
    "Use a supplied reference card for layout if available. Keep a generous safe margin and readable panels. No fantasy glow, extra limbs, plastic rendering or invented numbers.",
    f"Subject: {p['scientific_name']}. Stage: {'young vegetative plant or colony' if l['level']==1 else 'established reproductive plant or colony'}. {l['art']}",
    "Render these German labels and values exactly, without translating names or rounding further:",
    f"FUGENDUEL\n{p['name']}\n{p['scientific_name']}\nLEVEL {l['level']}",
    f"Spielwerte: Licht {l['light']} | Wasser {l['water']} | Wurzelraum {l['root_space']} | Triebe {l['shoots']}",
    f"Eigenschaft: {l['trait']}",facts(p),
    "Footer: Artwerte, keine Messung dieser Pflanze. Level und Spielwerte sind Spielentwurf. k. A. = keine Angabe."]
    if f['light'] is not None:
        lines.append("Sources label: Pladias; UNDERPLOT v39 (CC BY 4.0). L/F/N are ecological indicator values, not light intensity, litres of water or nitrogen quantities. "
        "Root depth and radius describe aggregated species reference data, not a measured size of this pictured juvenile or mature individual. CSR is a species strategy, not attack/defence. "
        "Preserve source rounding; the three CSR values can sum to 100.1 because the source rounds them.")
    else:
        lines.append("Sources label: Bryum argenteum, botanischer Entwurf. Do not invent vascular-plant indicator or CSR values for moss, and do not replace unavailable values by zero.")
    lines.append("This card is one side of a two-sided physical piece: Level 1 and Level 2 share the same species facts and frame. "
        "Only stage illustration, level, root-space game requirement, shoot game count and trait change. A higher level does not imply woodiness, frost immunity, infinite drought tolerance or doubled measured roots. "
        "Do not add unverified fungal partnerships, guaranteed seed transport, action costs, or combat statistics.")
    return '\n\n'.join(lines)
head="# Fugenduel — Pflanzen in zwei Leveln\n\nStand: 30.10.2026. Gemeinsame Quelle: [data/pflanzen.json](data/pflanzen.json). Neu erzeugen: `python3 scripts/render-pflanzen.py`.\n\n"
explanation=("Die beiden Seiten zeigen junge und etablierte Pflanzen. Botanische Artwerte bleiben gleich; Wurzelraum und Triebe sind vorgeschlagene Spielwerte, keine gemessenen Entwicklungsstufen. "
"Licht und Feuchte werden für die sieben Gefäßpflanzen aus **Pladias** in drei Kategorien zusammengefasst: **1–3 → 1, 4–6 → 2, 7–9 → 3**. Diese Einteilung ist eine Designentscheidung. "
"Die Pflanzenwerte sind Standortpräferenzen; passende Felder und zulässige Toleranzen vereinbaren die Kinder. Wurzelraum ist der Platzbedarf im Spiel und wird nicht aus Metern errechnet. "
"Beim Moos sind Licht 1–3 und Wasser 1 vorläufige Spielwerte ohne hier verifizierte Zeigerwerte. Fehlende Messwerte bleiben `k. A.`; Wurzelraum 0 bezeichnet Rhizoide.\n\n")
table="| Pflanze | Licht I / II | Wasser I / II | Wurzelraum I / II | Triebe I / II |\n|---|---|---|---|---|\n"
for p in DATA['plants']:
    a,b=p['levels'];table+=f"| {p['name']} | {a['light']} / {b['light']} | {a['water']} / {b['water']} | {a['root_space']} / {b['root_space']} | {a['shoots']} / {b['shoots']} |\n"
readme=ROOT/'01-werte-tabellen.md'; old=readme.read_text(); before=old.split('## 3. Die Werte der Pflanzenkarten')[0]
readme.write_text(before+'## 3. Die Werte der Pflanzenkarten — Level I und II\n\n'+explanation+table+'\nQuellen und Artwerte: [Pflanzenkatalog](04-pflanzen-katalog.md). Fertige Prompts: [Level 1](PROMPTS-LEVEL-1.txt), [Level 2](PROMPTS-LEVEL-2.txt).\n')
catalog=head+explanation+table+'\n## Botanische Referenzen und Spielverbindungen\n\n'
for p in DATA['plants']:
    f=p['facts']; catalog+=f"### {p['name']} — *{p['scientific_name']}*\n\n{facts(p)}\n\n"
    catalog+=f"Quelle: [Artprofil]({f['source']}). "
    if f['underplot_source']: catalog+=f"Untergrund: [UNDERPLOT v39]({f['underplot_source']}); Originalzeile im [Datenauszug](data/underplot-v39-auszug.csv). "
    catalog+='\n\n'
    if p['id']=='mauerraute': catalog+='Ein Farn bildet Sporen. Das im Quellfeld „Flowering period“ genannte Zeitfenster darf nicht als Blüte eines Farns beschriftet werden. Feuchte Keimbedingungen sind kein Beleg für zwingende Moosbindung oder Dürre-Immunität.\n\n'
    elif p['id']=='silbermoos': catalog+='Moos bildet Sporen und besitzt Rhizoide. Die vorliegenden Gefäßpflanzendaten belegen keine L/F/N- oder CSR-Zahlen für diese Art. Keine garantierte Wiederbelebung in exakt 20 Minuten aufdrucken.\n\n'
    else: catalog+=f"Phänologie im tschechischen Pladias-Datensatz: {f['reproductive_period']} (Artspanne, keine Garantie für jede Pflanze).\n\n"
    catalog+=f"Spielentwurf: Pilzverbindung {'als Test freigegeben' if p['fungal_game_permission'] else 'im Basistest nicht freigegeben'}; keine verifizierte Mykorrhiza-Aussage. "
    if p['id']=='zimbelkraut': catalog+='Kriechtrassen I/II: 1/3 als Sonderfähigkeit; keine Wurzeltiefen. UNDERPLOT führt die Art als nicht klonal, daher ist das Ausbreitungsnetz eine Spielabstraktion. '
    if p['ant_seed_game_permission']: catalog+='Ameisen-Samentransport im Spiel freigegeben; Elaiosomen sind botanisch belegt, garantierte Transporte sind Spielregeln. '
    catalog+='Eine Verbindung wird unabhängig von der Pflanze umgedreht; Pflanzen-Level II bedeutet weder verholzt noch frostfest.\n\n'
catalog+='## Quellenumfang\n\nPladias: abgerufen am 30.10.2026, tschechische Artprofile; nicht mit regional abweichenden FloraWeb-Werten vermischen. UNDERPLOT: Portalversion v39 / Version 7196, DOI und Download-Prüfsumme in data/pflanzen.json. RDepth ist die aggregierte maximale Wurzeltiefe, LRExtent der maximale Radius; keine Messung an der dargestellten Pflanze. Fehlende Werte wurden nicht ergänzt. Knospenbankwerte aus UNDERPLOT und einzelnen CLO-PLA/Pladias-Profilen können durch Aggregation voneinander abweichen. Der Originaldatenauszug bleibt erhalten.\n'
(ROOT/'04-pflanzen-katalog.md').write_text('\n'.join(line.rstrip() for line in catalog.splitlines())+'\n')
intro=("FUGENDUEL — KOPIERFERTIGE PROMPTS\nStand 30.10.2026; erzeugt aus data/pflanzen.json.\n"
"Jeden Prompt vollständig kopieren. Format 2:3 im jeweiligen Generator einstellen; keine herstellerspezifischen Versionsparameter nötig.\n"
"Die botanischen Zahlen sind Artwerte; die Levelzahlen sind ausdrücklich Spielentwurf. Fertige Schrift vor dem Druck mit der Tabelle vergleichen.\n\n")
blocks={}
for level in (1,2):
    blocks[level]=[]
    for p in DATA['plants']:
        l=p['levels'][level-1]
        blocks[level].append(f"{'='*70}\n{p['name']} ({p['scientific_name']}) — LEVEL {level}\n{'='*70}\n\n"+prompt(p,l))
    (ROOT/f'PROMPTS-LEVEL-{level}.txt').write_text(intro+'\n\n'.join(blocks[level])+'\n')
(ROOT/'PROMPTS-COPY-PASTE.txt').write_text(intro+'\n\n'.join(blocks[1]+blocks[2])+'\n')
md=head+explanation+table+'\n## Verwendung\n\nDie vollständigen Prompts stehen getrennt in [Level 1](PROMPTS-LEVEL-1.txt) und [Level 2](PROMPTS-LEVEL-2.txt), gesammelt in [Copy/Paste](PROMPTS-COPY-PASTE.txt). Sie enthalten exakte deutsche Kartenbeschriftungen und Quellenwerte. Jeder Prompt funktioniert ohne Anbieterparameter; das Seitenverhältnis im Generator auf 2:3 stellen. Eine Layoutreferenz kann zusätzlich mitgegeben werden.\n\nBei schlechter Schriftwiedergabe nur das Motiv generieren und die Beschriftungen anschließend unverändert im Layout setzen. Vor dem Druck Artname, Level, Zahlen und Symbole am Katalog prüfen. Jede Rückseite hat denselben Rahmen und dieselben Artwerte wie ihre Vorderseite.\n\n## Korrigierte Angaben\n\nPortulak: Wasser 2 statt 1 nach der angegebenen Pladias-Kategorisierung; Wurzelraum II bleibt 1 statt der zuvor widersprüchlichen 2. Rispengras: Licht 3 und Wasser 2 statt 2/3. Pflanzen-Level, Wurzelraum, Streifenanzahl und gemessene Tiefe werden getrennt geführt. Keine pauschale Datenbank-Bestätigung für Spielkräfte, keine erfundenen Jugendmesswerte. Für drei Arten fehlt RDepth in UNDERPLOT.\n'
(ROOT/'06-bild-prompts-pflanzen.md').write_text(md)
print('Generated 16 complete prompts, both level files, combined prompts, plant catalog and shared plant table.')
