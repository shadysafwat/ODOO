# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Motorcycle(models.Model):
    _name = 'motorcycle'

    name = fields.Char('Name')
    licence_expire_date = fields.Date('Licence Expire Date')
    motorcycle_mileage_ids = fields.One2many('motorcycle.mileage', 'motorcycle_id')
    remaining_days_for_expire = fields.Integer(compute='remaining_days_for_expire_function')
    assigned_to = fields.Many2one('res.users', string='Assigned To')

    @api.multi
    def remaining_days_for_expire_function(self):
        # calculate remaining days for motorcycle expiration date
        for rec in self:
            today = fields.Date.from_string(fields.Date.today())
            expire_date = fields.Date.from_string(rec.licence_expire_date)
            rec.remaining_days_for_expire = (expire_date - today).days
