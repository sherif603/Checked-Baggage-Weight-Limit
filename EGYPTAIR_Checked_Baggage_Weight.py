# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 15:00:34 2020

@author: hp
"""

# EGYPTAIR is known as the seventh carrier in the world and was founded in May 1932.
# EGYPTAIR is based at Cairo International Airport in Egypt and Serves more than 70 destinations.
# The airline serves Egypt, Africa, the Americas, Asia, Europe, and the Middle East.
# EGYPTAIR Baggage

# Carry-on Allowance:
# Passangers are subject to the following hand luggage restrictions on the 
# international and domestic flights:
# Business - two pieces of hand luggages with a maximum weight of 16 kg and one personal item.
# Economy - one piece of hand luggage with a maximum weight of 8 kg and one personal item.

# Checked Baggage:
# Passangers are entitled to the following free baggage allowance on international routes:
# Business - two pieces of baggages with a maximum weight of 32 kg (70 Ibs),
# and maximum dimensions of 158 cm (62 in).
# Economy - two pieces of baggages with a maximum weight of 23 kg (50 Ibs),
# and maximum dimensions of 158 cm (62 in).

print("EGYPTAIR")
print("Cairo International Airport")
print("Passenger name: Sherif Sakr")

checked_baggage = [("Baby Stroller",16),
                   ("Printer",5),
                   ("Portable Oxygen Concentrator",2),
                   ("Hardcover Book",2),
                   ("Infant car seat",8),
                   ("Personal Computer",10)]
weight = 0
items = []
for baggage_name, baggage_weight in checked_baggage:
    print("\nCurrent checked baggage weigh: {}".format(weight))
    if weight >= 32:
        print("You are exceed the free baggage allownce!")
        break
    elif weight + baggage_weight > 32:
        print("Skipping {} ({})".format(baggage_name,baggage_weight))
        continue
    else:
        print("Adding Baggage Items {} ({})".format(baggage_name,baggage_weight))
        items.append(baggage_name)
        weight += baggage_weight
print("\nFinal free baggage allowance weight: {}".format(weight))
print("Final Checked Baggage Items: {}".format(items))        