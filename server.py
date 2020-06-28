from flask import Flask, render_template, request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template("index.html")


@app.route('/<string:pageName>')
def dynamic(pageName):
    return render_template(pageName)

def cvsWrite(data):
	with open("Database.csv", mode="a",newline="") as Database2:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		cvsFile= csv.writer(Database2,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
		cvsFile.writerow( [email,subject,message])


def writeToFile(data):
	with open("Database.txt", mode="a") as Database:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		file= Database.write(f"\n {email},{subject},{message}")




@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == "POST":
		try:
			data=request.form.to_dict()
			cvsWrite(data)
			return redirect("./thankyou.html")
		except:
			return "did not save"
	else:
		return "faailed"  