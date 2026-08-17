import json
from pathlib import Path

import click

from .display import display_card, display_json


DATA_FILE = Path(__file__).resolve().parent / "resources" / "pokemon_database.json"

with DATA_FILE.open("r", encoding="utf-8") as file:
    pokemon_database = json.load(file)


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option(
    "-f",
    "--format",
    type=click.Choice(["card", "json"], case_sensitive=False),
    default="card",
    help="Output format.",
)
@click.option(
    "-s",
    "--style",
    type=click.Choice(["box", "block"], case_sensitive=False),
    default="box",
    help="ASCII font style for card format.",
)
@click.argument("pokemon")
def search(pokemon, format, style):
    """
    Command-line interface for quick browsing of data of fake Pokémon made by Arsoniztz.

    Positional argument POKEMON can be either an id or a name.
    """
    query = pokemon.lower()

    for pokemon in pokemon_database:
        if str(pokemon["id"]) == query or pokemon["name"].lower() == query:
            if format == "card":
                display_card(pokemon, pokemon_database, style)
            elif format == "json":
                display_json(pokemon)
            return

    print()
    print("Pokemon not found.")
    print()
