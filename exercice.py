#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(Mot):
    number_of_letter = len(Mot)
    even = number_of_letter % 2 == 0
    return even


def remove_third_char(word):
    new_word = word[:2] + word[3:]
    return new_word

def replace_char(string: str, old_char: str, new_char: str) -> str:
    word_mot = string
    replace_mot = word_mot.replace(old_char, new_char)
    return replace_mot


def get_number_of_char(string: str, char: str) -> int:
    word = ""
    for mot in string:
        if char == mot:
            word += mot
    return len(word)


def get_number_of_words(sentence: str, word: str) -> int:
    new_sentence = sentence
    number_of_words = new_sentence.count(word)
    return number_of_words


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans {chaine} est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
