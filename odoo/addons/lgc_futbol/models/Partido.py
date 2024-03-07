# -*- coding: utf-8 -*-
from odoo import models, fields



class Partido(models.Model):
    _name = 'lgc_futbol.partido'
    _description = 'Partido de fútbol'

    equipo_local = fields.Many2one('lgc_futbol.equipo', string='Equipo Local', required=True)
    equipo_visitante = fields.Many2one('lgc_futbol.equipo', string='Equipo Visitante', required=True)
    fecha = fields.Datetime('Fecha del partido')
    resultado = fields.Char('Resultado')
    
    jugadores = fields.Many2many('lgc_futbol.jugador', string='Jugadores')

    