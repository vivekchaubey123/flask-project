from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db
collection = db.items

@app.route("/submittodoitem", methods=["POST"])
def submit():
    itemName = request.form.get("itemName")
    itemDescription = request.form.get("itemDescription")

    data = {
        "name": itemName,
        "description": itemDescription
    }

    collection.insert_one(data)

    return "Item Saved"

if __name__ == "__main__":
    app.run(debug=True)