from os import getenv
from os.path import join
import argparse as ap
import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud

BACKGROUND_COLOR = '#FFFFFF'
COLORMAP = 'viridis'
REGEXP = r'\w+( [\w]+)?'

HOME_DIR = getenv('HOME')
FONT_PATH = join(HOME_DIR, 'font/Roboto-Regular.ttf')


def parse_args():
    parser = ap.ArgumentParser(
        description='Generate a word cloud from a word-frequency dictionary.')
    parser.add_argument('words_in',
                        help='path to word-frequency dictionary')
    parser.add_argument('wordcloud_out',
                        help='path to wordcloud')
    parser.add_argument('--font',
                        help='path to font',
                        default=getenv('FONT_PATH'))
    return parser.parse_args()


def read_word_list(words_in):
    with open(words_in, 'r') as src:
        word_dic = json.load(src)
        return word_dic


def generate_wordcloud(word_dic, font_path):
    wordcloud = WordCloud(prefer_horizontal=1,
                          background_color=BACKGROUND_COLOR,
                          font_path=font_path,
                          colormap=COLORMAP,
                          width=1536,
                          height=768,
                          regexp=REGEXP).generate_from_frequencies(word_dic)
    return wordcloud


def save_wordcloud(wordcloud_out, wordcloud):
    wordcloud.to_file(wordcloud_out)


def display_wordcloud(wordcloud):
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


def main():
    args = parse_args()
    if args.font and args.font != '':
        font_path = args.font
    else:
        font_path = FONT_PATH
    word_dic = read_word_list(args.words_in)
    wordcloud = generate_wordcloud(word_dic, font_path)
    save_wordcloud(args.wordcloud_out, wordcloud)
    display_wordcloud(wordcloud)


if __name__ == '__main__':
    main()
