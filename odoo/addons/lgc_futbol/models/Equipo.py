# -*- coding: utf-8 -*-
from odoo import models, fields

class Equipo(models.Model):
    _name = 'lgc_futbol.equipo'
    _description = 'Equipo de fútbol'

    name = fields.Char(string='Nombre', required=True)
    fundacion = fields.Date('Fecha de fundación')
    estadio = fields.Char('Estadio')
    ciudad = fields.Char('Ciudad')
    liga_id = fields.Many2one('lgc_futbol.liga', string='Liga')