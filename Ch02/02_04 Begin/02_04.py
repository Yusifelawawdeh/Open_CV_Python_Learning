import numpy as np
import cv2

color = cv2.imread("butterfly.jpg", 1)
cv2.imshow("image", color)
cv2.moveWindow("image",0,0)
print(color.shape)

# split the image into its base attributes
height,width,channels = color.shape

# similiar to remote sensing clas where you use imgread() in matlab to split() and image into its channels
# likely similiar function in ENVI
b,g,r = cv2.split(color)
rgb_split = np.empty([height, width*3, 3], 'uint8')
rgb_split[:, 0:width] = cv2.merge([b, b, b])
rgb_split[:, width:width*2] = cv2.merge([g, g, g])
rgb_split[:, width*2:width*3] = cv2.merge([r, r, r])

# show the image channels in their additive state aka they are b&w because r.g.b is numerical 0 - 255
cv2.imshow("channels", rgb_split)
cv2.moveWindow("channels", 0, height)

# converting from rgb to hsv Hue, saturation, value or luminance
# honestly feels like photoshop but in coding interface
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
hsv_split = np.concatenate((h,s,v), axis=1)
cv2.imshow("Split HSV", hsv_split)

cv2.waitKey(0)
cv2.destroyAllWindows()


