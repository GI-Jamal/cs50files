from cs50 import get_string
import re
import string


def main():
    text = get_string("Text: ")
    letter_count = count_letters(text)
    word_count = count_words(text)
    sentence_count = count_sentences(text)
    grade = calculate_grade(letter_count, word_count, sentence_count)
    if grade < 1:
        print("Before Grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")


def count_letters(text):
    new_text = text.translate(str.maketrans('', '', string.punctuation))
    words = re.split(r'\s', new_text)
    letter_count = 0
    for word in words:
        letter_count = letter_count + len(word)
    return letter_count


def count_words(text):
    words = re.split(r'\s', text)
    word_count = len(words)
    return word_count


def count_sentences(text):
    sentences = re.split(r'\.|\?|\!', text)
    sentence_count = len(sentences)
    return sentence_count - 1


def calculate_grade(letter_count, word_count, sentence_count):
    L = (letter_count / word_count) * 100
    S = (sentence_count / word_count) * 100
    grade = 0.0588 * L - 0.296 * S - 15.8
    return round(grade)


main()