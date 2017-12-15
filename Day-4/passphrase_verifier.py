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
        if (count_occurrences(word.replace('\n',''), words_in_phrase) > 1):
            return False
    return True

def count_occurrences(word, list):
    count = 0
    for item in list:
        if (word == item.replace('\n','')):
            count += 1
        if (count > 1):
            return count
    return count

main()