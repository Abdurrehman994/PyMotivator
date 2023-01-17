import requests
from twillio_conn import send_whatsapp_text,client
def get_quote_of_the_day(category):
    """
    Get a Quote from rest API by category
    """
  
    url="https://quotes.rest/qod?language=en&category={}".format(category)
    # quote="testing"
    response=requests.get(url=url)
    data_dict=response.json()
    status=response.status_code
    print(status)
    match status:
        case 200:
            quote=data_dict['contents']['quotes'][0]['quote']
        case 400:
            quote=data_dict['error']['message']
        case _:
            quote="sorry we could not get the code"
    return quote

quote=get_quote_of_the_day(category="inspire")
send_whatsapp_text(client,quote)