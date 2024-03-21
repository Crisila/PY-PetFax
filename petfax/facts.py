from flask import ( Blueprint, request, render_template, redirect )
from . import models


bp = Blueprint('facts', __name__, url_prefix='/facts')





@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Process the form data from the POST request
        form_data = request.form
        # Redirect to another route after processing the form data
        return redirect('/facts')  # Replace '/facts' with the desired URL
    
    facts_data = models.Fact.query.all()

    # If the request is GET, render the template for the index page
    return render_template('facts/index.html', facts=facts_data)

@bp.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        submitter = request.form['submitter']
        fact = request.form['fact']

        new_fact = models.Fact(submitter=submitter, fact=fact)
        models.db.session.add(new_fact)
        models.db.session.commit()


        return redirect('/facts')  # Replace '/facts' with the desired URL


    # If the request is GET, render the template for the index page
    return render_template('facts/new.html')

# pip install sqlalchemy
# flask db migrate == npx sequelize migration:generate
# flash db upgrade == npx sequelize migrate
# pip install Flask-Migrate