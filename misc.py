#! /usr/bin/env python3

import os
import time
import errno
import re


class WithTimer:
    def __init__(self, title = '', quiet = False):
        self.title = title
        self.quiet = quiet
        
    def elapsed(self):
        return time.time() - self.wall, time.time() - self.proc

    def enter(self):
        '''Manually trigger enter'''
        self.__enter__()
    
    def __enter__(self):
        self.proc = time.time()
        self.wall = time.time()
        return self
        
    def __exit__(self, *args):
        if not self.quiet:
            titlestr = (' ' + self.title) if self.title else ''
            print('Elapsed%s: wall: %.06f, sys: %.06f' % ((titlestr,) + self.elapsed()))



def mkdir_p(path):
    # From https://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise



def combine_dicts(dicts_tuple):
    '''Combines multiple dictionaries into one by adding a prefix to keys'''
    ret = {}
    for prefix,dictionary in dicts_tuple:
        for key in list(dictionary.keys()):
            ret['%s%s' % (prefix, key)] = dictionary[key]
    return ret


def tsplit(string, no_empty_strings, *delimiters):
    # split string using multiple delimiters

    pattern = '|'.join(map(re.escape, delimiters))
    strings = re.split(pattern, string)
    if no_empty_strings:
        strings = [_f for _f in strings if _f]

    return strings
