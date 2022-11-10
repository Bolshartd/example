class Products:
    def __init__(self, color_phone, phone_type): 
        self.color_phone = color_phone
        self.phone_type = phone_type
      
class Money:
    def __init__(self, value):
        self.value = value

class Buying_phone:
    def __init__(self, store_products: Products, my_money: Money):
        self.phone_color(store_products.color_phone)
        self.tele_type(store_products.phone_type, my_money.value, store_products.color_phone)
    
    def phone_color(self, color_phone):
        choose_color = input (f"Write the color \n {color_phone.values()}\n")
        if choose_color in color_phone.values():
            return color_phone.values()
        else:
            print ("Sorry, there is no such color... Try again\n")
            return Buying_phone.phone_color(self, color_phone)

    def tele_type(self, phone_type, value, color_phone):
        choose_type = input (f"Write the model from the list \n {phone_type.keys()}\n")
        if choose_type in phone_type.keys():
                if phone_type[choose_type] <= my_money.value:
                    print ("Congrat's with buy")
                    return
                else:
                    print("Sorry, you don't have enough money")
        else:
            print ("Sorry, there is no such type of the phone... Try again\n")
        return Buying_phone.tele_type(self, phone_type, value, color_phone)

store_products = Products({"Iphone": "Red", "Samsung": "White", "Sony": "Black", "Honor": "Yellow"}, 
{"Iphone": 46200, "Samsung": 52800, "Sony": 49900, "Honor": 50000})
my_money = Money(48920)
bye = Buying_phone(store_products, my_money)