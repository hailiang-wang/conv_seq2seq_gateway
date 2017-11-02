#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2017 <> All Rights Reserved
#
#
# File: /Users/hain/ai/conv_seq2seq_gateway/scripts/data_processor.py
# Author: Hai Liang Wang
# Date: 2017-11-02:17:05:31
#
#===============================================================================

"""
   
"""
from __future__ import print_function
from __future__ import division

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-11-02:17:05:31"


import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding("utf-8")
    # raise "Must be using Python 3"

import unittest
import json

# run testcase: python /Users/hain/ai/conv_seq2seq_gateway/scripts/data_processor.py Test.testExample
class Test(unittest.TestCase):
    '''
    
    '''
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_json_demo_data(self):
        from_ = os.path.join(curdir, os.path.pardir, "data", "textsum-demo.csv")
        to_ = os.path.join(curdir, os.path.pardir, "data", "textsum-demo.json")
        result = dict()
        ct = 1
        with open(from_, "r") as fin:
            for x in fin.readlines():
                x = x.strip().split("\t")
                assert len(x) == 3, "x should contain 3 members."
                c = x[0]
                t_o = x[1]
                t_p = x[2]
                result[ct] = dict({
                    "content": c,
                    "predict": t_p,
                    "headline": t_o
                })
                ct += 1

        json_str = json.dumps(result, ensure_ascii=False)  
        with open(to_, "w") as fout:
            fout.write(json_str)

def test():
    unittest.main()

if __name__ == '__main__':
    test()
