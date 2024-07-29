#Example of all functions being used on an example picture provided.

image=(r'Picture1.jpg')
resizingScalar=1 #1 is the same image, 4 is 25 % of the original resolution, cannot go below 1 or above height/width.
threshold=220 #This changes how the binarization occurs.
imageSizeInmm2=29.607266 #From 'calibrateDistance' function.
RGBBi='binary' #This could be 'r','g','b','binary'
flipBinaryOption = 1 #0 does nothing, 1 inverts binary

pitsInImage(image,resizingScalar,threshold,imageSizeInmm2,RGBBi,flipBinaryOption)

#Example of the function working.

image=(r'Picture1.jpg')
scaleBarDistance=0.500 #In millimeters
x1=190
x2=207
y1=155
y2=157
calibrateDistance(image,x1,x2,y1,y2,scaleBarDistance)
