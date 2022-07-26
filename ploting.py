import cv2 as cv
from matplotlib import pyplot as plt


img= cv.imread("messi5.jpg",-1)
img1= cv.cvtColor(img,cv.COLOR_BGR2RGB)

cv.imshow("image",img)

plt.imshow(img1)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
