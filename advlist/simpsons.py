#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""



challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

x= challenge[2][1]
y= challenge[2][0]
z= challenge[3]

print(f"My {x}! The {y} do {z}!")

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

x= trial[2]["goggles"]
y= trial[2]["eyes"]
z= trial[3]

print(f"My {x}! The {y} do {z}!")

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

x= nightmare[0]["user"]["name"]["first"]
y= nightmare[0]["kumquat"]
z= nightmare[0]["d"]

print(f"My {x}! The {y} do {z}!")

