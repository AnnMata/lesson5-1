# Система управления учетными записями пользователей

class User:

    def __init__(self, user_id, name, access='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access = access

    def get_user_id(self):
        return self.__user_id

    def get_user_name(self):
        return self.__name

    def get_user_access(self):
        return self.__access


class Admin(User):
    def __init__(self, user_id, name, access='admin'):
        super().__init__(user_id, name, access)
        self.__users_list = []

    def add_user(self, user):
        self.__users_list.append(user)

    def remove_user(self, user_id):
        for user in self.__users_list:
            if user.get_user_id() == user_id:
                self.__users_list.remove(user)
                return f'Пользователь {user.get_user_name()} с ID {user_id} успешно удален.'
        return 'Пользователь с таким ID не найден.'


user1 = User(1, "Петров")
user2 = User(2, "Васечкин")
admin = Admin(3, "Админ")

admin.add_user(user1)
admin.add_user(user2)

print(user1.get_user_name())
print(user2.get_user_name())

print(admin.get_user_access())
print(admin.remove_user(1))
