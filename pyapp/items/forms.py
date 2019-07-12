from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, DecimalField, FileField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange


class ItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired(message='Please enter a proper decimal number'), NumberRange(min=1, message='The price should be atleast 1')])
    image = FileField('Add Image (Leave blank to use default image)', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add')


class ItemUpdateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired(message='Please enter a proper decimal number'), NumberRange(min=1, message='The price should be atleast 1')])
    image = FileField('Add Image (Leave blank to keep current image)', validators=[FileAllowed(['jpg', 'png'])])
    percentage_off = IntegerField('Percentage Off', validators=[NumberRange(min=0, max=99, message='Enter a number between 0 and 99')], default=0)
    submit = SubmitField('Update')


class SearchForm(FlaskForm):
    query = StringField('Query', render_kw={"placeholder": "Search"})
    submit = SubmitField('Search')
    sort = SelectField(u'Order By', choices=[('name-az', 'Name(A-Z)'), ('name-za', 'Name(Z-A)'), ('price-lh', 'Price(Low to High)'), ('price-hl', 'Price(High to Low)'), ('sale', 'Biggest Sale')])
    clear = SubmitField('Clear Search')
