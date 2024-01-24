#!/usr/bin/python3
from googlesearch import search
import sys

def search_phone_number(number, language):
    if language == 'pt-br':
        print("Procurando fontes em que o número foi divulgado...")
    elif language == 'english':
        print("Looking for sources where the number was disclosed...")
    elif language == 'hindi':
        print("उन स्रोतों की तलाश की जा रही है जहां संख्या का खुलासा किया गया था...")

    query = f'"{number}"'
    results = list(search(query, num=1000000000, stop=1000000000, pause=2))  

    if not results:
        if language == 'pt-br':
            print("Parabéns! Seu número não foi divulgado.")
        elif language == 'english':
            print("Congratulations! Your Number Has Not Been Leaked.")
        elif language == 'hindi':
            print("बधाई हो! आपका नंबर लीक नहीं हुआ है.")
    else:
        if language == 'pt-br':
            print(f"Seu número foi divulgado em:")
        elif language == 'english':
            print(f"Your Number Was Leaked In:")
        elif language == 'hindi':
            print(f"आपका नंबर इसमें लीक हो गया था:")

        for site in results:
            print(site)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Err.")
    else:
        phone_number = sys.argv[1]
        language = sys.argv[2][2:]  
        search_phone_number(phone_number, language)
  
