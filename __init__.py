#This file is part account_invoice_jreport module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool
from .account_invoice import *

def register():
    Pool.register(
        Invoice,
        module='account_invoice_jreport', type_='model')
    Pool.register(
        InvoiceReport,
        module='account_invoice_jreport', type_='report')
