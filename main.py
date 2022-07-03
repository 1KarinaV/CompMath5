import Newton
#import matplotlib.pyplot as plt
from Functions import *
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)


class EulerMethod:
    def __init__(self, x0, y0, h, xn, function):
        self.x = x0
        self.y = y0
        self.h = h
        self.n = int((xn - x0)/h)
        self.function = function

    def euler_method(self):
        array_with_dots = [[self.x, self.y]]
        self.h2 = self.h/2
        for i in range(self.n):
            self.x += self.h
            self.y += self.h*self.function(self.x + self.h2, self.y + self.h2 * self.function(self.x, self.y))
            array_with_dots.append([self.x, self.y])
        return array_with_dots


def enter_args(func):
    x0 = int(input("Введите x0: "))
    y0 = float(input("Введите y0: "))
    h = float(input("Введите длину промежутка: "))
    if h <= 0:
        h = 0.5
    xn = int(input("Введите конец отрезка: "))
    return EulerMethod(x0, y0, h, xn, func)


while 1:
    chose = str(input("Выберите уравнение \n"
                      "1) y' = sin(x)\n"
                      "2) y' = x * y\n"
                      "3) y' = x ^ 2 - y\n"))
    if chose == str(1):
        try:
            EM = enter_args(f_sin)
            dots = EM.euler_method()
            x = np.array([dots[i][0] for i in range(len(dots))])
            y = np.array([dots[i][1] for i in range(len(dots))])
            a = Newton.coef(x, y)
            Newton.plot_graphic(x, a, y, f_sin_true)
            ylist = [f_sin_true(i) for i in x]
        except ValueError:
            print("Что-то пошло не так")
    elif chose == str(2):
        try:
            EM = enter_args(f1)
            dots = EM.euler_method()
            x = np.array([dots[i][0] for i in range(len(dots))])
            y = np.array([dots[i][1] for i in range(len(dots))])
            a = Newton.coef(x, y)
            Newton.plot_graphic(x, a, y, f1_true)
            ylist = [f1_true(i) for i in x]
        except ValueError:
            print("Что-то пошло не так")
    elif chose == str(3):
        try:
            EM = enter_args(z)
            dots = EM.euler_method()
            x = np.array([dots[i][0] for i in range(len(dots))])
            y = np.array([dots[i][1] for i in range(len(dots))])
            a = Newton.coef(x, y)
            Newton.plot_graphic(x, a, y, z_true)
            ylist = [z_true(i) for i in x]
        except ValueError:
            print("Что-то пошло не так")
    elif chose == "q":
        break
    else:
        print("Нет такой команды, попробуйте еще раз")
