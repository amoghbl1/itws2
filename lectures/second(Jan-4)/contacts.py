
from phonenum import *

def create_contacts():
	return {}

def add_contacts(contacts, name, phone_num, phone_type):
    if contacts.has_key(name):
        phone_nums = contacts[name]
        phone_nums.append(Phonenum(phone_num, phone_type))
    else:
    	contacts[name] = [ Phonenum(phone_num, phone_type) ]

