import pyttsx3
from datetime import datetime

class TextToSpeech():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 100)
        self.engine.setProperty('volume', 1.0)
        
    def read_article(self, article):
        """Creates an audio file (.mp3) from the article, returns the file path"""
        
        # "Read" the article
        text = article["title"] + ". " + article["description"]
        
        # Save to file
        # TODO: Remember to delete the file after doing the thing
        
        
        file_path = f"source_files/output.mp3"
        self.engine.save_to_file(text, file_path)
        
        # Run the engine
        self.engine.runAndWait()
        
        return file_path