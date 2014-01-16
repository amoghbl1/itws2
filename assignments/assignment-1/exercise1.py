
__all__ = ["add_friend","add_friends","glob","make_globals","remove_user","get_friends","get_friends_of_friends"]

def make_globals():
	global Users, Acquaintances, Messages
	Users = {}
	Acquaintances = {}
	Messages = {}

def add_friend(user_id, friend_id):
	if Acquaintances.has_key(user_id):
		Acquaintances[user_id] = Acquaintances[user_id]+[friend_id]
	else:
		Acquaintances[user_id] = [friend_id]
	return "TRUE"

def add_friends(user_id, friends_id):
	for ids in friends_id:
		Acquaintances[user_id] = Acquaintances[user_id]+[ids]
	return "TRUE"

def remove_user(user_id):
	if not Acquaintances.has_key(user_id):
		return "FALSE"
	else:
		Acquaintances.pop(user_id)
		return "TRUE"

def get_friends(user_id):
	if not Acquaintances.has_key(user_id):
		return None
	else:
		return tuple(Acquaintances.values())

def get_friends_of_friends(user_id):
	return_tupple = ()
	for friends in get_friends(user_id):
		for fof in get_friends(friends):
			if not fof in get_friends(friends):
				return_tupple = return_tupple + fof
	return return_tupple
