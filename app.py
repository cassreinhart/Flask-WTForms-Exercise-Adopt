from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'PetsAreKool817'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_home_page():
    """Show adoption agency home page."""
    pets = Pet.query.all()

    return render_template('/templates/home.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Show or process form to add a new pet."""

    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        # available = form.available.data

        else:
            return render_template('add_pet_form.html', form = form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_pet_detail_edit_pet_form(pet_id):
    """Display pet details and edit pet form"""

    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = pet.photo_url.data
        pet.notes = pet.notes.data
        pet.available = pet.available.data
        db.session.commit()
        flash(f"Pet {pet.name} updated!")
        return redirect(f"/{pet_id}")
    else:
        return render_template('')

