
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        coffee.orders(self)
        coffee.customers(customer)
        customer.orders(self)
        customer.coffees(coffee)
        self.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if isinstance(new_price, (int, float)) and 1 <= new_price <= 10:
            self._price = new_price
        else:
            raise Exception("Price must be a number between 1 and 10!")
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, new_customer):
        from classes.customer import Customer
        if isinstance(new_customer, Customer):
            self._customer = new_customer
        else:
            raise Exception("Invalid Customer!")
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, new_coffee):
        from classes.coffee import Coffee
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee
        else:
            raise Exception("Invalid Coffee!")
