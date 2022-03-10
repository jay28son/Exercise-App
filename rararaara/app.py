from flask import Flask, request, jsonify, redirect, url_for
from re import search
import os
import pandas as pd
import json

#init app
app = Flask(__name__)

# Database
exercise_Lists = 'C:/Users/jayso/OneDrive/Desktop/rararaara/fitness_exercises.csv'

exercise_csv = pd.read_csv(exercise_Lists)
#Exercise Dictionary
exercise_tuple = {}

#localhost:5000/exercise
@app.route('/exercise', methods=['Get'])
def get():
        return jsonify(exercise_tuple)    
    
#localhost:5000/exercise/glutes
@app.route('/exercise/glutes', methods=['Get'])
def glutes():
    for _, row in exercise_csv.iterrows():
        exercise_tuple = exercise_csv.loc[exercise_csv.target=='glutes']
        exercise_tuple = exercise_tuple.to_string()
        return jsonify(exercise_tuple)

  
#localhost:5000/exercise/abductors
@app.route('/exercise/abductors', methods=['Get'])
def abductors():
    for _, row in exercise_csv.iterrows():
        exercise_tuple = exercise_csv.loc[exercise_csv.target=='abductors']
        exercise_tuple = exercise_tuple.to_string()
        return jsonify(exercise_tuple)
      
#localhost:5000/exercise/adductors
@app.route('/exercise/adductors', methods=['Get'])
def adductors():
    for _, row in exercise_csv.iterrows():
        exercise_tuple = exercise_csv.loc[exercise_csv.target=='adductors']
        exercise_tuple = exercise_tuple.to_string()
        return jsonify(exercise_tuple)
      
#localhost:5000/exercise/biceps
@app.route('/exercise/biceps', methods=['Get'])
def biceps():
    for _, row in exercise_csv.iterrows():
        exercise_tuple = exercise_csv.loc[exercise_csv.target=='biceps']
        exercise_tuple = exercise_tuple.to_string()
        return jsonify(exercise_tuple)
      
#localhost:5000/exercise/cardiovascular_system
@app.route('/exercise/cardio', methods=['Get'])
def cardiovascular_system():
    for _, row in exercise_csv.iterrows():
        exercise_tuple = exercise_csv.loc[exercise_csv.target=='cardiovascular system']
        exercise_tuple = exercise_tuple.to_string()
        return jsonify(exercise_tuple)

#localhost:5000/exercise/delts
@app.route('/exercise/delts', methods=['Get'])
def delts():
    for _, row in exercise_csv.iterrows():
        exercise_tuple = exercise_csv.loc[exercise_csv.target=='delts']
        exercise_tuple = exercise_tuple.to_string()
        return jsonify(exercise_tuple)
    
#localhost:5000/exercise/forearms
@app.route('/exercise/forearms', methods=['Get'])
def forearms():
    for _, row in exercise_csv.iterrows():
        exercise_tuple = exercise_csv.loc[exercise_csv.target=='forearms']
        exercise_tuple = exercise_tuple.to_string()
        return jsonify(exercise_tuple)
    
    
#localhost:5000/exercise/hamstrings
@app.route('/exercise/hamstrings', methods=['Get'])
def hamstrings():
    for _, row in exercise_csv.iterrows():
        exercise_tuple = exercise_csv.loc[exercise_csv.target=='hamstrings']
        exercise_tuple = exercise_tuple.to_string()
        return jsonify(exercise_tuple)
    
    
#localhost:5000/exercise/lats
@app.route('/exercise/lats', methods=['Get'])
def lats():
    for _, row in exercise_csv.iterrows():
        exercise_tuple = exercise_csv.loc[exercise_csv.target=='lats']
        exercise_tuple = exercise_tuple.to_string()
        return jsonify(exercise_tuple)
    
#localhost:5000/exercise/levator_scapulae
@app.route('/exerciselevator_scapulae', methods=['Get'])
def levator_scapulae():
    for _, row in exercise_csv.iterrows():
        exercise_tuple = exercise_csv.loc[exercise_csv.target=='levator scapulae']
        exercise_tuple = exercise_tuple.to_string()
        return jsonify(exercise_tuple)
    
#localhost:5000/exercise/pectorals
@app.route('/exercise/pectorals', methods=['Get'])
def pectorals():
    for _, row in exercise_csv.iterrows():
        exercise_tuple = exercise_csv.loc[exercise_csv.target=='pectorals']
        exercise_tuple = exercise_tuple.to_string()
        return jsonify(exercise_tuple)
    
#localhost:5000/exercise/quads
@app.route('/exercise/quads', methods=['Get'])
def quads():
    for _, row in exercise_csv.iterrows():
        exercise_tuple = exercise_csv.loc[exercise_csv.target=='quads']
        exercise_tuple = exercise_tuple.to_string()
        return jsonify(exercise_tuple)
    
#localhost:5000/exercise/traps
@app.route('/exercise/traps', methods=['Get'])
def traps():
    for _, row in exercise_csv.iterrows():
        exercise_tuple = exercise_csv.loc[exercise_csv.target=='traps']
        exercise_tuple = exercise_tuple.to_string()
        return jsonify(exercise_tuple)
    
#localhost:5000/exercise/triceps
@app.route('/exercise/triceps', methods=['Get'])
def triceps():
    for _, row in exercise_csv.iterrows():
        exercise_tuple = exercise_csv.loc[exercise_csv.target=='triceps']
        exercise_tuple = exercise_tuple.to_string()
        return jsonify(exercise_tuple)
    
#localhost:5000/exercise/upper_back
@app.route('/exercise/upper_back', methods=['Get'])
def upper_back():
    for _, row in exercise_csv.iterrows():
        exercise_tuple = exercise_csv.loc[exercise_csv.target=='upper back']
        exercise_tuple = exercise_tuple.to_string()
        return jsonify(exercise_tuple)    

#localhost:5000/exercise/abs
@app.route('/exercise/abs', methods=['Get'])
def abs():
    for _, row in exercise_csv.iterrows():
        exercise_tuple = exercise_csv.loc[exercise_csv.target=='abs']
        exercise_tuple = exercise_tuple.to_string()
        return jsonify(exercise_tuple)    
#Run App
if __name__ == '__main__':
    app.run(debug=True)
