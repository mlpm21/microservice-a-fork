## Microservice A: Product Search
### Communication Contract:
- Base URL: ***http://127.0.0.1:5005***  
- Endpoint: ***/search***  
- Method: ***GET***  

#### How to programmatically REQUEST data:
- You can request data using an HTTP GET request with a required keyword parameter to the microservice at localhost:5005/search.
- Valid keywords are case-insensitive and must match part of a product name (e.g. "fuji", "200", "kodak400", etc.). 
```
# Example call:
import requests
response = requests.get("http://localhost:5005/search", params={"keyword": "kodak"})
``` 

#### How to programmatically RECEIVE data:
- After making the request, parse the returned JSON response.
```
# Example call:
data = response.json()
print(data)

# If keyword is found:
["Kodak200", "Kodak400"]

# If keyword is not found:
["Error: Keyword not found!"]

# If keyword is missing:
["Error: Keyword missing!"]
```
### UML Sequence Diagram
![UML Sequence Diagram](/CS361_UML_Sequence_Diagram.png)
