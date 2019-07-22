import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2

def img2ascii(filename, color_mode=True, fontsize=5):
    img = cv2.imread(filename)

    if type(img) == type(None):
        print("[-] Error 2 : Cannot find filename")
        return None, None

    fontpath = './d2coding.ttc'
    font = ImageFont.truetype(fontpath, fontsize)
    font_h = int(5+4/5*fontsize)
    font_w = int(1+2/5*fontsize)
    
    asciibright = '@#%$&/=+;. '
    h, w = img.shape[:2]

    newimg = np.zeros((int(h), w, 3), np.uint8)
    newimg[:,:] = (255,255,255)
    
    img_pil = Image.fromarray(newimg)
    draw = ImageDraw.Draw(img_pil)

    ## Color
    if color_mode:
        sum = [[[0 for k in range(3)] for i in range(int((w+font_w-1)/font_w))] for j in range(int((h+font_h-1)/font_h))]
        cnt = [[0 for i in range(int((w+font_w-1)/font_w))] for j in range(int((h+font_h-1)/font_h))]


        for y in range(h):
            for x in range(w):
                for k in range(3):
                    sum[int(y/font_h)][int(x/font_w)][k] += img[y][x][k]
                cnt[int(y/font_h)][int(x/font_w)] += 1

        txt=''
        for y in range(int((h+font_h-1)/font_h)):
            for x in range(int((w+font_w-1)/font_w)):
                txt = asciibright[int((sum[y][x][0]+sum[y][x][1]+sum[y][x][2])/3/cnt[y][x]/(256/len(asciibright)))]
                b,g,r,a = int(sum[y][x][0]/cnt[y][x]),int(sum[y][x][1]/cnt[y][x]),int(sum[y][x][2]/cnt[y][x]),0
                draw.text((x*font_w, y*font_h),  txt, font = font, fill = (b, g, r, a))
            txt+='\n'
    ## Grayscale
    else:
        sum = [[0 for i in range(int((w+font_w-1)/font_w))] for j in range(int((h+font_h-1)/font_h))]
        cnt = [[0 for i in range(int((w+font_w-1)/font_w))] for j in range(int((h+font_h-1)/font_h))]

        for y in range(h):
            for x in range(w):
                sum[int(y/font_h)][int(x/font_w)] += grayimg[y][x]
                cnt[int(y/font_h)][int(x/font_w)] += 1

        txt=''
        for y in range(int((h+font_h-1)/font_h)):
            for x in range(int((w+font_w-1)/font_w)):
                txt = temp[int(sum[y][x]/cnt[y][x]/(256/len(temp)))]
                b,g,r,a = 0,0,0,0
                draw.text((x*font_w, y*font_h),  txt, font = font, fill = (b, g, r, a))
            txt+='\n'

    newimg = np.array(img_pil)
    
    return img,newimg