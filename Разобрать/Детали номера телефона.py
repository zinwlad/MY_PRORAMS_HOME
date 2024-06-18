# To get the details of any number, we can use an amazing Python module known as phonenumbers. This module is created
# by David Drysdale and you can use it to get the details of any phone number from anywhere in the world.
#
# To install this Python module on your system, you can use the pip command on your terminal or the command prompt
# mentioned below:
#
# pip install phonenumbers
# There are a lot of details you can find about a number using this Python module. Here’s how you can find some
# of the basic details about a phone number using Python:

import phonenumbers as ph
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

number = input("+9185XXXXXXXX ")
number = ph.parse(number)
print(timezone.time_zones_for_number(number))
print(carrier.name_for_number(number, "en"))
print(geocoder.description_for_number(number, "en"))