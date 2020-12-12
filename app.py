from flask import Flask,redirect,url_for,render_template,request
from pytube import YouTube 
import requests as req

# Github @hammerinformation
app=Flask(__name__)

def download_video(url):
    YouTube(url).streams.filter(file_extension='mp4',progressive=True).first().download()

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')


@app.route("/download",methods=["GET","POST"])
def download():
    if request.method=="POST":
        url=request.form.get("url");
        if(url) and req.get(url).status_code==200 :
                download_video(url)
                return render_template("completed.html",
                title=YouTube(url).title,views=YouTube(url).views
                ,description=YouTube(url).description)

        else:
            return render_template("error.html")
        
        return render_template("error.html")

        
         
        
    else:
        return render_template("error.html")



if __name__ == '__main__':
    
    app.run(port=5000,debug=True)