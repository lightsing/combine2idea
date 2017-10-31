import random

from config import *

def get():
    return "%s%s%s%s%s%s" %
     (random.choice(leverage_word_list),
      random.choice(leverage_list),
      random.choice(create_word_list),
      random.choice(idea_prefix_list),
      random.choice(idea_list),
      random.choice(idea_type))
