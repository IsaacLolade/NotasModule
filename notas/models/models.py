# -*- coding: utf-8 -*-

from odoo import models, fields, api


class notas(models.Model):
     _name = 'notas.notas'
     _description = 'notas.notas'

     tema = fields.Char()
     categoria = fields.Char()
     etiqueta = fields.Char()
     description = fields.Text()

