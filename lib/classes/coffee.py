class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []
        self._customers = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and not hasattr(self, "name"):
            self._name = new_name
        else: 
            raise Exception
        
    def orders(self, new_order=None):
        from classes.order import Order
        if isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        if isinstance(new_customer, Customer) and new_customer not in self._customers:
            self._customers.append(new_customer)
        return self._customers
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        my_sum = 0
        for order in self._orders:
            my_sum += order.price
        return my_sum / len(self._orders)