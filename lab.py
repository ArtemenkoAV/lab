import math
import matplotlib.pyplot as pyplot
import control.matlab as matlab
import numpy as numpy

def choise():
    inertialessUnitName = 'Безынерционное звено'
    aperiodicUnitName = 'Апериодическое звено'
    integrationUnitName = 'Интегрирующее звено'
    idealDifferentiatingUnitname = 'Идеальное дифференцирующее звено'
    realDifferentiatingUnitname = 'Реальное дифференцирующее звено'

    newChoice = True

    while newChoice:
        userInput = input('Введите номер команды: \n'
                          '1 - ' + inertialessUnitName + ';\n'
                          '2 - ' + aperiodicUnitName + ';\n'
                          '3 - ' + integrationUnitName + ';\n'
                          '4 - ' + idealDifferentiatingUnitname + ';\n'
                          '5 - ' + realDifferentiatingUnitname + '.\n')

        if userInput.isdigit():
            newChoice = False
            userInput = int(userInput)
            if userInput == 1:
                name = 'Безынерционное звено'
            elif userInput == 2:
                name = 'Апериодическое звено'
            elif userInput == 3:
                name = 'Интегрирующее звено'
            elif userInput == 4:
                name = 'Идеальное дифференцирующее звено'
            elif userInput == 5:
                name = 'Реальное дифференцирующее звено'
            else:
                print('\nНедопустимое значение!')
        else:
            print('\nВведите числовое значение!')
            newChoice = True
    return name

def getUnit(name):

    newChoice = True
    while newChoice:
        newChoice = False
        k = input('Введите коэффициент "k": ')
        t = input('Введите коэффициент "t": ')
        if k.isdigit() and t.isdigit():
            k = int(k)
            t = int(t)
            if name == 'Безынерционное звено':
                unit = matlab.tf([k], [1])
            elif name == 'Апериодическое звено':
                unit = matlab.tf([k], [t, 1])
            elif name == 'Интегрирующее звено':
                unit = matlab.tf([k], [1, 0])
            elif name == 'Идеальное дифференцирующее звено':
                unit = matlab.tf([k, 0], [0.0000001,1])
            elif name == 'Реальное дифференцирующее звено':
                unit = matlab.tf([k, 0], [t, 1])
        else:
            print('\nВведите числовое значение!')
            newChoice = True
    return unit

def graph(num, title, y, x):
    pyplot.subplot(2,1, num)
    pyplot.grid(True)
    if title == 'Переходная характеристика':
        pyplot.plot(x, y)

    elif title == 'Импульсная характеристика':
        pyplot.plot(x, y)






    pyplot.title(title)
    pyplot.ylabel('Амплитуда')
    pyplot.xlabel('Время, (с)')

unitName = choise()
unit = getUnit(unitName)

timeLine = []
for i in range(0, 1000):
    timeLine.append(i/100)

[y, x] = matlab.step(unit, timeLine)
graph(1, 'Переходная характеристика', y, x)
[y, x] = matlab.impulse(unit, timeLine)
graph(2, 'Импульсная характеристика', y, x)


time = []
for i in range(0, 250):
    time.append(i/100)
pyplot.show()
pyplot.subplot()
pyplot.grid(True)
mag, phase, omega = matlab.freqresp(unit, time)
pyplot.plot(mag)
pyplot.title('АЧХ')
pyplot.ylabel('Амплитуда')
pyplot.xlabel('угловая частота, (рад/с)')
pyplot.show()

pyplot.subplot()
pyplot.grid(True)
pyplot.title('ФЧХ')
pyplot.ylabel('Фаза')
pyplot.xlabel('Угловая частота, (рад/с)')
pyplot.plot(phase*180/math.pi)
pyplot.show()