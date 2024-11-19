#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - My iffy script."""


message = 'With that grade you should probably'

# wrap connection in a float() to accept decimals as numbers
connection = float(input("What did you score on your math test?"))
# if input value was higher or equal to 25
if connection >= 95:
    message = message + 'ask your parents for more allowance'
elif connection >= 75:
    message = message + 'study a bit harder'
elif connection >= 60:
    message = message + 'consider a trade school'
else:
    message = message + 'tell your parents your dog ate it'
print(message)
