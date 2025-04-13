
class Item:

    def __init__(self, item_name: str = "unknown", item_price: int = 1):
        self.__item_name = None  # private
        self.__item_price = None  # private
        self.item_name = item_name
        self.item_price = item_price


    @property #Getter
    def item_name(self) -> str:
        return self.__item_name

    @property #Getter
    def item_price(self) -> int:
        return self.__item_price

    @item_name.setter #Setter
    def item_name(self, name):
        self.__item_name = name

    @item_price.setter #Setter
    def item_price(self, price):
        if price <= 0:
            raise RuntimeError(f'Item price cannot be negative or zero:{price}')

        self.__item_price = price

item1 = Item()
item1.item_name = "Laptop"
print(item1.item_name)
