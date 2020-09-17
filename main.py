from bottle import request, response, run, post, get, put, route
from operator import itemgetter
import json
from urllib.parse import urlparse
from schema import Schema, And, Use, Optional

# simulate the database
wine = [{'wine_id': 1, 'type': 'Merlot', 'profile': 'A rich, often dry wine', 'color': 'Dark Red', 'age': 2017},
        {'wine_id': 2, 'type': 'Cabernet Sauvignon', 'profile': 'A bold wine, favored by new drinkers', 'color': 'Ruby Red', 'age': 2016},
        {'wine_id': 3, 'type': 'Chardonnay', 'profile': 'Buttery and decadent', 'color': 'Golden', 'age': 2019},
        {'wine_id': 4, 'type': 'Pinot Grigio', 'profile': 'Dry and refreshing', 'color': 'Silver/Hay', 'age': 2018},
        {'wine_id': 5, 'type': 'Riesling', 'profile': 'Sweet and indulgent', 'color': 'Golden', 'age': 2017}]


@get('/wine')
def getwines():
    s = dict(request.query)

    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    if 'id' in s:
        id = int(s['id'])
        return next((item for item in wine if item['wine_id'] == id),
                    {'success': False, 'error_text': 'Wine type not found'})

    if 'type' in s:
        type = s['type']
        return next((item for item in wine if item['type'] == type),
                    {'success': False, 'error_text': 'Wine type not found'})
    if 'age' in s:
        age = int(s['age'])
        return next((item for item in wine if item['age'] == age),
                    {'success': False, 'error_text': 'Wine type not found'})

    else:
        return json.dumps({'wines': wine})

"""
@get('/wine/)
def getwinebytype():
    u = urlparse()

    if type != "":
        return next((item for item in wine if item['type'] == type), {'success': False, 'error_text': 'Wine type not found'})
    else:
        return {'success': False, 'error_text': 'Need a wine type'}
"""

@get('/wine/age/<age:int>')
def getwinebyage(age=1999):
        i = 0
        agedict = {}
        if age == 1999:
            print("We're gonna party like it's " + str(age))
        #return next((item for item in wine if item['age'] == age), {'success': False, 'text': 'No wine(s) by that age found'})
        for item in wine:
            if item['age'] == age:
                agedict[i] = item
            i += 1
        if len(agedict) == 0:
            return {"success": False, 'text': 'No results found'}
        return agedict

@get('/wine/<id:int>')
def getwinebyid(id=0):
    return next((item for item in wine if item['wine_id'] == id),
                {'success': False, 'text': 'No wine with that id found'})

@get('/wine/type/<type>/age/<age:int>')
def getwinebytypeandage(type='Merlot', age=1999):
    return next((item for item in wine if item['age'] == age and item['type'] == type),
                {'success': False, 'text': 'No wine(s) by that age found'})


@route('/')
def hello():
    u = urlparse('//localhost.com:8000/wines?type=merlot')
    print(u)
    return "Hello World!"

# Python has a fun and dangerous feature that allows you to... use unlimited params, this will be most handy when
# I figure out how to do queries in bottle, if at all possible
def multisearch(*search_param):
    pass

run(host='localhost', port=8000, reloader=True, debug=True)
