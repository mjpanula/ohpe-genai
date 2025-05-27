from flask import Flask, jsonify
import csv
from flask import request
import os
from flask import redirect
import omat_funktiot

app = Flask(__name__)

@app.route('/')
def root():
    return redirect('/static/index.html')

@app.route('/wishes', methods=['GET'])
def get_wishes():
    try:        
        with open('toiveet.csv', mode='r', encoding='utf-8') as csvfile:
            # lue tiedot csv.DictReader(csvfile) -komennolla
            # palauta lista joka sisältää toiveet sanakirja-muodossa
            wishes = omat_funktiot.lue_toiveet(csvfile)            
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404
    except KeyError as e:
        return jsonify({'error': f'Missing column in CSV: {e}'}), 400

    return jsonify(wishes)

@app.route('/wishes', methods=['POST'])
def add_wish():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part'}), 400
    kuvatiedosto = request.files['image']
    toiveen_nimi = request.form.get('name')
    toiveen_kuvaus = request.form.get('description')

    if not toiveen_nimi or not toiveen_kuvaus or kuvatiedosto.filename == '':
        return jsonify({'error': 'Missing data'}), 400

    # Save image
    img_filename = kuvatiedosto.filename
    img_path = os.path.join('static/kuvat', img_filename)
    kuvatiedosto.save(img_path)

    # Determine next id    
    max_id = 0
    try:
        with open('toiveet.csv', mode='r', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                id_number = int(row['id'])
                if id_number > max_id:
                    max_id = id_number
        next_id = str(max_id + 1)
    except FileNotFoundError:
        next_id = '1'

    # Write to CSV
    file_exists = os.path.isfile('toiveet.csv')
    with open('toiveet.csv', mode='a', encoding='utf-8', newline='') as csvfile:

        fieldnames = ['id', 'name', 'description', 'img-path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        ## Generoi sanakirja-muotoinen rivi (huomaa csv sarakkeiden otsikot)
        csv_rivi = omat_funktiot.generoi_toiveet_csv_rivi(next_id, toiveen_nimi, toiveen_kuvaus, f'kuvat/{img_filename}')
        writer.writerow(csv_rivi)

    return jsonify({'message': 'Wish added', 'id': next_id}), 201

@app.route('/wishes/<id>', methods=['DELETE'])
def delete_wish(id):
    wishes = []
    deleted = False
    # Read all wishes and filter out the one to delete
    try:
        with open('toiveet.csv', mode='r', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                if row['id'] == id:
                    deleted = True
                    # Optionally, delete the image file
                    img_path = row.get('img-path', '')
                    if img_path and img_path.startswith('kuvat/'):
                        img_file = os.path.join('static/kuvat', os.path.basename(img_path))
                        if os.path.isfile(img_file):
                            os.remove(img_file)
                else:
                    wishes.append(row) # ei-postettavat lisätään toiveet lisätään listaan
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404

    if not deleted:
        return jsonify({'error': 'Wish not found'}), 404 

    # wishes-lista sisältää nyt kaikki toiveet paitsi poistettavan
    # listan sisällöllä voi korvata csv-tiedoston sisällön (ylikirjoittaa)
    omat_funktiot.ylikirjoita_toiveet_csv(wishes)
   
    return jsonify({'message': 'Wish deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)