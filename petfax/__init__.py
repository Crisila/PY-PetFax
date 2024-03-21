from flask import Flask
from flask_migrate import Migrate


def create_app():
     app = Flask(__name__)
     
     @app.route('/')
     def hello():
          return 'Hello, PetFax!'
     
     from . import pets
     app.register_blueprint(pets.bp)

     from . import facts
     app.register_blueprint(facts.bp)


     # database config
     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Crisila:crisila@localhost:5433/petfax'
     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

     from . import models
     models.db.init_app(app)
     migrate = Migrate(app, models.db)

     return app

