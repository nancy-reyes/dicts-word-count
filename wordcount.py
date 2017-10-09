# put your code here.
import sys
import string

punctuation_list = list(string.punctuation)
filename = str(sys.argv[1])

print "This is the name of the script: ", sys.argv[0]
print "Number of arguments: ", len(sys.argv)
print "The arguments are: ", str(sys.argv)
print "sys.argv", sys.argv
# print "filename: ", filename
# print "input file: sys.argv[1] is:", sys.argv[1]
print "-----------------------------------"
"""
print "This is the name of the script: ", sys.argv[0]
print "Number of arguments: ", len(sys.argv)
print "The arguments are: " , str(sys.argv)

"""

def count_words(filename):
    """ Counts words in a text file. Returns results in a dictionary. """

    lines = open(str(filename))
    word_counts = {}

    for line in lines:
        words = line.split()
        for word in words:
            #word = word.lower()
            word_counts[word] = word_counts.get(word, 0) + 1
    lines.close()

    print word_counts["the"]
    return word_counts

print "this is the original"
# print count_words("twain.txt")
# print len(count_words("twain.txt"))
print len(count_words(filename))


def count_words2(filename):
    """ Counts words in a text file. Returns results in a dictionary. """

    lines = open(str(filename))
    word_counts = {}

    for line in lines:
        words = line.split()
        for word in words:
            word = word.lower()
            word = delete_punct(word)
            word_counts[word] = word_counts.get(word, 0) + 1
    lines.close()
    print word_counts["the"]

    return word_counts

def delete_punct(string):
  """Helper method: takes a string, returns it with only letters"""
  only_letters = []
  words = list(string)

  for char in words:
    if char not in punctuation_list:
        only_letters.append(char)
  new = "".join(only_letters)
  return new

# print count_words2("twain.txt")
#print count_words2("twain.txt")
print "this is the new word count (case insensitive, punctuation removed)"
print len(count_words2(filename))
# print count_words("twain.txt")

"""sort by value"""

def sort_by_value(D):
    for key, value in sorted(D.iteritems(), key = lambda (k,v): (v,k)):
        print "{} {} |".format(key, value),


print sort_by_value(count_words2(filename))
