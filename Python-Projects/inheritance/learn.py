from chef import Chef
from asianchef import AsianChef

myChef = Chef()
myChef.makes_surprise_dish()

myAsianChef = AsianChef()
myAsianChef.make_fried_rice()
myAsianChef.make_salad() # inheritance
myAsianChef.makes_surprise_dish() # inheritance
