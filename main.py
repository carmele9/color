import cv2
import numpy as np
import pandas as pd
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args["image"]
img = cv2.imread(img_path)

index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv("colores.csv", names= index, header= None)
b= g= r= xpos= ypos = 0
clicked = False
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r, xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos= y
        b,g,r = img[y,x]
        b = int(b)
        g= int(g)
        r = int(r)

def get_color_name(R,G,B):
    min = 10000
    for i in range (len(csv)):
        d = abs(R-int(csv.loc[i,"R"]))+ abs(G-int(csv.loc[i,"G"]))+ abs(B-int(csv.loc[i,"B"]))
        if d <= min:
            min = d
            cname = csv.loc[i,"color_name"]
    return cname

cv2.namedWindow("Image")
cv2.setMouseCallback("Image",draw_function)
while (True):
    cv2.imshow("Image", img)
    if clicked:
        cv2.rectangle(img,(20,20), (560,60),(b,g,r),thickness=-1)
        text = get_color_name(r,g,b) + " R: " + str(r) + " G: " + str(g) + " B: " + str(b)
        cv2.putText(img,text,(50,50),2, 0.8, (255,255,255), 2, cv2.LINE_AA)
        if r+g+b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        clicked = False
    if cv2.waitKey(20) & 0xff == 27:
        break
cv2.destroyAllWindows()





