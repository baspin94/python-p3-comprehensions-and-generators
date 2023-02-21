#!/usr/bin/env python3
#import ipdb

def return_evens(num_list):
    evens = [num for num in num_list if num % 2 == 0]
    return evens

def make_exclamation(sentence_list):
    exclamations = [sentence + "!" for sentence in sentence_list]
    return exclamations

sentences = ["Hello", "Wazzup", "Bananas"]

#ipdb.set_trace()
