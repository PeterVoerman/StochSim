import matplotlib.pyplot as plt
import numpy as np

def mandelbrot():
    good_z = []
    bad_z = []

    for a in np.arange(-3, 1.006, 0.006):
        for b in np.arange(-1.5, 1.506, 0.006):
            z_0 = complex(a, b)

            converges = does_converge(z_0)

            if converges:
                good_z.append(z_0)
            else:
                bad_z.append(z_0)

    print(len(good_z), len(bad_z))
    x_list = [x.real for x in good_z]
    y_list = [x.imag for x in good_z]
    plt.scatter(x_list, y_list, s = 1)
    plt.xlim(-2, 1)
    plt.ylim(-1.5, 1.5)
    plt.show()

def does_converge(z_0, treshold=2, max_iterations=25):
    
    z = z_0
    counter = 0
    while True:
        z = z ** 2 + z_0
        counter += 1

        if abs(z) > 2:
            return False
        if counter > max_iterations:
            return True

def determine_area(i = 25, s=10000):

    bounding_box_area = 4 * 4

    n_good_points = 0

    for _ in range(int(s)):
 
        a = np.random.uniform() * 4 - 2
        b = np.random.uniform() * 4 - 2
        z_0 = complex(a,b)
        
        if does_converge(complex(a, b), max_iterations=i):
            n_good_points += 1
    
    return bounding_box_area * (n_good_points / s)

def plot_i_s_contour(i_list, s_list, log=False):
    
    total_evaluations = len(i_list) * len(s_list)
    n_evaluations = 0

    expected_area = 1.506484

    data = []
    for i in i_list:

        results = []
        for s in s_list:
            results.append(determine_area(i=i, s=s) - expected_area)
            n_evaluations += 1

            if log and n_evaluations % 10 == 0:
                print(f"Progress: {n_evaluations/total_evaluations * 100:0f}%", end="\r")
        
        data.append(results)

    contour = plt.contourf(i_list, s_list, data, 10, cmap="PuBuGn_r")
    
    colorbar = plt.colorbar(contour)
    colorbar.set_label("Difference between expected area")

    plt.xlabel("Max iterations")
    plt.ylabel("Samples")

    plt.xscale("log")
    plt.yscale("log")
    plt.show()

def plot_i_s_variance(i_list, s_list, nruns=10, log=False):

    total_evaluations = len(i_list) * len(s_list) * nruns
    n_evaluations = 0

    expected_area = 1.506484

    data = []
    for i in i_list:

        results = []
        for s in s_list:

            run_results = []
            for run in range(nruns):
                run_results.append(determine_area(i=i, s=s))
                n_evaluations += 1

                if log and n_evaluations % 10 == 0:
                    print(f"Progress: {n_evaluations/total_evaluations * 100:1f}%", end="\r")

            results.append(np.var(run_results))
        
        data.append(results)

    contour = plt.contourf(s_list, i_list, data, 10, cmap="PuBuGn_r")
    
    colorbar = plt.colorbar(contour)
    colorbar.set_label("Variance in area")

    plt.xlabel("Samples")
    plt.ylabel("Max iterations")

    plt.xscale("log")
    plt.yscale("log")
    plt.show()

i_list = np.logspace(0, 3, 20)
s_list = np.logspace(1, 5, 20)
plot_i_s_contour(i_list, s_list, log=True)
plot_i_s_variance(i_list, s_list, nruns=20, log=True)