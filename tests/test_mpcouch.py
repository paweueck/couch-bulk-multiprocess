# -*- coding: utf-8 -*-

import unittest
import mpcouch


class mpcouchTest(unittest.TestCase):
    '''
    def test_pushData(self):
        myc = mpcouch.mpcouchPusher("http://127.0.0.1:5984/testdb",100)
        self.assertIsInstance(myc,mpcouch.mpcouchPusher)
        
        # for 1 through 100, all entries should be collected
        for i in range(1,100): self.assertEqual(myc.pushData({"id":i}),i)
        
        # the 101st should start an upload and reset the collection:
        self.assertEqual(myc.pushData({"id":101}),0)
        # this one counts form one onwards again:
        #self.assertEqual(myc.pushData({"id":102}),1)
        
        for i in range(102,152): self.assertEqual(myc.pushData({"id":i}),i-101)
        
        self.assertEqual(myc.finish(),50)
        
        self.assertEqual(myc.destroyDatabase(),None)
        del myc
        '''
    def test_pushDataBig(self):
        myc = mpcouch.mpcouchPusher("http://127.0.0.1:5984/testdb",30000)

        for i in range(0,5000000):
            myc.pushData({"id":i})
        myc.finish()
        del myc

unittest.main()
