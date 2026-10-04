import os
import time
while True:
    print(
        '''
    Выбирите приложение для запуска: 
    1) Steam 
    2) Firefox
    3) Alacrrity
    4) Discord
    5) Visual studio code
    '''
    )

    def steam():
        os.system('steam')

    def firefox():
        os.system('firefox')

    def shell():
        os.system('alacritty')

    def discord():
        os.system('discord')

    def code():
        os.system('code')
    
    while True:
        try:
            vvod = int(input('Выберите Приложение: '))
            if vvod in range(1, 6):
                break
            elif vvod not in range(1,6):
                print('Вводите только числа в диапозоне от 1 до 5')
        except ValueError:
            print('#ошибка Вводите только числа')
   

    if vvod == 1:
        steam()
    elif vvod == 2:
        firefox()
    elif vvod == 3:
        shell()
        
    elif vvod == 4:
        discord()
    elif vvod == 5:                       
        code()
    
    vvod2 = str(input(f'Хотите запустить что то еще?\nY or N: '))
    if vvod2 == 'y':
        continue
    if vvod2 == 'n':
        print('спасибо за использование :3')
        break    