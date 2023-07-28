from PIL import Image,ImageFilter

img = Image.open("images/pikachu.jpg")
print(img)
#ImageFilter has lot of methods like blur sharp smooth...
filtered_img = img.filter(ImageFilter.BLUR)
# jpg throws error so png is used
filtered_img.save("formatted_images/blur.png","png")

#we can even convert the images, L for black n white images
converted_img = img.convert('L')
converted_img.save("formatted_images/grey.png","png")
converted_img.show() #displays the image

#image rotation
rotate_img = converted_img.rotate(90)#rotates to 90 degrees
rotate_img.save("formatted_images/rotate.png","png")

#resize the image
resize_img = converted_img.resize((500,500))#takes dimensions in a tuple
resize_img.save("formatted_images/resize.png","png")

#crop the image
box = (100,100,400,400)
crop_image = converted_img.crop(box)
crop_image.save("formatted_images/crop.png","png")

#resize the image i.e., create a thumbnail without changing the aspect ratio
#resize will actually squeeze the image so use thumbnail to keep the aspect ration intact
#thumbnail - is useful wen u want to create profile pic for fb, insta etc
astro_img = Image.open("images/astro.jpg")
#print(astro_img.size)
# here the widthXheight will be max 400X200, the system intelligently decides which will be best
astro_img.thumbnail((400,200))
#print(astro_img.size)
astro_img.save("formatted_images/astro_thumb.jpg")