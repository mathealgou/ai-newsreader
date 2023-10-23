from modules import NewsApi, TextToSpeech
import json

def main():
    # Get some content, it ain't much but it's honest work, will do for now
	news_api = NewsApi()
	content = news_api.get()
	
	text_to_speech = TextToSpeech()
	text_to_speech.read_article(content)
 
if __name__ == "__main__":
    main()