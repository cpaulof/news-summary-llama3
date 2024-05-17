from flask import Flask, request

import database
db = database.database_instance

app = Flask(__name__)
port = 6565

@app.route("/news")
def get_summaries():
    amount = int(request.args.get("amount", 20))
    page = int(request.args.get("page", 0))
    
    r = db.get_processed_urls(amount, page)
    response = {
        'amount': amount,
        'page': page,
        'results':r
    }
    return response

def main():
    app.run(host="0.0.0.0", port=port)