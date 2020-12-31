import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_gradient_magnitude
from wordcloud import WordCloud, ImageColorGenerator

COLORMAP = 'summer'
BACKGROUND_COLOR = '#FFFFFF'
HEIGHT = 768
WIDTH = 1536
PREFER_HORIZONTAL = 1
RANDOM_STATE = 50
REPEAT = True


def generate_mask(image_path):
    colors = np.array(Image.open(image_path))
    mask = colors.copy()
    edges = np.mean(
        [gaussian_gradient_magnitude(colors[:, :, i] / 255.0, 2)
         for i in range(3)], axis=0)
    mask[edges > 0.8] = 255
    return colors, mask


def main(word_dic, image_path, font_path, use_image_colors):
    colors, mask = generate_mask(image_path)
    wordcloud = WordCloud(mask=mask,
                          font_path=font_path,
                          regexp=r'\w+( [\w]+)?',
                          colormap=COLORMAP,
                          background_color=BACKGROUND_COLOR,
                          height=HEIGHT,
                          width=WIDTH,
                          prefer_horizontal=PREFER_HORIZONTAL,
                          random_state=RANDOM_STATE,
                          repeat=REPEAT).generate_from_frequencies(word_dic)
    if use_image_colors:
        image_colors = ImageColorGenerator(colors)
        wordcloud.recolor(color_func=image_colors)
    return wordcloud
