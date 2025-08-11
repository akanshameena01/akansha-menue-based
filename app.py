import streamlit as st
import streamlit.components.v1 as components

# Sidebar menu
section = st.sidebar.selectbox(
    "📂 Select Section",
    ["Introduction", "Docker", "JS", "Python"]
)

# Section: Introduction
if section == "Introduction":
    st.header("👋 Welcome to the Dashboard")
    st.write("✅ Tasks: Overview, Getting Started")

# Section: Docker
elif section == "Docker":
    st.header("🐳 Docker Tasks")
    st.write("✅ Docker Setup")
    st.write("✅ Containerization Examples")

# Section: JS
elif section == "JS":
    st.header("🧠 JavaScript Tasks")
    st.write("✅ Webcam Embed")
    st.write("✅ EmailJS Integration")

    # 📸 Webcam Embed
    components.html("""
      <h2>Take a Photo</h2>
      <video id="video" width="300" height="200" autoplay></video><br>
      <button onclick="startCamera()">🎥 Start Camera</button>
      <button onclick="capturePhoto()">📸 Capture Photo</button>
      <button onclick="stopCamera()">🛑 Stop Camera</button><br><br>
      <canvas id="canvas" width="300" height="200" style="display:none;"></canvas>
      <img id="photo" alt="Your photo will appear here" />
      <script>
        let stream;
        const video = document.getElementById('video');
        function startCamera() {
          navigator.mediaDevices.getUserMedia({ video: true })
            .then(s => {
              stream = s;
              video.srcObject = stream;
            })
            .catch(err => {
              alert("Camera access dena padega: " + err);
            });
        }
        function capturePhoto() {
          const canvas = document.getElementById('canvas');
          const context = canvas.getContext('2d');
          context.drawImage(video, 0, 0, canvas.width, canvas.height);
          const photo = document.getElementById('photo');
          photo.src = canvas.toDataURL('image/png');
        }
        function stopCamera() {
          if (stream) {
            stream.getTracks().forEach(track => track.stop());
            video.srcObject = null;
          }
        }
      </script>
    """, height=500)

    # 📧 EmailJS Contact Form
    components.html("""
      <h2>📧 Contact Form</h2>
      <script src="https://cdn.emailjs.com/dist/email.min.js"></script>
      <script>
        (function(){
          emailjs.init("V8Q5nHfSyddX4EyiV"); // ✅ Your public key
        })();
      </script>
      <form id="contact-form">
        <input type="text" name="from_name" placeholder="Your Name" required><br><br>
        <input type="email" name="reply_to" placeholder="Your Email" required><br><br>
        <textarea name="message" placeholder="Your Message" required></textarea><br><br>
        <input type="hidden" name="to_email" value="meenaakansha03@gmail.com">
        <button type="submit">Send Email</button>
      </form>
      <script>
        document.getElementById('contact-form').addEventListener('submit', function(e) {
          e.preventDefault();
          emailjs.sendForm('service_3r15eqm', 'template_r30zdqt', this)
            .then(() => {
              alert('✅ Email sent successfully!');
            }, (error) => {
              alert('❌ Failed to send email: ' + JSON.stringify(error));
            });
        });
      </script>
    """, height=500)

# Section: Python
elif section == "Python":
    st.header("🐍 Python Tasks")
    st.write("✅ EmailJS (Embedded)")
    st.write("✅ WhatsApp Automation via Twilio")

    # EmailJS Form (embedded in Python section too, if you want)
    components.html("""
      <h2>📧 Contact Form</h2>
      <script src="https://cdn.emailjs.com/dist/email.min.js"></script>
      <script>
        (function(){
          emailjs.init("V8Q5nHfSyddX4EyiV");
        })();
      </script>
      <form id="contact-form">
        <input type="text" name="from_name" placeholder="Your Name" required><br><br>
        <input type="email" name="reply_to" placeholder="Your Email" required><br><br>
        <textarea name="message" placeholder="Your Message" required></textarea><br><br>
        <input type="hidden" name="to_email" value="meenaakansha03@gmail.com">
        <button type="submit">Send Email</button>
      </form>
      <script>
        document.getElementById('contact-form').addEventListener('submit', function(e) {
          e.preventDefault();
          emailjs.sendForm('service_3r15eqm', 'template_r30zdqt', this)
            .then(() => {
              alert('✅ Email sent successfully!');
            }, (error) => {
              alert('❌ Failed to send email: ' + JSON.stringify(error));
            });
        });
      </script>
    """, height=500)

    # WhatsApp Automation
    st.subheader("📲 Send WhatsApp Message via Twilio")
    if st.button("Send WhatsApp Message"):
        from twilio.rest import Client
        account_sid = 'AC97a2222c7281470b5f6ca6b653d0b54e'
        auth_token = '5e2b1c4378a4149cc1a31f494636c8bf'
        from_whatsapp_number = 'whatsapp:+14155238886'
        to_whatsapp_number = 'whatsapp:+918949248097'

        try:
            client = Client(account_sid, auth_token)
            client.messages.create(
                body='👋 Hello Akansha! Your Python WhatsApp automation is working! ✅',
                from_=from_whatsapp_number,
                to=to_whatsapp_number
            )
            st.success("✅ WhatsApp message sent successfully!")
        except Exception as e:
            st.error(f"❌ Failed to send message: {e}")
#yha ab kuch change nhi krna sb working code h........................................................
import streamlit as st
from twilio.rest import Client

st.subheader("📩 Send SMS via Twilio")

# Input fields
from_number = st.text_input("From Number (Twilio)", "+14632087029")
to_number = st.text_input("To Number", "+918949248097")
sms_body = st.text_area("Message", "👋 Hello Akansha! Your SMS from Python via Twilio worked successfully! ✅")

if st.button("Send SMS"):
    account_sid = 'AC97a2222c7281470b5f6ca6b653d0b54e'
    auth_token = '5e2b1c4378a4149cc1a31f494636c8bf'

    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=sms_body,
            from_=from_number,
            to=to_number
        )
        st.success(f"✅ Message sent successfully! SID: {message.sid}")
    except Exception as e:
        st.error(f"❌ Failed to send SMS: {e}")
import streamlit as st
import streamlit.components.v1 as components

st.title("📍 Your Location")

html_code = """
<h2>📍 Your Location</h2>
<button onclick="getLocation()">Get My Location</button>
<p id="locationOutput"></p>

<script>
    function getLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
      } else {
        document.getElementById("locationOutput").innerHTML = "Geolocation is not supported by this browser.";
      }
    }

    function showPosition(position) {
      const latitude = position.coords.latitude;
      const longitude = position.coords.longitude;
      document.getElementById("locationOutput").innerHTML = 
        `Latitude: ${latitude} <br>Longitude: ${longitude}`;
    }

    function showError(error) {
      switch(error.code) {
        case error.PERMISSION_DENIED:
          document.getElementById("locationOutput").innerHTML = "User denied the request for Geolocation.";
          break;
        case error.POSITION_UNAVAILABLE:
          document.getElementById("locationOutput").innerHTML = "Location information is unavailable.";
          break;
        case error.TIMEOUT:
          document.getElementById("locationOutput").innerHTML = "The request to get user location timed out.";
          break;
        case error.UNKNOWN_ERROR:
          document.getElementById("locationOutput").innerHTML = "An unknown error occurred.";
          break;
      }
    }
</script>
"""

components.html(html_code, height=300)

# Show HTML in Streamlit
st.components.v1.html(html_code, height=500)
import streamlit as st

st.set_page_config(page_title="Find Nearby Grocery Stores", layout="centered")

html_code = """
<!DOCTYPE html>
<html>
<head>
  <title>Find Nearby Grocery Stores</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      padding-top: 50px;
    }
    button {
      padding: 15px 25px;
      font-size: 18px;
      cursor: pointer;
    }
  </style>
</head>
<body>

  <h2>🛒 Find Grocery Stores Near You</h2>
  <button onclick="findGroceryStores()">Show on Google Maps</button>

  <script>
    function findGroceryStores() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
          const lat = position.coords.latitude;
          const lng = position.coords.longitude;
          const query = `https://www.google.com/maps/search/grocery+stores/@${lat},${lng},15z`;
          window.open(query, '_blank');
        }, () => {
          alert("⚠️ Location access denied.");
        });
      } else {
        alert("❌ Your browser does not support geolocation.");
      }
    }
  </script>

</body>
</html>
"""

# Render HTML inside Streamlit
st.components.v1.html(html_code, height=300)
import streamlit as st
import os
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from bs4 import BeautifulSoup

# Gmail API scope
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Credentials file ka absolute path
CREDENTIALS_PATH = r"C:\Users\akansha\OneDrive\Desktop\TASK\11\gmailreader\credentials.json"

def get_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def fetch_last_email():
    service = get_service()
    results = service.users().messages().list(userId='me', maxResults=1).execute()
    messages = results.get('messages', [])

    if not messages:
        return None

    msg = service.users().messages().get(userId='me', id=messages[0]['id'], format='full').execute()
    payload = msg['payload']
    headers = payload['headers']

    subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
    sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown Sender')

    parts = payload.get('parts', [])
    message_body = ""
    if parts:
        body_data = parts[0]['body']['data']
        body = base64.urlsafe_b64decode(body_data).decode('utf-8')
        message_body = BeautifulSoup(body, "html.parser").get_text()

    return {"subject": subject, "sender": sender, "body": message_body}

# Streamlit UI
st.set_page_config(page_title="Last Gmail Reader", layout="centered")
st.title("📧 Last Received Gmail")

if st.button("Fetch Last Email"):
    email_data = fetch_last_email()
    if email_data:
        st.subheader("Subject:")
        st.write(email_data["subject"])

        st.subheader("From:")
        st.write(email_data["sender"])

        st.subheader("Message Body:")
        st.write(email_data["body"])
    else:
        st.warning("No emails found.")
        #instapost
import streamlit as st
from instagrapi import Client

st.header("Instagram Photo Upload")

if st.button("Upload Photo to Instagram"):
    cl = Client()
    try:
        cl.login('vibeee144', 'akansha01')
        image_path = r"C:\Users\akansha\OneDrive\Desktop\TASK\13\chromedriver-win64\my_post.jpeg"
        cl.photo_upload(image_path, "my post")
        st.success("✅ Photo uploaded successfully!")
    except Exception as e:
        st.error(f"❌ Upload failed: {e}")

#product
import streamlit as st
import streamlit.components.v1 as components

product_view_html = """
<h2>Select a product to view:</h2>
<select id="productSelector">
  <option value="prodA">Product A</option>
  <option value="prodB">Product B</option>
  <option value="prodC">Product C</option>
</select>

<h3>Currently Viewing: <span id="productId"></span></h3>
<p>Wait at least 5 seconds before closing the tab to track as viewed.</p>

<script>
  let productId = document.getElementById("productSelector").value;
  document.getElementById("productId").innerText = productId;

  document.getElementById("productSelector").addEventListener("change", (e) => {
    productId = e.target.value;
    document.getElementById("productId").innerText = productId;
  });

  const viewStart = Date.now();

  window.addEventListener("beforeunload", () => {
    const viewEnd = Date.now();
    const duration = Math.round((viewEnd - viewStart) / 1000); // seconds
    const skipped = duration < 5;

    const viewData = { productId, duration, skipped };

    let views = JSON.parse(localStorage.getItem("views") || "[]");
    views.push(viewData);
    localStorage.setItem("views", JSON.stringify(views));
  });
</script>
"""

recommended_html = """
<h2>📢 Recommended Product:</h2>
<p id="recommended">Loading...</p>

<h3>📊 View Stats:</h3>
<pre id="stats"></pre>

<button onclick="clearData()">🧹 Clear Data</button>

<script>
  const views = JSON.parse(localStorage.getItem("views") || "[]");

  const filtered = views.filter(v => !v.skipped);

  const stats = {};

  filtered.forEach(view => {
    if (!stats[view.productId]) {
      stats[view.productId] = { views: 0, totalTime: 0 };
    }
    stats[view.productId].views += 1;
    stats[view.productId].totalTime += view.duration;
  });

  let recommended = null;
  let maxViews = 0;

  for (let productId in stats) {
    if (stats[productId].views > maxViews) {
      recommended = productId;
      maxViews = stats[productId].views;
    }
  }

  document.getElementById("recommended").innerText = recommended || "No views yet";
  document.getElementById("stats").innerText = JSON.stringify(stats, null, 2);

  function clearData() {
    localStorage.removeItem("views");
    alert("Data cleared!");
    location.reload();
  }
</script>
"""

st.title("Product View and Recommendation Tracker")

tab1, tab2 = st.tabs(["Product View", "Recommended Product"])

with tab1:
    components.html(product_view_html, height=300)

with tab2:
    components.html(recommended_html, height=350)
import streamlit as st
import streamlit.components.v1 as components

html_code = """
<!DOCTYPE html>
<html>
<head>
  <title>Get IP and Location</title>
</head>
<body style="font-family: Arial, sans-serif;">
  <h2>🌐 Your IP and Location Info</h2>
  <p id="output" style="font-size: 18px; color: darkgreen;"></p>

  <script>
    async function getIPInfo() {
      const output = document.getElementById("output");
      output.innerText = "Fetching your IP and location...";

      try {
        const response = await fetch("https://ipapi.co/json/");
        const data = await response.json();

        const ip = data.ip;
        const city = data.city;
        const region = data.region;
        const country = data.country_name;

        output.innerText = `Your current IP address is ${ip} and your location is ${city}, ${region}, ${country}.`;
      } catch (err) {
        output.innerText = "❌ Could not fetch your location.";
        console.error(err);
      }
    }

    // Automatically call on page load
    window.onload = getIPInfo;
  </script>
</body>
</html>
"""

st.title("🌐 IP and Location Fetcher")

components.html(html_code, height=200)
#docker1
import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("📈 Simple Linear Regression Predictor")

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 6, 9, 12, 15])

model = LinearRegression()
model.fit(X, y)

user_input = st.number_input("Enter a number to predict its output:", min_value=0, step=1, value=6)
input_array = np.array([[user_input]])
prediction = model.predict(input_array)[0]

st.write(f"Prediction for input {user_input} is **{prediction:.2f}**")
#docker2
import streamlit as st

st.title("Hello from Streamlit inside Docker!")
st.write("Welcome to your Streamlit app.")
#docker3
import streamlit as st

def main():
    st.title("📋 Simple Menu")

    menu_option = st.selectbox(
        "Choose an option:",
        ("Select", "Greet", "Add Two Numbers", "Exit")
    )

    if menu_option == "Greet":
        name = st.text_input("What's your name?")
        if st.button("Say Hello"):
            if name.strip():
                st.success(f"Hello, {name}!")
            else:
                st.error("Please enter your name.")

    elif menu_option == "Add Two Numbers":
        a = st.number_input("Enter first number:", value=0)
        b = st.number_input("Enter second number:", value=0)
        if st.button("Calculate Sum"):
            st.success(f"The sum is: {a + b}")

    elif menu_option == "Exit":
        st.write("Thank you! You can close the app now.")

    else:
        st.write("Please select an option from the menu.")

if __name__ == "__main__":
    main()
#route 
import streamlit as st
import streamlit.components.v1 as components

st.title("🗺️ Route from Current Location to Destination")

GOOGLE_MAPS_API_KEY = "AIzaSyCxY2bm8jrZ8MkkQBHu0NuqSMypgVwpgVQ"  # Replace this!

destination = st.text_input("Enter your destination address:", "Central Park, New York, NY")

if destination:
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <style>
        #map {{
          height: 500px;
          width: 100%;
        }}
        html, body {{
          margin: 0;
          padding: 0;
          height: 100%;
        }}
      </style>
    </head>
    <body>
      <div id="map"></div>
      <script>
        let map;
        let directionsService;
        let directionsRenderer;

        function initMap() {{
          directionsService = new google.maps.DirectionsService();
          directionsRenderer = new google.maps.DirectionsRenderer();

          map = new google.maps.Map(document.getElementById('map'), {{
            zoom: 7,
            center: {{ lat: 40.7128, lng: -74.0060 }} // Default center NYC
          }});

          directionsRenderer.setMap(map);

          if (navigator.geolocation) {{
            navigator.geolocation.getCurrentPosition(
              (position) => {{
                const origin = {{
                  lat: position.coords.latitude,
                  lng: position.coords.longitude
                }};
                calculateRoute(origin);
              }},
              (error) => {{
                alert("Error getting location: " + error.message);
              }},
              {{
                enableHighAccuracy: true,
                timeout: 10000,
                maximumAge: 0
              }}
            );
          }} else {{
            alert("Geolocation is not supported by this browser.");
          }}
        }}

        function calculateRoute(origin) {{
          directionsService.route(
            {{
              origin: origin,
              destination: "{destination}",
              travelMode: google.maps.TravelMode.DRIVING
            }},
            (response, status) => {{
              if (status === 'OK') {{
                directionsRenderer.setDirections(response);
              }} else {{
                alert('Directions request failed due to ' + status);
              }}
            }}
          );
        }}
      </script>

      <script src="https://maps.googleapis.com/maps/api/js?key={GOOGLE_MAPS_API_KEY}&callback=initMap" async defer></script>
    </body>
    </html>
    """

    components.html(html, height=550)
else:
    st.info("Please enter a destination address above.")
    #apache
import streamlit as st

st.title("Apache Page inside Streamlit")

apache_url = "http://localhost:8080"

st.markdown(f'<iframe src="{apache_url}" width="700" height="400"></iframe>', unsafe_allow_html=True)

#python
import streamlit as st
import psutil

ram = psutil.virtual_memory()

st.write(f"Total RAM     : {ram.total / (1024 ** 3):.2f} GB")
st.write(f"Available RAM : {ram.available / (1024 ** 3):.2f} GB")
st.write(f"Used RAM      : {ram.used / (1024 ** 3):.2f} GB")
st.write(f"RAM Usage     : {ram.percent}%")
#2
import streamlit as st
from twilio.rest import Client

account_sid = 'AC97a2222c7281470b5f6ca6b653d0b54e'
auth_token = '5e2b1c4378a4149cc1a31f494636c8bf'

client = Client(account_sid, auth_token)

if st.button("Send WhatsApp Message"):
    st.write("Button clicked, sending message...")
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='Hello Akansha! 👋 This is a WhatsApp message sent using Python & Twilio. 🚀',
            to='whatsapp:+918949248097'
        )
        st.success(f"✅ Message sent! SID: {message.sid}")
    except Exception as e:
        st.error(f"❌ Failed to send message: {e}")
#3
import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

st.title("📧 Send Email via Gmail SMTP")

sender_email = "meenaakansha03@gmail.com"
app_password = "hbhr xyyz auvp jzxt"
receiver_email = st.text_input("Receiver Email", "meenaakansha03@gmail.com")
subject = st.text_input("Subject", "Test Email from Akansha's Python Script 🚀")
body = st.text_area("Body", "Hello! 😊\n\nThis is a test email sent using Python. It works!")

if st.button("Send Email"):
    try:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        st.success("✅ Email sent successfully!")
    except Exception as e:
        st.error(f"❌ Failed to send email: {e}")
#4
import streamlit as st
from twilio.rest import Client

st.title("📲 Send SMS using Twilio")

account_sid = 'AC97a2222c7281470b5f6ca6b653d0b54e'
auth_token = '5e2b1c4378a4149cc1a31f494636c8bf'

client = Client(account_sid, auth_token)

to_number = st.text_input("Receiver Mobile Number (+91...)", "+918949248097")
from_number = st.text_input("Twilio Phone Number (+1...)", "+14632087029")
message_body = st.text_area("Message", "Hey! This is a normal SMS sent using Python 📱")

if st.button("Send SMS", key="send_sms_unique"):
    try:
        message = client.messages.create(
            body=message_body,
            from_=from_number,
            to=to_number
        )
        st.success(f"✅ SMS sent! SID: {message.sid}")
    except Exception as e:
        st.error(f"❌ Failed to send SMS: {e}")
#5
import streamlit as st
from twilio.rest import Client

st.title("📱 Send WhatsApp Message with Twilio")

account_sid = 'AC97a2222c7281470b5f6ca6b653d0b54e'
auth_token = '5e2b1c4378a4149cc1a31f494636c8bf'
client = Client(account_sid, auth_token)

to_number = st.text_input("Receiver WhatsApp Number (with whatsapp:+ prefix)", "whatsapp:+918949248097")
from_number = "whatsapp:+14155238886"  # Twilio sandbox WhatsApp number
message_body = st.text_area("Message", "Hello! 👋 This is a WhatsApp message sent from Python.")

if st.button("Send WhatsApp Message", key="send_whatsapp_msg"):
    try:
        message = client.messages.create(
            from_=from_number,
            to=to_number,
            body=message_body
        )
        st.success(f"✅ WhatsApp message sent! SID: {message.sid}")
    except Exception as e:
        st.error(f"❌ Failed to send message: {e}")
#6
import streamlit as st
from twilio.rest import Client

st.title("📞 Make a Voice Call with Twilio")

# Twilio credentials (aap apne credentials yahan daalein)
account_sid = 'AC97a2222c7281470b5f6ca6b653d0b54e'
auth_token = '5e2b1c4378a4149cc1a31f494636c8bf'
client = Client(account_sid, auth_token)

to_number = st.text_input("Receiver Phone Number (with country code, e.g. +918949248097)", "+918949248097")
from_number = '+14632087029'  # Your Twilio number

if st.button("Initiate Call", key="call_button"):
    try:
        call = client.calls.create(
            twiml='<Response><Say>Hey Akansha! This is a test call from Python using Twilio. Have a great day!</Say></Response>',
            to=to_number,
            from_=from_number
        )
        st.success(f"📞 Call initiated! SID: {call.sid}")
    except Exception as e:
        st.error(f"❌ Failed to make call: {e}")
#7
import streamlit as st
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def post_tweet(email, password, tweet_text):
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 30)

    try:
        driver.get("https://twitter.com/i/flow/login")

        email_input = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "input")))
        email_input.send_keys(email)
        email_input.send_keys(u'\ue007')
        time.sleep(3)

        try:
            username_input = wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))
            if username_input.get_attribute("autocomplete") == "username":
                username_input.send_keys(email.split("@")[0])
                username_input.send_keys(u'\ue007')
                time.sleep(2)
        except:
            pass

        password_input = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
        password_input.send_keys(password)
        password_input.send_keys(u'\ue007')
        time.sleep(5)

        tweet_button_xpath = '//a[@href="/compose/tweet"]'
        wait.until(EC.element_to_be_clickable((By.XPATH, tweet_button_xpath))).click()
        time.sleep(3)

        tweet_box_xpath = '//div[@aria-label="Tweet text"]'
        tweet_box = wait.until(EC.visibility_of_element_located((By.XPATH, tweet_box_xpath)))
        tweet_box.send_keys(tweet_text)

        tweet_send_xpath = '//div[@data-testid="tweetButtonInline"]'
        wait.until(EC.element_to_be_clickable((By.XPATH, tweet_send_xpath))).click()

        time.sleep(5)
        return "✅ Tweet posted successfully!"
    except Exception as e:
        return f"❌ Error: {e}"
    finally:
        driver.quit()

# Streamlit UI
st.title("🐦 Twitter Auto Tweeter")

email = st.text_input("Enter your Twitter Email")
password = st.text_input("Enter your Twitter Password", type="password")
tweet_text = st.text_area("Write your Tweet here")

if st.button("Post Tweet"):
    if not email or not password or not tweet_text:
        st.error("Please fill in all fields!")
    else:
        st.info("Posting your tweet... Please wait.")
        result = post_tweet(email, password, tweet_text)
        st.success(result)
#8
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.travelandleisure.com/worlds-best'
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"Failed to retrieve page, status code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.content, 'html.parser')

# Find article containers
articles = soup.find_all('a', class_='comp card')

data = []
for article in articles:
    title = article.find('h2')
    category = article.find('div', class_='category')
    link = article.get('href')

    data.append({
        'Title': title.text.strip() if title else None,
        'Category': category.text.strip() if category else None,
        'Link': f"https://www.travelandleisure.com{link}" if link else None
    })

if data:
    df = pd.DataFrame(data)
    df.to_csv('travel_data.csv', index=False)
    print("✅ Travel data saved to travel_data.csv")
else:
    print("No data found. The website structure might have changed.")
#9
import smtplib
from email.message import EmailMessage

sender_email = 'coder6040@gmail.com'
app_password = 'aiksnlnctifpejde'  # No spaces
receiver_email = 'meenaakansha03@gmail.com'

msg = EmailMessage()
msg['Subject'] = 'Python se bheja gaya email 📩'
msg['From'] = sender_email
msg['To'] = receiver_email
msg.set_content(
    '''Namaste 🙏,

Yeh email Python script se bheja gaya hai, bina kisi third-party tool ke.
App Password aur 2FA setup hone ke baad yeh 100% kaam karta hai.

– Akansha Meena
    '''
)

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        print("🔐 Gmail SMTP se connect ho rahe hain...")
        smtp.login(sender_email, app_password)
        print("✅ Login ho gaya!")
        smtp.send_message(msg)
        print(f"📧 Email bhej diya gaya: {receiver_email}")

except smtplib.SMTPAuthenticationError as e:
    print("❌ Login failed. Check App Password:")
    print(e)
except Exception as e:
    print("❌ Koi aur error aaya:")
    print(e)
#10
import streamlit as st
import sys
import timeit

st.title("📋 List vs Tuple Comparison")

# List Example
my_list = [10, 20, 30, 40]
my_list[1] = 25
my_list.append(50)

# Tuple Example
my_tuple = (10, 20, 30, 40)

st.subheader("List Example")
st.write(my_list)

st.subheader("Tuple Example")
st.write(my_tuple)

# Memory Usage
list_mem = sys.getsizeof(my_list)
tuple_mem = sys.getsizeof(my_tuple)

st.subheader("Memory Usage (in bytes)")
st.write(f"List Memory Size: {list_mem}")
st.write(f"Tuple Memory Size: {tuple_mem}")

# Speed Test
list_time = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_time = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)

st.subheader("Creation Time (for 1,000,000 creations)")
st.write(f"List Creation Time: {list_time:.5f} seconds")
st.write(f"Tuple Creation Time: {tuple_time:.5f} seconds")

st.markdown("""
---
**Summary:**

- Lists are mutable (changeable) and typically use more memory.
- Tuples are immutable (fixed) and faster to create with less memory usage.
""")
#11
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

def login(driver, email, password):
    driver.get("https://www.linkedin.com/login")
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password, Keys.RETURN)
    st.info("👉 Agar 2FA ya OTP aaye, manually complete karen aur phir yahan Enter dabayen.")
    st.text_input("Confirm after login", key="login_confirm", on_change=lambda: None)

def send_message(driver, profile_url, message_text):
    wait = WebDriverWait(driver, 15)
    driver.get(profile_url)

    try:
        msg_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@aria-label,'Message') or contains(.,'Message')]")
            )
        )
    except:
        more_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'More')]")))
        more_btn.click()
        msg_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'artdeco-dropdown__content')]//span[contains(.,'Message')]")
            )
        )

    msg_btn.click()

    input_box = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='textbox' and @contenteditable='true']"))
    )

    ActionChains(driver).move_to_element(input_box).click().perform()

    driver.execute_script("arguments[0].innerHTML = arguments[1];", input_box, message_text)

    input_box.send_keys(Keys.END)
    input_box.send_keys(Keys.RETURN)

def main():
    st.title("🔗 LinkedIn Auto Message Sender")

    email = st.text_input("Enter LinkedIn Email")
    password = st.text_input("Enter LinkedIn Password", type="password")
    profile_url = st.text_input("Enter LinkedIn Profile URL")
    message_text = st.text_area("Enter your message")

    if st.button("Send Message"):
        if not all([email, password, profile_url, message_text]):
            st.error("Please fill all fields!")
            return
        
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Headless mode, remove if you want browser to show
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        try:
            login(driver, email, password)
            st.info("Logged in, sending message...")
            send_message(driver, profile_url, message_text)
            st.success("✅ Message sent successfully!")
        except Exception as e:
            st.error(f"❌ Error occurred: {e}")
        finally:
            time.sleep(2)
            driver.quit()

if __name__ == "__main__":
    main()
#12
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

def create_image():
    width, height = 800, 400
    background_color = (30, 30, 30)

    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    draw.rectangle([(50, 50), (750, 350)], outline=(255, 255, 0), width=5)

    text = "Hello, It's me Akansha"
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2
    draw.text((text_x, text_y), text, font=font, fill=(255, 255, 255))

    return image

st.title("🎨 Dynamic Image with PIL and Streamlit")

img = create_image()

# Display image in Streamlit
st.image(img, caption="Generated Image by PIL", use_column_width=True)
