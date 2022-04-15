import smtplib

from email.message import EmailMessage
from email.utils import make_msgid
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


    
if __name__=="__main__":
    msg = EmailMessage()
    msg['Subject'] = "Wanna answer me?"
    msg['From'] = "miladul2014@gmail.com"
    msg['To'] = "miladul2014@gmail.com"
    
    asparagus_cid = make_msgid()
    msg.add_alternative("""\
    <html>
    <head></head>
    <body>
    <h2>Hey! Look what i found on the 
    <a href="https://www.pinterest.com/">pinterest</a></h2>
    <img src="cid:{asparagus_cid}" />
    </body>
    </html>
    """.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')
 
    
    with open("pinterest.jpeg", "rb") as img:
        msg.get_payload()[0].add_related(img.read(), 'image', 'jpeg', cid=asparagus_cid)
        
    #msg.attach(MIMEText(body, "plain"))
    with open("freckled's.png", "rb") as fr:
        part=MIMEBase("application", "octet-stream")
        part.set_payload(fr.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f'attachment; filename="freckled\'s.png')
    
    msg.attach(part)
        
    with open("outgoing.msg", "wb") as f:
        f.write(bytes(msg))
        
    server=smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.set_debuglevel(True)
    server.login("miladul2014@gmail.com", "biLLie2001")
    try:
        server.send_message(msg)
        print("-"*20)
        print(msg.get_content_type())
    finally:
        server.quit()
        
        