from odoo import models, fields


class MaintenanceRequest(models.Model):
    _inherit = "maintenance.request"

    solar_plant = fields.Char(string="Solar Plant")
    solar_asset = fields.Char(string="Solar Asset")
    equipment_type = fields.Selection(
        [
            ("inverter", "Inverter"),
            ("module", "PV Module"),
            ("transformer", "Transformer"),
            ("tracker", "Tracker"),
            ("other", "Other"),
        ],
        string="Equipment Type",
    )
    energy_loss_kwh = fields.Float(string="Estimated Energy Loss (kWh)")
    scada_alarm = fields.Char(string="SCADA Alarm")