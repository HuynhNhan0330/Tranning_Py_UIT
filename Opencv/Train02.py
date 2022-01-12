import cv2
import random

def edit_img (folder : str):
    img = cv2.imread(f'{folder}/img1.jpg')
    img_resize = cv2.resize(img, (0, 0), fx=0.4, fy=0.4)
    (h, w, d_color) = img_resize.shape
    center = (w//2, h//2)
    times_click = 0
    radian = 0
    while times_click < 22:
        img = cv2.imread(f'{folder}/img1.jpg')
        img_resize = cv2.resize(img, (0, 0), fx=0.4, fy=0.4)
        if times_click == 0:
            img_new = img_resize
        if times_click == 1:
            x = random.randrange(1, w)
            y = random.randrange(1, h)
            r = random.randrange(10, 30)
            img_new = cv2.circle(img_resize, (x, y), r, (255, 0, 0), 3)
        if times_click == 2:
            x1 = random.randrange(1, w)
            y1 = random.randrange(1, h)
            x2 = random.randrange(1, w)
            y2 = random.randrange(1, h)
            img_new = cv2.rectangle(img_resize, (x1, y1), (x2, y2), (0, 255, 0), 3)
        if times_click == 3:
            x = random.randrange(1, w)
            y = random.randrange(1, h)
            img_new = cv2.putText(img_resize, 'Huynh Mai Cao Nhan', (x, y), cv2.FONT_ITALIC, 5, (0, 0, 255), 2, cv2.LINE_AA)
        if times_click > 3:
            radian += 10
            matrix = cv2.getRotationMatrix2D(center, radian, 1.0)
            img_new = cv2.warpAffine(img_resize, matrix, (w, h))

        cv2.imshow("Anh", img_new)
        k = cv2.waitKey()
        if k == ord('q'):
            break
        times_click += 1

    cv2.destroyAllWindows()
