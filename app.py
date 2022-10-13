from flask import Flask
from helpers import get_pokemon_by_name


app = Flask(__name__)

# created a dictionary with all the data so we dont have all seperate datas
# pokemon_creature = {
#     "bulbasur": "dino",
#     "charmander": "reptile",
#     "pikachu": "rodent",
#     "eevee": "fox",
#     "diglett": "mole"
# } (removed this after as we wont need it. will use the pokemon api instead to fetch all data)

@app.get("/") #.get is they want to get info/.post is they want
# to provide some new info. / if the root of out app which means
# if we go to this url the output is what they should receive
def pokemon_list():
    return "bulbasur, charmander, pikachu, eevee, diglett"




# after we create the dictionary
# (if we want to insert a variable we put it in angle brackets).
# NEW endpoint with pokemon API
@app.get("/<pokemon_name>")
def pokemon_data(pokemon_name):
    pokemon = get_pokemon_by_name(pokemon_name)
    return f"this is {pokemon['name']}.\n" \
           f"Height: {pokemon['height']}.\n" \
           f"Weight: {pokemon['weight']}.\n" \
           f"Base experience: {pokemon['base_experience']}.\n" \
           f"Type(s): {' and '.join(type_info['type']['name'] for type_info in pokemon['types'])}"


# # @app.get("/charmander")
# # def charmander_data():
#     return "this is charmander, a generation 1 pokemon who looks like a reptile"
#
#
# @app.get("/pikachu")
# def pikachu_data():
#     return "this is pikachu, a generation 1 pokemon who looks like a rodent"
#
#
# @app.get("/eevee")
# def eevee_data():
#     return "this is eevee, a generation 1 pokemon who looks like a fox"
#
#
# @app.get("/diglett")
# def diglett_data():
#     return "this is diglett, a generation 1 pokemon who looks like a mole"



if __name__ == "__main__":
    app.run()

