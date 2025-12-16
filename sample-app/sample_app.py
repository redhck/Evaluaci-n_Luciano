# Add to this file for the sample app lab
from flask import Flask
from flask import request
from flask import render_template
import sys 

sample = Flask(__name__)

@sample.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    
    
    port_to_run = 8080 
    
   
    if len(sys.argv) > 1:
        try:
            port_to_run = int(sys.argv[1])
        except ValueError:
            
            pass 
            
    
    sample.run(host="0.0.0.0", port=port_to_run, debug=True)
