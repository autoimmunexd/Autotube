from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'none'

class LargeInputForm(FlaskForm):
    url_input_string = StringField('URL of Video, Playlist, or Channel')
    submit_button = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LargeInputForm()
    #if you click the button
    if form.validate_on_submit():
        print('clicked!')
        data = form.url_input_string.data
        print(data)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
