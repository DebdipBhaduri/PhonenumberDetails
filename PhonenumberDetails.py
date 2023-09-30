import phonenumbers
from phonenumbers import timezone, geocoder, carrier

def get_phone_info():
    number = input("Enter Your Number with +__: ")
    phone = phonenumbers.parse(number)
    time = timezone.time_zones_for_number(phone)
    car = carrier.name_for_number(phone, "en")
    reg = geocoder.description_for_number(phone, "en")

    print(f"Phone Number: {phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
    print(f"Timezone: {', '.join(time)}")
    print(f"Carrier: {car}")
    print(f"Region: {reg}")

while True:
    print("\nPhone Number Information Lookup")
    get_phone_info()
    another = input("Do you want to look up another phone number? (yes/no): ").lower()
    if another != "yes":
        break

print("Goodbye!")
