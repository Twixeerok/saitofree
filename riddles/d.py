
class Nu:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

    def sad(self):
        while True:
            try:
                self.x = input('num 1 ')
                if self.x == 'стоп':
                    break
                self.y = int(input('num 2 '))
                res = int(self.x) + int(self.y)
                print(res)
            except Exception as e:
                print(f'Ошибка: {e}')
    
    def good(self):
        while True:
            try:
                self.x = input('num 1 ')
                if self.x == 'стоп':
                    break
                self.y = int(input('num 2 '))
                res = int(self.x) - int(self.y)
                print(res)
                return ch()
            except Exception as e:
                print(f'Ошибка: {e}')

a = Nu()
def ch():
    s = input('Плюс или минус? ')
    if s.lower() == 'плюс':
        a.sad()
    elif s.lower() == 'минус':
        a.good()


ch()