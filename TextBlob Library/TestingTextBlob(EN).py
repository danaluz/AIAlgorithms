from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
train = [
('I love this sandwich.', 'pos'),
('This is an amazing place!', 'pos'),
('I feel very good about these beers.', 'pos'),
('I do not like this restaurant', 'neg'),
('I am tired of this stuff.', 'neg'),
("I can't deal with this", 'neg'),
("My boss is horrible.", "neg")]
cl = NaiveBayesClassifier(train)
cl.classify("I feel amazing!")

blob = TextBlob("I don't like Lise. But her sister is very nice.", classifier=cl)

for s in blob.sentences:
    print(s)
    print(s.classify())
