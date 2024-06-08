from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired

class input(FlaskForm):
    sl = FloatField('Sepal Length in cm', validators=[DataRequired()])
    sw = FloatField('Sepal Width in cm', validators=[DataRequired()])
    pl = FloatField('Petal Length in cm', validators=[DataRequired()])
    pw = FloatField('Petal Width in cm', validators=[DataRequired()])
    sub = SubmitField('Predict')