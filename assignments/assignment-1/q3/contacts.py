
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
	new_contact_list = []
	flag = False
	if not contacts.has_key(contact_name):
		return False
	elif contacts.has_key(contact_name):
		for contact in contacts[contact_name]:
			if not contact.__contains__(old_number):
				new_contact_list.append(contact)
			elif contact.__contains__(old_number):
				flag = True
				new_contact_list.append((new_number, contact[1]))
	contacts[contact_name] = new_contact_list
	return flag
