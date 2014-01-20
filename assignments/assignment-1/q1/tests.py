import q1
q1.make_globals()
q1.Users = {"uid1":("u1","p1","dob1"),"uid2":("u2","p2","dob2"),"uid3":("u3","p3","dob3"),"uid4":("u4","p4","dob4"),"uid5":("u5","p5","dob5")}

q1.add_friend("uid1","uid2")
q1.add_friend("uid2","uid3")
q1.add_friend("uid3","uid4")
q1.add_friend("uid4","uid5")
q1.add_friends("uid1",("uid3","uid4","uid5"))

q1.remove_user("uid1")

q1.get_friends("uid4")
q1.get_friend_of_friends("uid2")
q1.get_friend_of_friends("uid3")

q1.send_message("uid4","uid5","hey buddy!")

q1.send_group_message("uid4",("uid5","uid3","uid2"),"hey buddy!")

q1.get_messages_from_friend("uid5","uid4")

q1.get_messages_from_all_friends("uid5")
q1.get_messages_from_all_friends("uid4")

q1.get_birth_day_messages("uid2")
q1.get_birth_day_messages("uid3")

#commented out because message id is only obtained on runtime!
#q1.delete_message("uid5", messageID)
#q1.delete_messages("uid5" , messageID's tupple)

q1.delete_all_messages("uid5")
