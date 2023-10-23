from decouple import config
import requests
import json

class NewsApi():
    """This is gonna be a hell of a mess"""
    def get(self):
        API_KEY = config('NEWS_API_KEY')
        category = "technology" 
        country = "us"
        url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}"
        
        response = requests.get(url, headers={"X-Api-Key": API_KEY})
        
        if response.status_code == 200:
            content = response.json()
            
            # Title, and description with escape characters removed
            clean_content = {
                "title": content["articles"][0]["title"].encode('ascii', 'ignore').decode('ascii'),
                "description": content["articles"][0]["description"].encode('ascii', 'ignore').decode('ascii')
            }
            
            return clean_content
        else:
            raise Exception("Error: API request unsuccessful. Check API key, and query parameters.")
            return None