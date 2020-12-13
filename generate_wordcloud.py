from os import getenv
from os.path import join
import argparse as ap
import json
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.ndimage import gaussian_gradient_magnitude
from wordcloud import WordCloud, ImageColorGenerator

BACKGROUND_COLOR = '#FFFFFF'
COLORMAP = 'summer'
REGEXP = r'\w+( [\w]+)?'

HOME_DIR = getenv('HOME')
FONT_PATH = join(HOME_DIR, 'font/Roboto-Regular.ttf')
IMAGE_PATH = join(HOME_DIR, 'ellipse.png')


def parse_args():
    parser = ap.ArgumentParser(
        description='Generate a word cloud from a word-frequency dictionary.')
    parser.add_argument('words_in',
                        help='path to word-frequency dictionary')
    parser.add_argument('wordcloud_out',
                        help='path to wordcloud')
    parser.add_argument('--font',
                        help='path to font',
                        default=getenv('FONT_PATH', FONT_PATH))
    parser.add_argument('--image',
                        help='path to image to be used as mask',
                        default=getenv('IMAGE_PATH', IMAGE_PATH))
    return parser.parse_args()


def read_word_list(words_in):
    with open(words_in, 'r') as src:
        word_dic = json.load(src)
        return word_dic


def _generate_mask(image_path):
    colors = np.array(Image.open(image_path))
    mask = colors.copy()
    edges = np.mean(
        [gaussian_gradient_magnitude(colors[:, :, i] / 255.0, 2)
         for i in range(3)], axis=0)
    mask[edges > 0.8] = 255
    return colors, mask


def generate_wordcloud(word_dic, font_path, image_path):
    colors, mask = _generate_mask(image_path)
    wordcloud = WordCloud(prefer_horizontal=1,
                          background_color=BACKGROUND_COLOR,
                          font_path=font_path,
                          # relative_scaling=.25,
                          # random_state=28,
                          # margin=10,
                          repeat=True,
                          colormap=COLORMAP,
                          mask=mask,
                          width=1536,
                          height=768,
                          regexp=REGEXP).generate_from_frequencies(word_dic)
    # image_colors = ImageColorGenerator(colors)
    # wordcloud.recolor(color_func=image_colors)
    return wordcloud


def save_wordcloud(wordcloud_out, wordcloud):
    wordcloud.to_file(wordcloud_out)


def display_wordcloud(wordcloud):
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


def main():
    args = parse_args()
    word_dic = read_word_list(args.words_in)
    wordcloud = generate_wordcloud(word_dic, args.font, args.image)
    save_wordcloud(args.wordcloud_out, wordcloud)
    display_wordcloud(wordcloud)


if __name__ == '__main__':
    main()
