import argparse as ap
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def parse_args():
    parser = ap.ArgumentParser(
        description='Generate a word cloud from a list of words.')
    parser.add_argument('words_in', help='path to list of words')
    parser.add_argument('wordcloud_out', help='path to wordcloud')
    return parser.parse_args()


def read_word_list(words_in):
    with open(words_in, 'r') as src:
        words = src.read()
        return words


def generate_wordcloud(words):
    wordcloud = WordCloud().generate(words)
    return wordcloud


def save_wordcloud(wordcloud_out, wordcloud):
    wordcloud.to_file(wordcloud_out)


def display_wordcloud(wordcloud):
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


def main():
    args = parse_args()
    words = read_word_list(args.words_in)
    wordcloud = generate_wordcloud(words)
    save_wordcloud(args.wordcloud_out, wordcloud)
    display_wordcloud(wordcloud)


if __name__ == '__main__':
    main()
