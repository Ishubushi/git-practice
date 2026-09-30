import requests 
print("Fetching a random quote from web API...") 
response = requests.get("https://dummyjson.com/quotes/random") 
data = response.json() 
print(f"Status Code: {response.status_code}") 
print(f"Quote: \"{data['quote']}\"") 
print(f"Author: - {data['author']}") 
