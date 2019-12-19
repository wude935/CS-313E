# takes as input a positive integer n
# returns True if n is prime and False otherwise


def is_prime(n):
    if (n == 1):
        return False
    limit = int(n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True

# returns the nearest prime number that is larger than n


def find_prime(n):
    if (n % 2 == 0):
        n += 1
    while (is_prime(n) == False):
        n += 2
    return n


# takes as input a string in lower case and the size
# of the hash table and returns the index the string
# will hash into
def hash_word(s, size):
    hash_idx = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx

# takes as input a string in lower case and the constant
# for double hashing and returns the step size for that
# string


def step_size(s, const):
    step = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        step = const - (step * 26 + letter) % const
    return step

# takes as input a string and a hash table and enters
# the string in the hash table, it resolves collisions
# by double hashing


def insert_word(s, hash_table):
    length = len(hash_table)
    hash_idx = hash_word(s, length)
    while hash_table[hash_idx] != '':
        hash_idx += step_size(s, 13)
        if hash_idx >= len(hash_table):
            hash_idx %= len(hash_table)
    hash_table[hash_idx] = s


# takes as input a string and a hash table and returns True
# if the string is in the hash table and False otherwise
def find_word(s, hash_table):
    hash_idx = 0
    length = len(hash_table)
    step = step_size(s, 13)
    # finds the key value
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % length
        initial_idx = hash_idx
    while hash_table[hash_idx] != s:
        hash_idx += step
        hash_idx %= len(hash_table)
    return True

# recursively finds if a word is reducible, if the word is
# reducible it enters it into the hash memo and returns True
# and False otherwise


def is_reducible(s, hash_table, hash_memo):
    # returns true if is s is a, o, or i
    if s == 'a' or s == 'o' or s == 'i':
        return True
    # checks to see if there is a a, o, or i in the word
    elif 'a' or 'o' or 'i' in s:
        # iterates through the word, removing one letter at a time
        if find_word(s, hash_memo):
            return True
        else:
            # iterates through the word, choosing a letter from s
            for i in range(len(s)):
                # creates a new string from s with the letter removed
                test = s[:i] + s[i+1:]
                # checks to see if test can be reduced
                if is_reducible(test, hash_table, hash_memo):
                    print(hash_memo)
                    # adds s to hash_memo because the word can be reduced
                    insert_word(s, hash_memo)
                    print(hash_memo)
                    return True
                else:
                    # if the word is not reducible
                    return False
    else:
        # if the word has no a, o, or , i
        return False


# goes through a list of words and returns a list of words
# that have the maximum length
# def get_longest_words (string_list):
def main():
    # create an empty word_list
    word_list = []
    # open the file words.txt
    file_name = 'words.txt'
    with open(file_name, 'r') as file:
        # read words from words.txt and append to word_list
        word_list = file.read().splitlines()
    # close file words.txt
    file.close()
    # find length of word_list
    length = len(word_list)
    # determine prime number N that is greater than twice
    # the length of the word_list
    N = find_prime(length * 2)
    # create and empty hash_list
    hash_list = []
    # populate the hash_list with N blank strings
    hash_list = ['' for i in range(N)]
    # hash each word in word_list into hash_list
    # for collisions use double hashing
    for word in word_list:
        insert_word(word, hash_list)
    # create an empty hash_memo
    hash_memo = []
    # populate the hash_memo with M blank strings
    M = find_prime(27000)
    hash_memo = ['' for i in range(M)]
    # create and empty list reducible_words
    reducible_words = []
    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    is_reducible('pay', hash_list, hash_memo)
    # find words of the maximum length in reducible_words

    # print the words of maximum length in alphabetical order
    # one word per line


# This line above main is for grading purposes. It will not
# affect how your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
