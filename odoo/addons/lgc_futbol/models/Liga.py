# -*- coding: utf-8 -*-
from odoo import models, fields

class Liga(models.Model):
    _name = 'lgc_futbol.liga'
    _description = 'Liga de fútbol'

    name = fields.Char('Nombre', required=True)
    fecha_inicio = fields.Date('Fecha de inicio')
    fecha_fin = fields.Date('Fecha de finalización')
    equipos = fields.One2many('lgc_futbol.equipo', 'liga_id', string='Equipos')
    