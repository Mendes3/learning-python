from collections import Counter

text = "Python is an interpreted high-level general-purpose programming language. " \
       "Python's design philosophy emphasizes code readability with its notable use of s" \
       "ignificant indentation. Its language constructs as well as its object-oriented " \
       "approach aim to help programmers write clear, logical code for " \
       "small and large-scale projects."
# first we need to make a list
words = text.split()
print(words)
counter = Counter(words)
print(counter)
most_frequent = counter.most_common(3)
print(most_frequent)



