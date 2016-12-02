from flask import Flask
from src.api.user import setup_urls as user_setup_urls


app = Flask(__name__)
app.debug = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.secret_key = "CattleKrushSecretKey"

user_setup_urls(app)
