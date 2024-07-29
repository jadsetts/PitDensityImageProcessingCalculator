#This function will measure the pits in the image based on an initial image processing step.
#This function requires some optimization and includes inherent subjectiveness.
#For images with many pits, it saves time, for an image with <10 pits, it likely doesn't save time.

#These are all the libraries you need.
import cv2 
import numpy as np 
from PIL import Image
import pyclesperanto_prototype as cle
import matplotlib.pyplot as plt

def flipBinary(array):
        returnThisArray=array
        for index1,i in enumerate(array):
            for index2,j in enumerate(i):
                if RGBBi == 'r':
                    returnThisArray[index1,index2]=255-j[0]
                elif RGBBi == 'g':
                    returnThisArray[index1,index2]=255-j[1]
                elif RGBBi == 'b':
                    returnThisArray[index1,index2]=255-j[2]
                elif RGBBi == 'binary':
                    returnThisArray[index1,index2]=255-j
        return returnThisArray

def pitsInImage(image, resizingScalar=1, threshold=100, imageSizeInmm2=10, RGBBi='binary', flipBinaryOption=0):

    #This prevents errors in the function.
    if resizingScalar < 1:
        return 'Cannot run function because \'resizingScalar\' is <1.'
    if RGBBi != 'r' and RGBBi != 'g' and RGBBi != 'b' and RGBBi != 'binary':
        return 'This function will not work.'
    #Resize the image based on resizingScalar
    image=Image.open(image)
    image2 = np.array(image.resize((int(image.size[0]/resizingScalar),int(image.size[1]/resizingScalar)), Image.Resampling.LANCZOS))
    
    #Load image and process it in 1 of 4 ways.
    imageLoaded=image2
    if RGBBi == 'r': #This converts RGB to R
        imageLoaded[:, :, 1] = 0
        imageLoaded[:, :, 2] = 0
    elif RGBBi == 'g': #This converts RGB to G
        imageLoaded[:, :, 0] = 0
        imageLoaded[:, :, 2] = 0
    elif RGBBi == 'b': #This converts RGB to B
        imageLoaded[:, :, 0] = 0
        imageLoaded[:, :, 1] = 0
    elif RGBBi == 'binary': #This converts RGB to R+G+B
        RGBPlusArray=np.zeros((imageLoaded.shape[0],imageLoaded.shape[1]))
        for xInt,x in enumerate(imageLoaded):
            for yInt,y in enumerate(x):
                RGBPlusArray[xInt][yInt]=imageLoaded[xInt,yInt,0]+imageLoaded[xInt,yInt,1]+imageLoaded[xInt,yInt,2]

    #Takes in a picture with RGB coordinates and flips them upside down, if requested.
    if flipBinaryOption == 1:
        if RGBBi == 'r' or RGBBi == 'g' or RGBBi == 'b': #This binarizes imageLoaded.
            imageLoaded=flipBinary(np.array(imageLoaded))
        elif RGBBi == 'binary': #This binarizes RGBPlusArray.
            RGBPlusArray=flipBinary(np.array(RGBPlusArray))

    #Binarizing images.
    if RGBBi == 'r' or RGBBi == 'g' or RGBBi == 'b': #This binarizes imageLoaded.
        binaryArray=np.zeros((imageLoaded.shape[0],imageLoaded.shape[1]))
        for xInt,x in enumerate(imageLoaded):
            for yInt,y in enumerate(x):
                if y[0] > threshold:
                    binaryArray[xInt][yInt]=1
                if y[0] <= threshold:
                    binaryArray[xInt][yInt]=0
    elif RGBBi == 'binary': #This binarizes RGBPlusArray.
        binaryArray=np.zeros((RGBPlusArray.shape[0],RGBPlusArray.shape[1]))
        for xInt,x in enumerate(RGBPlusArray):
            for yInt,y in enumerate(x):
                if y >= threshold:
                    binaryArray[xInt][yInt]=1
                if y < threshold:
                    binaryArray[xInt][yInt]=0

    #Labelling components
    cle.select_device("GTX")
    labeled = cle.connected_components_labeling_box(binaryArray)
    
    num_labels = cle.maximum_of_all_pixels(labeled)

    #Showing the binary array, then the labelled components.
    plt.figure()
    plt.imshow(image)
    plt.title('Original Image')
    plt.xticks(())
    plt.yticks(())

    plt.figure()
    plt.imshow(binaryArray)
    if flipBinaryOption == 1:
        plt.title('Binarized & Flipped')
    elif flipBinaryOption == 0:
        plt.title('Binarized & Not Flipped')
    plt.xticks(())
    plt.yticks(())

    plt.figure()
    plt.imshow(labeled)
    plt.title('Labeled Components')
    plt.xticks(())
    plt.yticks(())

    if num_labels == 0:
        return print('Please modify threshold or consider if this is appropriate because no pits were detected.')
    elif num_labels > 0:
        return print('The number of objects in this image is '+str(int(num_labels-1))+'.\nThe pit density is '+str(round(((num_labels-1)/imageSizeInmm2),4))+' pits/mm.')

#Calibrate the distance in images and provide size of image in millimeters squared.

#This is a trial and error function:
#You must continuously try co-ordinates that frame the scalebar perfectly (x1-x2,y1-y2).
#You must also add the distance the iamges scale bar is (scaleBarDistance).
#If you resize the photo for pit identification, you must redo this section.
#Put scaleBarDistance in millimeters.
#Most common image files are supported. List here: https://note.nkmk.me/en/python-opencv-imread-imwrite/

def calibrateDistance(image,x1,x2,y1,y2,scaleBarDistance):

    imageScalebar = cv2.imread(image)
    plt.figure()
    plt.imshow(imageScalebar)
    plt.xlim((x1,x2))
    plt.ylim((y1,y2))
    millimetersPerPixel=scaleBarDistance/(x2-x1)

    return print('The scalebar is '+str(round(millimetersPerPixel,6))+' mm/pixel, and the image is '+str(round(imageScalebar.shape[0]*millimetersPerPixel*imageScalebar.shape[1]*millimetersPerPixel,6))+' mm\u00b2. \nThe image below should perfectly frame the x positions of the scalebar.')
