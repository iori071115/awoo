import requests as req
import pprint as pp

def id_is_six(id):
    url = f"https://pokeapi.co/api/v2/pokemon/{id}/"
    res = req.get(url)
    return res.json()["name"]


def id_is_less_than_20():
    id = 1
    pokes = {}
    while id > 0 and id < 20 :
        url = f"https://pokeapi.co/api/v2/pokemon/{id}/"   
        res = req.get(url)
        pokes[f'{res.json()["name"]}'] = res.json()["id"],res.json()["types"]
        id+=1
    sorted_pokes = sorted(pokes.items(), key=lambda x: x[1])
    return sorted_pokes
    
def weight_is_less_than_50():
    id = 1
    pokes = {}
    while id > 0 and id < 100 :
        url = f"https://pokeapi.co/api/v2/pokemon/{id}/"   
        res = req.get(url)
        # print(id, res.json()["name"], res.json()["weight"]  )
        if res.json()["weight"] < 50:
            pokes[f'{res.json()["name"]}'] = res.json()["weight"]
        id+=1
    sorted_pokes = sorted(pokes.items(), key=lambda x: x[1], reverse=True)
    return sorted_pokes



def is_item_count():
    url = "https://pokeapi.co/api/v2/item/"   
    res = req.get(url)
    return res.json()["count"]



def is_item_name():
    id = 1
    ims = {}
    while id > 0 and id < 20 :
        url = f"https://pokeapi.co/api/v2/item/{id}/"   
        res = req.get(url)
        ims[f'{res.json()["name"]}'] = {res.json()["id"]}
        id+=1
    sorted_items = sorted(ims.items(), key=lambda x: x[1])
    return sorted_items

def cost__is_less_than_1500():
    id = 1
    ims = {}
    while id > 0 and id < 50 :
        url = f"https://pokeapi.co/api/v2/item/{id}/"   
        res = req.get(url)
        # print(id, res.json()["name"], res.json()["cost"]  )
        if res.json()["cost"] <= 1500:
            ims[f'{res.json()["name"]}'] = res.json()["cost"]
        id+=1
    sorted_items = sorted(ims.items(), key=lambda x: x[1], reverse=True)
    return sorted_items




print(id_is_six(6))
pp.pprint(id_is_less_than_20())
pp.pprint(weight_is_less_than_50())

print(is_item_count())
pp.pprint(is_item_name())
pp.pprint(cost__is_less_than_1500())