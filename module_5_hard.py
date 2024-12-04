import time

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
                    self.log_in(nickname, password)
                    break # без этого прерывания цикл проходит по только что добавленному пользователю?


    def log_in(self, nickname, password):
        num_of_users = len(self.users)
        for user in self.users:
            num_of_users -= 1
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print(f'{nickname}, вы успешно авторизовались!')
                # print(self.current_user)
                break
            elif user.nickname != nickname or user.password != hash(password):
                if num_of_users == 0:
                    print('Неправильный логин или пароль')
                else:
                    continue

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        sum_of_videos = len(self.videos)
        for item in args:
            if sum_of_videos == 0:
                self.videos.append(item)
            else:
                for video in self.videos:
                    if video.title != item.title:
                        self.videos.append(item)
        # print(self.videos) # Проверка. Добавились видосы или нет

    def get_videos(self, search_string):
        for item in self.videos:
            if search_string.lower() in item.title.lower():
                print(f'{item.title}')
            # else:
            #     print(f'Слово "{search_string}" не найдено')

    def watch_video(self, watched_title):
        sum_of_videos = len(self.videos)
        for item in self.videos:
            sum_of_videos -= 1
            if watched_title in item.title:
                # print('Проверяем что сейчас в current_user:', self.current_user)
                if self.current_user == None:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                elif item.adult_mode == True and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    for i in range(1, 11):
                        print(i, end=' ', flush=True)
                        time.sleep(0.5) # Поставил меньше 1, чтобы "время" быстрее шло..
                    print('Конец видео')
            elif sum_of_videos == 0:
                print("Такого видео нет")

if __name__ == '__main__':
    # My chek
    # ur = UrTube()
    # vid1 = Video('Борька ест кашу', 250, 14, True)
    # print(vid1.time_now)
    # usr1 = User("Гена", 'lolkekcheburek', 14)
    # usr2 = User('Victor', 'Hjp89%t,jk', 44)
    # ur.register('Victor', "12345678", 28)
    # ur.register('Vasyok', "987654321", 13)
    # ur.register('Victor', "678", 33)
    # ur.log_in('Victor', "12345678")
    # ur.log_in('Victor', "1235678")
    # ur.log_in('Гурген', "12356")

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')