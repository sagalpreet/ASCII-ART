from PIL import Image
import numpy as np

image = Image.open('Source') # replace with source file path
y = 1000
image = image.resize((int(1.75*y),y))
imageArray = np.asarray(image)

imageArray = imageArray.astype('float64')

xx = (np.max(imageArray))
imageArray = ( imageArray / xx ) * 255
np.sum(imageArray>0)

try:
    grayImageArray = np.array([[0 for i in range(imageArray.shape[1])] for j in range(imageArray.shape[0])])
    for i in range(imageArray.shape[0]):
        for j in range(imageArray.shape[1]):
            x = ( (imageArray[i][j][0]) + (imageArray[i][j][1]) + (imageArray[i][j][2]) )
            grayImageArray[i][j] = x/3
except:
    grayImageArray = imageArray
dest = open ( 'Destination' , 'w' ) # replace with destination file path

grayLevels = '.:-=+*#%@'

for i in range(imageArray.shape[0]):
    for j in range(imageArray.shape[1]):
        densityLevel = ( 9 * (grayImageArray[i][j]) ) // 255
        densityLevel = int(min(densityLevel, 8))
        print(grayLevels[densityLevel], end='')
        dest.write(grayLevels[densityLevel])
    print()
    dest.write('\n')
