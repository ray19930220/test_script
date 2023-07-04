import cv2
import var


def puttext():
    blank = var.blank_image.copy()
    blank = cv2.putText(
        blank,
        f"skill:{(int)(var.skill_time)}",
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2,
    )
    # blank = cv2.putText(blank, f"t:{(int)(var.T_time_happen)}", (30, 90), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 255, 255), 2)
    # blank = cv2.putText(blank, f"g:{(int)(var.G_time_happen)}", (30, 130), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 255, 255), 2)
    img_copy = var.img.copy()
    img_copy = cv2.line(img_copy, (var.value, 30), (var.value, 150), (0, 0, 255), 2)
    img_copy = cv2.line(
        img_copy, (var.value + 20, 30), (var.value + 15, 150), (0, 0, 255), 2
    )
    display_images("img_copy", img_copy)


def display_images(window_name, image):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.imshow(window_name, image)

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # cv2.imshow("Image", var.img)
        print(ix, iy, x, y)
        var.region = (ix + 10, iy + 30, x, y)

    if event == cv2.EVENT_RBUTTONDOWN:
        var.value = x
        print("座標：({},{})".format(x, y))
