
from contacts import create_contacts
from contacts import add_contacts
from phonenum import *

def test_add_multiple_contact_numbers():
    c = create_contacts()
    add_contacts(c, 'ken', "1234567890", "home")
    add_contacts(c, 'ken', "2345678901", "work")
    add_contacts(c, 'ken', "2345678902", "work")
    assert(len(c.keys()) == 1)

def test_generic_contacts_behavior():
	contacts = {}
	contacts["Guido"] = Phonenum("0987654321", "home")
	contacts["Ritchie"] = Phonenum("5678904321", "home")
	contacts["Rob"] = Phonenum("1234567890", "work")
	contacts["Steve"] = Phonenum("1234567", "work")
	assert(len(contacts.keys()) == 4)

	phone_steve = contacts["Steve"] 
	assert(phone_steve is None)

	try:
	    phone_ken = contacts["ken"]
	    assert(0)
	except KeyError as e:
		assert(1)


if __name__ == '__main__':
    test_generic_contacts_behavior()
    test_add_multiple_contact_numbers()


