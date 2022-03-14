from  flask import Flask, jsonify
from bs4 import BeautifulSoup as bs
import json, random, string , requests

from config import PORT
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home_page():

    url = F"https://www.dictionary.com/e/word-of-the-day/"

    response = requests.get(url)
    Status = response.status_code
    soup = bs(response.text,"lxml")
    anchor1= soup.find_all('div',"otd-items wotd-items")
    for element in anchor1:
        Date = element.find('div',"otd-item-headword__date").text.strip()
        Word = element.find('div',"otd-item-headword__word").text.strip()
    anchor1= soup.find('div',"otd-item-headword__pos-blocks")
    Class = anchor1.find('span',"luna-pos").text.strip()
    element = anchor1.find_all('p')[-1]
    Meaning = element.get_text()
    Sound = soup.find_all('div',"otd-item-headword__pronunciation")
    for i in Sound:
        a = i.find('a')["href"]
        Voice = a
        break
    
    def main():
       (Date,Word,Class,Meaning,Voice)
    Word_Detail = {}
    Word_Detail = {
        
        'Status': Status,
        'Date': Date,
        'Word': Word,
        'Class': Class,
        'Meaning': Meaning,
        'Pronounce': Voice
        }

    New_Data = str(json.dumps(Word_Detail, indent = 2))
    main()
    with open("word.json", "w") as file:
       file.write(f"[{New_Data}]")
       file.write("\n") 
       json_dump = Word_Detail
       return json_dump

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port= PORT)
