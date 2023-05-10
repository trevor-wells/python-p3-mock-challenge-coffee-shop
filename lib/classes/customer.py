class Customer:
    def __init__(self, name):
        self.name = name
        self._coffees = []
        self._orders = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name
        else:
            raise Exception("Name must be a string between 1 and 15 characters!")
        
    def orders(self, new_order=None):
        from classes.order import Order
        if isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
    
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        if isinstance(new_coffee, Coffee) and new_coffee not in self._coffees:
            self._coffees.append(new_coffee)
        return self._coffees
    
    def create_order(self, coffee, price):
        from classes.order import Order
        Order(self, coffee, price)