class User:
    def log(self):
        print(self)

class Teacher(User):
    def log(self):
        print("Iam a teacher")

class Customer(User):
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
    # Create a method
    def update_membership(self, new_membership):
        #invoke an API
        #update a database
        #charge the customer
        #calculate costs
        print("Calculating costs: ")
        self.membership_type = new_membership
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    #Overriding methods
    def __str__(self):
        print("converting to string")
        return self.name + " " + self.membership_type

    def print_all_customers(customers):
        for customer in customers:
            print(customer)
            
     # Overriding and comparing data        
    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False;
    
    __hash__ = None
    __repr__ = __str__
users = [Customer("Junaid","Gold"), Customer("Caleb", "Bronze"), Teacher()]

for user in users:
    user.log()