
__all__ = ["add_friend", "add_friends", "glob", "make_globals", "remove_user", "get_friends", "get_friends_of_friends", "send_message", "send_group_message", "get_messages_from_friend", "get_messages_from_all_friends", "get_birth_day_messages", "delete_message", "delete_messages", "delete_all_messages", "delete_messaged_from_friend"]

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
	return True

def add_friends(user_id, friends_id):
	for ids in friends_id:
		Acquaintances[user_id] = Acquaintances[user_id]+[ids]
	return True

def remove_user(user_id):
	if not Acquaintances.has_key(user_id):
		return False
	else:
		Acquaintances.pop(user_id)
		return True

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

def send_message(sender_id, receiver_id, msg):
	message (sender_id, time.strftime("%D-%H:%M:%S"), msg, time.strftime("%D"), time.strftime("%H:%M:%S"))
	if Messages.has_key(receiver_id):
		Messages[receiver_id] += message
	else:
		Messages[receiver_id] = message
	return True

def send_group_message(sender_id, receiver_tupple, msg):
	if not Users.has_key(sender_id):
		return False
	for r in receiver_tupple:
		if not Users.has_key(r):
			return False
	for receiver in receiver_tupple:
		send_message(sender_id, receiver, msg)

def get_messages_from_friend(receiver_id, friend_id):
	if not Users.has_key(receiver_id):
		return None
	elif not Acquaintances[receiver_id].__contains__(friend_id):
		return None
	return_tupple = ()
	for i in Messages[receiver_id]:
		for j in i:
			if j.__contains__(friend_id):
				return_tupple += j
	return receiver_tupple

def get_messages_from_all_friends(receiver_id):
	return_tupple = ()
	for friend in Acquaintances[receiver_id]:
		return_tupple += get_messages_from_friend(receiver_id, friend)
	return return_tupple

def get_birth_day_messages(receiver_id):
	birthday = Users[receiver_id][2]
	return_tupple = ()
	for messages in get_messages_from_all_friends(receiver_id):
		for message in messages:
			if messages.__contains__(birthday):
				return_tupple += messages
	return return_tupple

def delete_message(user_id, msg_id):
	for messages in get_messages_from_all_friends(user_id):
		for message in messages:
			if message.__contains__(msg_id)
				messages.remove(message)

def delete_messages(user_id, messages_tupple):
	for message in messages_tupple:
		delete_message(user_id, message)


