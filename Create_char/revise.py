import os
import csv
def analyze_training_database(folder: str):
    # folder = "/home/nhan/Computer/tranning/label/V2/2"
    open_class = open(f'{folder}/classes.txt', 'r')
    content = open_class.read()
    list_of_class = content.split()
    chose_folder = os.listdir(folder)

    list_img = [f for f in chose_folder if f.endswith('.jpg')]

    list_area = [[] for i in range(12)]

    for i in chose_folder:
        if i.endswith('.txt'):
            if i == 'classes.txt':
                continue
            with open(os.path.join(folder, i), 'r') as file:
                lines = csv.reader(file)
                for line in lines:
                    # line : array with size = 1
                    paras = line[0]
                    class_index_str, x, y, w, h = paras.split(' ')
                    class_index_str, x, y, w, h = int(class_index_str), float(x), float(y), float(w), float(h)
                    list_area[class_index_str].append(w*h)

    list_max_area = []
    list_min_area = []
    list_aver_area = []
    list_median_area = []
    for i in range(12):
        op_area = list_area[i]
        list_max_area.append(max(op_area))
        list_min_area.append(min(op_area))
        list_aver_area.append(sum(op_area) / len(op_area))
        if len(op_area) % 2 == 0:
            list_median_area.append((op_area[int(len(op_area) / 2)] + op_area[int(len(op_area)/2 - 1)] / 2))
        else:
            list_median_area.append(op_area[int(len(op_area)/2)])
    return list_of_class, list_max_area, list_min_area, list_aver_area, list_median_area
