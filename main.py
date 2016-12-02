from flask import Flask
from src.api.atm import setup_urls as atm_setup_urls
from src.api.account import setup_urls as account_setup_urls


app = Flask(__name__)
app.debug = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.secret_key = "CattleKrushSecretKey"

atm_setup_urls(app)
account_setup_urls(app)
