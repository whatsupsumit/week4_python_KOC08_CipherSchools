# installation of pillow library 
# change the image extension 
# resize image files
# resize image files
# resize multiple images using for loop
# sharpness 
# brightness
# color 
# contrast
# image blur , guassian blur


from PIL import Image, ImageEnhance
import os
img1 = Image.open('v.jpg')
# img1 = Image.open('v.jpg')
# img1.show('v.pdf')
max_size = (250,250)
img1.thumbnail(max_size)
img1.save('vsmall.jpg')
for item in os.listdir():
    if item.endswith(".jpg"):
      img1= Image.open(item)
      filename, extension = os.path.splitext(item)
      img1.save(f'{filename}.png')
img1 = Image.open('v.jpg')
enhancer = ImageEnhance.Sharpness(img1)
enhancer.enhance(5).save('vedited.jpg')

        
    
    