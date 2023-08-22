from matplotlib import pyplot
from matplotlib.image import imread

training_damaged_image = "train/damage/image (1).jpeg"

# load image pixels
image = imread(training_damaged_image)

pyplot.title("damaged: Image 1")

# plot raw pixel data
pyplot.imshow(image)

# show the figure
pyplot.show()