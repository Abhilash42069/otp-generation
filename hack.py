import smtplib
import random as r
import pyttsx3
eng = pyttsx3.init()

def otp_gen():
    return ''.join([str(r.randint(1,9)) for i in range(4)])
otp = otp_gen()
eng.say('your otp is '+otp)
eng.runAndWait()

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login('abc@gmail.com', 'password')
conn.sendmail('xyz@gmail.com', 'pqr@gmail.com',\
              'Subject:Alert\n\n your otp:'+ otp_gen())
conn.quit()
eng.say('Your OTP is mailed')
eng.runAndWait()
