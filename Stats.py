TechSt = {'ВЫН':7, 'ЛОВ':2, 'ДВЖ':5, 'МТК':2, 'ВОЛ':3, 'ИНТ':5, 'ОЗ':11, 'СТК':1, 'ПБр':2, 'ЗБр':1, 'ПСб':1, 'ЗСб':1, 'МОЗ':11, 'РМ':5, 'ВД':2}
SoldSt = {'ВЫН':5, 'ЛОВ':3, 'ДВЖ':5, 'МТК':6, 'ВОЛ':3, 'ИНТ':2, 'ОЗ':7, 'СТК':1, 'ПБр':2, 'ЗБр':1, 'ПСб':2, 'ЗСб':2, 'МОЗ':7, 'РМ':2, 'ВД':3}
MBISt = {'ВЫН':4, 'ЛОВ':4, 'ДВЖ':4, 'МТК':3, 'ВОЛ':5, 'ИНТ':2, 'ОЗ':8, 'СТК':1, 'ПБр':2, 'ЗБр':1, 'ПСб':1, 'ЗСб':1, 'МОЗ':8, 'РМ':2, 'ВД':4}
TrooperSt = {'ВЫН':5, 'ЛОВ':4, 'ДВЖ':4, 'МТК':4, 'ВОЛ':3, 'ИНТ':3, 'ОЗ':10, 'СТК':1, 'ПБр':2, 'ЗБр':1, 'ПСб':1, 'ЗСб':1, 'МОЗ':10, 'РМ':3, 'ВД':4}
SniperSt = {'ВЫН':3, 'ЛОВ':4, 'ДВЖ':5, 'МТК':6, 'ВОЛ':1, 'ИНТ':5, 'ОЗ':7, 'СТК':1, 'ПБр':2, 'ЗБр':1, 'ПСб':1, 'ЗСб':1, 'МОЗ':7, 'РМ':5, 'ВД':4}
MutantSt = {'ВЫН':4, 'ЛОВ':4, 'ДВЖ':4, 'МТК':4, 'ВОЛ':3, 'ИНТ':2, 'ОЗ':16, 'СТК':1, 'ПБр':2, 'ЗБр':1, 'ПСб':1, 'ЗСб':1, 'МОЗ':16, 'РМ':2, 'ВД':4}

STA = {'Техник':TechSt.get('ВЫН'), 'Пехота':SoldSt.get('ВЫН'), 'МБИ':MBISt.get('ВЫН'), 'Десантник':TrooperSt.get('ВЫН'), 'Снайпер':SniperSt.get('ВЫН'), 'Мутант':MutantSt.get('ВЫН')}
AGI = {'Техник':TechSt.get('ЛОВ'), 'Пехота':SoldSt.get('ЛОВ'), 'МБИ':MBISt.get('ЛОВ'), 'Десантник':TrooperSt.get('ЛОВ'), 'Снайпер':SniperSt.get('ЛОВ'), 'Мутант':MutantSt.get('ЛОВ')}
MOV = {'Техник':TechSt.get('ДВЖ'), 'Пехота':SoldSt.get('ДВЖ'), 'МБИ':MBISt.get('ДВЖ'), 'Десантник':TrooperSt.get('ДВЖ'), 'Снайпер':SniperSt.get('ДВЖ'), 'Мутант':MutantSt.get('ДВЖ')}
AIM = {'Техник':TechSt.get('МТК'), 'Пехота':SoldSt.get('МТК'), 'МБИ':MBISt.get('МТК'), 'Десантник':TrooperSt.get('МТК'), 'Снайпер':SniperSt.get('МТК'), 'Мутант':MutantSt.get('МТК')}
WILL = {'Техник':TechSt.get('ВОЛ'), 'Пехота':SoldSt.get('ВОЛ'), 'МБИ':MBISt.get('ВОЛ'), 'Десантник':TrooperSt.get('ВОЛ'), 'Снайпер':SniperSt.get('ВОЛ'), 'Мутант':MutantSt.get('ВОЛ')}
INT = {'Техник':TechSt.get('ИНТ'), 'Пехота':SoldSt.get('ИНТ'), 'МБИ':MBISt.get('ИНТ'), 'Десантник':TrooperSt.get('ИНТ'), 'Снайпер':SniperSt.get('ИНТ'), 'Мутант':MutantSt.get('ИНТ')}
HP = {'Техник':TechSt.get('ОЗ'), 'Пехота':SoldSt.get('ОЗ'), 'МБИ':MBISt.get('ОЗ'), 'Десантник':TrooperSt.get('ОЗ'), 'Снайпер':SniperSt.get('ОЗ'), 'Мутант':MutantSt.get('ОЗ')}
T = {'Техник':TechSt.get('СТК'), 'Пехота':SoldSt.get('СТК'), 'МБИ':MBISt.get('СТК'), 'Десантник':TrooperSt.get('СТК'), 'Снайпер':SniperSt.get('СТК'), 'Мутант':MutantSt.get('СТК')}
FA = {'Техник':TechSt.get('ПБр'), 'Пехота':SoldSt.get('ПБр'), 'МБИ':MBISt.get('ПБр'), 'Десантник':TrooperSt.get('ПБр'), 'Снайпер':SniperSt.get('ПБр'), 'Мутант':MutantSt.get('ПБр')}
RA = {'Техник':TechSt.get('ЗБр'), 'Пехота':SoldSt.get('ЗБр'), 'МБИ':MBISt.get('ЗБр'), 'Десантник':TrooperSt.get('ЗБр'), 'Снайпер':SniperSt.get('ЗБр'), 'Мутант':MutantSt.get('ЗБр')}
FSv = {'Техник':TechSt.get('ПСб'), 'Пехота':SoldSt.get('ПСб'), 'МБИ':MBISt.get('ПСб'), 'Десантник':TrooperSt.get('ПСб'), 'Снайпер':SniperSt.get('ПСб'), 'Мутант':MutantSt.get('ПСб')}
RSv = {'Техник':TechSt.get('ЗСб'), 'Пехота':SoldSt.get('ЗСб'), 'МБИ':MBISt.get('ЗСб'), 'Десантник':TrooperSt.get('ЗСб'), 'Снайпер':SniperSt.get('ЗСб'), 'Мутант':MutantSt.get('ЗСб')}
MHP = {'Техник':TechSt.get('МОЗ'), 'Пехота':SoldSt.get('МОЗ'), 'МБИ':MBISt.get('МОЗ'), 'Десантник':TrooperSt.get('МОЗ'), 'Снайпер':SniperSt.get('МОЗ'), 'Мутант':MutantSt.get('МОЗ')}
RM = {'Техник':TechSt.get('РМ'), 'Пехота':SoldSt.get('РМ'), 'МБИ':MBISt.get('РМ'), 'Десантник':TrooperSt.get('РМ'), 'Снайпер':SniperSt.get('РМ'), 'Мутант':MutantSt.get('РМ')}
SB = {'Техник':TechSt.get('ВД'), 'Пехота':SoldSt.get('ВД'), 'МБИ':MBISt.get('ВД'), 'Десантник':TrooperSt.get('ВД'), 'Снайпер':SniperSt.get('ВД'), 'Мутант':MutantSt.get('ВД')}

a = {'Техник':TechSt, 'Пехота':SoldSt, 'МБИ':MBISt, 'Десантник':TrooperSt, 'Снайпер':SniperSt,'Мутант':MutantSt}
glstts = {'ВЫН':STA, 'ЛОВ':AGI, 'ДВЖ':MOV, 'МТК':AIM, 'ВОЛ':WILL, 'ИНТ':INT, 'ОЗ':HP, 'СТК':T, 'ПБр':FA, 'ЗБр':RA, 'ПСб':FSv, 'ЗСб':RSv}
x = 1

print('Привет, я X-COM бот, мои команды: "персонаж", "характеристика", урон, хил, баф, дебаф, рм, вд, поднять')
while x != 0:
    print('Введите команду:')
    x = input()
    if x in a:
        print(a.get(x))
    elif x in glstts:
        print(glstts.get(x))
    elif x == 'урон':
        print('введите персонажа')
        name = (input())
        print('ОЗ =',(a.get(name)).get('ОЗ'), ', МОЗ =',(a.get(name)).get('МОЗ'))
        print('сколько урона получил персонаж?')
        dmg = int(input())
        (a.get(name))['ОЗ'] -= dmg
        if ((a.get(name))['МОЗ'])*2 <= dmg:
            print(name, 'получил фатальный урон')
            print('Персонаж погиб, подъём на пределе сил невозможен')
            (a.get(name))['ОЗ'] = 0
        elif (a.get(name))['ОЗ'] <= 0:
            print(name, 'получил тяжёлое ранение')
            (a.get(name))['ОЗ'] = 0
        print('ОЗ =', (a.get(name))['ОЗ'])
    elif x == 'хил':
        print('введите персонажа')
        name = (input())
        print('ОЗ =', (a.get(name)).get('ОЗ'), ', МОЗ =',(a.get(name)).get('МОЗ'))
        print('сколько лечения получил персонаж?')
        heal = int(input())
        (a.get(name))['ОЗ'] += heal
        if (a.get(name))['ОЗ'] > (a.get(name))['МОЗ']:
            (a.get(name))['ОЗ'] = (a.get(name))['МОЗ']
        print('ОЗ =', (a.get(name))['ОЗ'])
    elif x == 'баф':
        print('введите персонажа и характеристику, или название бафа')
        name = input()
        stat = input()
        stat = stat.upper()
        print(name, stat, '=', a.get(name)[stat])
        print('введите величину бонуса')
        change = int(input())
        (a.get(name))[stat] += change
        print(name, stat, '=', a.get(name)[stat])
    elif x == 'дебаф':
        print('введите персонажа и характеристику, или название бафа')
        name = input()
        stat = input()
        stat = stat.upper()
        print(name, stat, '=', a.get(name)[stat])
        print('введите величину ослабления')
        change = int(input())
        (a.get(name))[stat] -= change
        print(name, stat, '=', a.get(name)[stat])
    elif x == 'рм':
        print('введите персонажа')
        name = (input())
        print('РМ =', (a.get(name)).get('РМ'))
        print('сколько зарядов рационального мышления потрачено?')
        charge = int(input())
        if charge > a.get(name)['РМ']:
            print('У персонажа недостаточно зарядов рационального мышления')
        else:
            (a.get(name))['РМ'] -= charge
            print('РМ =', (a.get(name))['РМ'])
    elif x == 'вд':
        print('введите персонажа')
        name = (input())
        print('ВД =', (a.get(name)).get('ВД'))
        print('сколько зарядов второго дыхания потрачено?')
        charge = int(input())
        if charge > a.get(name)['РМ']:
            print('У персонажа недостаточно зарядов рационального мышления')
        else:
            (a.get(name))['РМ'] -= charge
            print('РМ =', (a.get(name))['РМ'])
    elif x == 'подъём' or x == 'рес' or x == 'поднять':
        print('введите персонажа')
        name = input()
        print('поднимает врач или поддержка?')
        res = input()
        if res == 'нет':
            print('потратить 3 заряда аптечки, чтобы не уменьшать Стойкость?')
            tchng = input()
            if tchng == 'нет':
                if (a.get(name))['МОЗ']-1 == 0 or (a.get(name))['ВЫН']-1 == 0 or (a.get(name))['ЛОВ']-1 == 0 or (a.get(name))['ДВЖ']-1 == 0 or (a.get(name))['МТК']-1 == 0 or (a.get(name))['ВОЛ']-1 == 0 or (a.get(name))['ИНТ']-1 == 0 or (a.get(name))['СТК']-1 == 0:
                    print('Невозможно выполнить подъём на пределе сил')
                else:
                    (a.get(name))['МОЗ'] -= 1
                    (a.get(name))['ВЫН'] -= 1
                    (a.get(name))['ЛОВ'] -= 1
                    (a.get(name))['ДВЖ'] -= 1
                    (a.get(name))['МТК'] -= 1
                    (a.get(name))['ВОЛ'] -= 1
                    (a.get(name))['ИНТ'] -= 1
                    (a.get(name))['СТК'] -= 1
                    (a.get(name))['ОЗ'] = 1
                    print('Персонаж',name,'возвращён в бой на пределе сил')
                    print(a.get(name))
            else:
                (a.get(name))['МОЗ'] -= 1
                (a.get(name))['ВЫН'] -= 1
                (a.get(name))['ЛОВ'] -= 1
                (a.get(name))['ДВЖ'] -= 1
                (a.get(name))['МТК'] -= 1
                (a.get(name))['ВОЛ'] -= 1
                (a.get(name))['ИНТ'] -= 1
                (a.get(name))['ОЗ'] = 1
                print('Персонаж',name,'возвращён в бой на пределе сил')
                print(a.get(name))
        else:
            (a.get(name))['ОЗ'] = 1
            print(a.get(name))
    elif x == 'слом':
        x = 1
        print('пока не готово)))')