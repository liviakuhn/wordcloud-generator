# Wordcloud Generator #

### Summary ###

* This tool uses the wordcloud library to generate wordclouds from word-frequency dictionaries. 
* Version: 1.0.0

### Requirements ###

* [wordcloud](https://pypi.org/project/wordcloud/)
* [numpy](https://numpy.org/install/)
* [scipy](https://pypi.org/project/scipy/)
* [pillow](https://pypi.org/project/Pillow/)
* [matplotlib](https://pypi.org/project/matplotlib/)
* Python version: 3.6+

### Usage ###

* `python wordcloud_generator/__init__.py -h` to display help message.
* Usage: `python wordcloud_generator/__init__.py <words_in> <wordcloud_out> --image
  <path_to_image> --font <path_to_font> --display`
* Example usage: `python wordcloud_generator/__init__.py word_frequencies wordcloud.png --image
  bubble.jpeg --font fonts/Roboto-Regular.ttf --display`
* The image and font can also be specified by setting the environment variables
  `IMAGE_PATH` and `FONT_PATH`, respectively.

### Author ###

liv.kuhn@gmail.com
