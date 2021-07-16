from flask import Flask ,render_template , request
from flask_uploads import UploadSet, configure_uploads, IMAGES
#from flask_cors import CORS, cross_origin
from Models.runapp import predict


import _pickle as cPickle
from numpy import loadtxt
from keras.models import load_model

with open('Models\lr1.pkl', 'rb') as fid:
      lr = cPickle.load(fid)
with open('Models\sgd1.pkl', 'rb') as fid:
      sgd = cPickle.load(fid)


app = Flask(__name__)
#cors = CORS(app,resources={r"/upload/*": {"origins":"*"}})
#app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def my_form():
    return "NULL-Navigate"

@app.route('/home',methods=['GET','POST'])
def home():
    welcome = "Hey People!"
    return welcome

@app.route('/upload',methods=['GET','POST'])
#@cross_origin()
def upload():
    
    if request.method == "POST":
        curr_text = request.form['source']
        curr_text = curr_text.lower()

        prediction = predict(curr_text,lr,sgd)
        if(prediction["prediction"]=="bad"):
            answer = "There's a high chance that the text is abusive"
        else:
            answer = "The Text Seems fine:)"
        
        return answer

    return render_template('upload.html')


if __name__ == "__main__":
    app.run(port=5000,debug=True)