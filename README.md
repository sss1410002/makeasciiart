# asciiart
Convert image to ascii art

## Dependency
```
pip install opencv-python
pip install numpy
```
```python
import img2ascii as i2a

import numpy as np
import cv2
```

## img2ascii.py
```python
def img2ascii(filename, color_mode=True, fontsize=5):
return img,newimg # img : original image, newimg : ascii art image
```

## Example 1
```python
filename = 'test.jfif'
origin, newimg = i2a.img2ascii(filename)
if type(newimg) == type(None):
    exit()
cv2.imshow("origin", origin)
cv2.imshow("res", newimg)
cv2.waitKey()
cv2.destroyAllWindows()
```
