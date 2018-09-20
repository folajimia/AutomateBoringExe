from py_day_test import MessageUsers


obj = MessageUsers()
obj.add_user("Justin", 123.32, email="folajimia@gmail.com")
obj.add_user("john", 94.23, email="folajimia@gmail.com")
obj.add_user("Emilee", 124.32, email="folajimia@gmail.com")
obj.add_user("Jim", 323.4, email="folajimia@gmail.com")
print(obj.get_details())
print(obj.send_email())




