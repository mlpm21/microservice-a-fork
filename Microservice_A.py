# Author: Ho Gia Bao Le
# Date: 08/04/2025
# Description: Implement microservice A for Lapatrada Liawpairoj (Mint).

from flask import Flask, request, jsonify
app = Flask(__name__)

def product_search(query):
    products = [
        "Kodak200", "Fujifilm200", "Cinestill200", "Lomography200",
        "Kodak400", "Fujifilm400", "Cinestill400", "Lomography400",
    ]
    query = query.strip().lower()
    result = []
    for product in products:
        if query.lower() in product.lower():
            result.append(product)
    return result

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("keyword", "")
    print(f"Keyword received: {query}")
    print(f"Responding...")
    if not query:
        print("Error: Keyword missing!")
        return jsonify(["Error: Keyword missing!"]), 400
    result = product_search(query)
    if not result:
        print("Error: Keyword not found!")
        return jsonify(["Error: Keyword not found!"]), 404
    else:
        print(f"Result is: {result}")
        return jsonify(result)

if __name__ == "__main__":
    app.run(port=5005)