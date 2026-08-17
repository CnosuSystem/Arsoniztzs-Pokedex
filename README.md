# Arsoniztz's Pokédex

A simple command-line Pokédex for browsing data of fake Pokémon made by Arsoniztz directly from your terminal.

## Installation

You can install the latest version directly from this repository:

```
pip install "git+https://github.com/CnosuSystem/Arsoniztzs-Pokedex.git"
```

If you installed the project but want to update it to the latest version, use:

```
pip install --upgrade "git+https://github.com/CnosuSystem/Arsoniztzs-Pokedex.git"
```

No PyPi install is planned, as this is a minor/niche project and I prefer to keep it off PyPi.

## Building from Source

### 1. Clone the repository

Make sure you have Git installed, then clone the repository:

```
git clone https://github.com/CnosuSystem/Arsoniztzs-Pokedex.git
cd Arsoniztzs-Pokedex
```

If you don't have Git, simply download the raw source .zip file from GitHub and put it in your preffered directory. Then open it in the terminal.

### 2. Install the project

Install the project and its dependencies with:

```
python -m pip install .
```

The project's package configuration will install its required dependencies (click>=8.0 and colorama>=0.4.6) and register the a-dex command.

## Usage

```
a-dex --help
Usage: a-dex [OPTIONS] POKEMON

  Command-line interface for quick browsing of data of fake Pokémon made by
  Arsoniztz.

  Positional argument POKEMON can be either an id or a name.

Options:
  -f, --format [card|json]  Output format.
  -s, --style [box|block]   ASCII font style for card format.
  -h, --help                Show this message and exit.
```

## Authors

* [@Cnosu](https://spacehey.com/cnosu) - The guy that did all the coding
* [@Arsoniztz](https://arsoniztz.carrd.co/) - The person that did all the Pokemon designing

## License

This project is licensed under the [GNU GPLv3 License](https://www.gnu.org/licenses/gpl-3.0.en.html#license-text) - see the [LICENSE.md](https://github.com/CnosuSystem/Arsoniztzs-Pokedex?tab=GPL-3.0-1-ov-file) file for details

## Acknowledgments

* Heavy inspiration from [Tenchi2xh/pokedex-cli](https://github.com/Tenchi2xh/pokedex-cli)