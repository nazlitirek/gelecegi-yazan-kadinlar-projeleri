import requests
BASE_URL = "https://gyk.halitkalayci.com/blogs"
def get_blogs():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json()
    return f"hata oluştu : {response.status_code} {response.text}"

print(get_blogs())

def create_blogs(title, content,author) :
    payload = {
        "title" : title,
        "content" : content,
        "author" : author
    }
    response = requests.post(BASE_URL, json=payload)
    if response.status_code == 201:
        return response.json()
    return f"hata oluştu : {response.status_code} {response.text}"