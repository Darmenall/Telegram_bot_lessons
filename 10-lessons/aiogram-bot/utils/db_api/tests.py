# from sqlite import Database
#
#
# def test():
#     db = Database(path_to_db='test.db')
#     db.create_table_users()
#     db.add_user(1, "One", "email", 'ru')
#     db.add_user(2, "Alim", "Alim@gmail.com", 'uz')
#     db.add_user(3, 1, 1)
#     db.add_user(4, 1, 1)
#     db.add_user(5, "John", "john@mail.com")
#
#     users = db.select_all_users()
#     print(f"Hamme paydalaniwshilar: {users}")
#
#     user = db.select_user(Name="John", id=5)
#     print(f"Bir paydalaniwshini koriw: {user}")
#
#
#
# test()