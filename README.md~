#cooler
#======
#A set of image processing and computer vision utilities.
#Developers:
#Indu
import os
import sys
import Image
import ImageFilter
import ImageEnhance
img_fil = Image.open("cutest_puppy-wide.jpg")
img_log = Image.open("logo.png")
img_log.show()
print img_fil.format, img_fil.size, img_fil.mode
enh=ImageEnhance.Contrast(img_fil)
enh.enhance(1.3).show("30% more contrast")
new_log_height=0.15*img_fil.size[1]
new_log_width=img_log.size[0]*new_log_height/img_log.size[1]
img_log=img_log.resize((int(new_log_width),int(new_log_height)),Image.ANTIALIAS)
img_fil.paste(img_log,(img_fil.size[0]-img_log.size[0],img_fil.size[1]-img_log.size[1]))
img_fil.show()
