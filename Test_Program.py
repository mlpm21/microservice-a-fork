# Author: Ho Gia Bao Le
# Date: 08/04/2025
# Description: Test program for microservice A.

import requests

while True:
    keyword = input("Enter product keyword: ")
    try:
        response = requests.get("http://localhost:5005/search", params={"keyword": keyword})
        data = response.json()
        print("Search Result:", data)
    except Exception as e:
        print("Failed to connect to microservice:", e)
    print("------------------------------")