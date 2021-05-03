from PIL import Image
# you need to have an image in the same directory as the python file
img = Image.open('me.jpg')        # img is the object of class image
print(img.size)      # shows the size of the image
print(img.format)      # shows the format of the file
img.show()       # the image opens in default image processing software either photoshop or any browser
