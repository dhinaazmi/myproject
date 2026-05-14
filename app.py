from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
return """
<!DOCTYPE html>
<html>
<head>
<title>Cognix</title>
<style>
body {
font-family: Arial, sans-serif;
background: linear-gradient(to right, #141e30, #243b55);
color: white;
text-align: center;
padding: 50px;
}

.container {
max-width: 800px;
margin: auto;
background: rgba(255,255,255,0.1);
padding: 30px;
border-radius: 15px;
box-shadow: 0px 4px 10px rgba(0,0,0,0.4);
}

h1 {
font-size: 50px;
color: #00d4ff;
}

p {
font-size: 20px;
line-height: 1.6;
}

.btn {
display: inline-block;
margin-top: 20px;
padding: 12px 25px;
background: #00d4ff;
color: black;
text-decoration: none;
border-radius: 8px;
font-weight: bold;
}

.features {
margin-top: 40px;
text-align: left;
}

.feature-box {
background: rgba(255,255,255,0.1);
padding: 15px;
margin: 10px 0;
border-radius: 10px;
}
</style>
</head>

<body>
<div class="container">
<h1>Welcome to Cognix</h1>

<p>
Cognix is an innovative technology company focused on
building smart AI-powered solutions for the future.
</p>

<a href="#" class="btn">Get Started</a>

<div class="features">
<h2>Our Features</h2>

<div class="feature-box">
🚀 AI-Powered Solutions
</div>

<div class="feature-box">
🔒 Secure & Reliable Systems
</div>

<div class="feature-box">
🌐 Modern Web Technologies
</div>

<div class="feature-box">
📈 Scalable Business Tools
</div>
</div>
</div>
</body>
</html>
"""

if __name__ == "__main__":
port = int(os.environ.get("PORT", 8080))
app.run(host="0.0.0.0", port=port)
