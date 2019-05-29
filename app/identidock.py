
from flask import Flask
app = Flask(__name__)
default_name = 'JoeBloggs'

@app.route('/')
def get_identicon():
   name = default_name
   header = '<html><head><title>Identidock</title></head><body>'
   body = '''<form nethod = "POST">
             hello <input type="text" name="name" value="{}">
             <input type="submit" value="submiti">
             </form>
             <p>You Look a:
             <img src="/monster/monster.png"/>
             '''.format(name)
   footer = '</body></html>'

   return header + body + footer

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


