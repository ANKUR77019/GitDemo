class Phone:
    phone_directory=[]

    def __init__(self,name,number):
        self.name=name
        self.number=number
        Phone.phone_directory.append(self)

    def show_contact(self):
        print(f"name-{self.name},number-{self.number}")

    @classmethod
    def show_all_contact(cls):
        if len(cls.phone_directory)==0:
            print("No contact in phone directory")
        else:
            for i in cls.phone_directory:
                i.show_contact()
    @classmethod
    def search_contact(cls,name):
        for contact in cls.phone_directory:
            if contact.name.lower()==name.lower():
                print(f" It is present {name}-{contact.number}")
                break

            print(f" following details of {name} not available")
            break
    @staticmethod
    def validate(number):
        if len(number)==10 and number.isdigit() :
           return True
        else:
           return False


n=int(input("Enter number of contacts you want to enter: "))
for i in range(n):
    name=input("Enter name of contact: ")
    number=input("Enter the mobile number: ")
    if Phone.validate(number):
        Phone(name,number)
    else:
        print(f"Invalid phone number for {name}")

Phone.show_all_contact()