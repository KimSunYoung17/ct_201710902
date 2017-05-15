
from PIL import Image

m = Image.open("C:\\Users\\SeonYoungKim\\Downloads\\italy-1587287_1920.jpg")

m.show()

get_ipython().magic(u'matplotlib inline')
from matplotlib.pyplot import imshow
imshow(m)



from PIL import Image
m = Image.open("C:\\Users\\SeonYoungKim\\Downloads\\italy-1587287_1920.jpg")
m.save("C:\\Users\\SeonYoungKim\\Downloads\\italy-1587287_1920.gif")


m.show()

get_ipython().magic(u'matplotlib inline')
from matplotlib.pyplot import imshow
imshow(m)

