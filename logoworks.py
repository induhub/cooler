import os
import sys
import Image
import ImageFilter
import ImageEnhance
import numpy as np
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
# color transparency
threshold=100
dist=5
img=Image.open(logo.png).convert('RGBA')
# np.asarray(img) is read only. Wrap it in np.array to make it modifiable.
arr=np.array(np.asarray(img))
r,g,b,a=np.rollaxis(arr,axis=-1)    
mask=((r>threshold)
      & (g>threshold)
      & (b>threshold)
      & (np.abs(r-g)<dist)
      & (np.abs(r-b)<dist)
      & (np.abs(g-b)<dist)
      )
arr[mask,3]=0
img=Image.fromarray(arr,mode='RGBA')
img.save('/tmp/out.png')
img_fil.show()
