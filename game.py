import pymysql
from config import host, user, password, db
import time
import sys
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

class color:
    Red = '\033[91m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Blue = '\033[94m'
    Magenta = '\033[95m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Grey = '\033[90m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def hello():
    print("\033[97mДобро пожаловать в главное меню игры \033[96mMonster Crush AUTO RPG\033[97m.\033[0m\n")
    time.sleep(1)
    list_command = [color.White + "   • Авторизация (" + color.Red + "1" + color.White + ")", color.White +  "   • Регистрация (" + color.Red + "2" + color.White + ")", color.White +  "   • О игре (" + color.Red + "3" + color.White + ")", color.White + "   • Выход из игры (" + color.Red + "4" + color.White + ")" + color.END]
    print(color.White + "Доступные действия:" + color.END)
    for text in list_command:
        print(text)
        time.sleep(1)
    print()
    hello_message = input(color.White + "Введите необходимую вам цифру без скобок: " + color.END)
    print()
    if hello_message == '1':
        print(color.White + "Авторизация:" + color.END)
        try:
            connection = pymysql.connect(
                host=host,
                port=38719,
                user=user,
                password=password,
                database=db,
                cursorclass=pymysql.cursors.DictCursor
            )
            try:
                with connection.cursor() as cursor:

                    name = input(color.White + "Введите никнейм: " + color.END)
                    passwd = input(color.White + "Введите пароль: " + color.END)

                    cursor.execute(f"SELECT `nickname`, `password` FROM game.users WHERE `nickname`='{name}'")
                    auto_data = cursor.fetchone()
                    user_data = dict()
                    user_data['nickname'] = name
                    user_data['password'] = passwd
                    if user_data == auto_data:
                        cursor.execute(f"SELECT `nickname`, `password`, `lvl`, `damage`, `coins`, `stage`, `monster`, `monsterHp`, `loot`, `damageCost` FROM game.users WHERE `nickname`='{name}'")
                        data = cursor.fetchone()
                        print()
                        print(color.Green + "Вы успешно авторизовались." + color.END)
                        print()
                        name = data['nickname']
                        passwd = data['password']
                        lvl = data['lvl']
                        damage = data['damage']
                        coins = data['coins']
                        stage = data['stage']
                        monster = data['monster']
                        if monster == 0:
                            monster = 1
                        monsterHp = data['monsterHp']
                        loot = data['loot']
                        damageCost = data['damageCost']
                        return name, passwd, lvl, damage, coins, stage, monster, monsterHp, loot, damageCost
                    else:
                        print()
                        print(color.Red + "Неправльный ник или пароль." + color.END)
                        print()
                        return hello()
            finally:
                connection.close()
        except Exception as ex:
            print(color.Red + "Произошла ошибка." + color.END)
            print(ex)
            return hello()


    elif hello_message == '2':
        print(color.White + "Регистрация:" + color.END)
        lvl = 1
        damage = 1
        coins = 0
        stage = 1
        monster = 1
        monsterHp = 3
        loot = 1
        damageCost = 3
        try:
            connection = pymysql.connect(
                host=host,
                port=38719,
                user=user,
                password=password,
                database=db,
                cursorclass=pymysql.cursors.DictCursor
            )

            try:
                with connection.cursor() as cursor:

                    name = input(color.White + "Введите имя: " + color.END)
                    passwd = input(color.White + "Введите пароль: " + color.END)
                    lvl = 1
                    damage = 1
                    coins = 0
                    stage = 1
                    monsterHp = 3
                    loot = 1
                    damageCost = 3

                    cursor.execute(f"SELECT `nickname` FROM game.users WHERE `nickname`='{name}'")
                    data = cursor.fetchone()
                    if data is None:
                        insert_query = f"INSERT INTO `users` (nickname, password, lvl, damage, coins, stage, monster, monsterHp, loot, damageCost) VALUES ('{name}', '{passwd}', '{lvl}', '{damage}', '{coins}', '{stage}', '{monster}', '{monsterHp}', '{loot}', '{damageCost}');"
                        cursor.execute(insert_query)
                        connection.commit()
                        Registration_data = {
                                color.White + "Ваш никнейм" + color.END: color.Cyan + "{}".format(name) + color.END,
                                color.White + "Ваш пароль" + color.END : color.Cyan + "{}".format(passwd) + color.END
                        }
                        print()
                        print(color.Red + "Запомните эти данные:" + color.END)
                        for key, value in Registration_data.items():
                            print("{0}: {1}".format(key, value))
                        print()
                        print(color.Green + 'Вы зарегистрировались.' + color.END)
                        print()
                        return name, passwd, lvl, damage, coins, stage, monster, monsterHp, loot, damageCost
                    else:
                        print()
                        print(color.Red + "Этот ник занят." + color.END)
                        print()
                        return hello()
            finally:
                connection.close()
        except Exception as ex:
            print(color.Red + "Произошла ошибка." + color.END)
            print(ex)
            return hello()


    elif hello_message == '3':
        print()
        print(color.Red + "Версия игры" + color.White + ": " + color.Cyan + "1.0" + color.END)
        time.sleep(1)
        print(color.Red + "Описание" + color.White +": " + color.Cyan + "Monster Crush AUTO RPG " + color.White + "- это полностью автоматическая или 'самоиграющая' игра, написанная на языках программирования Python и MySQL." + color.END)
        time.sleep(5)
        print(color.White + "При запуске предлагается авторизация или регистрация аккаунта, это значит что создав аккаунт однажды, можно будет использовать его неограниченное количество раз." + color.END)
        time.sleep(5)
        print(color.Red + "ВНИМАНИЕ: ЗАПОМНИТЕ СВОИ ДАННЫЕ ДЛЯ АВТОРИЗАЦИИ АККАУНТА. В СЛУЧАЕ ПОТЕРИ ДАННЫХ ДЛЯ АВТОРИЗАЦИИ АККАУНТА - ВОЗМОЖНОСТЬ ИХ ВОССТАНОВЛЕНИЯ ПРЕДОСТАВЛЯТЬСЯ НЕ БУДЕТ." + color.END)
        time.sleep(5)
        print(color.White + "Также в случае потери данных авторизации аккаунта у вас есть возможность зарегистрировать новый аккаунт." + color.END)
        time.sleep(4)
        print(color.White + "Регистрация и владение несколькими аккаунтами " + color.Green + "разрешается" + color.White + "; регистрация новых аккаунтов " + color.Green + "неограничена" + color.White + "." + color.END)
        time.sleep(4)
        print(color.Red + "Сюжет" + color.White +  ": Другой мир, что носит название «"+ color.Cyan + "Кроминонг" + color.White +"», нуждается в спасении от сил зла. Призываются авантюристы со всего Кроминонга. Вы готовы стать одним из них?" + color.END)
        time.sleep(5)
        print(color.White + "Сможете ли вы забраться на 100-ый этаж Небесного Лабиринта и искоренить зло в " + color.Cyan + "Кроминонге" + color.White + "?" + color.END)
        time.sleep(3)
        print(color.Red + "Целевая аудитория" + color.White + ": офисные работники, старшие школьники и студенты, имеющие свободный доступ к компьютеру, а также мечту об становлении авантюристом, независимо от пола." + color.END)
        time.sleep(5)
        print()
        list_command = [color.White + "   • Главное меню (" + color.Red + "1" + color.White + ")", color.White + "   • Выход (" + color.Red + "2" + color.White + ")" + color.END]
        print(color.White + "Доступные действия:" + color.END)
        for text in list_command:
            print(text)
            time.sleep(1)
        print()
        hello_message_two = input(color.White + "Введите необходимую вам цифру без скобок: " + color.END)
        print()
        if hello_message_two == '1':
            return hello()
        elif hello_message_two == '2':
            sys.exit()

    elif hello_message == '4':
        sys.exit()

name, passwd, lvl, damage, coins, stage, monster, monsterHp, loot, damageCost = hello()

End = False

# parameters - характеристкии, позже будут запиываться в базу (надеюсь)
# Вывод параметров
def parameters():
    global monster
    if monster != 11:
        if (coins % 10 == 1 and coins != 11) and (damage % 10 == 1 and damage != 11):
            print(color.White + "У тебя " + color.Cyan + "{}".format(lvl) + color.White + " уровень, " + color.Cyan + "{}".format(damage) + color.Blue + " урон, " + color.Cyan + "{}".format(coins) + color.Yellow + " монета, " + color.Cyan + "{}".format(stage) + color.White + " этаж, " + color.Cyan + "{}".format(monster) + color.White + " монстр." + color.END)
        elif (2 <= coins % 10 <= 4 and coins // 10 != 1) and (2 <= damage % 10 <= 4 and damage // 10 != 1):
            print(color.White + "У тебя " + color.Cyan + "{}".format(lvl) + color.White + " уровень, " + color.Cyan + "{}".format(damage) + color.Blue + " урона, " + color.Cyan + "{}".format(coins) + color.Yellow + " монеты, " + color.Cyan + "{}".format(stage) + color.White + " этаж, " + color.Cyan + "{}".format(monster) + color.White + " монстр." + color.END)
        elif (2 <= coins % 10 <= 4 and coins // 10 != 1) and (damage % 10 == 1 and damage != 11):
            print(color.White + "У тебя " + color.Cyan + "{}".format(lvl) + color.White + " уровень, " + color.Cyan + "{}".format(damage) + color.Blue + " урон, " + color.Cyan + "{}".format(coins) + color.Yellow + " монеты, " + color.Cyan + "{}".format(stage) + color.White + " этаж, " + color.Cyan + "{}".format(monster) + color.White + " монстр." + color.END)
        elif (damage % 10 == 1 and damage != 11) and (coins % 10 == 0):
            print(color.White + "У тебя " + color.Cyan + "{}".format(lvl) + color.White + " уровень, " + color.Cyan + "{}".format(damage) + color.Blue + " урон, " + color.Cyan + "{}".format(coins) + color.Yellow + " монет, " + color.Cyan + "{}".format(stage) + color.White + " этаж, " + color.Cyan + "{}".format(monster) + color.White + " монстр." + color.END)
        else:
            print(color.White + "У тебя " + color.Cyan + "{}".format(lvl) + color.White + " уровень, " + color.Cyan + "{}".format(damage) + color.Blue + " урона, " + color.Cyan + "{}".format(coins) + color.Yellow + " монет, " + color.Cyan + "{}".format(stage) + color.White + " этаж, " + color.Cyan + "{}".format(monster) + color.White + " монстр." + color.END)
    else:
        if (monster == 11) and (damage % 10 == 1 and damage != 11) and (coins % 10 == 0):
            print(color.White + "У тебя " + color.Cyan + "{}".format(lvl) + color.White + " уровень, " + color.Cyan + "{}".format(damage) + color.Blue + " урон, " + color.Cyan + "{}".format(coins) + color.Yellow + " монет, " + color.Cyan + "{}".format(stage) + color.White + " этаж, " + color.Red + "БОСС" + color.White + "." + color.END)
        elif (monster == 11) and (coins % 10 == 1 and coins != 11) and (damage % 10 == 1 and damage != 11):
            print(color.White + "У тебя " + color.Cyan + "{}".format(lvl) + color.White + " уровень, " + color.Cyan + "{}".format(damage) + color.Blue + " урон, " + color.Cyan + "{}".format(coins) + color.Yellow + " монета, " + color.Cyan + "{}".format(stage) + color.White + " этаж, " + color.Red + "БОСС" + color.White + "." + color.END)
        elif (monster == 11) and (2 <= coins % 10 <= 4 and coins // 10 != 1) and (2 <= damage % 10 <= 4 and damage // 10 != 1):
            print(color.White + "У тебя " + color.Cyan + "{}".format(lvl) + color.White + " уровень, " + color.Cyan + "{}".format(damage) + color.Blue + " урона, " + color.Cyan + "{}".format(coins) + color.Yellow + " монеты, " + color.Cyan + "{}".format(stage) + color.White + " этаж, " + color.Red + "БОСС" + color.White + "." + color.END)
        elif (monster == 11) and (2 <= coins % 10 <= 4 and coins // 10 != 1) and (damage % 10 == 1 and damage != 11):
            print(color.White + "У тебя " + color.Cyan + "{}".format(lvl) + color.White + " уровень, " + color.Cyan + "{}".format(damage) + color.Blue + " урон, " + color.Cyan + "{}".format(coins) + color.Yellow + " монеты, " + color.Cyan + "{}".format(stage) + color.White + " этаж, " + color.Red + "БОСС" + color.White + "." + color.END)
        elif (monster == 11) and (damage % 10 == 1 and damage != 11) and (coins % 10 == 0):
            print(color.White + "У тебя " + color.Cyan + "{}".format(lvl) + color.White + " уровень, " + color.Cyan + "{}".format(damage) + color.Blue + " урон, " + color.Cyan + "{}".format(coins) + color.Yellow + " монет, " + color.Cyan + "{}".format(stage) + color.White + " этаж, " + color.Red + "БОСС" + color.White + "." + color.END)

# Вывод монет
def printCoins():
    if coins % 10 == 1 and coins != 11:
        print(color.White + "У тебя сейчас " + color.Cyan + "{}".format(coins) + color.Yellow + " монета" + color.White + "." + color.END)
    elif 2 <= coins % 10 <= 4 and coins // 10 != 1:
        print(color.White + "У тебя сейчас " + color.Cyan + "{}".format(coins) + color.Yellow + " монеты" + color.White + "." + color.END)
    else:
        print(color.White + "У тебя сейчас " + color.Cyan + "{}".format(coins) + color.Yellow + " монет" + color.White + "." + color.END)

#Вывод урона
def printDamage():
    if damage % 10 == 1 and damage != 11:
        print(color.White + "У тебя сейчас " + color.Cyan + "{}".format(damage) + color.Blue + " урон" + color.White + "." + color.END)
    else:
        print(color.White + "У тебя сейчас " + color.Cyan + "{}".format(damage) + color.Blue + " урона" + color.White + "." + color.END)

#Качалка
def workout_room():
    global damage
    global coins
    global damageCost

#Покупка
    def gain(Dmgcost):
        global coins
        if coins >= Dmgcost:
            coins -= Dmgcost
            time.sleep(2)
            return True
        else:
            print(color.Red + "Недостаточно монет." + color.END)


    global damageCost
    Dmgboost = 2

    print(color.White + "Ты попал в качалку, здесь ты можешь увеличить свой" + color.Blue + "урон" + color.White + "." + color.END)
    parameters()
    print()

    #автоматическая закупка урона пока хватает монет, иначе происходит выход на босса.
    while coins >= damageCost:
        if damageCost % 10 == 1 and damageCost != 11:
            print(color.White + "Ты получишь " + color.Cyan + "{}".format(Dmgboost) + color.Blue + " урона" + color.White + " за " + color.Cyan + "{}".format(damageCost) + color.Yellow + " монету" + color.White + "." + color.END)
        elif 2 <= damageCost % 10 <= 4 and damageCost // 10 != 1:
            print(color.White + "Ты получишь " + color.Cyan + "{}".format(Dmgboost) + color.Blue + " урона" +  color.White + " за " + color.Cyan + "{}".format(damageCost) + color.Yellow + " монеты" + color.White + "." + color.END)
        else:
            print(color.White + "Ты получишь " + color.Cyan + "{}".format(Dmgboost) + color.Blue + " урона" + color.White + " за " + color.Cyan + "{}".format(damageCost) + color.Yellow + " монет" + color.White + "." + color.END)
        print()
        if gain(damageCost):
            print(color.Green + "Успешно!" + color.END)
            damage += Dmgboost
            damageCost += 2
            printCoins()
            printDamage()
            time.sleep(2)
            print()

# Драка с монстрами.
def monsters():
    global coins
    global stage
    global monster
    global monsterHp
    global loot
    global damageCost
    global End

    HP = monsterHp

    if damage % 10 == 1 and damage != 11:
        print(color.White + "У монстра " + color.Red + "{}".format(monsterHp) + " HP" + color.White + ", у тебя " + color.Cyan + "{}".format(damage) + color.Blue + " урон" + color.White + "." + color.END)
    else:
        print(color.White + "У монстра " + color.Red + "{}".format(monsterHp) + " HP" + color.White + ", у тебя " + color.Cyan + "{}".format(damage) + color.Blue + " урона" + color.White + "." + color.END)

    while HP > 0:
        HP -= damage
        if HP > 0:
            print(color.White + "У монстра осталось", color.Red, HP, "HP" + color.White + "." + color.END)
            time.sleep(1)

        else:
            if monster == 11:
                monster = 0
                stage += 1
                # Увеличивает кол-во монет поле босса
                loot += 1
                # Увеличивает HP босса
                monsterHp *= 2

            print(color.White + "У монстра осталось " + color.Green + "0" + color.Red + " HP" + color.White + "." + color.END)
            if loot % 10 == 1 and loot != 11:
                print(color.White + "Ты одолел монстра и получил ", color.Cyan + "{}".format(loot), color.Yellow + "монету" + color.White + "." + color.END)
            elif 2 <= loot % 10 <= 4 and loot // 10 != 1:
                print(color.White + "Ты одолел монстра и получил ", color.Cyan + "{}".format(loot), color.Yellow + "монеты" + color.White + "." + color.END)
            else:
                print(color.White + "Ты одолел монстра и получил " + color.Cyan + "{}".format(loot), color.Yellow + "монет" + color.White + "." + color.END)
            coins += loot
            time.sleep(1)
            print()
            printCoins()
            print()
            monster += 1
            # += Увеличивает HP ко всем монтрам, включая босса
            monsterHp += 3
            time.sleep(1)
            # update data
            connection = pymysql.connect(
                host=host,
                port=38719,
                user=user,
                password=password,
                database=db,
                cursorclass=pymysql.cursors.DictCursor
            )
            with connection.cursor() as cursor:
                update_query = f"UPDATE `users` SET lvl = '{lvl}', coins = '{coins}', stage = '{stage}', monster = '{monster}', monsterHp = '{monsterHp}', loot = '{loot}', damage = '{damage}', damageCost = '{damageCost}' WHERE nickname = '{name}';"
                cursor.execute(update_query)
                connection.commit()

            if monster != 11:
                if stage == 100:
                    monster = 0
                    print(color.White + "Этаж " + color.Magenta + "100" + color.White + "." + color.White +"\nВы избавили" + color.Cyan + "Кроминонг" + color.White + "от зла." + color.END)
                    End = True
                    return
                else:
                    time.sleep(1)
                    print(color.White + "Этаж " + color.Cyan + "{}".format(stage) + color.White +  ", Монстр " + color.Cyan + "{}".format(monster), color.END)


            else:
                # Перед боссом автоматческий вход в качалку
                if coins >= damageCost:
                    workout_room()
                else:
                    print(color.White + "У тебя явно " + color.Red + "недостаточно " + color.Yellow + "монет " + color.White + "на прокачку, так что даже не стоит заходить туда." + color.END)
                    print()
                time.sleep(1)
                print(color.White + "Этаж ", color.Cyan + "{}".format(stage) + color.White + ",", color.Red + "БОСС" + color.END)
                # time.sleep(1)
                print(color.Red + "Ты встретил монстр-босса!" + color.END)
                time.sleep(1)

                # update data
                connection = pymysql.connect(
                    host=host,
                    port=38719,
                    user=user,
                    password=password,
                    database=db,
                    cursorclass=pymysql.cursors.DictCursor
                )
                with connection.cursor() as cursor:
                    update_query = f"UPDATE `users` SET lvl = '{lvl}', coins = '{coins}', stage = '{stage}', monster = '{monster}', monsterHp = '{monsterHp}', loot = '{loot}', damage = '{damage}', damageCost = '{damageCost}' WHERE nickname = '{name}';"
                    cursor.execute(update_query)
                    connection.commit()

            if stage > 1 and stage <= 3:
                monsterHp += 4
            elif stage >= 4 and stage <= 6:
                monsterHp += 15
            elif stage > 7 and stage <= 11:
                monsterHp += 66
            elif stage > 12 and stage <= 20:
                monsterHp += 100
            elif stage > 21 and stage <= 31:
                monsterHp += 200
            elif stage > 31 and stage <= 51:
                monsterHp += 350
            elif stage > 52 and stage <= 90:
                monsterHp += 650
            elif stage > 90 and stage <= 99:
                monsterHp += 1000

#Инициализация
def initGame(initLvl ,initDmg, initCoins, initStage, initMonster, initMonsterHp, initLoot, initDamageCost, initName):

    lvl = initLvl
    damage = initDmg
    coins = initCoins
    stage = initStage
    monster = initMonster
    monsterHp = initMonsterHp
    loot = initLoot
    damageCost = initDamageCost
    name = initName

    print(color.White + "Ты отправился в" + color.Cyan + " Небесный Лабиринт " + color.White + "навстречу приключениям и опасностям. Удачи, " + color.Green + "{}".format(name) + color.White + "." + color.END)
    print()
    time.sleep(2)
    parameters()
    print()
    if monster != 11:
        print(color.White + "Этаж " + color.Cyan + "{}".format(stage) + color.White +  ", Монстр " + color.Cyan + "{}".format(monster), color.END)
    else:
        print(color.White + "Этаж", color.Cyan + "{}".format(stage) + color.White + ",", color.Red + "БОСС" + color.END)

# зацикленное действие
def gameLoop():
    monsters()

# Начальные характеристики
# lvl, damage, coins, stage, monster, monsterHp, loot, damageCost, nickname
initGame(lvl, damage, coins, stage, monster, monsterHp, loot, damageCost, name)

# Сам игровой цикл
while True:
    gameLoop()

    if End == True:
        break
