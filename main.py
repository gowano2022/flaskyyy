from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from telegram import Bot

# Telegram bot setup
bot = Bot(token="6941631904:AAHfNlGSRsCLs23y6QMtFoq_p9o8p1gEW9w")

# Flask app
app = Flask(__name__)

# Form
class AttendanceForm(FlaskForm):
   name = StringField('Name')
   submit = SubmitField('Submit')
   
@app.route('/', methods=['GET', 'POST'])  
def index():

   form = AttendanceForm()
   
   if form.validate_on_submit():

      # Process form data   
      name = form.name.data
      
      # Send message to Telegram bot
      bot.send_message(chat_id="c3dspeed_bot", text=f"Name: {name}")
      
      return redirect('/')
      
   return render_template('index.html', form=form)
   
if __name__ == '__main__':
   app.run(debug=True)
