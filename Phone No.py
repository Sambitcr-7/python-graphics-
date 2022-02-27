import phonenumbers
from phonenumbers import timezone,geocoder,carrier

phonenumbers = phonenumbers.parse("+917739376261")

timezone = timezone.time_zones_for_number(phonenumbers)

carrier = carrier.name_for_number(phonenumbers,'en')

Region = geocoder.description_for_number(phonenumbers,'en')

print(phonenumbers)
print(timezone)
print(carrier)
print(Region)