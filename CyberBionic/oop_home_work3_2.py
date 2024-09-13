class English:
    def greeting(self):
        return f'Good day'
    

class Spanish:
    def greeting(self):
        return f'Buenas tardes'


def hello_friend(*args) -> None:
    for lang in args:
        print(lang)


eng = English()
spa = Spanish()
hello_friend(eng.greeting(), spa.greeting())