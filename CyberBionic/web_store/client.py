class Client:
    def __init__(
        self,
        client_id: int,
        client_name: str,
        client_email: str,
        client_phone: str,
        client_address: str,
    ):
        self.client_id = client_id
        self.client_name = client_name
        self.client_email = client_email
        self.client_phone = client_phone
        self.client_address = client_address
        self.client_order_history = []

    def add_order(self, order):
        self.client_order_history.append(order)
        print("Added order")
    
    def remove_order(self, order_id):
        for order in self.client_order_history:
            if order.get("order_id") == order_id:
                self.client_order_history.remove(order)
                print(f"Removed order {order_id}")
            else:
                print(f'order_id {order_id} didn`t find')
    
    def get_order_history(self):
        return self.client_order_history
    
    def update_client(self, new_client_name: str, new_client_email: str, new_client_phone: str, new_client_address: str)
        self.client_name = new_client_name
        self.client_email = new_client_email
        self.client_phone = new_client_phone
        self.client_address = new_client_address
        print("Client`s info updated")

    def __str__(self):
        return f"Client ID: {self.client_id}, Name: {self.client_name}, Email: {self.client_email}, Phone: {self.client_phone}, Address: {self.client_address}"