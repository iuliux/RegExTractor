import numpy as np


def long_substr(strgs):
    """
    Returns a list with the longest common substring sequences from @strgs
    Based on: http://stackoverflow.com/questions/2892931/longest-common-substring-from-more-than-two-strings-python
    """
    # Copy the list
    strgs = strgs[:]
    if len(strgs) > 1 and len(strgs[0]) > 0:
        substrs = []
        substr = None
        maxlen = 1
        while True:
            if substr is not None and len(substr) >= maxlen:
                # A max lenght seq
                substrs.append(substr)
                maxlen = len(substr)
                for i, s in enumerate(strgs):
                    strgs[i] = s.replace(substr, '', 1)
            elif substr is not None and len(substr) < maxlen:
                # Not the first run and not longest seq also
                break

            substr = ''
            for i in range(len(strgs[0])):
                for j in range(len(strgs[0]) - i + 1):
                    if j > len(substr) and all(strgs[0][i:i+j] in x for x in strgs):
                        substr = strgs[0][i:i+j]
        return substrs
    elif len(strgs) == 1:
        return [strgs[0]] if len(strgs[0]) > 0 else []
    else:
        return []

def levenshtein(source, target):
    """ Computes the Levenshtein distance between 2 strings """
    if len(source) < len(target):
        return levenshtein(target, source)
    # So now we have len(source) >= len(target).
    if len(target) == 0:
        return len(source)
    # We call tuple() to force strings to be used as sequences
    # ('c', 'a', 't', 's') - numpy uses them as values by default.
    source = np.array(tuple(source))
    target = np.array(tuple(target))
    # We use a dynamic programming algorithm, but with the
    # added optimization that we only need the last two rows
    # of the matrix.
    previous_row = np.arange(target.size + 1)
    for s in source:
        # Insertion (target grows longer than source):
        current_row = previous_row + 1
        # Substitution or matching:
        # Target and source items are aligned, and either
        # are different (cost of 1), or are the same (cost of 0).
        current_row[1:] = np.minimum(current_row[1:],
                                     np.add(previous_row[:-1], target != s))
        # Deletion (target grows shorter than source):
        current_row[1:] = np.minimum(current_row[1:],
                                     current_row[0:-1] + 1)
        previous_row = current_row

    return previous_row[-1]


if __name__ == '__main__':
    s1 = 'Oh, hello, my friend...'
    s2 = 'I prefer Jelly Belly beans...'
    s3 = 'When hell freezes... over!'
    print(long_substr([s1, s2, s3]))
    print(long_substr(['0', 'a']))
    print(long_substr(['abba']))
    print(long_substr(['']))
    print(long_substr([]))
    print(levenshtein(s1, s2))
    print(levenshtein(s1, s3))
    print(levenshtein(s2, s3))
