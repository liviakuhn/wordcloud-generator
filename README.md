# Wordcloud Generator #

### Summary ###

* This tool uses the wordcloud library to generate wordclouds from word-frequency dictionaries. 
* Version: 0.1.0

### Requirements ###

* [wordcloud](https://pypi.org/project/wordcloud/)
* [numpy](https://numpy.org/install/)
* [pillow](https://pypi.org/project/Pillow/)
* [matplotlib](https://pypi.org/project/matplotlib/)
* Python version: 3.6+

### Usage ###

* `python generate_wordcloud.py -h` to display help message.
* Usage: `python generate_wordcloud.py <words_in> <wordcloud_out> --font
  <path_to_font>`
* Example usage: `python generate_wordcloud.py words.json wordcloud.png --font
  /home/ubuntu/font/Roboto-Regular.ttf`
* The font can also be specified by setting the environment variable `FONT_PATH`.

### Author ###

liv.kuhn@gmail.com
