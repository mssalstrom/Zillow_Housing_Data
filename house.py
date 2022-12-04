class House:
    def __init__(self, address, price, city, state, zip_code, living_area, bedroom, bath):
        self.address = address
        self.price = price
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.living_area = living_area
        self.bedroom = bedroom
        self.bath = bath

    def print_house(self):
        print('-----------------------')
        print(f'{"Address: ":<20}{self.address}')
        print(f'{"Price: ":<20}${self.price:,.2f}')
        print(f'{"Location: ":<20}{self.city}, {self.state}, {self.zip_code}')
        print(f'{"Square Footage: ":<20}{self.living_area}')
        print(f'{"Bedroom Count: ":<20}{self.bedroom}')
        print(f'{"Bathroom Count: ":<20}{self.bath}')
        print('-----------------------')

    def get_address(self):
        return self.address

    def get_price(self):
        return self.price

    def get_bedroom_count(self):
        return self.bedroom

    def get_bathroom_count(self):
        return self.bath

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip(self):
        return int(self.zip_code)

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price
