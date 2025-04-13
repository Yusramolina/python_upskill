
class Items:


    def __init__(self, item_name: str = "unknown", item_price: int = 1):
        self.__item_name = None #private
        self.__item_price = None #private
        self.set_item_name(item_name)
        self.set_item_price(item_price)

    # Getter
    def get_item_name(self) ->  str:
        return self.__item_name

    # Getter
    def get_item_price(self) -> int:
        return self.__item_price

    # Setter
    def set_item_name(self, item_name):
        self.__item_name = item_name

    # Setter
    def set_item_price(self, item_price: int):
        if item_price <= 0:
            raise RuntimeError(f'Item price cannot be negative or zero:{item_price}')
        self.__item_price = item_price #Setter


item1 = Items()
item1.set_item_name("Laptop")
item1.set_item_price(100)

print(item1.get_item_name())
print(item1.get_item_price())

item2 = Items("Phone",6666)

print(item2.get_item_name())
print(item2.get_item_price())

