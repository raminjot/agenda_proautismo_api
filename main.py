# Application import
from app import app

# Modules import
import controllers

# Register controllers
app.register_blueprint(controllers.example)
app.register_blueprint(controllers.tasks)
app.register_blueprint(controllers.users)

# Starting the app
if __name__ == '__main__':
    app.run(port = 3000, debug = True)
