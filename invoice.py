#This file is part account_invoice_jreport module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.modules.jasper_reports.jasper import JasperReport

__all__ = ['Invoice', 'InvoiceReport']


class InvoiceReport(JasperReport, metaclass=PoolMeta):
    __name__ = 'account.invoice'


class Invoice(metaclass=PoolMeta):
    __name__ = 'account.invoice'

    def print_invoice(self):
        '''
        When post invoice call print report and cache
        More fast post invoice without generate PDF report
        '''
        return
