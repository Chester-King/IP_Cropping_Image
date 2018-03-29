from PIL import Image
import numpy as np
# Using pillow and numpy libraries
ml=[]
img=Image.open("IP.png") #opening image IP.png

a=np.asarray(img) #a is a numpy nd.array which stores the RGB value of each pixel
k=list(a.shape)  #create list of cordinates of the image(Number of rows and columns of pixels)

hx=0
lx=0
hy=0
ly=0
for i in range(k[0]):  #running loop to check RGB value of each pixel
    for j in range(k[1]):
        if(a[i,j].all()==0):
            ml.append([i,j]) #storing the address of all the pixels which are black in color

#Initializing all the four variables to define the required square
hx=ml[0][0]
lx=ml[0][0]
hy=ml[0][1]
ly=ml[0][1]


for y in ml:  # looping through all the address of pixels  which are black
    if(y[0]>hx):
        hx=y[0]   # max value of x coordinate
    if (y[0] < lx):
        lx = y[0]  #min value of x coordinate
    if (y[1] > hy):
        hy = y[1]   # max value of y coordinate
    if (y[1] < ly):
        ly = y[1]  # min value of y coordinate
newarray=a[lx:hx+1,ly:hy+1] # keeping only necessary part of the array
newim=Image.fromarray(newarray)  # forming image using numpy arary containing 'RGB' values
newim.show()  # Show Image