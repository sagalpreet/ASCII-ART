from PIL import Image
import numpy as np

image = Image.open('d:/z_temp/za.png')
imageArray = np.asarray(image)

imageArray.shape

image = image.resize((1750, int(1000 * int(imageArray.shape[0])/int(imageArray.shape[1]) ) ) )
image.size
imageArray = np.asarray(image)

grayImageArray = np.array([[0 for i in range(imageArray.shape[1])] for j in range(imageArray.shape[0])])
for i in range(imageArray.shape[0]):
     for j in range(imageArray.shape[1]):
        x = ( int(imageArray[i][j][0]) + int(imageArray[i][j][1]) + int(imageArray[i][j][2]) )
        grayImageArray[i][j] = np.uint8(x // 3)

grayLevels = '.:-=+*#%@'

for i in range(imageArray.shape[0]):
    for j in range(imageArray.shape[1]):
        densityLevel = ( 9 * int(grayImageArray[i][j]) ) // 255
        densityLevel = min(densityLevel, 8)
        print(grayLevels[densityLevel], end='')
    print()
