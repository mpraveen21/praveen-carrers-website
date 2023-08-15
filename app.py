from flask import Flask ,render_template ,jsonify

app = Flask(__name__)
JOBS = [
  {"Id":1,
  "Title":"Promt Engineer",
  "Location":"Bangalore",
   "Salary":"1,00,000"
   
  },
  {"Id":2,
  "Title":"Frontend Engineer",
  "Location":"Chennai",
   "Salary":"2,00,000"
   
  },
  {"Id":3,
  "Title":"Backend Engineer",
  "Location":"bangalore",
   "Salary":"3,00,000"
   
  },
  {"Id":4,
  "Title":"Machine Learning   Engineer",
  "Location":"bangalore",
   "Salary":"4,00,000"
   
  },
  {"Id":5,
  "Title":"Data Analyst",
  "Location":"Chennai",
   "Salary":"5,00,000"
   
  }
]



@app.route("/")
def helloworld():
    return render_template("home.html",jobs = JOBS)


@app.route("/job_info")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)