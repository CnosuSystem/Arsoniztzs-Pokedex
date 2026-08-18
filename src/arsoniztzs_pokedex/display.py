import json
import textwrap

from colorama import Fore, Style, init

from .formatting import format_evolution, format_id, format_type


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

    TARGET_WIDTH = 40
    TARGET_DESCRIPTION_ROWS = 5

    pad1 = " " * (TARGET_WIDTH - len(line1) - len(id_art[0]))
    pad2 = " " * (TARGET_WIDTH - len(line2) - len(id_art[1]))
    pad3 = " " * (TARGET_WIDTH - len(line3) - len(id_art[2]))

    print()
    print(f"{Fore.WHITE}{Style.BRIGHT}{line1}{Style.RESET_ALL}{pad1}{id_art[0]}")
    print(f"{Fore.WHITE}{Style.NORMAL}{line2}{Style.RESET_ALL}{pad2}{id_art[1]}")
    print(f"{Fore.WHITE}{Style.DIM}{line3}{Style.RESET_ALL}{pad3}{id_art[2]}")
    print()

    formatted_types = [format_type(t) for t in types]
    print(" ".join(formatted_types))

    wrapped_description = textwrap.fill(description, width=TARGET_WIDTH)
    description_lines = wrapped_description.splitlines()

    # Add blank lines until the description occupies the target number of rows
    description_lines += [""] * max(0, TARGET_DESCRIPTION_ROWS - len(description_lines))

    print()
    print("\n".join(description_lines))

    print()
    formatted_evolution = format_evolution(evolution_ids, id, pokemon_database)
    print(formatted_evolution)
    print()

def display_detailed_card(pokemon, pokemon_database, font_style):
    display_card(pokemon, pokemon_database, font_style)