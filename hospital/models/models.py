from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Record'

    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname', required=True)
    symptoms = fields.Text(string='Symptoms')
    
class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Record'

    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname', required=True)
    license_number = fields.Char(string='License Number', required=True)

class HospitalDiagnosis(models.Model):
    _name = 'hospital.diagnosis'
    _description = 'Diagnosis Record'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    diagnosis = fields.Text(string='Diagnosis', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date > fields.Date.today():
                raise ValidationError("Start date cannot be in the future.")
            if record.end_date < fields.Date.today():
                raise ValidationError("End date cannot be in the past.")    