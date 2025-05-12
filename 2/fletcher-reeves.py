import math
import numpy as np
from scipy.optimize import minimize_scalar

def func(x, y):
    return x ** 2 + 7 * y ** 2 - x * y + x

def grad(x, y):
    return 2 * x - y + 1, 14 * y - x

def check_positive(M):
    return M[0][0] > 0 and (M[0][0] * M[1][1] - M[0][1] * M[1][0]) > 0

def fletcher_reeves(x, y, eps1, eps2, M):
    xk = [x, y]
    k = 0

    k_checker = 0

    H = np.array([[2, -1],
                  [-1, 14]])
    rev_H = np.linalg.inv(H)

    while k <= M:
        print('k = ', k)

        gradf = grad(xk[0], xk[1])

        print('grad = ', gradf)
        print('||grad|| = ', np.linalg.norm(gradf))
        if np.linalg.norm(gradf) < eps1:
            return xk, k + 1, 'Условие 1: ||grad(f)|| < eps1', rev_H

        if k == 0: d = [-1 * gradf[0], -1 * gradf[1]]

        if k >= 1:
            B = np.linalg.norm(gradf) ** 2 / np.linalg.norm(grad(xk_prev[0], xk_prev[1])) ** 2
            d = [-1 * gradf[0] + B * d_prev[0], -1 * gradf[1] + B * d_prev[1]]
            print(f"B = {B}")

        t = (-d[0] - 2 * d[0] * xk[0] + d[1] * xk[0] - 14 * d[1] * xk[1] + d[0] * xk[1]) / (2 * d[0] ** 2 + 14 * d[1] ** 2 - 2 * d[0] * d[1])

        print(f"d = {d}\nt = {t}")

        xk_next = [xk[0] + t * d[0], xk[1] + t * d[1]]
        print(f"xk+1 = {xk_next}")

        print('||xk+1 - xk|| = ', np.linalg.norm([x - y for x, y in zip(xk_next, xk)]))
        print('|f(xk+1) - f(xk)| = ', abs(func(xk_next[0], xk_next[1]) - func(xk[0], xk[1])))

        if (np.linalg.norm([x - y for x, y in zip(xk_next, xk)]) < eps2) \
                and (abs(func(xk_next[0], xk_next[1]) - func(xk[0], xk[1])) < eps2):
            if (k_checker == 1):
                return xk_next, k + 1, 'Условие 3: ||xk+1 - xk|| < eps2 & |f(xk+1) - f(xk)| < eps2', rev_H
            k_checker += 1
        else:
            k_checker = 0

        xk_prev = xk
        xk = xk_next
        d_prev = d
        k += 1

    return xk, k + 1, 'Условие 2: достигнуто предельное число итераций', rev_H

x0, y0 = 1.1, 1.1
eps1, eps2 = 0.1, 0.15
M = 10

xk, iter_count, cond, rev_H = fletcher_reeves(x0, y0, eps1, eps2, M)

print('-------------')
print(f"x* = ({xk[0]:.2f}, {xk[1]:.2f})\nf(x*) = {func(xk[0], xk[1])}\nКоличество итераций: {iter_count}\n{cond}"
      f"\nrev_H = \n{rev_H}")