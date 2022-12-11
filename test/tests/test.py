# -*- coding: utf-8 -*-

from odoo.tests import common


class TestModule(common.TransactionCase):

    def test_create_data(self):
        test_material = self.env['test.material'].create({
            'name': 'TestName',
            'code': 'TestCode',
            'type' : 'TestType',
            'buy_price' : 'TestPrice'
        })

        # Check if the project name and the task name match
        self.assertEqual(test_material.name, 'TestMaterial')
        self.assertEqual(test_material.name, 'TestName')
        self.assertEqual(test_material.code, 'TestCode')
        self.assertEqual(test_material.type, 'TestType')
        self.assertEqual(test_material.buy_price, 'TestPrice')
        print('Your test was succesfull!')