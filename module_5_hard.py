class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    users = []
    videos = []
    current_user = None

    def register(self, nickname, password, age):
        num_of_users = len(self.users)
        if num_of_users == 0: # Это нужно для регистрации первого пользователя
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            print(f"Пользователь с именем {nickname} успешно зарегистрирован!")
        else:
            for user in self.users:
                num_of_users -= 1
                if user.nickname == nickname:
                    print('Пользователь с таком именем уже существует!')
                    break # Если есть пользователь в базе, не надо дальше перебирать
                elif user.nickname != nickname and num_of_users == 0:
                    new_user = User(nickname, password, age)
                    self.users.append(new_user)
                    print(f"Пользователь с именем {nickname} успешно зарегистрирован!")
                    break # без этого прерывания цикл проходит по только что добавленному пользователю?


    def log_in(self, nickname, password):
        num_of_users = len(self.users)
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print(f'{nickname}, вы успешно авторизовались!')
                break
            elif user.nickname != nickname or user.password != hash(password) and num_of_users == 0:
                print('Неправильный логин или пароль')

if __name__ == '__main__':
    ur = UrTube()
    vid1 = Video('Борька ест кашу', 250, 14, True)
    print(vid1.time_now)
    usr1 = User("Гена", 'lolkekcheburek', 14)
    usr2 = User('Victor', 'Hjp89%t,jk', 44)
    ur.register('Victor', "12345678", 28)
    ur.register('Vasyok', "987654321", 13)
    ur.register('Victor', "678", 33)
    ur.log_in('Victor', "12345678")
    ur.log_in('Victor', "1235678")
