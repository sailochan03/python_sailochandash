import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path
from card import Card
from deckOfCards import DeckOfCards as dc

deck = dc()
path = Path('.').joinpath('card_images')

fig, axes_list = plt.subplots(nrows = 13, ncols = 4)

for axes in axes_list.ravel():
    axes.set_axis_off()
    image_name = deck.deal_card().image_name()
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)

plt.show()