'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
    return

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # Clean the Pokemon name parameter
    pokemon_name = str(pokemon_name).strip().lower()

    # Build a clean URL and use it to send a GET request
    CLEAN_URL = POKE_API_URL + pokemon_name 

    print(f'Getting information for {pokemon_name}.....', end='')
    response_msg = requests.get(CLEAN_URL)

    # If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    if response_msg.status_code == requests.codes.ok:
        print("success!")
        body_dict = response_msg.json()
        print(f"Getting information for {pokemon_name}......success")
        return body_dict

        
    else:
        print("failure:(")
        print(f"{response_msg.status_code} {response_msg.reason} {response_msg.text}")


if __name__ == '__main__':
    main()