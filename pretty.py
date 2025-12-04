import numpy as np
import matplotlib.pyplot as plt
import time

# Time to run is around 30s, mostly from the rendering, smaller iterations
# speeds it up a lot
start = time.clock()
# Linearly scales a number to be within a given range
def scale(num,num_min,num_max,range_min,range_max):
    return(((num - num_min)/(num_max-num_min))*(range_max - range_min) + range_min)

# Iterating like this is faster than z**n
def compow(z,n):
    if n >= 2:
        for q in range(1,n):
            z = z*z
    return(z)
    
    
# Produces a plot of the Julia set
# pixel_x, pixel_y denotes the size of the image
# zx_min/max is the range of the real component of the complex plane we plot on
# Similarly for zy_min/max but it is the complex component
# c is the constant in z_n = (z_n-1)*n + c
# n is the power in the recurrence relation
# Method:   
# We take a pixel and scale it to be in the complex plane and then determine
# how many iterations for it to diverge, essentially like storing a normal image
# where the number is the RGB value or similar.
# This was far faster than plotting each point which would take almost a minute
# whereas this method takes a few seconds 
    

def julia(pixel_x, pixel_y, zx_min, zx_max, zy_min, zy_max, c, n, iterations):
    # Create a matrix that will hold the number of iterations for each pixel
    mat = np.zeros((pixel_y,pixel_x))
    # Iterate over every pixel
    for x in range(pixel_x):
        for y in range(pixel_y):
            i = 0
            # Scale the pixel to be within the complex plane
            xn = scale(x,0,pixel_x-1,-2,2)
            yn = scale(y,0,pixel_y-1,-1,1)
            # Convert into a complex number
            z = complex(xn,yn)
            zt = z
            # Iterate the relation until it either diverges or we reach max
            # iterations which implies it is bounded
            while (i < iterations) and (zt.real*zt.real + zt.imag*zt.imag <= 5):
                zt = compow(zt,n) + c
                i += 1
            # If it diverges leave it as a color value of 0
            if i == iterations:
                mat[y,x] = 0
            # Assign the color to the pixel position in the matrix
            else:
                mat[y,x] = i
    return(mat)
    
# Essentially the same as the Julia function but instead we are testing values
# of c and iterating from z = 0 as the initial value
def mandelbrot(pixel_x, pixel_y, zx_min, zx_max, zy_min, zy_max, n, iterations):
    # Create a matrix that will hold the number of iterations for each pixel
    mat = np.zeros((pixel_y,pixel_x))
    # Iterate over every pixel
    for x in range(pixel_x):
        for y in range(pixel_y):
            xn = scale(x,0,pixel_x-1,-2,2)
            yn = scale(y,0,pixel_y-1,-1,1)
            c = complex(xn,yn)
            i = 0
            zt = 0
            # Iterate the relation until it either diverges or we reach max
            # iterations which implies it is bounded
            while (i < iterations) and (zt.real*zt.real + zt.imag*zt.imag <= 5):
                zt = compow(zt,n) + c
                i += 1
            # If it diverges leave it as a color value of 0
            if i == iterations:
                mat[y,x] = 0
            # Assign the color to the pixel position in the matrix
            else:
                mat[y,x] = i
    return(mat)
  
    



fig = plt.figure()
# f(z) = z^2 - (-0.75 +0.25i), 'seahorse dust' creates a very nice looking  picture
#ar = julia(1920,1080,-2,2,-1,1,complex(-0.75,0.25),2,200)
ar = julia(3840,2160,-2,2,-1,1,complex(0.5,-0.4),3,200)
plt.imshow(ar,cmap = 'viridis')
plt.imsave('coollightning.png', ar)
plt.show()


print(time.clock() - start)  




    
