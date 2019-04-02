# Importing modules...
import json
from flask import Flask, request, jsonify
import sqlite3
 
app = Flask(__name__)
 
# class for sorting...
class Sortify:
    # configure database
    def __init__(self):
        self.cur = sqlite3.connect('Sortify.db')
        self.cur.execute('drop table if exists Dict')
        self.cur.execute('CREATE TABLE IF NOT EXISTS Dict (id integer, name integer);')
   
    # Stores the request json into db
    def json_to_dict(self, data):
        listt = json.loads(data)
        for i in listt:
            x = i['id']
            y = i['name']
            self.cur.execute('INSERT INTO dict (id, name) values (?, ?);', (x, int(y[1:]),))
 
    # fetches the data from db and sorts the values of a dict in a list
    def sorted_list(self):
        result = self.cur.execute('SELECT id, name FROM Dict order by name ASC')
        listt = list()
        for k, v in result:
            print(k,v)
            dictt = {}
            dictt['id'] = k
            dictt['name'] = 'a'+ str(v)
            listt.append(dictt)
        return listt
 
 # Sample input
l = [{'id': 92, 'name': 'a21'}, {'id': 12, 'name': 'a10'}, {'id': 15, 'name': 'a5'}, {'id': 72, 'name': 'a82'}]
 # sample output
t = [{'id': 15, 'name': 'a5'}, {'id': 12, 'name': 'a10'}, {'id': 92, 'name': 'a21'}, {'id': 72, 'name': 'a82'}]

# Route to return sorted json
@app.route('/sort_dict', methods=['POST'])
def sort_dict_db():
    if (len(request.data)<1):
        return jsonify({"error": "Invalid Values"}), 200
    sorty = Sortify()
    sorty.json_to_dict(request.data)
    x = sorty.sorted_list()
    return jsonify(x), 200 #Returns JSON with status code of 200
 
if '__name__' == '__main__':
    app.run(debug=true)
