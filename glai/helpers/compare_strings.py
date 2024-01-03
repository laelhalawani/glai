import difflib


def compare_two_strings(compare_a:str, compare_b:str, case_sensitive=False):
    if not case_sensitive:
        compare_a = compare_a.lower()
        compare_b = compare_b.lower()
    sequence_matcher = difflib.SequenceMatcher(None, compare_a, compare_b)
    #print(sequence_matcher)
    return sequence_matcher.ratio()


def find_most_similar(query:str, find_in_iter:str, cutoff:float=0.5, case_sensitive=False):
    """
    Returns a list of tuples of the form (similarity, string)
    sorted by similarity
    """
    results = []
    if isinstance(find_in_iter, str):
        find_in_iter = [find_in_iter]
    oringinal_pos = 0
    for compare_b in find_in_iter:
        result = compare_two_strings(query, compare_b, case_sensitive)
        if result >= cutoff:
            results.append((result, compare_b, oringinal_pos))
        oringinal_pos += 1
    results.sort(key=lambda x: x[0], reverse=True)
    return results

def find_most_similar_squared(query:str, find_in_iter:str, cutoff:float=0.5, case_sensitive=False):
    """
    Returns a list of tuples of the form (similarity, string)
    sorted by similarity
    """
    results = []
    if isinstance(find_in_iter, str):
        find_in_iter = [find_in_iter]

    original_pos = 0
    for compare_b in find_in_iter:
        result = compare_two_strings(query, compare_b, case_sensitive)
        if result >= cutoff:
            results.append((result**2, compare_b, original_pos))
    results.sort(key=lambda x: x[0], reverse=True)
    return results

def compare_two_strings_squared(compare_a:str, compare_b:str, case_sensitive=False):
    if not case_sensitive:
        compare_a = compare_a.lower()
        compare_b = compare_b.lower()
    sequence_matcher = difflib.SequenceMatcher(None, compare_a, compare_b)
    #print(sequence_matcher)
    return sequence_matcher.ratio()**2
