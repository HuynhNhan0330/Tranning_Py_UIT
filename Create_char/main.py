from revise import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
folder = "/home/nhan/Computer/tranning/label/V2/2"
x = analyze_training_database(folder)
name_points = np.array(x[0])
# max_points = np.array(x[1])
# min_points = np.array(x[2])
# aver_points = np.array(x[3])
# median_points = np.array(x[4])
#
Bar_width = 0.2
#
# plt.bar(name_points + 0.0, max_points, color="red", width=Bar_width, label='Max')
# plt.bar(name_points, min_points, color="green", width=Bar_width, label='Min')
# plt.bar(name_points, aver_points, color="yellow", width=Bar_width, label='Aver')
# plt.bar(name_points, median_points, color="blue", width=Bar_width, label='Median')
label_points = ["Max", "Min", "Aver", "Median"]

# Lan luot 4 bieu do

for i in range(1, 5):
    plt.bar(name_points, x[i], color="red", width=Bar_width)
    plt.title("Barchart about special values of each class")
    plt.xlabel("Object")
    plt.ylabel("Area")
    plt.legend([label_points[i-1]])
    plt.show()

# bieu do 4 cot
# plotdata = pd.DataFrame(
#     {
#         "Max": x[1],
#         "Min": x[2],
#         "Aver": x[3],
#         "Median": x[4]
#     },
#     index=x[0]
# )
# plotdata.plot(kind="bar")
# plt.title("Barchart about special values of each class")
# plt.xlabel("Object")
# plt.ylabel("Area")
# plt.legend()
# plt.show()
