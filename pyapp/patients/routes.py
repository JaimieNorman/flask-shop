from flask import Blueprint, render_template, flash, url_for, request, redirect
from pyapp import db

from pyapp.models import Patient
from pyapp.patients.forms import PatientForm

patients = Blueprint('patients', __name__)


@patients.route('/patient/add', methods=['GET', 'POST'])
def add_patient():
    form = PatientForm()
    if form.validate_on_submit():
        patient = Patient(
            first_name=form.data.first_name,
            last_name=form.data.last_name,
            marital_state=form.data.marital_state,
            age=form.data.age,
            gender=form.data.gender,
            race=form.data.race,
            nationality=form.data.nationality,
            blood_group=form.data.blood_group,
            organ_donor=form.data.organ_donor,
            disabilities=form.data.disabilities,
            occupation=form.data.occupation,
            street_address=form.data.street_adress,
            house_number=form.data.house_number,
            city=form.data.city,
            province=form.data.province,
            zip_code=form.data.zip_code
        )
        db.session.add(patient)
        db.session.commit()
        flash('Patient Successfully Added!', 'success')
    return render_template('add_patient.html', form=form)
