# Check the number of vowels in a given sentence
# and calculate its score, which is accounted by
# 1 for odd number of vowels and 2 for even number
# of vowels


def is_vowel(letters):

    vowels = ['a', 'e', 'i', 'o', 'u', 'y']     # list of vowels

    return [letter for letter in letters if letter in vowels]


def score_words(word):

    score = 0

    for word in words:
        num_vowels = len(is_vowel(word))

        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1

    return score


words = input().split()
print(words)
print(score_words(words))
