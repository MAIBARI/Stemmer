# -*- coding: utf-8 -*-
"""
Created on Mon May 29 12:48:57 2023

@author: Bari
"""

#from hausastemmer.HausaStemmer import HausaStemmer

from HausaStemmer1 import HausaStemmer1 




__stemmer = HausaStemmer1()


def stem(term, lookup=True):
    # type: (str, bool) -> str
    """Stem Hausa language term (word).
    :param term: term (word) to stem
    :param lookup: whether to use lookup dictionary for stemming
    :return: stemmed term, or original term if the term can't be stemmed
    :rtype: str
    """

    term_stem = __stemmer.stem(p=term, lookup=lookup)

    return term_stem


for term in 'Kare kazanta kunne mummunan sabuwar'.split():
    
    print('%s => %s' % (term, stem(term)))
