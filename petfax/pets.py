from flask import Blueprint, render_template, redirect, request, url_for
import json


pets = json.load(open('pets.json'))
print(pets)

# Create a Blueprint named 'pets' with the URL prefix '/pets'
bp = Blueprint('pets', __name__, url_prefix='/pets')

# Define the index route for the 'pets' Blueprint
@bp.route('/', methods=['GET'])
def index():
    return render_template('pets/index.html', pets=pets)


# Define the show route
@bp.route('/<int:pet_id>', methods=['GET'])
def show(pet_id):
    # Find the pet with the specified ID from the sample data
    pet = next((pet for pet in pets if pet['pet_id'] == pet_id), None)
    if pet:
        return render_template('pets/show.html', pet=pet)
    else:
        return 'Pet not found', 404
    


# @bp.route('/facts', methods=['GET'])
# def new_fact():
#     return render_template('new.html')



