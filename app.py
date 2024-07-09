from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  
  return render_template('arcademy.html')

@app.route('/dashboard')
def dashboard():
  return render_template('index.html')

@app.route('/iot/run_program')  # Specific route for IoT program
def run_iot_program():
  # Code to execute your main.py program (explained later)
  import main  # Assuming main.py is your program file
  main.run_program()  # Assuming you have a run_program function
  return render_template('iot.html', message="IoT program executed!")  # Optional feedback

@app.route('/music/run_program')  # New route for Music section
def run_music_program():
  import Air_Drums  # Assuming Air_Drums.py is your program file
  Air_Drums.run_program()  # Assuming you have a run_program function
  return render_template('music.html', message="Air Drums program executed!")

if __name__ == '__main__':
  app.run(debug=True)

