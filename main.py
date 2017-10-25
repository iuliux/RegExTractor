'''
RegExTractor
------------

Python regex extractor.

Takes 2 or more strings (or even a single one) and generates a RegEx that
matches similar strings.
The generated RegEx always matches the original strings, but it also
generalizes, usually matching more.

Iulius Curt, 2014
'''

from subseq_tree import gen_tree, tree_to_regex, tree_to_HTML


def extract(strs):
    ''' (The main function)
    Takes a list of strings and generates a RegEx that matches similar strings.
    '''
    tree = gen_tree(strs)
    # import pprint
    # pp = pprint.PrettyPrinter()
    # pp.pprint(tree)
    return tree_to_regex(tree)

def extract_HTML(strs):
    tree = gen_tree(strs)
    return tree_to_HTML(tree)


if __name__ == '__main__':
    s1 = 'abc$1250'
    s2 = 'xby#340'
    s3 = 'sbs@00000'
    print extract([s1, s2, s3])
    print

    s1 = 'skull'
    s2 = 'school'
    print extract([s1, s2])
    print

    s1 = '<div></div>'
    s2 = '<span></span>'
    print extract([s1, s2])
    print
