# Assignment-7, Cognitive Computing UCS420
# NLP Lab-I
# Nilabh Kishore Gupta

# Install once if needed: pip install nltk textblob matplotlib

import re
import string
from collections import Counter

import nltk
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, RegexpStemmer, WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.util import ngrams
from textblob import TextBlob


# NLTK needs these data files in addition to the Python package.
for package in ("punkt_tab", "stopwords", "wordnet", "omw-1.4",
                "averaged_perceptron_tagger_eng"):
    nltk.download(package, quiet=True)


# Q1. Basic text operations
text = """Natural Language Processing is an important area of Artificial Intelligence.
It enables computers to process and understand human language.
NLP is used in chatbots, search engines and recommendation systems."""

print("Q1. Basic text")
print(text)
print("characters:", len(text))
print("lowercase:", text.lower())
words = text.split()
print("words:", words)
print("word count:", len(words))


# Q2. Regular expressions: find a word, extract numbers and clean text
print("\nQ2. Regular expressions")
sentence = "CognitiveComputing: A computer science subject for geeks"
match = re.search("subject", sentence)
print("subject starts at", match.start(), "and ends at", match.end())

contact = "My number is 987654321 and my friend's number is 123456789"
print("numbers:", re.findall(r"\d+", contact))
print("split at spaces:", re.split(r"\s+", "NLP is useful"))
print("replace digits:", re.sub(r"\d", "X", contact))


# Q3. Word and sentence tokenization
print("\nQ3. Tokenization")
sample = "NLP is interesting. It helps computers process language."
print("split():", sample.split())
print("word_tokenize():", word_tokenize(sample))
print("sent_tokenize():", sent_tokenize(sample))
# split() keeps punctuation with the word; word_tokenize() separates it.


# Q4. Lowercasing, punctuation and stopwords
print("\nQ4. Text cleaning")
sample = "This is a simple example to demonstrate the removal of stopwords in NLP."
cleaned = sample.lower().translate(str.maketrans("", "", string.punctuation))
tokens = word_tokenize(cleaned)
stop_words = set(stopwords.words("english"))
stop_words.add("example")
stop_words.discard("not")  # useful to keep negation for tasks like sentiment analysis
filtered = [word for word in tokens if word not in stop_words]
print("lowercase and punctuation removed:", cleaned)
print("after stopword removal:", filtered)


# Q5. Stemming using a regex rule and Porter stemmer
print("\nQ5. Stemming")
stem_words = ["running", "flies", "studies", "played", "jumps"]
regex_stemmer = RegexpStemmer(r"ing$|ed$|es$")
porter = PorterStemmer()
for word in stem_words:
    print(word, "-> regex:", regex_stemmer.stem(word),
          "porter:", porter.stem(word))


# Q6. Lemmatization (POS helps with words like 'better' and 'running')
print("\nQ6. Lemmatization")
lemmatizer = WordNetLemmatizer()
for word, part in [("rocks", "n"), ("geese", "n"),
                   ("better", "a"), ("running", "v")]:
    print(word, "->", lemmatizer.lemmatize(word, pos=part))


# Q7. Part-of-speech tagging
print("\nQ7. POS tagging")
sentence = "The intelligent student solved the difficult problem."
for word, tag in pos_tag(word_tokenize(sentence)):
    print(word, tag)


# Q8. Tokens, types, word frequency and Zipf's law
print("\nQ8. Word frequency")
paragraph = """NLP studies language. Language appears in books and messages.
NLP helps us process language. We can count words in language and compare them."""
word_list = re.findall(r"[a-z]+", paragraph.lower())
counts = Counter(word_list)
print("tokens:", len(word_list))
print("types:", len(counts))
print("word frequencies:", counts.most_common())
print("rank, word, frequency, rank x frequency:")
for rank, (word, frequency) in enumerate(counts.most_common(), start=1):
    print(rank, word, frequency, rank * frequency)
# Zipf's law says frequent words tend to appear roughly in inverse rank order.
# This paragraph is too small for the numbers to fit the law closely.


# Q9. Singular/plural forms and translation with TextBlob
print("\nQ9. TextBlob")
print("children ->", TextBlob("children").words[0].singularize())
print("city ->", TextBlob("city").words[0].pluralize())
spanish = TextBlob("Buenos dias")
try:
    print("Spanish to English:", spanish.translate(from_lang="es", to="en"))
except Exception as error:
    # Recent TextBlob versions do not include translate(); older ones need internet.
    print("translation unavailable:", type(error).__name__)


# Q10. N-grams
print("\nQ10. N-grams")
tokens = ["machine", "learning", "is", "very", "useful"]
print("unigrams:", list(ngrams(tokens, 1)))
print("bigrams:", list(ngrams(tokens, 2)))
print("trigrams:", list(ngrams(tokens, 3)))
