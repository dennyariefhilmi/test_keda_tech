from odoo import fields, models, api
from odoo.exceptions import ValidationError

class TestMaterial(models.Model):
    _name = 'test.material'
    _description = ''

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)

    type = fields.Selection(string='Type',
                            selection=[('fabric', 'Fabric'),
                                       ('jeans', 'Jeans'),
                                       ('cotton', 'Cotton')],
                            required=True)
    buy_price = fields.Integer(string='Buy Price',
                               required=True)

    @api.constrains('buy_price')
    def checkprice(self):
        for rec in self:
            if rec.buy_price < 100:
                raise ValidationError("Input cannot be less than 100!")
            else:
                return rec

    supplier = fields.Many2one(
        comodel_name='test.supplier',
        string='Supplier',
        required=True)

class TestSupplier(models.Model):
    _name = 'test.supplier'
    _description = 'Supplier'

    name = fields.Char(string="Name", required=True)
    address = fields.Text(string="Address",
                          required=False)
    phone = fields.Integer(string='Phone',
                           required=False)



