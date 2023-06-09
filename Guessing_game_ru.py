# Импортируем
import random

# Функция которая проверяет ввёл ли пользователь правильное число
def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= 100

# Знакомства
print('-------------------------------')
print('Компютер загадал число, от 1 до 100 поптобуйте угадать!')
print('У вас сейчас на счету 100 очков за каждую ошибку вы теряете 15 очков за каждый выигрыш 20 очков')


# Переменная которая запрашивает продолжение игры
play_again = ''
# Переменная для подсчитание игр
game = 0
# Переменная для попыток
attemts = 0
# Список удачливых попыток
attemts_lst = []

# Очки
point = 100

record_attemts = 0
record_attemts_lst = []



# Главный цикл
while play_again == '':

    # Переменная для подбора случайный цифр
    pc_number = random.randrange(10, 99)

    # Флаг для остановки внутренного цикла
    flag = True





    # Внутренный цикл
    while flag:

        # Собираем и показываем данные (очки, рекорд пользователя)
        print('-------------------------------')
        print(f'Заработано очков: {point}')
        print(f'Рекорд: {attemts}')

        print('-------------------------------')

        if point >= 0:

            # Пользователь угадывает случайное число
            user = input('Введите число от 10 до 99: ')

            # Гланое условия для проверки число
            if is_valid(user):
                user = int(user)
                # Переменная для подсказок. Определяет разницу между цифрой которая загадано и которая ввел пользователь
                positive_modul = abs(user - pc_number)

                # Внутренне условия для подсказок
                if user != pc_number:

                    if 70 <= positive_modul <= 89:
                        print('-------------------------------')
                        print("Ледяной ветер")
                        point -= 15
                        attemts += 1
                        record_attemts += 1

                    elif 50 <= positive_modul <= 69:
                        print('-------------------------------')
                        print("Ты очень далеко от ответа")
                        point -= 15
                        attemts += 1
                        record_attemts += 1

                    elif 30 <= positive_modul <= 49:
                        print('-------------------------------')
                        print("холодно")
                        point -= 15
                        attemts += 1
                        record_attemts += 1

                    elif 15 <= positive_modul <= 29:
                        print('-------------------------------')
                        print("Попробуй ёще")
                        point -= 15
                        attemts += 1
                        record_attemts += 1

                    elif 5 <= positive_modul <= 14:
                        print('-------------------------------')
                        print("Круто, ты уже очень близок")
                        point -= 15
                        attemts += 1
                        record_attemts += 1

                    else:
                        print('-------------------------------')
                        print("Теплее!!!")
                        point -= 15
                        attemts += 1
                        record_attemts += 1


                else:
                    print("***********************")
                    print('PERFECT!!! GREAT!!! САЛЮТ!!!')
                    print('Поздравляем! Победа!')
                    point += 20
                    attemts += 1
                    record_attemts += 1
                    flag = False

            # Если пользователь ввел неправильное число или строку это подсказка для исправление ошибки
            else:
                print('С вас списывается 10 очков потому что, вы ввели не цифру а строку или вы ввели цифру выходящей за границу диапозона')
                point -= 10
                print(point)

        else:
            print('У вас закончились очки GAME OVER')
            flag = False


    game += 1
    attemts_lst.append(attemts)
    record_attemts_lst.append(record_attemts)
    record_attemts = 0

    if point <= 0:
        point = 100
    play_again = input('Нажмите на ENTER чтобы поиграть ёще раз или нажмите на любую цифру чтобы выйти: ')





print("Игра закончился.")
print(f'Вы сыграли {game} игр.')
print(f'За {game} игр вы {attemts} раз попытались угадать число.')
print(f"Ваш личный рекорд {min(record_attemts_lst)}. Вам потребовалась {min(record_attemts_lst)} попыток чтобы угадать число")
