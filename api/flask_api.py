from flask import Flask, request

import database
import config

db = database.database_instance

app = Flask(__name__)

@app.route("/news")
def get_summaries():
    amount = int(request.args.get("amount", config.DEFAULT_GET_SUMMARIES_AMOUNT))
    page = int(request.args.get("page", 0))
    
    r = db.get_processed_urls(amount, page)
    response = {
        'amount': amount,
        'page': page,
        'results':r
    }
    return response

def main():
    app.run(host=config.FLASK_API_HOST, port=config.FLASK_API_PORT)