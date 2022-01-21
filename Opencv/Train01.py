import cv2
import os

def next_img (folder : str):
    chose_folder = os.listdir(folder)
    index = 0
    list_img = [f for f in chose_folder if f.endswith('.jpg')]
    n = len(list_img)
    while index < n:
        file_img = list_img[index]

        img = cv2.imread(f'{folder}/{file_img}')
        img_resize = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow("Anh", img_resize)
        k = cv2.waitKey()
        if k == ord('q'):
            break
        if k == 82 and index > 0:
            index -= 1
        if k == 84 and index < n-1:
            index += 1
    cv2.destroyAllWindows()

