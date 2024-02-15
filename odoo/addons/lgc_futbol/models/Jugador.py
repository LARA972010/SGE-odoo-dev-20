# -*- coding: utf-8 -*-
from odoo import models, fields

class Jugador(models.Model):
    _name = 'lgc_futbol.jugador'
    _description = 'Jugador de fútbol'

    name = fields.Char('Nombre', required=True)
    edad = fields.Integer('Edad')
    posicion = fields.Char('Posición')
    equipo_id = fields.Many2one('lgc_futbol.equipo', string='Equipo')