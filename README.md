### New Shakespeare Poem Generator
### Markov Chains/Web Scraper

I decided to build a web scraper using Markov Chains to create a poem generator that scrapes Sonnets 1-154 of William Shakespeare from literaturepage.com and generate them into a new poem.

### Future Iterations

I would like to create a way to implement auto punctuation. As well I would like to implement a method of abstracting a certain amount of them at once and to properly title them.

### How to Run

*To run, clone this repository and run newshakespeare.py*


### How to add this to your project

Clone this repository into your Python project folder. Alternatively, you can download the zip archive and extract it into a directory in your project folder called markov_python.
You will need to import this file based on it's relative path. If your main runnable Python script is in the same directory as the markov_python directory, you can import this by including the following at the top of the runnable script: from markov_python.cc_markov import MarkovChain
How to use the Markov Chain text generator
After importing this module into your main project script, create an instance of MarkovChain and assign it to a variable. For example mc = MarkovChain()
Use one of the methods to read a local text file or a string. You can call this method multiple times to add additional data.
Call the generate_text() function on the instance of MarkovChain you created to generate text from the Markov Chain. You can call this method multiple times to generate additional data. This function will output a list of words. If your project requires a different format, you should convert the output accordingly.

### License

Read about in the LICENSE file. This means it is free to use, copy, distribute, and modify, but you must disclose the original code and copyright under the same terms.
