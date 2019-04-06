# -*- coding: utf-8 -*-

import unittest

class ParametrizedTestCase(unittest.TestCase):
    """TestCase classes that want to be parametrized should inherit from this class."""
    def __init__(self,methodName='runTest',param01=None,param02=None,param03=None,param04=None,param05=None):
        super(ParametrizedTestCase,self).__init__(methodName)
        self.param01 = param01
        self.param02 = param02
        self.param03 = param03
        self.param04 = param04
        self.param05 = param05
    @staticmethod
    def parametrize(testcase_klass,param01=None,param02=None,param03=None,param04=None,param05=None):
        """Creat a suite containing all tests taken from the given subclass,passing them the parameter 'param'"""
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name,param01=param01,param02=param02,param03=param03,param04=param04,param05=param05))
        return suite
