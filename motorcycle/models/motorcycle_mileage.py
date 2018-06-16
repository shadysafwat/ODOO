# -*- coding: utf-8 -*-

from odoo import fields, models


class MotorcycleMileage(models.Model):
    _name = 'motorcycle.mileage'

    name = fields.Float('Mileage')
    date = fields.Datetime('Date')
    motorcycle_id = fields.Many2one('motorcycle')
