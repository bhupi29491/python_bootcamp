class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"storage type: {cls.storage_type}")

    def get_info(self):
        print(f"laptop has {self.RAM} RAM & {self.storage} storage {self.storage_type}")

    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"Discounted final price: {final_price}")

l1 = Laptop("16gb", "512gb")
l2 = Laptop("256gb", "512gb")

# l1.get_info()
# l2.get_info()
#
# Laptop.get_storage_type()
# l1.get_storage_type()
# l2.get_storage_type()

l1.calc_discount(90_000, 10)