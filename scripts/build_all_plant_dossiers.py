import os
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PLANTS = [
    {
        "id": "breitwegerich",
        "folder": "breitwegerich",
        "name": "Breitwegerich",
        "scientific_name": "Plantago major",
        "family": "Plantaginaceae (Wegerichgewächse)",
        "common_names": ["Breitwegerich", "Wiesenpflaster", "König der Wege", "Großer Wegerich", "Greater Plantain"],
        "life_form": "Hemicryptophyt (Knospen an der Erdoberfläche)",
        "life_cycle": "Ausdauernd (Mehrjährig)",
        "botany": {
            "indicator_values": {
                "light": 7,
                "moisture": 5,
                "nutrients": 6,
                "soil_reaction": 7,
                "salinity": 1
            },
            "csr_strategy": {
                "c_percent": 82.3,
                "s_percent": 0.0,
                "r_percent": 17.7,
                "primary_class": "CR (Competitor-Ruderal / Tritt-Konkurrent)"
            },
            "morphology": {
                "height_min_m": 0.1,
                "height_max_m": 0.4,
                "growth_form": "Bodennahe Rosette mit derben, parallelnervigen Blättern",
                "root_system": "Kräftiges Homorhizes Faserwurzelsystem mit dichtem Wurzelstock",
                "max_root_depth_m": 0.497,
                "root_radius_m": 0.33,
                "bud_bank_size": 20.0
            },
            "phenology": {
                "flowering_period": "Juni bis Oktober",
                "dispersal_mechanism": "Epizoochorie / Anthropochorie (Schleimsamen haften an Schuhsohlen und Tierpfoten)"
            },
            "sources": [
                {"name": "Pladias Database", "url": "https://pladias.cz/en/taxon/data/Plantago%20major"},
                {"name": "UNDERPLOT v39 (IDIV)", "url": "https://doi.org/10.25829/idiv.3610-56acy9"}
            ]
        },
        "goodies": {
            "folk_names": ["Wiesenpflaster", "König der Wege", "Fußstapfen des weißen Mannes", "Wegetritt"],
            "tradition_lore": "Schon in antiken und mittelalterlichen Kräuterbüchern das verlässlichste Wundkraut für Wanderer und Reisende. Von indigenen Völkern Nordamerikas als 'Fußstapfen des weißen Mannes' bezeichnet, da er überall dort keimte, wo europäische Siedler Wege anlegten.",
            "medicinal_uses": {
                "title": "Das grüne Notfall-Pflaster",
                "summary": "Kühlt und heilt Mückenstiche, Brennnesselverbrennungen, kleine Schürfwunden und Blasen an den Füßen.",
                "preparation": "Ein frisches Blatt pflücken, kurz reinigen, zwischen Fingern zerreiben oder kauen, bis grüner Pflanzensaft austritt, und direkt auf die Wunde pressen."
            },
            "culinary_uses": {
                "title": "Wildsalat & Wegerich-Gemüse",
                "summary": "Junge zarte Blätter im Frühjahr haben ein feines, leicht nussig-pilziges Aroma. Roh in Wildkräutersalaten oder kurz gedünstet wie Spinat. Die reifen Samen im Spätsommer liefern mineralstoffreiches Wildgetreide.",
                "taste": "Nussig, mineralisch, dezent champignonartig",
                "edibility": "Voll essbar (junge Blätter und reife Samen)"
            },
            "active_compounds": [
                {"name": "Aucubin", "effect": "Natürliches Iridoidglykosid mit stark antibiotischer, antibakterieller und entzündungshemmender Wirkung."},
                {"name": "Kieselsäure", "effect": "Stärkt das Bindegewebe und fördert die schnelle Wundschließung."},
                {"name": "Schleimstoffe & Gerbstoffe", "effect": "Legen einen schützenden Film über gereizte Haut und Schleimhäute."}
            ],
            "game_healing_effect": {
                "name": "Grünes Pflaster",
                "effect": "Heilt 1 befreundeten Trieb nach Trittschaden oder Frost.",
                "description": "Wird eine benachbarte Pflanze von Tritten getroffen, darf der Breitwegerich-Spieler einen Trieb zur Wundheilung einsetzen."
            },
            "street_discovery_tip": "Such nach Gehwegplatten oder Pflasterfugen, auf die ständig getreten wird! Zupfe vorsichtig an einem Blattstiel: Du siehst elastische, sehnige Fäden – die 'Panzer-Rippen', die dafür sorgen, dass das Blatt selbst unter schweren Stiefeln nicht zerreißt."
        },
        "game_adaptations": {
            "board_game": {
                "level_1": {
                    "level": 1,
                    "stage": "Junge bodennahe Rosette",
                    "light": 3,
                    "water": 2,
                    "root_space": 1,
                    "shoots": 1,
                    "trait": "Junge bodennahe Rosette",
                    "special_power": "Trittfeste Fugenrosette"
                },
                "level_2": {
                    "level": 2,
                    "stage": "Breite Rosette mit Blütenähren",
                    "light": 3,
                    "water": 2,
                    "root_space": 2,
                    "shoots": 2,
                    "trait": "Moos-Ersticker / Panzer-Gummiblatt",
                    "special_power": "Zähe Längsrippen federn Stiefel ab; wirft Dauerschatten auf Konkurrenten"
                },
                "network_affinities": {
                    "root_connection": True,
                    "fungal_connection": True,
                    "ant_connection": False,
                    "notes": "Nutzt kräftige Faserwurzeln zur Verankerung; bildet Mykorrhiza hinter Gehwegsteinen."
                }
            },
            "card_game": {
                "stats_0_10": {"wurzel": 5, "tritt": 9, "duerre": 6, "saat": 4, "tempo": 4, "chemie": 4, "total": 32},
                "signature_skills": [
                    {"name": "Trittplatte", "type": "Passiv", "condition": "Störung >= 7", "effect": "Verdoppelt TRITT bei starker Trittbelastung"},
                    {"name": "Sohlenfracht", "type": "Nutzen", "condition": "Passantenkontakt", "effect": "Klebrige Schleimsamen haften an Schuhsohlen und reisen in Nachbararenen"}
                ]
            }
        },
        "media": {
            "images": [
                {"filename": "breitwegerich-datenkarte.png", "type": "datenkarte", "title": "Botanische Datenkarte (Wurzelschnitt & Traits)"},
                {"filename": "breitwegerich-level-2.jpg", "type": "karte_level_2", "title": "Fugenduel Spielkarte Level 2: Breitwegerich"}
            ]
        }
    },
    {
        "id": "zimbelkraut",
        "folder": "zimbelkraut",
        "name": "Zimbelkraut",
        "scientific_name": "Cymbalaria muralis",
        "family": "Plantaginaceae (Wegerichgewächse)",
        "common_names": ["Zimbelkraut", "Mauer-Zimbelkraut", "Mauerblümchen", "Rittersporn der Armen", "Ivy-Leaved Toadflax"],
        "life_form": "Hemicryptophyt / Chamaephyt (Kriechtriebe an der Fugenwand)",
        "life_cycle": "Ausdauernd (Mehrjährig)",
        "botany": {
            "indicator_values": {
                "light": 6,
                "moisture": 4,
                "nutrients": 5,
                "soil_reaction": 7,
                "salinity": 0
            },
            "csr_strategy": {
                "c_percent": 37.3,
                "s_percent": 0.0,
                "r_percent": 62.7,
                "primary_class": "R / SR (Ruderal-Kletterer / Mauerfugen-Pionier)"
            },
            "morphology": {
                "height_min_m": 0.1,
                "height_max_m": 0.4,
                "growth_form": "Kriechend bis hängend, stielrunde rötliche Triebe mit efeuartig gelappten Blättern",
                "root_system": "Feine Adventivwurzeln an den Sprossknoten (Mörtelanker)",
                "max_root_depth_m": None,
                "root_radius_m": None,
                "bud_bank_size": 15.0
            },
            "phenology": {
                "flowering_period": "Mai bis September",
                "dispersal_mechanism": "Autochorie / Aktiver Negativer Phototropismus: Nach der Bestäubung wenden sich Fruchtstiele vom Licht ab und schieben die Samenkapseln aktiv tief in dunkle Fugenritzen!"
            },
            "sources": [
                {"name": "Pladias Database", "url": "https://pladias.cz/en/taxon/data/Cymbalaria%20muralis"},
                {"name": "UNDERPLOT v39 (IDIV)", "url": "https://doi.org/10.25829/idiv.3610-56acy9"}
            ]
        },
        "goodies": {
            "folk_names": ["Mauerblümchen", "Rittersporn der Armen", "Zymbelkraut", "Venushaar der Mauern"],
            "tradition_lore": "Ursprünglich im Mittelmeerraum auf Kalkfelsen beheimatet, wurde im 16. Jahrhundert mit Marmorstatuen nach Mitteleuropa eingeschleppt und eroberte als 'König der Burgmauern' ganz Europa.",
            "medicinal_uses": {
                "title": "Die historische Wundkompresse",
                "summary": "Früher zur Blutstillung bei Schnittwunden und als lindernde Auflage bei Hämorrhoiden und Hautentzündungen genutzt.",
                "preparation": "Frische Blätter zerdrücken und als Breiumschlag auf entzündete Hautpartien legen."
            },
            "culinary_uses": {
                "title": "Mauer-Kresse auf dem Pausenbrot",
                "summary": "Junge Blätter und Blüten haben einen herrlich würzigen, pfeffrig-säuerlichen Geschmack, der stark an Kresse oder Brunnenkresse erinnert. Hervorragend auf Butterbrot, in Salaten oder Kräuterquark.",
                "taste": "Pfeffrig, säuerlich, würzig wie Gartenkresse",
                "edibility": "Voll essbar (Blätter und Blüten roh)"
            },
            "active_compounds": [
                {"name": "Vitamin C", "effect": "Hoher Ascorbinsäuregehalt, stärkt die Immunabwehr."},
                {"name": "Flavonoide & Bitterstoffe", "effect": "Entzündungshemmend und adstringierend."},
                {"name": "Glykoside", "effect": "Sanfte antimikrobielle Oberflächenwirkung."}
            ],
            "game_healing_effect": {
                "name": "Wundverschluss & Mörtelnaht",
                "effect": "Verschließt aufgebrochene Fugen gegen Kahlfrost.",
                "description": "Schützt angeschlossene Nischen vor Frostschäden durch dichten Geflechtsteppich."
            },
            "street_discovery_tip": "Such an alten Backstein- oder Sandsteinmauern! Schau dir verblühte Stängel genau an: Während die Blüten der Sonne entgegenstreben, krümmen sich die verblühten Fruchtstiele um 180 Grad zurück und bohren ihre Kapsel wie ein kleiner Bohrer in den finstersten Mauerspalt."
        },
        "game_adaptations": {
            "board_game": {
                "level_1": {
                    "level": 1,
                    "stage": "Zarter Kriechtrieb",
                    "light": 2,
                    "water": 2,
                    "root_space": 1,
                    "shoots": 1,
                    "trait": "Zarter Kriechtrieb (sucht ersten Mörtelanker)",
                    "special_power": "Legt 1 Kriechtrasse in Nachbarslot"
                },
                "level_2": {
                    "level": 2,
                    "stage": "Etabliertes Polster mit Mauerrückzug",
                    "light": 2,
                    "water": 2,
                    "root_space": 2,
                    "shoots": 2,
                    "trait": "Samenkapseln in Mauerspalten",
                    "special_power": "Der Mauer-Rückzug (Kriechtrassen max. 3; negativer Phototropismus schützt Samen vor Vögeln)"
                },
                "network_affinities": {
                    "root_connection": True,
                    "fungal_connection": True,
                    "ant_connection": False,
                    "notes": "Hervorragender Trassenbauer: Kann im Spiel bis zu 3 Wurzel-/Kriechverbindungen legen!"
                }
            },
            "card_game": {
                "stats_0_10": {"wurzel": 4, "tritt": 3, "duerre": 6, "saat": 7, "tempo": 6, "chemie": 4, "total": 30},
                "signature_skills": [
                    {"name": "Mauer-Rückzug", "type": "Aktiv", "condition": "Vertikale Wand", "effect": "Fruchtstiele schieben Samen direkt in geschützte Risse; immun gegen Straßenkehrer"},
                    {"name": "Kriechspross", "type": "Passiv", "condition": "Kalkfuge", "effect": "Erhöht Ausbreitungsreichweite um +1 Nische"}
                ]
            }
        },
        "media": {
            "images": [
                {"filename": "zimbelkraut-level-1.jpg", "type": "karte_level_1", "title": "Fugenduel Spielkarte Level 1: Zimbelkraut"},
                {"filename": "zimbelkraut-level-2.jpg", "type": "karte_level_2", "title": "Fugenduel Spielkarte Level 2: Zimbelkraut"}
            ]
        }
    },
    {
        "id": "mauerraute",
        "folder": "mauerraute",
        "name": "Mauerraute",
        "scientific_name": "Asplenium ruta-muraria",
        "family": "Aspleniaceae (Streifelanfargewächse)",
        "common_names": ["Mauerraute", "Mauerstreifenfarn", "Steinfarn", "Mauer-Haarfarn", "Wall-Rue Fern"],
        "life_form": "Hemicryptophyt (Immergrüner Fels- und Mauerfarn)",
        "life_cycle": "Ausdauernd (Mehrjährig, langlebig bis 80-100 Jahre)",
        "botany": {
            "indicator_values": {
                "light": 8,
                "moisture": 3,
                "nutrients": 3,
                "soil_reaction": 8,
                "salinity": 0
            },
            "csr_strategy": {
                "c_percent": 12.6,
                "s_percent": 54.6,
                "r_percent": 32.8,
                "primary_class": "S (Stress-Tolerator / Extremer Fels- & Kalkspezialist)"
            },
            "morphology": {
                "height_min_m": 0.05,
                "height_max_m": 0.2,
                "growth_form": "Dichte Horste mit ledrigen, rautenförmig geteilten blaugrünen Wedeln",
                "root_system": "Kurz kriechendes, dicht beschupptes Rhizom mit drahtigen Felswurzeln",
                "max_root_depth_m": None,
                "root_radius_m": None,
                "bud_bank_size": 10.0
            },
            "phenology": {
                "flowering_period": "Sporenreife Juli bis September (Farn bildet Sporen, keine Blüten oder Samen!)",
                "dispersal_mechanism": "Anemochorie: Rund 10 Millionen mikroskopisch feine Sporen pro Pflanze und Jahr mit dem Wind"
            },
            "sources": [
                {"name": "Pladias Database", "url": "https://pladias.cz/en/taxon/data/Asplenium%20ruta-muraria"},
                {"name": "UNDERPLOT v39 (IDIV)", "url": "https://doi.org/10.25829/idiv.3610-56acy9"}
            ]
        },
        "goodies": {
            "folk_names": ["Mauerraute", "Steinfarn", "Mauer-Haarfarn", "Hustenfarn", "Rauten-Streifenfarn"],
            "tradition_lore": "Im Mittelalter hoch geschätztes Kraut der Klostermedizin. Wegen seiner rautenförmigen Blätter und seiner Unzerstörbarkeit auf sonnigen Burgmauern galt er als Symbol ewigen Lebens.",
            "medicinal_uses": {
                "title": "Das historische Lungen- und Hustenkraut",
                "summary": "Wurde früher als schleimlösender Tee gegen hartnäckigen Husten, Keuchhusten und Bronchitis sowie bei Milz- und Gelbsuchtleiden getrunken.",
                "preparation": "Getrocknete Wedel als Aufguss (Tee). Heute wegen Naturschutz an Naturfelsen nur noch historisch bedeutsam."
            },
            "culinary_uses": {
                "title": "Keine Speisepflanze",
                "summary": "Geschmacklich zäh, bitter und ungenießbar. Reine Heil-, Schutz- und Pionierpflanze.",
                "taste": "Bitter, adstringierend, zäh",
                "edibility": "Nicht giftig, aber ungenießbar"
            },
            "active_compounds": [
                {"name": "Gerbstoffe", "effect": "Stark adstringierend, gewebestraffend und antibakteriell."},
                {"name": "Schleimstoffe", "effect": "Reizlindernd auf die Atemwege."},
                {"name": "Flavonoide & Bitterstoffe", "effect": "Zellschützend vor UV-B-Strahlung auf sonnigen Mauerkronen."}
            ],
            "game_healing_effect": {
                "name": "Felsbalsam",
                "effect": "Schützt Nachbarpflanzen vor Pilzbefall.",
                "description": "Erzeugt durch basischen Kalkmörtel ein alkalisches Mikroklima, das schädliche Pilze hemmt."
            },
            "street_discovery_tip": "Such an alten Kirchen, Friedhofsmauern oder Brückenpfeilern nach Mauern mit weißem Kalkmörtel. Wenn du die Wedel im Hochsommer bei 35 Grad siehst, wirken sie oft braun und wie vertrocknet. Nach dem ersten Gewitterguss entfalten sie sich innerhalb weniger Stunden wieder saftig grün (Poikilohydrie)!"
        },
        "game_adaptations": {
            "board_game": {
                "level_1": {
                    "level": 1,
                    "stage": "Jungfarn im feuchten Spalt",
                    "light": 3,
                    "water": 1,
                    "root_space": 1,
                    "shoots": 1,
                    "trait": "Jungfarn im feuchten Spalt",
                    "special_power": "Keimt im feuchten Moosbett auf Kalkmörtel"
                },
                "level_2": {
                    "level": 2,
                    "stage": "Reife Wedel mit Sporenlagern",
                    "light": 3,
                    "water": 1,
                    "root_space": 1,
                    "shoots": 2,
                    "trait": "Reife Wedel mit Sporenlagern",
                    "special_power": "Austrocknungsstarre: Übersteht glühende Sommerhitze; immun gegen Sonnenbrand"
                },
                "network_affinities": {
                    "root_connection": True,
                    "fungal_connection": True,
                    "ant_connection": False,
                    "notes": "Gedeiht besonders auf Kalkmörtel (pH > 7.5); benötigt Moos-Patches als feuchtes Keimbett für Sporen."
                }
            },
            "card_game": {
                "stats_0_10": {"wurzel": 6, "tritt": 2, "duerre": 9, "saat": 4, "tempo": 2, "chemie": 5, "total": 28},
                "signature_skills": [
                    {"name": "Kalkanker", "type": "Passiv", "condition": "Kalkfuge", "effect": "+3 WURZEL in historischem Mörtel"},
                    {"name": "Austrocknungsstarre", "type": "Ultimate", "condition": "Dürre-Runde verloren", "effect": "Erholt sich nach Dürre sofort; kein Deckungsverlust unter 5%"}
                ]
            }
        },
        "media": {
            "images": [
                {"filename": "mauerraute-level-1.jpg", "type": "karte_level_1", "title": "Fugenduel Spielkarte Level 1: Mauerraute"}
            ]
        }
    },
    {
        "id": "schoellkraut",
        "folder": "schoellkraut",
        "name": "Schöllkraut",
        "scientific_name": "Chelidonium majus",
        "family": "Papaveraceae (Mohngewächse)",
        "common_names": ["Schöllkraut", "Warzenkraut", "Augenwurz", "Goldwurz", "Greater Celandine"],
        "life_form": "Hemicryptophyt (Kräftige Staude am Mauerfuß)",
        "life_cycle": "Ausdauernd (Mehrjährig)",
        "botany": {
            "indicator_values": {
                "light": 6,
                "moisture": 5,
                "nutrients": 8,
                "soil_reaction": 7,
                "salinity": 0
            },
            "csr_strategy": {
                "c_percent": 54.7,
                "s_percent": 6.6,
                "r_percent": 38.8,
                "primary_class": "CR (Competitor-Ruderal / Stickstoff-Gigant)"
            },
            "morphology": {
                "height_min_m": 0.3,
                "height_max_m": 0.9,
                "growth_form": "Verzweigte, behaarte Staude mit weichen gefiederten Blättern und leuchtend gelben Blüten",
                "root_system": "Kräftige Pfahlwurzel mit verzweigtem Wurzelstock; enthält leuchtend orangen Milchsaft",
                "max_root_depth_m": None,
                "root_radius_m": None,
                "bud_bank_size": 20.0
            },
            "phenology": {
                "flowering_period": "Mai bis September",
                "dispersal_mechanism": "Myrmekochorie (Ameisenausbreitung): Glänzend schwarze Samen tragen ein saftiges, fett- und eiweißreiches Anhängsel (Elaiosom), das Ameisen als Larvenfutter in ihre Nester tragen!"
            },
            "sources": [
                {"name": "Pladias Database", "url": "https://pladias.cz/en/taxon/data/Chelidonium%20majus"},
                {"name": "UNDERPLOT v39 (IDIV)", "url": "https://doi.org/10.25829/idiv.3610-56acy9"}
            ]
        },
        "goodies": {
            "folk_names": ["Warzenkraut", "Augenwurz", "Goldwurz", "Schwalbenkraut", "Herrgottsgabe"],
            "tradition_lore": "Schon von den alten Griechen beschrieben; der Name Chelidonium leitet sich von 'chelidon' (griechisch für Schwalbe) ab, weil es blüht, wenn die Schwalben kommen, und vergeht, wenn sie ziehen.",
            "medicinal_uses": {
                "title": "Der Kiez-Warzen-Killer",
                "summary": "Der leuchtend orangene Milchsaft ist ein uraltes Hausmittel gegen Warzen. Punktuell aufgetragen lösen die Enzyme und Alkaloide das verhornte Warzengewebe auf.",
                "preparation": "Einen Stängel abbrechen und den austretenden orangen Saft tropfenweise punktuell auf die Warze tupfen. VORSICHT: Giftig beim Verschlucken, nicht in die Augen reiben!"
            },
            "culinary_uses": {
                "title": "Giftpflanze — Nicht essbar!",
                "summary": "Vollständig ungenießbar und giftig. Schmeckt extrem bitter und brennend scharf.",
                "taste": "Bitter, scharf, reizend",
                "edibility": "Giftig! Reine Heil- und Schutzkraft."
            },
            "active_compounds": [
                {"name": "Chelidonin & Coptisin", "effect": "Isochinolin-Alkaloide mit antiviraler, schmerzlindernder und krampflösender Wirkung."},
                {"name": "Proteolytische Enzyme", "effect": "Eiweißabbauende Enzyme im Milchsaft, die Warzengewebe zerstören."},
                {"name": "Flavonoide & Saponine", "effect": "Antioxidativ und pilzhemmend."}
            ],
            "game_healing_effect": {
                "name": "Ätzmilch",
                "effect": "Vertreibt Schnecken und Schädlinge; neutralisiert feindliche Angriffe.",
                "description": "Schützt die eigene Nische durch chemische Abwehrstoffe vor Fraßfeinden."
            },
            "street_discovery_tip": "Such an schattigen Hauswänden, Mauersockeln oder unter Zäunen, wo Tauben oder Hunde für viel Stickstoff sorgen. Brich vorsichtig ein Blatt ab: Es tritt sofort ein intensiv orangeroter Saft aus, der wie Jod aussieht!"
        },
        "game_adaptations": {
            "board_game": {
                "level_1": {
                    "level": 1,
                    "stage": "Junger krautiger Trieb",
                    "light": 2,
                    "water": 2,
                    "root_space": 2,
                    "shoots": 1,
                    "trait": "Junger krautiger Trieb",
                    "special_power": "Explosives Wachstum auf Stickstofffeldern (Guano +2)"
                },
                "level_2": {
                    "level": 2,
                    "stage": "Reife Samen mit Ameisenbrot",
                    "light": 2,
                    "water": 2,
                    "root_space": 3,
                    "shoots": 3,
                    "trait": "Reife Samen mit Ameisenbrot",
                    "special_power": "Ameisen-Express: Elaiosomen locken Ameisenstraßen an; garantiert Samenfahrt im Herbst"
                },
                "network_affinities": {
                    "root_connection": True,
                    "fungal_connection": True,
                    "ant_connection": True,
                    "notes": "Beste Ameisen-Partnerin im Spiel! Bildet kräftige Wurzeln und hohe Nährstoffansprüche (N 8)."
                }
            },
            "card_game": {
                "stats_0_10": {"wurzel": 5, "tritt": 4, "duerre": 4, "saat": 6, "tempo": 5, "chemie": 9, "total": 33},
                "signature_skills": [
                    {"name": "Milchröhren", "type": "Aktiv", "condition": "Angriff", "effect": "CHEMIE +2 für eine Runde; senkt gegnerische Chemie"},
                    {"name": "Ameisenpost", "type": "Passiv", "condition": "Herbst", "effect": "Samen mit Elaiosomen werden kostenlos 1 Zone weitergetragen"}
                ]
            }
        },
        "media": {
            "images": []
        }
    },
    {
        "id": "behaartes-schaumkraut",
        "folder": "behaartes-schaumkraut",
        "name": "Behaartes Schaumkraut",
        "scientific_name": "Cardamine hirsuta",
        "family": "Brassicaceae (Kreuzblütler)",
        "common_names": ["Behaartes Schaumkraut", "Spring-Schaumkraut", "Springkresse", "Winterkresse", "Gartenschaumkraut", "Hairy Bittercress"],
        "life_form": "Therophyt (Einjährige bis winterannuelle Pflanze)",
        "life_cycle": "Einjährig (extrem schneller Lebenszyklus von nur 4 bis 6 Wochen)",
        "botany": {
            "indicator_values": {
                "light": 6,
                "moisture": 5,
                "nutrients": 6,
                "soil_reaction": 6,
                "salinity": 0
            },
            "csr_strategy": {
                "c_percent": 22.5,
                "s_percent": 0.0,
                "r_percent": 77.5,
                "primary_class": "R (Ruderal / Opportunistischer Schnellstarter)"
            },
            "morphology": {
                "height_min_m": 0.1,
                "height_max_m": 0.25,
                "growth_form": "Zierliche Grundrosette mit gefiederten Blättern und aufrechten Blütenstängeln",
                "root_system": "Feine, zarte Pfahl- und Faserwurzeln",
                "max_root_depth_m": 0.37,
                "root_radius_m": 0.155,
                "bud_bank_size": 2.5
            },
            "phenology": {
                "flowering_period": "April bis Juni (bei mildem Wetter schon ab Januar/Februar bis zum Winterfrost)",
                "dispersal_mechanism": "Ballochorie (Schleuderfrucht): Bei Berührung oder Reife rollen sich die Fruchtklappen explosionsartig spiralförmig auf und katapultieren die Samen bis zu 2 Meter weit!"
            },
            "sources": [
                {"name": "Pladias Database", "url": "https://pladias.cz/en/taxon/data/Cardamine%20hirsuta"},
                {"name": "UNDERPLOT v39 (IDIV)", "url": "https://doi.org/10.25829/idiv.3610-56acy9"}
            ]
        },
        "goodies": {
            "folk_names": ["Springkresse", "Winterkresse", "Viermänniges Schaumkraut", "Katapultkraut"],
            "tradition_lore": "Gärtner fürchten es wegen seiner Schleuderkraft, aber Feinschmecker und Kräuterkundige lieben es als das früheste frische Frühlingsgewürz des Jahres, das oft schon im Februar unter dem Schnee hervorspitzt.",
            "medicinal_uses": {
                "title": "Frühjahrs-Vitamingift & Immun-Kick",
                "summary": "Enthält reichlich Vitamin C und scharfe Senfölglykoside, die traditionell bei Frühjahrsmüdigkeit und zur Blutreinigung nach dem Winter gegessen wurden.",
                "preparation": "Frisch gepflückt als Kraut roh essen oder fein gehackt auf Quark und Salate streuen."
            },
            "culinary_uses": {
                "title": "Das beste wilde Straßen-Gewürz",
                "summary": "Schmeckt herrlich knackig, saftig und angenehm scharf wie beste Brunnenkresse, Wasabi oder Radieschen. Ein echter Delikatessen-Snack auf dem Butterbrot!",
                "taste": "Knackig, scharf-würzig wie Gartenkresse oder Rettich",
                "edibility": "Voll essbar (Rosettenblätter, Blüten und unreife Schoten)"
            },
            "active_compounds": [
                {"name": "Glucosinolate (Senföle)", "effect": "Scharfe Schwefelverbindungen mit natürlicher antibiotischer und antibakterieller Schutzwirkung."},
                {"name": "Vitamin C (Ascorbinsäure)", "effect": "Stärkt das Immunsystem und die körpereigenen Abwehrkräfte."},
                {"name": "Bitterstoffe", "effect": "Fördern Verdauung und Magensaftsekretion."}
            ],
            "game_healing_effect": {
                "name": "Frühjahrs-Kick",
                "effect": "Schaltet im ersten Frühlingsmonat sofortige Keimung frei.",
                "description": "Keimt bereits beim ersten Tauwetter und besetzt freie Nischen, bevor Konkurrenten erwachen."
            },
            "street_discovery_tip": "Such im Vorfrühling in Fugen vor Haustüren oder an Mauern. Streife mit dem Finger vorsichtig über die reifen aufrechten Schoten: Mit einem leisen 'Plopp' spürst du kleine Samengeschosse gegen deine Fingerspitzen fliegen!"
        },
        "game_adaptations": {
            "board_game": {
                "level_1": {
                    "level": 1,
                    "stage": "Kleine Blattrosette",
                    "light": 2,
                    "water": 2,
                    "root_space": 1,
                    "shoots": 1,
                    "trait": "Kleine Blattrosette",
                    "special_power": "Frühstarter: Keimt bei mildem Winterwetter sofort"
                },
                "level_2": {
                    "level": 2,
                    "stage": "Reife Schoten schleudern Samen",
                    "light": 2,
                    "water": 2,
                    "root_space": 1,
                    "shoots": 1,
                    "trait": "Reife Schoten schleudern Samen",
                    "special_power": "Samen-Katapult: Schleudert Samen bei Störung bis zu 2 Slots weit!"
                },
                "network_affinities": {
                    "root_connection": True,
                    "fungal_connection": False,
                    "ant_connection": False,
                    "notes": "PILZ-SPERRE! Als Kreuzblütler sondert es Senföle ab, die Pilzmyzel zersetzen. Kann nicht an Pilzstreifen angeschlossen werden!"
                }
            },
            "card_game": {
                "stats_0_10": {"wurzel": 3, "tritt": 4, "duerre": 3, "saat": 8, "tempo": 9, "chemie": 5, "total": 32},
                "signature_skills": [
                    {"name": "Schleudersitz", "type": "Reaktion", "condition": "Bei Niederlage", "effect": "Schleudert bei Vernichtung sofort Samen in zwei Nachbararenen"},
                    {"name": "Senföl-Barriere", "type": "Passiv", "condition": "Permanent", "effect": "Zerstört gegnerische Pilzverbindungen an dieser Nische"}
                ]
            }
        },
        "media": {
            "images": []
        }
    },
    {
        "id": "sommer-portulak",
        "folder": "sommer-portulak",
        "name": "Sommer-Portulak",
        "scientific_name": "Portulaca oleracea",
        "family": "Portulacaceae (Portulakgewächse)",
        "common_names": ["Sommer-Portulak", "Gemüse-Portulak", "Bürzelkraut", "Kreta-Superfood", "Common Purslane"],
        "life_form": "Therophyt (Einjährige sukkulente Wärmepflanze)",
        "life_cycle": "Einjährig (Spätkeimer, liebt glühende Hitze)",
        "botany": {
            "indicator_values": {
                "light": 8,
                "moisture": 4,
                "nutrients": 7,
                "soil_reaction": 7,
                "salinity": 1
            },
            "csr_strategy": {
                "c_percent": 0.3,
                "s_percent": 0.0,
                "r_percent": 99.7,
                "primary_class": "R (Extremer Ruderal-Überlebenskünstler / Hitze-Sukkulente)"
            },
            "morphology": {
                "height_min_m": 0.05,
                "height_max_m": 0.3,
                "growth_form": "Niederliegend ausgebreitete, fleischig verdickte rötliche Stängel mit spatelförmigen Blättern",
                "root_system": "Tiefreichende Pfahlwurzel mit verzweigten Saugwurzeln",
                "max_root_depth_m": 0.25,
                "root_radius_m": 0.12,
                "bud_bank_size": 1.2
            },
            "phenology": {
                "flowering_period": "Juni bis Oktober (kleine gelbe Blüten öffnen sich nur an sonnigen Vormittagen)",
                "dispersal_mechanism": "Autochorie / Endozoochorie: Deckelkapseln ('Pyxidium') öffnen sich wie ein Dosendeckel und streuen hunderte winzige schwarze Glanzsamen aus"
            },
            "sources": [
                {"name": "Pladias Database", "url": "https://pladias.cz/en/taxon/data/Portulaca%20oleracea"},
                {"name": "UNDERPLOT v39 (IDIV)", "url": "https://doi.org/10.25829/idiv.3610-56acy9"}
            ]
        },
        "goodies": {
            "folk_names": ["Bürzelkraut", "Saubürzel", "Kreta-Superfood", "Sommergemüse", "Fettkraut"],
            "tradition_lore": "Im antiken Ägypten, Griechenland und Rom hochgeschätztes Kulturgemüse. Bestandteil der berühmten Kreta-Diät, die für Herzgesundheit und Langlebigkeit steht.",
            "medicinal_uses": {
                "title": "Herz- und Zellschutz der Wüste",
                "summary": "Kühlt entzündete Haut und Magenschleimhäute, senkt Blutfette und schützt die Zellen vor oxidativem Stress.",
                "preparation": "Frische fleischige Blätter kauen oder als kühlenden Saft auf leichten Sonnenbrand auftragen."
            },
            "culinary_uses": {
                "title": "Echtes Gourmet-Gemüse",
                "summary": "Die saftigen, knackigen Blätter schmecken herrlich erfrischend säuerlich, leicht nussig und mild salzig. Perfekt in griechischen Sommersalaten, Gazpacho oder kurz in Olivenöl geschwenkt.",
                "taste": "Knackig, saftig, erfrischend säuerlich-salzig",
                "edibility": "Hervorragend essbar (Blätter und Triebe roh oder gedünstet)"
            },
            "active_compounds": [
                {"name": "Omega-3-Fettsäuren (ALA)", "effect": "Höchster Gehalt an Alpha-Linolensäure unter allen bekannten grünen Landpflanzen!"},
                {"name": "Glutathion & Betalaine", "effect": "Mächtige Antioxidantien für den Zellschutz bei extremer UV-Strahlung."},
                {"name": "Magnesium & Kalium", "effect": "Wertvolle Elektrolyte, die Wasser im Pflanzengewebe binden."}
            ],
            "game_healing_effect": {
                "name": "Power-Snack",
                "effect": "Spendet +1 Energie im heißen Hochsommer.",
                "description": "Erfrischt Mitspieler bei Hitzewellen durch saftige Wasserspeicherung."
            },
            "street_discovery_tip": "Such im Juli und August auf glühend heißen Asphaltparkplätzen oder an Süd-Gehsteigen! Wenn alle Gräser gelb und verdorrt sind, leuchtet der Portulak als sattgrüner, praller Fleischteppich direkt auf dem kochenden Pflaster."
        },
        "game_adaptations": {
            "board_game": {
                "level_1": {
                    "level": 1,
                    "stage": "Junge sukkulente Pflanze",
                    "light": 3,
                    "water": 2,
                    "root_space": 1,
                    "shoots": 1,
                    "trait": "Junge sukkulente Pflanze",
                    "special_power": "Hitzeschild: Immun gegen Austrocknung bei voller Sonne"
                },
                "level_2": {
                    "level": 2,
                    "stage": "Reife Pflanze mit gelben Blüten",
                    "light": 3,
                    "water": 2,
                    "root_space": 1,
                    "shoots": 3,
                    "trait": "Reife Pflanze mit gelben Blüten",
                    "special_power": "C4/CAM-Turbo: Schaltet bei über 35 °C auf Wüstenstoffwechsel um und wächst weiter!"
                },
                "network_affinities": {
                    "root_connection": True,
                    "fungal_connection": False,
                    "ant_connection": False,
                    "notes": "Extremer Flachwurzler (Wurzelraum 1); bildet keine typische Mykorrhiza auf trockenem Asphalt."
                }
            },
            "card_game": {
                "stats_0_10": {"wurzel": 4, "tritt": 4, "duerre": 10, "saat": 7, "tempo": 6, "chemie": 4, "total": 35},
                "signature_skills": [
                    {"name": "C4-Turbo", "type": "Passiv", "condition": "Hitze > 35°C", "effect": "+6 DÜRRE in glühenden Sommerrunden"},
                    {"name": "Fleischblatt-Schild", "type": "Verteidigung", "condition": "Dürre-Welle", "effect": "Halbiert Deckungsverlust durch Hitzestress"}
                ]
            }
        },
        "media": {
            "images": []
        }
    },
    {
        "id": "einjaehriges-rispengras",
        "folder": "einjaehriges-rispengras",
        "name": "Einjähriges Rispengras",
        "scientific_name": "Poa annua",
        "family": "Poaceae (Süßgräser)",
        "common_names": ["Einjähriges Rispengras", "Vogelgras", "Gänsefutter", "Straßengras", "Annual Meadow Grass"],
        "life_form": "Therophyt / Hemicryptophyt (Flacher rasenbildender Kosmopolit)",
        "life_cycle": "Einjährig bis kurzlebig mehrjährig (Ganzjahresblüher)",
        "botany": {
            "indicator_values": {
                "light": 7,
                "moisture": 6,
                "nutrients": 8,
                "soil_reaction": 6,
                "salinity": 1
            },
            "csr_strategy": {
                "c_percent": 6.8,
                "s_percent": 35.0,
                "r_percent": 58.2,
                "primary_class": "R / SR (Ruderaler Schnellstarter & Tritt-Tolerator)"
            },
            "morphology": {
                "height_min_m": 0.05,
                "height_max_m": 0.25,
                "growth_form": "Kleine, hellgrüne Horste mit charakteristisch kahnförmigen Blattspitzen",
                "root_system": "Dichtes, aber sehr flaches Faserwurzelgeflecht",
                "max_root_depth_m": 0.17,
                "root_radius_m": 0.11,
                "bud_bank_size": 4.2
            },
            "phenology": {
                "flowering_period": "Januar bis Dezember (blüht und fruchtet 12 Monate im Jahr bei Plustemperaturen!)",
                "dispersal_mechanism": "Anemochorie / Anthropochorie: Unzählige winzige Ährchen reifen in nur 45 Tagen vom Samen zum neuen Samen"
            },
            "sources": [
                {"name": "Pladias Database", "url": "https://pladias.cz/en/taxon/data/Poa%20annua"},
                {"name": "UNDERPLOT v39 (IDIV)", "url": "https://doi.org/10.25829/idiv.3610-56acy9"}
            ]
        },
        "goodies": {
            "folk_names": ["Vogelgras", "Gänsefutter", "Pflastergras", "Allerweltsgras"],
            "tradition_lore": "Das wohl am weitesten verbreitete Gras der Erde. Es wächst sogar in Forschungsstationen der Antarktis und übersteht selbst ständige Rasenmäher und Tritte.",
            "medicinal_uses": {
                "title": "Notverband & Polstermaterial",
                "summary": "Historisch wurden saubere getrocknete Grasfasern als saugfähiges Polstermaterial für Wundverbände oder in Schuhen gegen Kälte genutzt.",
                "preparation": "Getrocknete Halme als saugfähiges Füllmaterial."
            },
            "culinary_uses": {
                "title": "Stadtvogel-Futterbar",
                "summary": "Für Menschen faserig und ungenießbar, aber für Haussperlinge, Tauben, Meisen und Kaninchen die unverzichtbare Grundnahrung in der Betonwüste.",
                "taste": "Grasig, faserig, süßlich",
                "edibility": "Nicht giftig, aber für Menschen zu zäh. Perfekt für Tiere!"
            },
            "active_compounds": [
                {"name": "Kieselsäure", "effect": "Macht die Grashalme elastisch und trittfest."},
                {"name": "Pflanzliche Proteine & Stärke", "effect": "Energiereiche Nahrung für Vögel in den Samen."},
                {"name": "Zellulose", "effect": "Dichte Faserstruktur für Bodenbindung."}
            ],
            "game_healing_effect": {
                "name": "Vogellocke",
                "effect": "Lockt Stadtvögel an, die Schädlinge und Raupen fressen.",
                "description": "Schützt Nachbarpflanzen vor Insektenfraß."
            },
            "street_discovery_tip": "Streiche über die Spitze eines Grashalms: Drücke die Blattspitze sanft zusammen – sie sieht aus wie der Bug eines kleinen Kanus oder Ruderboots ('kahnförmige Blattspitze'). Das ist das Erkennungszeichen aller Rispengräser!"
        },
        "game_adaptations": {
            "board_game": {
                "level_1": {
                    "level": 1,
                    "stage": "Junger Grasbüschel",
                    "light": 3,
                    "water": 2,
                    "root_space": 1,
                    "shoots": 1,
                    "trait": "Junger Grasbüschel",
                    "special_power": "Trittfest: Nimmt keinen Schaden durch Passanten"
                },
                "level_2": {
                    "level": 2,
                    "stage": "Lockere Rispen mit Ährchen",
                    "light": 3,
                    "water": 2,
                    "root_space": 1,
                    "shoots": 2,
                    "trait": "Lockere Rispen mit Ährchen",
                    "special_power": "Dauerblüte: Produziert in allen Jahreszeiten kontinuierlich neue Triebe"
                },
                "network_affinities": {
                    "root_connection": True,
                    "fungal_connection": True,
                    "ant_connection": False,
                    "notes": "Sehr flacher Wurzelraum (0.17 m); teilt Wasser über Pilzfäden im Sockelbereich."
                }
            },
            "card_game": {
                "stats_0_10": {"wurzel": 3, "tritt": 6, "duerre": 4, "saat": 8, "tempo": 10, "chemie": 3, "total": 34},
                "signature_skills": [
                    {"name": "Dauerblüte", "type": "Priorität", "condition": "Gleichstand", "effect": "Gewinnt jeden Initiativ-Gleichstand; blüht 12 Monate im Jahr"},
                    {"name": "Samenregen", "type": "Passiv", "condition": "Rundenende", "effect": "Füllt die eigene Samenbank in jeder Runde mit 1 neuem Samen"}
                ]
            }
        },
        "media": {
            "images": []
        }
    },
    {
        "id": "silber-birnmoos",
        "folder": "silber-birnmoos",
        "name": "Silber-Birnmoos",
        "scientific_name": "Bryum argenteum",
        "family": "Bryaceae (Birnmoosgewächse)",
        "common_names": ["Silber-Birnmoos", "Silbermoos", "Silberfilz", "Wundmoos", "Silver Moss"],
        "life_form": "Bryophyt (Poikilohydres Polstermoos)",
        "life_cycle": "Ausdauernd (Mehrjährig, extrem regenerationsfähig)",
        "botany": {
            "indicator_values": {
                "light": 7,
                "moisture": 4,
                "nutrients": 6,
                "soil_reaction": 7,
                "salinity": 1
            },
            "csr_strategy": {
                "c_percent": 0.0,
                "s_percent": 80.0,
                "r_percent": 20.0,
                "primary_class": "S (Extremer Stress-Tolerator / Trockenkünstler)"
            },
            "morphology": {
                "height_min_m": 0.005,
                "height_max_m": 0.02,
                "growth_form": "Dichte, silbrig schimmernde Polster mit dachziegelartig anliegenden Blättchen",
                "root_system": "Keine echten Wurzeln! Feine braune Rhizoide zur rein mechanischen Verankerung",
                "max_root_depth_m": 0.0,
                "root_radius_m": 0.0,
                "bud_bank_size": None
            },
            "phenology": {
                "flowering_period": "Sporenkapseln im Herbst bis Frühjahr (Moos bildet Sporen auf rötlichen Kapselstielen, keine Blüten!)",
                "dispersal_mechanism": "Anemochorie & vegetative Fragmentation: Jeder winzige Polsterfetzen kann durch Wind, Schuhe oder Regen eine neue Kolonie begründen"
            },
            "sources": [
                {"name": "British Bryological Society", "url": "https://www.britishbryologicalsociety.org.uk/learning/species-finder/bryum-argenteum/"},
                {"name": "BBS Field Guide", "url": "https://www.britishbryologicalsociety.org.uk"}
            ]
        },
        "goodies": {
            "folk_names": ["Silbermoos", "Silberfilz", "Wundmoos", "Gehweg-Polster"],
            "tradition_lore": "Wegen seines silbrigen Glanzes unverwechselbar. Seine farblosen, chlorophyllfreien Blattspitzen reflektieren das grelle Sonnenlicht wie winzige Sonnenspiegel.",
            "medicinal_uses": {
                "title": "Antibakterielle Wundwatte",
                "summary": "Moose wurden seit der Steinzeit und bis in den Ersten Weltkrieg als saugfähiges, steriles Wundpolstermaterial verwendet, da sie das Zehnfache ihres Trockengewichts an Feuchtigkeit aufsaugen und Bakterienwachstum hemmen.",
                "preparation": "Historisch getrocknet und gereinigt als Wundauflage."
            },
            "culinary_uses": {
                "title": "Nicht essbar",
                "summary": "Kein Nahrungsmittel für Menschen. Spielt aber eine gigantische Rolle als Wasserspeicher und Ammenpflanze für alle anderen Arten.",
                "taste": "Erdig, bitter",
                "edibility": "Ungenießbar"
            },
            "active_compounds": [
                {"name": "Phenolische Säuren", "effect": "Hemmen das Wachstum von Bakterien und Schimmelpilzen."},
                {"name": "Antimikrobielle Terpene", "effect": "Natürlicher Schutz vor Verwesung und Verrottung."},
                {"name": "Flavonoide in den Blattspitzen", "effect": "Wirken als UV-Schild gegen extreme Sonnenstrahlung."}
            ],
            "game_healing_effect": {
                "name": "Feuchtverband",
                "effect": "Versorgt trockene Sämlinge tagelang mit Feuchtigkeit.",
                "description": "Dient als Ammen-Plättchen, speichert +1 Wasser und senkt Hitzeschaden."
            },
            "street_discovery_tip": "Geh an einem sonnigen Tag über Pflastersteine und schau schräg gegen das Licht: Du siehst kleine, silbrig glänzende Samtkissen zwischen den Ziegeln glitzern. Wenn du einen Tropfen Wasser aus deiner Trinkflasche darauf gibst, wird das Silberkissen innerhalb von 30 Sekunden smaragdgrün!"
        },
        "game_adaptations": {
            "board_game": {
                "level_1": {
                    "level": 1,
                    "stage": "Junge Mooskolonie",
                    "light": "1–3",
                    "water": 1,
                    "root_space": 0,
                    "shoots": 1,
                    "trait": "Junge Mooskolonie",
                    "special_power": "Besenschutz: Durch flachen Wuchs vollkommen immun gegen Straßenbesen"
                },
                "level_2": {
                    "level": 2,
                    "stage": "Dichtes Polster mit Sporenkapseln",
                    "light": "1–3",
                    "water": 1,
                    "root_space": 0,
                    "shoots": 2,
                    "trait": "Dichtes Polster mit Sporenkapseln",
                    "special_power": "Ammenfunktion: Spendet +1 Feuchtigkeit für alle Keimlinge im selben Slot"
                },
                "network_affinities": {
                    "root_connection": False,
                    "fungal_connection": False,
                    "ant_connection": False,
                    "notes": "Besitzt Rhizoide statt Wurzeln (Wurzelraum 0); fungiert als Oberflächen-Plättchen (Moos-Patch)."
                }
            },
            "card_game": {
                "stats_0_10": {"wurzel": 3, "tritt": 5, "duerre": 10, "saat": 3, "tempo": 2, "chemie": 4, "total": 27},
                "signature_skills": [
                    {"name": "Poikilohydrie", "type": "Passiv", "condition": "Dürre", "effect": "Verliert bei 0% Feuchtigkeit keine Lebenskraft; fällt in schadlose Trockenstarre"},
                    {"name": "Ammenbett", "type": "Unterstützung", "condition": "Nachbarkeimung", "effect": "+1 Lebenskraft für jeden neuen Keimling"}
                ]
            }
        },
        "media": {
            "images": []
        }
    },
    {
        "id": "loewenzahn",
        "folder": "loewenzahn",
        "name": "Gewöhnlicher Löwenzahn",
        "scientific_name": "Taraxacum officinale",
        "family": "Asteraceae (Korbblütler)",
        "common_names": ["Gewöhnlicher Löwenzahn", "Pusteblume", "Butterblume", "Kuhblume", "Common Dandelion"],
        "life_form": "Hemicryptophyt (Kräftige Rosette mit Pfahlwurzel)",
        "life_cycle": "Ausdauernd (Mehrjährig)",
        "botany": {
            "indicator_values": {
                "light": 7,
                "moisture": 5,
                "nutrients": 6,
                "soil_reaction": 7,
                "salinity": 0
            },
            "csr_strategy": {
                "c_percent": 45.0,
                "s_percent": 5.0,
                "r_percent": 50.0,
                "primary_class": "RC (Ruderal-Competitor / Zäher Allrounder)"
            },
            "morphology": {
                "height_min_m": 0.1,
                "height_max_m": 0.4,
                "growth_form": "Grundständige Blattrosette mit scharf gezähnten Blättern und hohlen Blütenstandsschäften",
                "root_system": "Fleischige, bis zu 1 bis 2 Meter tiefe Pfahlwurzel; regeneriert aus kleinsten Fragmenten",
                "max_root_depth_m": 1.0,
                "root_radius_m": 0.35,
                "bud_bank_size": 20.0
            },
            "phenology": {
                "flowering_period": "März bis November (Hauptblüte im April/Mai)",
                "dispersal_mechanism": "Anemochorie: Fallschirmchen (Pappus) tragen rund 5.000 Flugsamen pro Pflanze bis zu mehrere Kilometer weit!"
            },
            "sources": [
                {"name": "Pladias Database", "url": "https://pladias.cz/en/taxon/data/Taraxacum%20sect.%20Taraxacum"},
                {"name": "UNDERPLOT v39 / TRY DB", "url": "https://doi.org/10.25829/idiv.3610-56acy9"}
            ]
        },
        "goodies": {
            "folk_names": ["Pusteblume", "Kuhblume", "Butterblume", "Märzenbecher", "Piss-en-lit", "Röhrliblüemli"],
            "tradition_lore": "Der Inbegriff des urbanen Überlebenskünstlers: Er sprengt buchstäblich Teerbeläge und Betonplatten auf. In Frankreich als 'Piss-en-lit' bekannt wegen seiner stark harntreibenden Wirkung.",
            "medicinal_uses": {
                "title": "Der Kiez-Stoffwechsel-Booster",
                "summary": "Die enthaltenen Bitterstoffe regen Leber, Galle und Bauchspeicheldrüse an, reinigen das Blut und wirken harntreibend.",
                "preparation": "Junge Blätter im Frühjahr als Entschlackungssalat; getrocknete Wurzeln als reinigender Lebertee oder geröstet als koffeinfreier Löwenzahn-Kaffee."
            },
            "culinary_uses": {
                "title": "Delikatessen-Salat & Löwenzahn-Honig",
                "summary": "Junge Blätter vor der Blüte schmecken herb-würzig und aromatisch. Die sonnengelben Blütenköpfe werden mit Zitrone und Zucker zu goldgelbem 'Löwenzahn-Honig' eingekocht.",
                "taste": "Herb-würzig, zartbitter, nussig",
                "edibility": "Vollständig essbar (Blätter, Blüten, Knospen und Wurzeln)"
            },
            "active_compounds": [
                {"name": "Taraxacin (Bitterstoffe)", "effect": "Fördert die Verdauungssäfte und kurbelt den Gallenfluss an."},
                {"name": "Inulin", "effect": "Präbiotischer Ballaststoff in der Wurzel (bis zu 40 % im Herbst!), nährt gesunde Darmbakterien."},
                {"name": "Cholin & Kalium", "effect": "Leberstärkend und natürlicher Elektrolytausgleich."}
            ],
            "game_healing_effect": {
                "name": "Wurzel-Regeneration",
                "effect": "Regeneriert selbst nach Zerstörung aus verbliebenen Wurzelfragmenten.",
                "description": "Erlaubt ein Wiederauferstehen in derselben Nische im nächsten Frühjahr."
            },
            "street_discovery_tip": "Puste auf eine reife Pusteblume: Jeder einzelne Fallschirm (Pappus) trägt genau einen Samen. Die winzigen Federchen erzeugen bei der leisesten Brise einen Mini-Wirbelsturm über dem Schirm, der ihn wie einen Heißluftballon hunderte Meter über Straßen und Häuserblöcke segeln lässt."
        },
        "game_adaptations": {
            "board_game": {
                "level_1": {
                    "level": 1,
                    "stage": "Junge Pfahlwurzel-Rosette",
                    "light": 3,
                    "water": 2,
                    "root_space": 2,
                    "shoots": 1,
                    "trait": "Pfahlwurzelbohrer",
                    "special_power": "Tiefwurzler: Erschließt Wasser aus tiefen Erdklüften"
                },
                "level_2": {
                    "level": 2,
                    "stage": "Ausgewachsene Blattrosette mit Pusteblume",
                    "light": 3,
                    "water": 2,
                    "root_space": 3,
                    "shoots": 2,
                    "trait": "Fallschirmwolke & Samenbank",
                    "special_power": "Pappus-Schwarm: Sendet Flugsamen über das gesamte Spielbrett"
                },
                "network_affinities": {
                    "root_connection": True,
                    "fungal_connection": True,
                    "ant_connection": False,
                    "notes": "Pfahlwurzler mit starker Tiefenwirkung; sprengt verdichteten Untergrund auf."
                }
            },
            "card_game": {
                "stats_0_10": {"wurzel": 5, "tritt": 5, "duerre": 5, "saat": 6, "tempo": 7, "chemie": 4, "total": 32},
                "signature_skills": [
                    {"name": "Fallschirmwolke", "type": "Aktiv", "condition": "Rundensieg", "effect": "+2% Coverage durch weitreichenden Samenausstoß"},
                    {"name": "Pfahlwurzelbohrer", "type": "Passiv", "condition": "Zerstörung", "effect": "Halbiert Deckungsverlust bei Wurzelstress und regeneriert"}
                ]
            }
        },
        "media": {
            "images": []
        }
    }
]

def make_markdown_dossier(p):
    b = p["botany"]
    g = p["goodies"]
    ga = p["game_adaptations"]
    m = p["media"]
    iv = b["indicator_values"]
    csr = b["csr_strategy"]
    morph = b["morphology"]
    pheno = b["phenology"]
    bg = ga["board_game"]
    cg = ga["card_game"]

    md = f"""# {p['name']} (*{p['scientific_name']}*)

> **Familie:** {p['family']}  
> **Lebensform:** {p['life_form']}  
> **Lebenszyklus:** {p['life_cycle']}  
> **Volksmund:** {', '.join(p['common_names'])}

---

## 📸 Bildübersicht & Spielkarten

"""
    if m["images"]:
        for img in m["images"]:
            md += f"### {img['title']}\n\n![{img['title']}](bilder/{img['filename']})\n\n"
    else:
        md += "*Für diese Art sind noch keine finalen Bildkarten im Ordner hinterlegt. Die exakten Prompts zur Generierung von Level 1 und Level 2 befinden sich am Ende dieser Akte und in `prompts.txt`.*\n\n"

    md += f"""---

## 🌿 1. Echte botanische Daten (Wissenschaftliche Basis)

Diese Daten stammen aus empirischen botanischen Datenbanken (**Pladias**, **UNDERPLOT v39**) und bilden das unveränderliche wissenschaftliche Fundament dieser Pflanze.

### Standort-Zeigerwerte (Ellenberg / Pladias)
* ☀️ **Lichtzahl (L):** `{iv['light']}` / 9
* 💧 **Feuchtezahl (F):** `{iv['moisture']}` / 9
* 🧪 **Reaktionszahl / Kalk (R):** `{iv['soil_reaction']}` / 9
* 🥩 **Stickstoffzahl (N):** `{iv['nutrients']}` / 9
* 🧂 **Salzzahl (S):** `{iv['salinity']}` / 9

### Funktionelle Ökologie & C-S-R-Strategie (nach Grime / Pierce)
* **Strategietyp:** `{csr['primary_class']}`
* **C (Competitor - Konkurrenz):** `{csr['c_percent']} %`
* **S (Stress-Tolerator - Stresstoleranz):** `{csr['s_percent']} %`
* **R (Ruderal - Störungstoleranz):** `{csr['r_percent']} %`

### Morphologie & Wurzelmessungen (UNDERPLOT v39)
* **Wuchshöhe:** `{morph['height_min_m']} – {morph['height_max_m']} m`
* **Wuchsform:** {morph['growth_form']}
* **Wurzelsystem:** {morph['root_system']}
* **Maximale Wurzeltiefe:** `{morph['max_root_depth_m'] if morph['max_root_depth_m'] is not None else 'k. A.'} m`
* **Maximaler Wurzelradius:** `{morph['root_radius_m'] if morph['root_radius_m'] is not None else 'k. A.'} m`
* **Knospenbank-Größe:** `{morph['bud_bank_size'] if morph['bud_bank_size'] is not None else 'k. A.'}`

### Phänologie & Ausbreitung
* **Blütezeit:** {pheno['flowering_period']}
* **Ausbreitungsmechanismus:** {pheno['dispersal_mechanism']}

### Quellen
"""
    for s in b["sources"]:
        md += f"* [{s['name']}]({s['url']})\n"

    md += f"""
---

## 🎁 2. Die Goodies: Kiez-Apotheke, Wildküche & Superkräfte

### 📜 Volksmund & Kulturgeschichte
> *{g['tradition_lore']}*

### 💊 Kiez-Apotheke (Heilwirkung & Erste Hilfe)
* **{g['medicinal_uses']['title']}:** {g['medicinal_uses']['summary']}
* **Zubereitung & Anwendung:** {g['medicinal_uses']['preparation']}

### 🥗 Wildküche & Geschmack
* **{g['culinary_uses']['title']}:** {g['culinary_uses']['summary']}
* **Geschmack:** *{g['culinary_uses']['taste']}*
* **Essbarkeit:** {g['culinary_uses']['edibility']}

### 🧪 Aktive biochemische Inhaltsstoffe
"""
    for c in g["active_compounds"]:
        md += f"* **{c['name']}:** {c['effect']}\n"

    md += f"""
### 💚 Optionaler Spiel-Heileffekt
* **{g['game_healing_effect']['name']}:** {g['game_healing_effect']['effect']}
* *{g['game_healing_effect']['description']}*

### 🔍 Draußen-Entdeckertipp für Kinder
> 💡 **Tipp für den Gehweg:** {g['street_discovery_tip']}

---

## 🎲 3. Spielwerte in den verschiedenen Spielsystemen

Jedes Spiel wählt aus den botanischen Merkmalen die passenden Spielwerte aus:

### A. Fugenduel Brettspiel (Taktile Kirchenmauer & Fugen-Netzwerk)
*Skala 1 bis 3 basierend auf den Pladias- und Traitwerten:*

| Stufe / Seite | Stufe | ☀️ Licht | 💧 Wasser | 🪴 Wurzelraum | 🌿 Triebe | Eigenschaft / Superkraft |
|---|---|:---:|:---:|:---:|:---:|---|
| **Seite A (Level 1)** | {bg['level_1']['stage']} | `{bg['level_1']['light']}` | `{bg['level_1']['water']}` | `{bg['level_1']['root_space']}` | `{bg['level_1']['shoots']}` | {bg['level_1']['trait']} |
| **Seite B (Level 2)** | {bg['level_2']['stage']} | `{bg['level_2']['light']}` | `{bg['level_2']['water']}` | `{bg['level_2']['root_space']}` | `{bg['level_2']['shoots']}` | {bg['level_2']['trait']} |

* **Netzwerk-Aktivität:**
  * 🪵 Wurzelstreifen: `{'Ja' if bg['network_affinities']['root_connection'] else 'Nein'}`
  * 🍄 Pilzstreifen (Mykorrhiza): `{'Ja' if bg['network_affinities']['fungal_connection'] else 'Nein (Gesperrt)'}`
  * 🐜 Ameisenstraße: `{'Ja' if bg['network_affinities']['ant_connection'] else 'Nein'}`
  * *Hinweis:* {bg['network_affinities']['notes']}

### B. Kartenspiel & Duell (0–10 RPG-Skala)
* **WURZEL:** `{cg['stats_0_10']['wurzel']}` / 10
* **TRITT:** `{cg['stats_0_10']['tritt']}` / 10
* **DÜRRE:** `{cg['stats_0_10']['duerre']}` / 10
* **SAAT:** `{cg['stats_0_10']['saat']}` / 10
* **TEMPO:** `{cg['stats_0_10']['tempo']}` / 10
* **CHEMIE:** `{cg['stats_0_10']['chemie']}` / 10
* **Gesamt-Budget:** `{cg['stats_0_10']['total']}` / 36

**Signatur-Fähigkeiten im Kartenspiel:**
"""
    for sk in cg["signature_skills"]:
        md += f"* **{sk['name']}** ({sk['type']} | Bedingung: *{sk['condition']}*): {sk['effect']}\n"

    md += f"""
---

## 🎨 4. Bild-Prompts für Kartengenerierung (2:3 Format)

### Prompt Level 1 (Vorderseite)
```text
Create one finished FUGENDUEL botanical game card, portrait 2:3, full card visible with identical dimensions and layout across the series. Use a restrained weathered brick and dark stone frame, warm parchment panels, dark legible type, natural macro photography style and authentic urban plant anatomy.
Subject: {p['scientific_name']}. Stage: young vegetative plant or colony. {bg['level_1']['trait']}.
Render these German labels and values exactly:
FUGENDUEL
{p['name']}
{p['scientific_name']}
LEVEL 1
Spielwerte: Licht {bg['level_1']['light']} | Wasser {bg['level_1']['water']} | Wurzelraum {bg['level_1']['root_space']} | Triebe {bg['level_1']['shoots']}
Eigenschaft: {bg['level_1']['trait']}
Footer: Artwerte, keine Messung dieser Pflanze. Level und Spielwerte sind Spielentwurf. k. A. = keine Angabe.
```

### Prompt Level 2 (Rückseite)
```text
Create one finished FUGENDUEL botanical game card, portrait 2:3, full card visible with identical dimensions and layout across the series. Use a restrained weathered brick and dark stone frame, warm parchment panels, dark legible type, natural macro photography style and authentic urban plant anatomy.
Subject: {p['scientific_name']}. Stage: established reproductive plant or colony. {bg['level_2']['trait']}.
Render these German labels and values exactly:
FUGENDUEL
{p['name']}
{p['scientific_name']}
LEVEL 2
Spielwerte: Licht {bg['level_2']['light']} | Wasser {bg['level_2']['water']} | Wurzelraum {bg['level_2']['root_space']} | Triebe {bg['level_2']['shoots']}
Eigenschaft: {bg['level_2']['trait']}
Footer: Artwerte, keine Messung dieser Pflanze. Level und Spielwerte sind Spielentwurf. k. A. = keine Angabe.
```
"""
    return md

for p in PLANTS:
    folder = ROOT / "pflanzen/arten" / p["folder"]
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "bilder").mkdir(exist_ok=True)

    # 1. plant.json
    (folder / "plant.json").write_text(json.dumps(p, indent=2, ensure_ascii=False) + "\n")

    # 2. README.md
    md_content = make_markdown_dossier(p)
    (folder / "README.md").write_text(md_content)

    # 3. prompts.txt
    bg = p["game_adaptations"]["board_game"]
    prompts_text = f"""{'='*70}
{p['name']} ({p['scientific_name']}) — LEVEL 1
{'='*70}

Create one finished FUGENDUEL botanical game card, portrait 2:3, full card visible with identical dimensions and layout across the series. Use a restrained weathered brick and dark stone frame, warm parchment panels, dark legible type, natural macro photography style and authentic urban plant anatomy.
Subject: {p['scientific_name']}. Stage: young vegetative plant or colony. {bg['level_1']['trait']}.
Render these German labels and values exactly:
FUGENDUEL
{p['name']}
{p['scientific_name']}
LEVEL 1
Spielwerte: Licht {bg['level_1']['light']} | Wasser {bg['level_1']['water']} | Wurzelraum {bg['level_1']['root_space']} | Triebe {bg['level_1']['shoots']}
Eigenschaft: {bg['level_1']['trait']}
Footer: Artwerte, keine Messung dieser Pflanze. Level und Spielwerte sind Spielentwurf. k. A. = keine Angabe.

{'='*70}
{p['name']} ({p['scientific_name']}) — LEVEL 2
{'='*70}

Create one finished FUGENDUEL botanical game card, portrait 2:3, full card visible with identical dimensions and layout across the series. Use a restrained weathered brick and dark stone frame, warm parchment panels, dark legible type, natural macro photography style and authentic urban plant anatomy.
Subject: {p['scientific_name']}. Stage: established reproductive plant or colony. {bg['level_2']['trait']}.
Render these German labels and values exactly:
FUGENDUEL
{p['name']}
{p['scientific_name']}
LEVEL 2
Spielwerte: Licht {bg['level_2']['light']} | Wasser {bg['level_2']['water']} | Wurzelraum {bg['level_2']['root_space']} | Triebe {bg['level_2']['shoots']}
Eigenschaft: {bg['level_2']['trait']}
Footer: Artwerte, keine Messung dieser Pflanze. Level und Spielwerte sind Spielentwurf. k. A. = keine Angabe.
"""
    (folder / "prompts.txt").write_text(prompts_text)

print(f"Successfully generated dossiers, plant.json, and prompts for {len(PLANTS)} plants!")
