import requests


def get_damage(key: str):
    """Get information about damage.
    Args:
        key (str): Name of json's key.
    Returns:
        Number of damage multiplier for one type.
    """

    if key.startswith("double"):
        return 2
    elif key.startswith("half"):
        return 0.5
    elif key.startswith("no"):
        return 0
    else:
        return 1


def calculate_damage(first_pokemon: str,second_pokemon: str):
    """Get information about pokemon and calculate damages.
    Args:
        first_pokemon (str): Type of first pokemon.
        second_pokemon (str): Type of second pokemon.

    Returns:
        (str): Number of damage multiplier.
    """

    type_1_of_second_pokemon=type_2_of_second_pokemon=None
    damage_1=damage_2=1

    try:
        type_1_of_second_pokemon, type_2_of_second_pokemon=second_pokemon.split(' ')
    except ValueError:
        type_1_of_second_pokemon=second_pokemon
    url = f'https://pokeapi.co/api/v2/type/{first_pokemon}'
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    response = r.json()
    for key in response['damage_relations']:
        if key.endswith("to"):
            damage_names=[_['name'] for _ in response['damage_relations'][key]]
            if type_1_of_second_pokemon and type_1_of_second_pokemon in damage_names:
                damage_1=get_damage(key)
            if type_2_of_second_pokemon and type_2_of_second_pokemon in damage_names:
                damage_2=get_damage(key)
  
    return str(damage_1 * damage_2)+'x'
