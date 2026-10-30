"""Generate plant tables and copy/paste prompts from the shared, sourced data."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / 'pflanzen/pflanzen.json').read_text() if (ROOT / 'pflanzen/pflanzen.json').exists() else (ROOT / 'data/pflanzen.json').read_text())

def num(v):
    return 'k. A.' if v is None else f'{v:.3f}'.rstrip('0').rstrip('.') if isinstance(v, float) else str(v)

def facts(p):
    f = p['facts']
    if f['light'] is None:
        return 'Botanik: Rhizoide, keine echten Wurzeln; Sporen statt Samen. L/F/N, CSR und Messmaße: k. A. Spielwerte vorläufig.'
    csr = ' / '.join(num(v) for v in f['csr_percent'])
    return (f"Botanik (Artwerte): L {f['light']} | F {f['moisture']} | N {f['nutrients']}; "
            f"Höhe {f['height_m']} m; CSR % {csr}; maximale Wurzeltiefe {num(f['root_depth_m'])} m; "
            f"Wurzelradius {num(f['root_radius_m'])} m; Knospenbank {num(f['bud_bank_size'])}.")

def prompt(p, l):
    f = p['facts']
    lines = [
        "Create one finished FUGENDUEL botanical game card, portrait 2:3, full card visible with identical dimensions and layout across the series. "
        "Use a restrained weathered brick and dark stone frame, warm parchment panels, dark legible type, natural macro photography style and authentic urban plant anatomy. "
        "Use a supplied reference card for layout if available. Keep a generous safe margin and readable panels. No fantasy glow, extra limbs, plastic rendering or invented numbers.",
        f"Subject: {p['scientific_name']}. Stage: {'young vegetative plant or colony' if l['level']==1 else 'established reproductive plant or colony'}. {l['art']}",
        "Render these German labels and values exactly, without translating names or rounding further:",
        f"FUGENDUEL\n{p['name']}\n{p['scientific_name']}\nLEVEL {l['level']}",
        f"Spielwerte: Licht {l['light']} | Wasser {l['water']} | Wurzelraum {l['root_space']} | Triebe {l['shoots']}",
        f"Eigenschaft: {l['trait']}",
        facts(p),
        "Footer: Artwerte, keine Messung dieser Pflanze. Level und Spielwerte sind Spielentwurf. k. A. = keine Angabe."
    ]
    if f['light'] is not None:
        lines.append(
            "Sources label: Pladias; UNDERPLOT v39 (CC BY 4.0). L/F/N are ecological indicator values, not light intensity, litres of water or nitrogen quantities. "
            "Root depth and radius describe aggregated species reference data, not a measured size of this pictured juvenile or mature individual. CSR is a species strategy, not attack/defence. "
            "Preserve source rounding; the three CSR values can sum to 100.1 because the source rounds them."
        )
    else:
        lines.append("Sources label: Bryum argenteum, botanischer Entwurf. Do not invent vascular-plant indicator or CSR values for moss, and do not replace unavailable values by zero.")
    lines.append(
        "This card is one side of a two-sided physical piece: Level 1 and Level 2 share the same species facts and frame. "
        "Only stage illustration, level, root-space game requirement, shoot game count and trait change. A higher level does not imply woodiness, frost immunity, infinite drought tolerance or doubled measured roots. "
        "Do not add unverified fungal partnerships, guaranteed seed transport, action costs, or combat statistics."
    )
    return '\n\n'.join(lines)

explanation = (
    "Die beiden Seiten zeigen junge und etablierte Pflanzen. Botanische Artwerte bleiben gleich; Wurzelraum und Triebe sind vorgeschlagene Spielwerte, keine gemessenen Entwicklungsstufen. "
    "Licht und Feuchte werden für die sieben Gefäßpflanzen aus **Pladias** in drei Kategorien zusammengefasst: **1–3 → 1, 4–6 → 2, 7–9 → 3**. Diese Einteilung ist eine Designentscheidung. "
    "Die Pflanzenwerte sind Standortpräferenzen; passende Felder und zulässige Toleranzen vereinbaren die Kinder. Wurzelraum ist der Platzbedarf im Spiel und wird nicht aus Metern errechnet. "
    "Beim Moos sind Licht 1–3 und Wasser 1 vorläufige Spielwerte ohne hier verifizierte Zeigerwerte. Fehlende Messwerte bleiben `k. A.`; Wurzelraum 0 bezeichnet Rhizoide.\n\n"
)

table = "| Pflanze | ☀️ Licht I / II | 💧 Wasser I / II | 🪴 Wurzelraum I / II | 🌿 Triebe I / II |\n|---|:---:|:---:|:---:|:---:|\n"
for p in DATA['plants']:
    a, b = p['levels']
    table += f"| {p['name']} | {a['light']} / {b['light']} | {a['water']} / {b['water']} | {a['root_space']} / {b['root_space']} | {a['shoots']} / {b['shoots']} |\n"

# Update prompts
intro = (
    "FUGENDUEL — KOPIERFERTIGE PROMPTS\nStand 30.10.2026; erzeugt aus data/pflanzen.json.\n"
    "Jeden Prompt vollständig kopieren. Format 2:3 im jeweiligen Generator einstellen; keine herstellerspezifischen Versionsparameter nötig.\n"
    "Die botanischen Zahlen sind Artwerte; die Levelzahlen sind ausdrücklich Spielentwurf. Fertige Schrift vor dem Druck mit der Tabelle vergleichen.\n\n"
)
blocks = {1: [], 2: []}
for level in (1, 2):
    for p in DATA['plants']:
        l = p['levels'][level - 1]
        blocks[level].append(f"{'='*70}\n{p['name']} ({p['scientific_name']}) — LEVEL {level}\n{'='*70}\n\n" + prompt(p, l))

# Write prompt files into pflanzen/bild-prompts/
prompts_dir = ROOT / 'pflanzen/bild-prompts'
prompts_dir.mkdir(parents=True, exist_ok=True)
(prompts_dir / 'level-1.txt').write_text(intro + '\n\n'.join(blocks[1]) + '\n')
(prompts_dir / 'level-2.txt').write_text(intro + '\n\n'.join(blocks[2]) + '\n')
(prompts_dir / 'alle-prompts.txt').write_text(intro + '\n\n'.join(blocks[1] + blocks[2]) + '\n')

print("Successfully rendered plant tables and prompts!")
