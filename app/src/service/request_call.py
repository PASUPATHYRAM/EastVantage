import requests
import asyncio

base_url='https://api.opencagedata.com/geocode/v1/json?q='
api_key='' #your api key

def make_request(search):
    url=base_url+search+'&key='+api_key
    to=search.split(',')
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        extracted_data={}
        if data:
            extracted_data['lat']=data['results'][0]['geometry']['lat']
            extracted_data['long']=data['results'][0]['geometry']['lng']
            extracted_data['state']=data['results'][0]['components']['state']
            extracted_data['city']=data['results'][0]['components'].get('town',to[1])
            extracted_data['country'] = data['results'][0]['components']['country']
            extracted_data['zipcode']=data['results'][0]['components']['postcode']
            extracted_data['address']=search
            return extracted_data
        else:
            print("address not found")
    else:
        print(response.status_code)

# print(make_request('1700 Swanson Drive, Rock Springs, WY 82901'))





