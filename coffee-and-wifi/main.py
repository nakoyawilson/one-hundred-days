from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location_url = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    opening_time = StringField('Opening Time e.g. 8:00AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=[('☕️'), ('☕️☕️'), ('☕️☕️☕️'), ('☕️☕️☕☕️'), ('☕️☕️☕☕️☕️')], validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Strength Rating',  choices=[('✘'), ('💪️'), ('💪️💪️'), ('💪💪💪️'), ('💪️💪💪💪️'), ('💪️💪💪💪💪️')], validators=[DataRequired()])
    power_socket = SelectField('Power Socket Availability', choices=[('✘'), ('🔌️'), ('🔌️🔌️'), ('🔌🔌🔌'), ('🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌')], validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a') as csv_file:
            csv_file.write(f"\n{form.cafe.data},{form.location_url.data},{form.opening_time.data},{form.closing_time.data},{form.coffee_rating.data},{form.wifi_rating.data},{form.power_socket.data}")
            return redirect('/cafes')
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
