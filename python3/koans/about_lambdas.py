#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based slightly on the lambdas section of AboutBlocks in the Ruby Koans
#

from runner.koan import *

class AboutLambdas(Koan):
    def test_lambdas_can_be_assigned_to_variables_and_called_explicitly(self):
        add_one = lambda n: n + 1
        self.assertEqual(11, add_one(10))

    # ------------------------------------------------------------------

    """
    so we're creating fn make_order which requires str arg order 
    the lambda fn itself also requires an int arg qty (see above for add_one)
    so we then create a variable assignment for the lambda, ex make_order('sausage')
    when we then call that variable we pass the qty arg to it to complete the lambda
    """

    def make_order(self, order):
        return lambda qty: str(qty) + " " + order + "s"

    def test_accessing_lambda_via_assignment(self):
        sausages = self.make_order('sausage')
        eggs = self.make_order('egg')

        self.assertEqual('3 sausages', sausages(3))
        self.assertEqual('2 eggs', eggs(2))
        self.assertEqual('4 bacons', self.make_order('bacon')(4))

    def test_accessing_lambda_without_assignment(self): #lol! figured it out before looking here
        self.assertEqual('39823 spams', self.make_order('spam')(39823)) 
