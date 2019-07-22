
import img2ascii as i2a

import numpy as np
import cv2

## Display
filename = 'test.jfif'
origin, newimg = i2a.img2ascii(filename)
if type(newimg) == type(None):
    exit()
cv2.imshow("origin", origin)
cv2.imshow("res", newimg)
cv2.waitKey()
cv2.destroyAllWindows()