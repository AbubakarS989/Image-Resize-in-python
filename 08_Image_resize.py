import cv2 

# welcome window

print("welcome to the :\n   I M A G E - R E S I Z E - P R O G R A M")
#  all Inputs

# image name
user_src=input("Enter the location of the image")
image=cv2.imread(user_src)
# image resized percentage
image_percent=int(input("Enter the REsize Percentage of the image"))
#  image destination
destination=input("Enter your New Resize image name of any formate.")



#  calculate the original image with image_percent
new_width=int(image.shape[1]*image_percent/100)
new_height=int(image.shape[0]*image_percent/100)    


#  create tuple 
dsize=(new_width,new_height)

# resize function use image with tuple where height and width is store
output=cv2.resize(image,dsize)

#  here we output the resize pic

cv2.imwrite(destination,output)

cv2.waitKey(0)