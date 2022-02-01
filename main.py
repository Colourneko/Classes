#import Address

is_for_sale = bool
num_of_room = int
price = float
address = str

class House:
    def __init__(self, is_for_sale:bool,num_of_room:int,price:float ,address:str):
        self._is_for_sale = is_for_sale
        self._num_of_room = num_of_room
        self._price = price
        self._address = address
        #super(Address.street, Address.city,Address.province,Address.postal_code,Address.country)

    def get_is_for_sale(self):
        return self._is_for_sale

    def get_num_of_room(self):
        return self._num_of_room

    def get_price(self):
        return self._price

    def get_address(self):
        return self._address


    def set_is_for_sale(self, is_for_sale):
        self._is_for_sale = is_for_sale

    def set_num_of_room(self,num_of_room):
        self._num_of_room = num_of_room

    def set_price(self, price):
        self._price = price

    def set_address(self, address):
        self._address = address

    def open_garage_door(self):
        return f'the garage dooe is opening'
    def mow_lawn(self):
        return f'the lawn is being mowed'
    def clean_up(self):
        return f'the house is being cleaned'

new_test = House(is_for_sale = True ,num_of_room = 10 ,price = 999.999 ,address = "1ppd" )
test = House(is_for_sale = True ,num_of_room = 11 ,price = 1999.999 ,address = "2ppd")
#test1 = Address(street ="Roachesline", city = "Bay Roberts", province = "NewFoundLand", postal_code ="A1A 4G0", country ="canada")





print(new_test.open_garage_door())
print(new_test.mow_lawn())
print(new_test.clean_up())
print(test.get_is_for_sale())
#print(test1.Address.street)