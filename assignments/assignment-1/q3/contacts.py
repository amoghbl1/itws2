
from phonenum import *

def create_contacts():
	return {}

def add_contacts(contacts, name, phone_num, phone_type):
    if contacts.has_key(name) and (len(phone_num) == 10 or len(phone_num) == 14):
        phone_nums = contacts[name]
        phone_nums.append(Phonenum(phone_num, phone_type))
    elif len(phone_num) == 10 or len(phone_num) == 14:
		contacts[name] = [ Phonenum(phone_num, phone_type) ]


def update_contact_number(contacts, contact_name, old_number, new_number):
	if not contacts.has_key(contact_name):
		return "ERROR: CONTACT NOT FOUND"
	elif (len(new_number) != 10 and len(new_number) != 14):
		return "ERROR: NEW NUMBER LENGTH IS INVALID , PLEASE PROVIDE LENGTH 10 OR 14"


