from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import img_to_array, load_img, array_to_img
import tqdm

datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest")

image = load_img(r"E:\Coding\Python\PROJECTS\ML\Data_augumentation\sampledata\monkey.jpg")
x = img_to_array(image) #(549, 976, 3)
print(x.shape)
x = x.reshape((1,) + x.shape)  #adding another dimension(1, 549, 976, 3)
print(x.shape) 

i = 0
for batch in datagen.flow(x, batch_size=1, save_to_dir=r"E:\Coding\Python\PROJECTS\ML\Data_augumentation\sampledata", save_prefix="augumented", save_format="jpg"):
    i += 1
    if i > 20:
        break  #will save 20 images  other wise it will save infinate images