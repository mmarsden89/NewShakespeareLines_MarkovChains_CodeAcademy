### Code Academy - Final Project - Markov Chains/Web Scraper
### New Shakespeare Poem Generator

For my final project for Code Academy, using Markov Chains, I decided to create a poem generator that scrapes Sonnets 1-154 of William Shakespeare from literaturepage.com and generated them into a new poem.

*To run, clone this repository and run newshakespeare.py*


Codecademy Markov Chain text generator module. This is an implementation of a Markov Chain that generates random text based on content provided by the user. It is designed to be used as a local Python module for instructional purposes.

### How to add this to your project
Clone this repository into your Python project folder. Alternatively, you can download the zip archive and extract it into a directory in your project folder called markov_python.
You will need to import this file based on it's relative path. If your main runnable Python script is in the same directory as the markov_python directory, you can import this by including the following at the top of the runnable script: from markov_python.cc_markov import MarkovChain
How to use the Markov Chain text generator
After importing this module into your main project script, create an instance of MarkovChain and assign it to a variable. For example mc = MarkovChain()
Use one of the methods to read a local text file or a string. You can call this method multiple times to add additional data.
Call the generate_text() function on the instance of MarkovChain you created to generate text from the Markov Chain. You can call this method multiple times to generate additional data. This function will output a list of words. If your project requires a different format, you should convert the output accordingly.
### License
Read about in the LICENSE file. This means it is free to use, copy, distribute, and modify, but you must disclose the original code and copyright under the same terms.
