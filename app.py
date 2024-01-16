from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'none'

class LargeInputForm(FlaskForm):
    select_field_quality = SelectField('Select Quality', choices=[
        ('best', 'Best'),
        ('320', '320'),
        ('192', '192'),
        ('128', '128')
    ])
    #MP4, M4A, MP3, OPUS, WAV
    select_field_format = SelectField('Select Format', choices=[
        ('mp3', 'mp3'),
        ('mp4', 'mp4'),
        ('w4a', 'm4a'),
        ('wave', 'wav'),
        ('opus','opus')
    ])
    url_input_string = StringField('URL of Video, Playlist, or Channel :')
    submit_button = SubmitField('Submit')
#best, 320, 192, 128

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LargeInputForm()
    #if you click the button
    if form.validate_on_submit():
        selected_quality = form.select_field_quality.data
        selected_format = form.select_field_format.data
        data = form.url_input_string.data.lower()
        #identify the input
        #match data:
        #    case ""
        
        #sanizize the url
        #cleaned = data.split('&')[0].strip().split('=')[1]

        try:
            command = f'youtube-dl --extract-audio --audio-format mp3 --audio-quality best {data}'
        except:
            print('Error')
        
        
        #youtube-dl --extract-audio --audio-format mp3 --audio-quality 320K <YouTube-Video-URL>
        #youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]' <YouTube-Video-URL>
        #differentiate between channel, playlist, or single video
        #https://www.youtube.com/watch?v=5mpqhtK0NuU&list=PLCg4BmjNch8hKt_6BzvThMe-njUhFEM02 VIDEO WITH LIST
        #https://www.youtube.com/watch?v=5mpqhtK0NuU VIDEO
        #https://www.youtube.com/@HDgreenstudio/featured CHANNEL HOME
        #https://www.youtube.com/@HDgreenstudio/videos CHANNEL VIDEOS
        #https://www.youtube.com/playlist?list=PLAJMBElONP_FLESzq42kIIxM2c8jg_beQ PLAYLIST
        

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
