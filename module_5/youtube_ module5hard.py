from time import sleep


class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration  # продолжительность
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __eq__(self, other):
        return self.title == other.title


class UrTube:
    users = []
    videos = []
    current_user = None

    def register(self, nickname, password, age):
        for i in self.users:
            if nickname == str(i):
                return print(f"Пользователь {nickname} уже существует")
        user = User(nickname, password, age)
        self.users.append(user)
        self.log_in(nickname, password)

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname == str(i):
                if hash(password) == i.password:
                    self.current_user = i
                    return print(f"Вход выполнен под логином {self.current_user}")
        return print(f"Пользователя {nickname} нет в системе, зарегистрируйтесь")

    def log_out(self):
        self.current_user = None

    def add(self, *list_video: Video):
        for i in list_video:
            key_j = False
            for j in self.videos:
                if i == j:
                    print(f"Видео с названием \"{i}\" уже существует")
                    key_j = True
                    break
            if key_j is False:
                self.videos.append(i)

    def get_videos(self, search: str):
        answer_search = []
        for i in self.videos:
            if search.lower() in (str(i)).lower():
                answer_search.append(str(i))
        if answer_search:
            return answer_search
        else:
            return f"Видео по запросу {search} не найдено"

    def watch_video(self, title_video: str):
        if self.current_user is None:
            return print("Войдите в аккаунт, чтобы смотреть видео")
        current_video = self.find_video(title_video)
        if current_video:
            if current_video.adult_mode is True:
                if self.current_user.age < 18:
                    return print("Вам нет 18 лет, пожалуйста покиньте страницу")
            while current_video.time_now < current_video.duration:
                print(current_video.time_now)
                current_video.time_now += 1
                sleep(1)
            print("Конец видео")

    def find_video(self, title: str):
        for i in self.videos:
            if title == str(i):
                return i


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
