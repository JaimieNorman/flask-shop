from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, DecimalField, FileField, IntegerField, SelectField, BooleanField
from wtforms.validators import DataRequired, NumberRange


class PatientForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    marital_state = StringField('Marital Status', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=1, message="Please enter a valid age")])
    gender = StringField('Gender', validators=[DataRequired()])
    race = StringField('Race', validators=[DataRequired()])
    nationality = StringField('Nationality', validators=[DataRequired()])
    blood_group = StringField('Blood Group', validators=[DataRequired()])
    organ_donor = BooleanField('Organ Donor', validators=[DataRequired()])
    disabilities = StringField('Disabilities', validators=[DataRequired()])
    occupation = StringField('Occupation', validators=[DataRequired()])
    house_number = StringField('House Number', validators=[DataRequired()])
    street_address = StringField('Street Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    province = StringField('Province', validators=[DataRequired()])
    zip_code = IntegerField('Zip Code', validators=[DataRequired()])
    submit = SubmitField('Add')
