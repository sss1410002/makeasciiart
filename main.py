import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2
import time

## Make canvas and set the color
img = cv2.imread('./test.jpg')
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

fontsize = 5
temp = '@#%$&/=+;. '
h, w = grayimg.shape[:2]

# Grayscale version
newimg = np.zeros((int(h), w, 3), np.uint8)
newimg[:,:] = (255,255,255)
font_h = 9*fontsize/5
font_w = 3*fontsize/5
#fontsize = 10
#font_h = 13*fontsize/fontsize
#font_w = 5*fontsize/fontsize
print(h)
print(w)

fontpath = './d2coding.ttc'
font = ImageFont.truetype(fontpath, fontsize)
img_pil = Image.fromarray(newimg)
draw = ImageDraw.Draw(img_pil)

sum = [[0 for i in range(int((w+font_w-1)/font_w))] for j in range(int((h+font_h-1)/font_h))]
cnt = [[0 for i in range(int((w+font_w-1)/font_w))] for j in range(int((h+font_h-1)/font_h))]

for y in range(h):
    for x in range(w):
        sum[int(y/font_h)][int(x/font_w)] += grayimg[y][x]
        cnt[int(y/font_h)][int(x/font_w)] += 1
#        print(grayimg[y][x], end=' ')
#    print()

txt=''
for y in range(int((h+font_h-1)/font_h)):
    for x in range(int((w+font_w-1)/font_w)):
        txt = temp[int(sum[y][x]/cnt[y][x]/(256/len(temp)))]
        b,g,r,a = 0,0,0,0
        #draw.text((y*font_h, x*font_w),  txt, font = font, fill = (b, g, r, a))
        draw.text((x*font_w, y*font_h),  txt, font = font, fill = (b, g, r, a))
#        print(sum[y][x], end=' ')
#    print()
    txt+='\n'

newimg = np.array(img_pil)

# Color version
newimg2 = np.zeros((int(h), w, 3), np.uint8)
newimg2[:,:] = (255,255,255)
img_pil = Image.fromarray(newimg2)
draw = ImageDraw.Draw(img_pil)

sum = [[[0 for k in range(3)] for i in range(int((w+font_w-1)/font_w))] for j in range(int((h+font_h-1)/font_h))]
cnt = [[0 for i in range(int((w+font_w-1)/font_w))] for j in range(int((h+font_h-1)/font_h))]

for y in range(h):
    for x in range(w):
        for k in range(3):
            sum[int(y/font_h)][int(x/font_w)][k] += img[y][x][k]
        
        cnt[int(y/font_h)][int(x/font_w)] += 1
#        print(grayimg[y][x], end=' ')
#    print()

txt=''
for y in range(int((h+font_h-1)/font_h)):
    for x in range(int((w+font_w-1)/font_w)):
        txt = temp[int((sum[y][x][0]+sum[y][x][1]+sum[y][x][2])/3/cnt[y][x]/(256/len(temp)))]
        b,g,r,a = int(sum[y][x][0]/cnt[y][x]),int(sum[y][x][1]/cnt[y][x]),int(sum[y][x][2]/cnt[y][x]),0
        #draw.text((y*font_h, x*font_w),  txt, font = font, fill = (b, g, r, a))
        draw.text((x*font_w, y*font_h),  txt, font = font, fill = (b, g, r, a))
#        print(sum[y][x], end=' ')
#    print()
    txt+='\n'

newimg2 = np.array(img_pil)

## Display 
cv2.imshow("gray", grayimg)
cv2.imshow("res", newimg)
cv2.imshow("color", img)
cv2.imshow("res2", newimg2)
cv2.waitKey()
cv2.destroyAllWindows()