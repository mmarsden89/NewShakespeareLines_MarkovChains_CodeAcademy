"""
This is the launcher to run the New Shakespeare Sonnet Generator
"""

from fetchshakespeare import fetch_data
from markov_python.cc_markov import MarkovChain
import textwrap

#creates and adds the randomly generated data to the string
def get_words():
	mc.add_string(fetch_data())

#generator 
mc = MarkovChain()
get_words()
poem_length = 100
output = mc.generate_text(poem_length)
output = " ".join(output)
print((textwrap.fill(output,width=35).capitalize()))