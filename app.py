from flask import Flask


app = Flask(__name__)


@app.get("/") #.get is they want to get info/.post is they want
# to provide some new info. / if the root of out app which means
# if we go to this url the output is what they should receive
def pokemon_list():
    return "bulbasur, charmander, pikachu, eevee, diglett"


@app.get("/bulbasur")
def bulbasur_data():
    return "this is bulbasur, a generation 1 pokemon who looks like a dino"


@app.get("/charmander")
def charmander_data():
    return "this is charmander, a generation 1 pokemon who looks like a reptile"


@app.get("/pikachu")
def pikachu_data():
    return "this is pikachu, a generation 1 pokemon who looks like a rodent"


@app.get("/eevee")
def eevee_data():
    return "this is eevee, a generation 1 pokemon who looks like a fox"


@app.get("/diglett")
def diglett_data():
    return "this is diglett, a generation 1 pokemon who looks like a mole"



if __name__ == "__main__":
    app.run()

