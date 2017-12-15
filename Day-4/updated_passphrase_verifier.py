def main():
    with open('data/passlist.txt') as pass_list:
        print(count_valid_passphrases(pass_list))

def count_valid_passphrases(pass_list):
    count = 0
    for phrase in pass_list:
        if (phrase_is_valid(phrase)):
            count += 1
    return count

def phrase_is_valid(phrase):
    words_in_phrase = phrase.split(' ')
    for word in words_in_phrase:
        if (is_anagram_to_other_words(word.replace('\n',''), words_in_phrase)):
            return False
    return True

def is_anagram_to_other_words(word, list):
    anagram_count = 0
    for item in list:
        if (are_anagrams(word, item.replace('\n', ''))):
            anagram_count += 1
        if (anagram_count > 1):
            return True
    return False

def are_anagrams(first_word, second_word):
    first_sorted = ''.join(sorted(first_word))
    second_sorted = ''.join(sorted(second_word))
    return first_sorted == second_sorted
main()