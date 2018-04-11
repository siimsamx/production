# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api

class Proceso(models.Model):
		_name = 'siimsa_production.proceso'
	 
		name = fields.Char('Pieza')
		num_dib = fields.Char('Número de dibujo')
		ope_pro = fields.Char('Operador')
		fec_cap = fields.Datetime('Fecha')
		lis_act = fields.Many2many('siimsa_production.plannin', 'Nuevo registro')
	
class Plannin(models.Model):
		_name = 'siimsa_production.actividad'
	
		num_opr = fields.Float('N° de operación')
		num_pza = fields.Float('N° de piezas')
		tpo_ser = fields.Selection([('Maquinado', 'Maquinado'), 
								('Fresado', 'Fresado'), 
								('Soldadura','Soldadura'),
								('Corte', 'Corte'), 
								('Rectificado', 'Rectificado'),
								('Medicion', 'Medición')], 'Tipo de servicio')
		tie_pla = fields.Float('Tiempo planeado')
		tie_rea = fields.Float('Tiempo real')
		dato = fields.Integer('Porcentaje')
		ids_maq = fields.Many2one('maintenance.equipment', 'Maquina')
	