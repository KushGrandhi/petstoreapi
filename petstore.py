from flask import Flask, jsonify, request, render_template 
import sqlite3
import json
import random


app = Flask(__name__) 

with sqlite3.connect('store.sqlite') as conn:
        cur = conn.cursor()
        cur.execute(''' CREATE TABLE IF NOT EXISTS pets (
            pet_name TEXT PRIMARY KEY,
            pet_type TEXT NOT NULL,
            owner TEXT NOT NULL
            );''')
        
        conn.commit()

@app.route('/')
def home():
    return render_template('readme.html')
@app.route('/hello')
def hello():
    heya = ''
    ans = ['woof', 'howdy', 'moo?', 'meow', 'oink oink','cock-a-doodle-doo']
    with sqlite3.connect('store.sqlite') as conn:
        cur = conn.cursor()
        cur.execute('''SELECT pet_name FROM PETS''')
        al = cur.fetchall()
        conn.commit()
    for i in al:
        heya += str(i[0]) + '  :'+ ans[random.randrange(0,len(ans))] +' ;  '
    try:
        return jsonify(greetings=heya)
    except:
        return jsonify(greetings='please open the store first')   

@app.route('/allpets', methods =['GET'])
def allpets():
    with sqlite3.connect('store.sqlite') as conn:
        cur = conn.cursor()
        cur.execute('''SELECT pet_name FROM PETS''')
        al = cur.fetchall()
        conn.commit()
    try:
        return jsonify(pet_names=al)
    except:
        return jsonify(pet_names='Table empty')

@app.route('/pet', methods = ['GET'])
def pet():
    if 'id' in request.args:
        id = (request.args['id'])
        with sqlite3.connect('store.sqlite') as conn:
            cur = conn.cursor()
            cur.execute('''SELECT * FROM PETS WHERE pet_name = '{}' '''.format(id))
            al = cur.fetchall()
            conn.commit()
        return jsonify(mypet = al)
    else:
        return jsonify(mypet = 'pet not found')

@app.route('/newpet', methods = ['POST']) 
def addpet():
   if request.method == 'POST':
        user = request.get_json(force=True)
        with sqlite3.connect('store.sqlite') as conn:
            cur = conn.cursor()
            cur.execute('''INSERT INTO pets VALUES ('{}','{}','{}'); '''.format(user['pet_name'],user['pet_type'],user['owner']))
            al = cur.fetchall()
            conn.commit()
        return jsonify(response = 'pet added')
@app.route('/updatepet', methods = ['POST'])
def updatepet():
    if request.method == 'POST':
        user = request.get_json(force=True)
        with sqlite3.connect('store.sqlite') as conn:
            cur = conn.cursor()
            cur.execute('''UPDATE pets SET pet_type = '{}',owner = '{}' WHERE pet_name ='{}'  '''.format(user['pet_type'],user['owner'],user['pet_name']))
            al = cur.fetchall()
            conn.commit()
        return jsonify(response = 'pet updated')
@app.route('/delpet', methods = ['DELETE'])
def delpet():
    if 'id' in request.args:
        id = (request.args['id'])
        with sqlite3.connect('store.sqlite') as conn:
            cur = conn.cursor()
            cur.execute('''DELETE FROM pets WHERE pet_name = '{}' '''.format(id))
            al = cur.fetchall()
            conn.commit()
        return jsonify(response='Deleted Elements')
    else:
        return jsonify(response = 'Provide Valid Pet Name to Delete')

@app.route('/mypets',methods=['GET'])
def mypets():
    if 'id' in request.args:
        id = (request.args['id'])
        with sqlite3.connect('store.sqlite') as conn:
            cur = conn.cursor()
            cur.execute('''SELECT pet_name FROM pets WHERE owner = '{}' '''.format(id))
            al = cur.fetchall()
            conn.commit()
        return jsonify(response=al)

@app.route('/whosepet', methods=['GET'])
def whosepet():
    if 'id' in request.args:
        id = (request.args['id'])
        with sqlite3.connect('store.sqlite') as conn:
            cur = conn.cursor()
            cur.execute('''SELECT owner FROM pets WHERE pet_name = '{}' '''.format(id))
            al = cur.fetchall()
            conn.commit()
    return jsonify(response=al)

@app.route('/owner',methods=['GET'])
def owner():

    with sqlite3.connect('store.sqlite') as conn:
        cur = conn.cursor()
        cur.execute('''SELECT DISTINCT owner FROM pets''')
        al = cur.fetchall()
        conn.commit()
    return jsonify(response=al)  

if __name__ == '__main__': 
    app.run(debug = True) 