import requests

def is_valid_word(word: str) -> bool:
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
           return True
        if response.status_code == 404:
           return False
        response.raise_for_status() #prevents from silently continuing    
    except requests.exceptions.HTTPError as e:
         print("HTTP error occurred:", e)
    except requests.exceptions.RequestException as e:
         print("A request error occurred:", e)
   
    return False