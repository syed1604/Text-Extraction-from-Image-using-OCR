import os
from flask import Flask, render_template, request
from werkzeug import secure_filename
# import our OCR function
from ocr import ocr

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'C:\\Users\\Desktop\\flask\\static'

# route and function to handle the upload page
@app.route('/', methods=['GET', 'POST'])
def upload():  
    if request.method == 'POST':
        file = request.files['file']
        
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        path='C:\\Users\\Desktop\\flask\\static\\{}'.format(filename)
        src_image=path
        # call the OCR function on it
        extracted_text = ocr(path)
            # extract the text and display it
        return render_template('output.html',extracted_text=extracted_text,img_src=filename)
    elif request.method == 'GET':
        return render_template('output.html')


if __name__ == '__main__':
    app.run(debug=True)