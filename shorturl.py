from uuid_shortener import UuidShortener
import uuid

def shorten_url(url):
     shortener = UuidShortener("http://grace/")
     uuid_5 = uuid.uuid5(uuid.NAMESPACE_URL,url)
     short_uuid = shortener.shorten(uuid_5)
     print(type(short_uuid))
     url_dict[short_uuid] = url
     print('the shorter url is: ',short_uuid)
     
         
def get_original_url(short_url):
    found = 0
    for key in url_dict.keys():
            if short_url in key:
                found = 1
                print ("the original url is :",url_dict[key])
    if(found == 0):
        print("HTTP 404")
   
        
url = input("Enter an url: ")
url_dict = {}
shorten_url(url)
long_url = input("Enter a short url: ")
get_original_url(long_url)
print("have a good day")
