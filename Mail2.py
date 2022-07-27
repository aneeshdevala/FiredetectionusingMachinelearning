import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
 

def sendmail(usermailid):
    
    img_data = open("test.jpg", 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'Fire Detection Image Mail123'
    msg['From'] = 'aneesh172.ant@gmail.com'
    msg['To'] = 'seattlecbe@gmail.com'
    print("in func")
    text = MIMEText("Fire detected on cam 01")
    msg.attach(text)
    image = MIMEImage(img_data, name="Fire_detection.jpg")
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('aneesh172.ant@gmail.com', 'ranji@276')
    s.sendmail('seattlecbe@gmail.com', 'seattlecbe@gmail.com', msg.as_string())
   
    s.quit()
  
    print("Sent Successfully")
   
