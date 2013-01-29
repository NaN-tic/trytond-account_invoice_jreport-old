#This file is part account_invoice_jreport module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.transaction import Transaction
from trytond.modules.jasper_reports.jasper import JasperReport

__all__ = ['Invoice', 'InvoiceReport']
__metaclass__ = PoolMeta


class Invoice:
    'Invoice'
    __name__ = 'account.invoice'

    @classmethod
    def __register__(cls, module_name):
        cursor = Transaction().cursor
        cursor.execute("UPDATE ir_action_report SET "\
                "report = 'account_invoice_jreport/invoice.jrxml', "\
                "extension = 'pdf' "\
                "WHERE report_name = 'account.invoice'")
        super(Invoice, cls).__register__(module_name)


class InvoiceReport(JasperReport):
    __name__ = 'account.invoice'
