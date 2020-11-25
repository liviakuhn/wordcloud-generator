import argparse as ap
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


LINKEDIN_COLORS = ['#0077B5', '#dce6f1']
CONTEXTA_COLORS = ['#00adee', '#e4097f']

BACKGROUND_COLOR = '#FFFFFF'
FONT_PATH = '/home/livia/font/Roboto-Regular.ttf'
COLORMAP = 'YlOrRd'
REGEXP = r'\w+( [\w]+)?'


def parse_args():
    parser = ap.ArgumentParser(
        description='Generate a word cloud from a list of words.')
    parser.add_argument('words_in', help='path to list of words')
    parser.add_argument('wordcloud_out', help='path to wordcloud')
    return parser.parse_args()


def read_word_list(words_in):
    with open(words_in, 'r') as src:
        words = [word.strip('\n') for word in src]
        word_dic = {}
        for word in words:
            if word not in word_dic:
                word_dic[word] = 1
            elif word in word_dic:
                word_dic[word] += 1
        return word_dic


def generate_wordcloud(word_dic):
    wordcloud = WordCloud(prefer_horizontal=1,
                          background_color=BACKGROUND_COLOR,
                          font_path=FONT_PATH,
                          colormap=COLORMAP,
                          regexp=REGEXP).generate(word_dic)
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
    wordcloud = generate_wordcloud(word_dic)
    save_wordcloud(args.wordcloud_out, wordcloud)
    display_wordcloud(wordcloud)


if __name__ == '__main__':
    main()
