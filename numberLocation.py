import phonenumbers
from phonenumbers import geocoder
import folium
number=input("Give Your Number with country code: ")

key="3fec379053c84a38a91085bf21f63c36"
samNumber=phonenumbers.parse(number)

yourLocation= geocoder.description_for_number(samNumber,"en")
print(yourLocation)

from phonenumbers import carrier

service_provider=phonenumbers.parse(number)
# print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query=str(yourLocation)
results=geocoder.geocode(yourLocation)
# print(query)
print(len(results))
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
myMap=folium.Map(location=[lat,lng],zoom_start=9)
for result in results:
    lat=result['geometry']['lat']
    lng=result['geometry']['lng']
    folium.Marker([lat,lng],popup=yourLocation).add_to(myMap)

# print(lat,lng)



myMap.save("myLocation.html")



