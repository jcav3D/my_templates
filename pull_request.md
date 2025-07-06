# Pull Request: Weighted Pokémon Selection and Utility Functions

## Summary

This pull request introduces a set of utility functions designed to interact with a dataset of the original Pokémon. The main feature added is a weighted random selection mechanism that uses each Pokémon's `spawn_chance` to influence the probability of selection. This allows for more realistic simulations of Pokémon appearances.

## Functions Included

- `load`: Loads and prepares the Pokémon dataset.
- `get_pokemon_data_by_name`: Retrieves data for a specific Pokémon by name.
- `get_all_pokemons_of_type`: Returns all Pokémon of a given type.
- `get_all_pokemons_not_of_type`: Returns all Pokémon that are not of a given type.
- `get_pokemon_by_height`: Returns a list of all Pokémon whose height is less than or equal to the specified value.
- `get_pokemon_heavier_than`: Finds Pokémon heavier than a given weight.
- `get_pokemon_by_evolution`: Retrieves the original Pokémon based on the given evolution.
- `get_pokemon_evolution_by_name`: Returns a list of the evolutions of the given Pokémon.
- `compare_pokemon_types_and_weaknesses`: Compares two Pokémon based on their types and weaknesses.
- `spawn`: Selects a Pokémon index using a weighted random algorithm based on spawn chance.
