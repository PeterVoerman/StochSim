import matplotlib.pyplot as plt
import numpy as np

def mandelbrot():
    good_z = []
    bad_z = []

    for a in np.arange(-2, 1.006, 0.006):
        print(a)
        for b in np.arange(-1.5, 1.506, 0.006):
            z_0 = complex(a, b)
            z = z_0
            counter = 0
            checked = False

            while checked == False:
                z = z ** 2 + z_0
                counter += 1
                if abs(z) > 2:
                    bad_z.append(z_0)
                    checked = True
                if counter > 25:
                    good_z.append(z_0)
                    checked = True

    print(len(good_z), len(bad_z))
    x_list = [x.real for x in good_z]
    y_list = [x.imag for x in good_z]
    plt.scatter(x_list, y_list, s = 1)
    plt.xlim(-2, 1)
    plt.ylim(-1.5, 1.5)
    plt.show()

mandelbrot()