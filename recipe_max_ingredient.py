import os

import requests
from dotenv import load_dotenv

load_dotenv()


class Spoonacular:
    """
    Clase para llamar a la api de Spoonacular: https://spoonacular.com/food-api
    
    args:
        'url': url de la api
        'id': id de la receta 
    """
    def __init__(self, url, recipe_id):
        self.url = f"{url}/recipes/{recipe_id}/information"
        self.api_key = os.getenv("SPOONACULAR_API_KEY")

    def get_ingredient(self):
        """
        Función que retorna el ingrediente maximo de una receta de Spoonacular

        return:
            dict: Un diccionario que contiene el titulo del ingrediente mayor y su peso
        """
        headers = {"x-api-key": self.api_key}
        response = requests.get(self.url, headers=headers)
        response.raise_for_status()

        print(response.status_code)
        data = response.json()

        ingredient_name = None
        ingredient_amount_major = 0

        for ingredient in data["extendedIngredients"]:
            if ingredient["amount"] > ingredient_amount_major:
                ingredient_name = ingredient["name"]
                ingredient_amount_major = ingredient["amount"]

        return {  # Retorno en forma de diccionario, por defeco tambien puedo retornar en forma de tupla y desempaquetarlo
            "ingredient_max": ingredient_name,
            "amount": ingredient_amount_major,
        }


def main():

    spoon = Spoonacular("https://api.spoonacular.com", "716429") # Instancia de la clase 
    print(spoon.get_ingredient())


if __name__ == "__main__":
    main()
