from flask import Flask, render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)     
            return redirect('/thankyou.html')
        except:
            return 'Did not saved to database'
    else:
        return 'Someting went wrong..'


# This function will write the data in the txt file
def extract_response(dict1):
    index = __file__[:len(__file__)][::-1].index('\\')
    currentDirectoryPath=__file__[:len(__file__)-index]
    file1 = open(currentDirectoryPath+"Database.txt","a")
    counter=1
    for items in dict1:
        if counter==len(dict1):
            file1.writelines(dict1[items]+'\n')
            break
        else: 
            file1.writelines(dict1[items]+', ')
        counter=counter+1
        
    file1.close()

# This function will write the data in the csv file
def write_to_csv(dict):
    index = __file__[:len(__file__)][::-1].index('\\')
    currentDirectoryPath=__file__[:len(__file__)-index]
    with open(currentDirectoryPath+'database.csv',mode='a') as database2:
        email = dict['email']
        subject = dict['subject']
        message = dict['message']
        csv_writer = csv.writer(database2,delimiter=',',  quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])