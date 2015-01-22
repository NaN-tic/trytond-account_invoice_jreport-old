#!/usr/bin/env python
#This file is part account_invoice_jreport module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends


class AccountInvoiceJreportTestCase(unittest.TestCase):
    '''
    Test Account Invoice Jasper Report module.
    '''

    def setUp(self):
        trytond.tests.test_tryton.install_module('account_invoice_jreport')

    def test0006depends(self):
        '''
        Test depends.
        '''
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SurveyCase))
    return suite

