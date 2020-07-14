from src.app import app
from src.config import PORT
from src.controllers.initpag import *
from src.controllers.create_user import *
from src.controllers.chat_create import *
from src.controllers.sentimental import *


app.run("0.0.0.0",PORT,debug=True)