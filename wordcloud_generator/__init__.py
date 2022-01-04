from os import getenv
from os.path import join, dirname
import argparse as ap
import json

import matplotlib.pyplot as plt

import generate

DIR_NAME = dirname(__file__)
IMAGE_PATH = join(DIR_NAME, '..', 'rectangle.png')
FONT_PATH = join(DIR_NAME, '..', 'fonts/roboto/OpenSans-Regular.ttf')


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
    parser.add_argument('--display',
                        help='display wordcloud upon generation',
                        action='store_true')
    parser.add_argument('--use_image_colors',
                        help='use colors of image',
                        action='store_true')
    return parser.parse_args()


def read_word_list(words_in):
    with open(words_in, 'r') as src:
        word_dic = json.load(src)
        return word_dic


def save_wordcloud(wordcloud_out, wordcloud):
    wordcloud.to_file(wordcloud_out)


def display_wordcloud(wordcloud):
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


def main():
    args = parse_args()
    word_dic = read_word_list(args.words_in)
    wordcloud = generate.main(word_dic,
                              args.image,
                              args.font,
                              args.use_image_colors)
    save_wordcloud(args.wordcloud_out, wordcloud)
    if args.display:
        display_wordcloud(wordcloud)


if __name__ == '__main__':
    main()
