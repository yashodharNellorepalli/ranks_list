# Import flask and template operators
import os
from flask import Flask

# Application Definition
app = Flask(__name__,
            instance_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), '../instance'),
            instance_relative_config=True)

# Initializing configuration
app.config.from_pyfile('env.cfg', silent=True)


# Import a module / component using its blueprint handler variable (catalog_module)
from app.ranks.controllers import ranks_module

# Register blueprint(s)
app.register_blueprint(ranks_module)
