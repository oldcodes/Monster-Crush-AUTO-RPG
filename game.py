import sqlite3
import time

# Регистрация пользователя в базе
def registration():
    connect = sqlite3.connect('game.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS gamerpg(
        nickname TEXT,
        password TEXT,
        lvl INTERGER,
        damage INTERGER,
        coins INTERGER,
        stage INTERGER,
        monster INTERGER,
        monsterHp INTERGER,
        loot INTERGER,
        damageCost INTERGER
    )""")
    connect.commit()

    nickname = input("Введите свой ник: ")
    password = input("Введите пароль: ")
    print(nickname, password)

    cursor.execute(f"SELECT nickname FROM gamerpg WHERE nickname = '{nickname}'")
    data = cursor.fetchone()
    if data is None:
        cursor.execute(f"INSERT INTO gamerpg(nickname, password, lvl, damage, coins, stage, monster, monsterHp, loot) VALUES('{nickname}', '{password}', {lvl}, {damage}, {coins}, {stage}, {monster}, {monsterHp}, {loot})")
        connect.commit()
        print('Вы успешно внесены в базу.')
    else:
        print('Вы уже внесены в базу.')

    return nickname

# parameters - характеристкии, позже будут запиываться в базу (надеюсь)
lvl = 0
damage = 0
coins = 0
stage = 0
monster = 0
monsterHp = 0
loot = 0
damageCost = 0
End = False
nickname = registration()

# Вывод параметров
def parameters():
    global monster
    if monster != 11:
        if (coins % 10 == 1 and coins != 11) and (damage % 10 == 1 and damage != 11):
            print("У тебя {0} уровень, {1} урон, {2} монета, {3} этап, {4} монстр.".format(lvl, damage, coins, stage, monster))
        elif (2 <= coins % 10 <= 4 and coins // 10 != 1) and (2 <= damage % 10 <= 4 and damage // 10 != 1):
            print("У тебя {0} уровень, {1} урона, {2} монеты, {3} этап, {4} монстр.".format(lvl, damage, coins, stage, monster))
        elif (2 <= coins % 10 <= 4 and coins // 10 != 1) and (damage % 10 == 1 and damage != 11):
            print("У тебя {0} уровень, {1} урон, {2} монеты, {3} этап, {4} монстр.".format(lvl, damage, coins, stage, monster))
        elif (damage % 10 == 1 and damage != 11) and (coins % 10 == 0):
            print("У тебя {0} уровень, {1} урон, {2} монет, {3} этап, {4} монстр.".format(lvl, damage, coins, stage, monster))
        else:
            print("У тебя {0} уровень, {1} урона, {2} монет, {3} этап, {4} монстр.".format(lvl, damage, coins, stage, monster))
    else:
        if (monster == 11) and (damage % 10 == 1 and damage != 11) and (coins % 10 == 0):
            print("У тебя {0} уровень, {1} урон, {2} монет, {3} этап, БОСС.".format(lvl, damage, coins, stage))
        elif (monster == 11) and (coins % 10 == 1 and coins != 11) and (damage % 10 == 1 and damage != 11):
            print("У тебя {0} уровень, {1} урон, {2} монета, {3} этап, БОСС.".format(lvl, damage, coins, stage))
        elif (monster == 11) and (2 <= coins % 10 <= 4 and coins // 10 != 1) and (2 <= damage % 10 <= 4 and damage // 10 != 1):
            print("У тебя {0} уровень, {1} урона, {2} монеты, {3} этап, БОСС.".format(lvl, damage, coins, stage))
        elif (monster == 11) and (2 <= coins % 10 <= 4 and coins // 10 != 1) and (damage % 10 == 1 and damage != 11):
            print("У тебя {0} уровень, {1} урон, {2} монеты, {3} этап, БОСС.".format(lvl, damage, coins, stage))
        elif (monster == 11) and (damage % 10 == 1 and damage != 11) and (coins % 10 == 0):
            print("У тебя {0} уровень, {1} урон, {2} монет, {3} этап, БОСС.".format(lvl, damage, coins, stage))

# Вывод монет
def printCoins():
    if coins % 10 == 1 and coins != 11:
        print("У тебя сейчас", coins, "монета.")
    elif 2 <= coins % 10 <= 4 and coins // 10 != 1:
        print("У тебя сейчас", coins, "монеты.")
    else:
        print("У тебя сейчас", coins, "монет.")

#Вывод урона
def printDamage():
    if damage % 10 == 1 and damage != 11:
        print("У тебя сейчас", damage, "урон.")
    else:
        print("У тебя сейчас", damage, "урона.")

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
            printCoins()
            return True
        print("Недостаточно монет.")
        return False

    Dmgcost = damageCost
    Dmgboost = 2

    print("Ты попал в качалку, здесь ты можешь увеличить свой урон.")
    parameters()

    #автоматическая закупка урона пока хватает монет, иначе происходит выход на босса.
    while coins >= Dmgcost:
        print("Ты получишь", Dmgboost, "урона за", Dmgcost, "монеты.")
        choice = "да"
        if choice == "да":
            if gain(Dmgcost):
                damage += Dmgboost
                Dmgcost += 2
                printDamage()
                time.sleep(2)
        elif choice == "нет":
            break

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
        print("У монстра", monsterHp, "HP, у тебя", damage, "урон.")
    else:
        print("У монстра", monsterHp, "HP, у тебя", damage, "урона.")

    while HP > 0:
        HP -= damage
        if HP > 0:
            print("У монстра осталось", HP, "HP.")
            time.sleep(1)

        else:
            print("У монстра осталось 0 HP.")
            print("Ты одолел монстра и получил", loot, "монеты.")
            coins += loot
            time.sleep(1)
            printCoins()
            monster += 1
            # += Увеличивает HP ко всем монтрам, включая босса
            monsterHp += 3
            time.sleep(1)

            if monster != 11:
                if stage == 100:
                    monster = 0
                    print("Этап 100.\nВы прошли игру.")
                    End = True
                    return
                else:
                    time.sleep(1)
                    print("Этап", stage,',', "Монстр", monster)

            else:
                # Перед боссом автоматческий вход в качалку
                if coins >= damageCost:
                    workout_room()
                else:
                    print("У тебя явно недостаточно денег на прокачку, так что даже не стоит заходить туда.")
                time.sleep(1)
                print("Этап", stage,',', "БОСС")
                time.sleep(1)
                print("Ты встретил монстр-босса!")
                monster = 0
                stage += 1
                # Увеличивает кол-во монет поле босса
                loot += 1
                # Увеличивает HP босса
                monsterHp *= 2
                time.sleep(1)

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
            # elif stage == 100 and monster == 1:
            #     print("Вы прошли игру.")
            #     End = True

#Инициализация
def initGame(initLvl ,initDmg, initCoins, initStage, initMonster, initMosterHp, initLoot, initDamageCost, initNickname):
    global lvl
    global damage
    global coins
    global stage
    global monster
    global monsterHp
    global loot
    global damageCost
    global nickname

    lvl = initLvl
    damage = initDmg
    coins = initCoins
    stage = initStage
    monster = initMonster
    monsterHp = initMosterHp
    loot = initLoot
    damageCost = initDamageCost
    nickname = initNickname

    print("Ты отправился навстречу приключениям и опасностям. Удачи, {}.".format(nickname))
    time.sleep(2)
    parameters()
    print("Этап", stage,',', "Монстр", monster)

# зацикленное действие
def gameLoop():
    monsters()

# Начальные характеристики
#lvl, damage, coins, stage, monster, monsterHp, loot, damageCost, nickname
initGame(1, 1, 0, 1, 1, 3, 2, 3, nickname)

# Сам игровой цикл
while True:
    gameLoop()

    if End == True:
        break