# 06/05/2017
'''
1.  Slim the enable1 dictionary so that it only contains "not-embedded" words;
    This is done through the not_embedded_wordlist function and takes forever (~2h) to run.
2.  Create an initial solution using a simple algorithm in the embed_word function.
    Current initial solution has length 390.
3.  ????
'''

import os.path
import time

def get_substrings(string, n):
    result = []
    for i in range(1+len(string)-n):
        result.append(string[i:i+n])
    return result

def is_embedded(string_a, string_b):
    '''Checks if string_a is embedded in string_b.
       [WIP] May or may not return the interval in which string_a is embedded in b.'''

    i = 0
    for j in range(0, len(string_b)):
        if string_a[i] == string_b[j]:
            #if i == 0:
            #    first_index = j
            i += 1
            if i == len(string_a):
                return True
                #return (first_index, j)
    return False

def not_embedded_wordlist(all_words):
    '''Slims down a dictionary so that only "un-embedded" words are present.'''

    print("Slimming down your dictionary...")
    print("Initial dictionary size: {} words".format(len(all_words)))

    all_words = sorted(all_words, key=len, reverse=True)
    not_embedded = []

    start = time.process_time()
    for sub_word in all_words:
        flag = False
        for word in not_embedded:
            if is_embedded(sub_word, word) != False:
                flag = True
                break
        if not flag:
            not_embedded.append(sub_word)
    elapsed = time.process_time() - start

    print("New dictionary size: {} words".format(len(not_embedded)))
    print("This took {} seconds.".format(elapsed))
    return not_embedded

def embed_word(word, solution):
    '''Returns a new solution so that word is now embedded.
       Explanation:
       LATER
    '''

    missing_f, missing_b = [], []

    for w, s, m in zip([word, word[::-1]],[solution, solution[::-1]], [missing_f, missing_b]):
        curr_index = 0
        for char in w:
            result = s.find(char, curr_index)
            if result == -1:
                m.append((char, curr_index))
            else:
                curr_index = result + 1

    condition = len(missing_f) < len(missing_b)
    missing = missing_f if condition else missing_b
    new_solution = list(solution) if condition else list(solution[::-1])

    already_included = 0
    for chars, pos in missing:
        new_solution.insert(pos+already_included, chars)
        already_included += 1

    return ''.join(new_solution) if condition else ''.join(new_solution[::-1])

def create_solution(wordlist):
    '''Creates a solution from the given wordlist.'''

    solution = ""
    for word in wordlist:
        if not is_embedded(word, solution):
            solution = embed_word(word, solution)

    return solution

def test_valid(solution, wordlist):
    '''Tests wheter or not every word in the wordlist is embedded in the solution.'''

    for word in wordlist:
        if not is_embedded(word, solution):
            return False
    return True

if __name__ == "__main__":
    if not os.path.isfile("not_embedded.txt"):
        with open(r"..\\..\\other\\enable1.txt", "r") as f:
            ENABLE_WORDS = [w.rstrip() for w in f.readlines()]
        NEW_WORDLIST = not_embedded_wordlist(ENABLE_WORDS)
        with open("not_embedded.txt", "a+") as f:
            f.write('\n'.join(NEW_WORDLIST))
    else:
        with open("not_embedded.txt", "r") as f:
            NEW_WORDLIST = [w.rstrip() for w in f.readlines()]

    INITIAL_SOLUTION = create_solution(NEW_WORDLIST)
    print("Initial solution's length: {}.".format(len(INITIAL_SOLUTION)))
    print("Passes tests: {}.".format(test_valid(INITIAL_SOLUTION, NEW_WORDLIST)))
