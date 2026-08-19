import json
import textwrap

from colorama import Fore, Style, init

from .formatting import format_padding, format_description, format_evolution, format_id, format_type, format_shape


init()


def display_json(pokemon):
    print()
    print(json.dumps(pokemon, indent=4))
    print()


def display_card(pokemon, pokemon_database, font_style):
    id = pokemon["id"]
    id_art = format_id(id, font_style)
    name = pokemon["name"]
    species = pokemon["profile"]["species"]
    height = pokemon["profile"]["height"]
    weight = pokemon["profile"]["weight"]
    types = pokemon["type"]
    description = pokemon["profile"]["description"]
    evolution_ids = pokemon.get("evolution", [])

    line1 = name
    line2 = f"{species} Pokémon"
    line3 = f"{height} / {weight}"

    print()
    pad = format_padding(line1)
    print(f"{Fore.WHITE}{Style.BRIGHT}{line1}{Style.RESET_ALL}{pad}{id_art[0]}")
    pad = format_padding(line2)
    print(f"{Fore.WHITE}{Style.NORMAL}{line2}{Style.RESET_ALL}{pad}{id_art[1]}")
    pad = format_padding(line3)
    print(f"{Fore.WHITE}{Style.DIM}{line3}{Style.RESET_ALL}{pad}{id_art[2]}")
    print()

    formatted_types = [format_type(t) for t in types]
    print(" ".join(formatted_types))

    print()
    print("\n".join(format_description(description)))

    print()
    formatted_evolution = format_evolution(evolution_ids, id, pokemon_database)
    print(formatted_evolution)
    print()

def display_detailed_card(pokemon, pokemon_database, font_style):
    display_card(pokemon, pokemon_database, font_style)

    shape = format_shape(pokemon["profile"]["shape"])
    abilities = pokemon["abilities"]
    egg = pokemon["profile"]["egg"]
    male_chance = pokemon["profile"]["gender_ratio"]["male"]
    female_chance = pokemon["profile"]["gender_ratio"]["female"]

    hp = pokemon["base_stats"]["HP"]
    attack = pokemon["base_stats"]["Attack"]
    defense = pokemon["base_stats"]["Defense"]
    sp_attack = pokemon["base_stats"]["Sp. Attack"]
    sp_defense = pokemon["base_stats"]["Sp. Defense"]
    speed = pokemon["base_stats"]["Speed"]

    print()

    pad = " " * (TARGET_WIDTH - len("Shape:") - len(shape))
    print(f"Shape:{pad}{shape}")

    pad = " " * (TARGET_WIDTH - len("Abilities:") - len(abilities[0]))
    print(f"Abilities:{pad}{abilities[0]}")
    for i in range(len(abilities) - 1):
        pad = " " * (TARGET_WIDTH - len(abilities[i + 1]))
        print(f"{pad}{abilities[i + 1]}")

    pad = " " * (TARGET_WIDTH - len("Egg Group:") - len(egg[0]))
    print(f"Egg Group:{pad}{egg[0]}")
    for i in range(len(egg) - 1):
        pad = " " * (TARGET_WIDTH - len(egg[i + 1]))
        print(f"{pad}{egg[i + 1]}")

    pad = " " * (TARGET_WIDTH - len("Gender Ratio [M/F]:") - len(male_chance) - len("/") - len(female_chance))
    print(f"Gender Ratio [M/F]:{pad}{male_chance}/{female_chance}")

    print()

    print("Base Stats:")
    pad = " " * (TARGET_WIDTH - len("HP:") - len(str(hp)))
    print(f"HP:{pad}{hp}")
    pad = " " * (TARGET_WIDTH - len("Attack:") - len(str(attack)))
    print(f"Attack:{pad}{attack}")
    pad = " " * (TARGET_WIDTH - len("Defense:") - len(str(defense)))
    print(f"Defense:{pad}{defense}")
    pad = " " * (TARGET_WIDTH - len("Sp. Attack:") - len(str(sp_attack)))
    print(f"Sp. Attack:{pad}{sp_attack}")
    pad = " " * (TARGET_WIDTH - len("Sp. Defense:") - len(str(sp_defense)))
    print(f"Sp. Defense:{pad}{sp_defense}")
    pad = " " * (TARGET_WIDTH - len("Speed:") - len(str(speed)))
    print(f"Speed:{pad}{speed}")