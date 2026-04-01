from flask import Flask
application = Flask(  name  )



@application.route('/') def hello_world():
  return "<h1>CI/CD Pipeline is Live!</h1><p>Version 1.0: Initial Deployment.</p>"



if  name	== ' main ': 
  application.run(debug=True)
