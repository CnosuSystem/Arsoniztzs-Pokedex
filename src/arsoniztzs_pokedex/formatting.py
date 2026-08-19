import textwrap

from colorama import Back, Fore, Style, init


init()


TARGET_WIDTH = 40
TARGET_DESCRIPTION_ROWS = 5

TYPE_COLORS = {
    "Normal": Back.WHITE,
    "Fire": Back.RED,
    "Water": Back.BLUE,
    "Grass": Back.GREEN,
    "Electric": Back.YELLOW,
    "Ice": Back.CYAN,
    "Fighting": Back.RED,
    "Poison": Back.MAGENTA,
    "Ground": Back.YELLOW,
    "Flying": Back.CYAN,
    "Psychic": Back.MAGENTA,
    "Bug": Back.GREEN,
    "Rock": Back.YELLOW,
    "Ghost": Back.MAGENTA,
    "Dragon": Back.MAGENTA,
    "Dark": Back.BLACK,
    "Steel": Back.WHITE,
    "Fairy": Back.MAGENTA,
}

FONTS = {
    "box": {
        "0": ["┌─┐", "│ │", "└─┘"],
        "1": [" ┌┐", "  │", " ─┴"],
        "2": ["┌─┐", "┌─┘", "└──"],
        "3": ["──┐", " ─┤", "──┘"],
        "4": ["│ │", "└─┤", "  │"],
        "5": ["┌──", "└─┐", "──┘"],
        "6": ["┌──", "├─┐", "└─┘"],
        "7": ["──┐", "  │", "  │"],
        "8": ["┌─┐", "├─┤", "└─┘"],
        "9": ["┌─┐", "└─┤", "  │"],
    },
    "block": {
        "0": ["█▀█", "█ █", "█▄█"],
        "1": [" █ ", " █ ", " █ "],
        "2": ["▀▀█", "█▀▀", "███"],
        "3": ["▀▀█", " ▀█", "▄▄█"],
        "4": ["█ █", "▀▀█", "  █"],
        "5": ["█▀▀", "▀▀█", "▄▄█"],
        "6": ["█▀▀", "█▀█", "█▄█"],
        "7": ["▀▀█", "  █", "  █"],
        "8": ["█▀█", "█▀█", "█▄█"],
        "9": ["█▀█", "▀▀█", "▄▄█"],
    },
}

SHAPE_NAMES = {
    0: "Head",
    1: "Head & Legs",
    2: "Fins",
    3: "Insectoid",
    4: "Four Legs",
    5: "Four Wings",
    6: "Gathering",
    7: "Tentacles/Multiped",
    8: "Upright Torso",
    9: "Two Legs & Tail",
    10: "Two Legs & No Tail",
    11: "Two wings",
    12: "Serpentine",
    13: "Head & Arms",
}


def format_padding(string):
    return " " * (TARGET_WIDTH - len(string))


def format_description(description):
    wrapped_description = textwrap.fill(description, width=TARGET_WIDTH)
    description_lines = wrapped_description.splitlines()

    # Add blank lines until the description occupies the target number of rows
    description_lines += [""] * max(0, TARGET_DESCRIPTION_ROWS - len(description_lines))
    return description_lines


def format_id(id, font_style):
    font_dict = FONTS.get(font_style.lower(), FONTS["box"])
    id_str = f"{id:03}"
    lines = ["", "", ""]

    for idx, char in enumerate(id_str):
        art = font_dict.get(char, ["   ", "   ", "   "])
        for i in range(3):
            lines[i] += art[i]
            if idx < len(id_str) - 1:
                lines[i] += " "

    return lines


def format_type(t):
    bg_color = TYPE_COLORS.get(t, Back.RESET)

    if t == "Dark":
        fg_color = Fore.WHITE
    else:
        fg_color = Fore.BLACK

    return f"{bg_color}{fg_color} {t.upper()} {Style.RESET_ALL}"


def format_evolution(evolution_ids, current_id, pokemon_database):
    db_lookup = {p["id"]: p["name"] for p in pokemon_database}

    formatted_ids = []
    formatted_names = []

    for evo_id in evolution_ids:
        evo_name = db_lookup.get(evo_id, "Unknown")
        id_str = f"#{evo_id:03}"

        col_width = max(len(id_str), len(evo_name))
        centered_id = id_str.center(col_width)
        centered_name = evo_name.center(col_width)

        if evo_id == current_id:
            styled_id = f"{Fore.WHITE}{Style.BRIGHT}{centered_id}{Style.RESET_ALL}"
            styled_name = f"{Fore.WHITE}{Style.BRIGHT}{centered_name}{Style.RESET_ALL}"
        else:
            styled_id = f"{Fore.WHITE}{Style.DIM}{centered_id}{Style.RESET_ALL}"
            styled_name = f"{Fore.WHITE}{Style.DIM}{centered_name}{Style.RESET_ALL}"

        formatted_ids.append(styled_id)
        formatted_names.append(styled_name)

    ids_line = "   ".join(formatted_ids)
    names_line = f" {Fore.BLUE}>{Style.RESET_ALL} ".join(formatted_names)

    return f"{ids_line}\n{names_line}"


def format_shape(shape_id):
    return SHAPE_NAMES.get(shape_id, "Unknown")