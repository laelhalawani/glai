import os
import re




def split_by_letters(text, max_letters=1):
    # split text into separate characters
    chars = list(text)
    # split into batches of max_chars_per_batch
    batches = ["".join(chars[i:i + max_letters]) for i in range(0, len(chars), max_letters)]
    return batches

def split_by_words(text, max_words=1):
    # split text into separate words
    words = text.split(" ")
    # split into batches of max_words_per_batch
    batches = [" ".join(words[i:i + max_words]) for i in range(0, len(words), max_words)]
    return batches

def split_by_lines(text):
    # split text into separate lines
    lines = text.split("\n")
    return lines

def split_by_double_lines(text):
    # split text into separate double lines
    double_lines = text.split("\n\n")
    return double_lines

def split_by_sentences(text):
    # split text into separate sentences
    sentences = text.split(".")
    return sentences


def batch_input_simple(input_text: str, _is_within_context_len: callable) -> list:
    if _is_within_context_len(input_text):
        return [input_text]
    else:
        print("Warning! Text was too long. Batching!")
        #split text
        split_text = split_by_words(input_text)
        #build sentences
        batched_input = []
        current_words_group = []
        for word in split_text:
            proposed_chunk = " ".join(current_words_group) + " " + word
            if _is_within_context_len(proposed_chunk):
                current_words_group.append(word)
            else:
                batched_input.append(current_words_group)
                current_words_group = [word]
        if len(current_words_group) > 0:
            batched_input.append(current_words_group)
        batched = [" ".join(batch) for batch in batched_input]
        print(f"Bached into {len(batched)} batches.")
        return batched

def remove_non_letters(string):
    print(string)
    pattern = r'[^a-zA-Z\s]'
    string =  re.sub(pattern, '', string)
    pattern = r'\s+'
    string = re.sub(pattern, ' ', string)
    string = string.strip()
    return string

def remove_list_formatting(string):
    pattern = r'\n[0-9]+\. '
    string = re.sub(pattern, '', string)
    pattern = r'\n[0-9]+\) '
    string = re.sub(pattern, '', string)
    pattern = r'\s[0-9]+\. '
    string = re.sub(pattern, '', string)
    pattern = r'\s[0-9]+\) '
    string = re.sub(pattern, '', string)
    pattern = r'\s{2,}'
    string = re.sub(pattern, ' ', string)
    string = string.strip()
    return string

