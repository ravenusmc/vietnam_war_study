from flask import Flask, jsonify, request
from flask_cors import CORS

#importing code that I wrote
from data import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

# This route will deal with getting the user the data for the total number
# of deaths between two years.
@app.route('/one', methods=['GET', 'POST'])
def deathData():
    if request.method == 'POST':
        data = Data()
        post_data = request.get_json()
        yearOne = int(post_data['yearOne'])
        yearTwo = int(post_data['yearTwo'])
        death_count = data.get_total_deaths_between_years(yearOne, yearTwo)
        return jsonify(death_count)

#This route will get the data for the second graph
@app.route('/firstGraph', methods=['GET'])
def graphOne():
    data = Data()
    death_data = data.get_number_of_deaths_total()
    return jsonify(death_data)

#This route will get data for the second graph
@app.route('/secondGraph', methods=['GET', 'POST'])
def graphTwo():
    if request.method == 'POST':
        data = Data()
        post_data = request.get_json()
        yearOne = int(post_data['yearOne'])
        yearTwo = int(post_data['yearTwo'])
        branch_death_data = data.get_data_second_graph(yearOne, yearTwo)
        return jsonify(branch_death_data)

#This route will get data for the third graph
@app.route('/thirdGraph', methods=['GET', 'POST'])
def graphThree():
    if request.method == 'POST':
        data = Data()
        post_data = request.get_json()
        yearOne = int(post_data['yearOne'])
        yearTwo = int(post_data['yearTwo'])
        return jsonify('WORK?!')

if __name__ == '__main__':
    app.run()
