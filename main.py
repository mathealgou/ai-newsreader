from news_api import NewsApi
import json

def main():
	news_api = NewsApi()
	content = news_api.get()
	print(json.dumps(content, indent=4))
 
if __name__ == "__main__":
    main()