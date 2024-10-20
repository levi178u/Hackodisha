import smtplib
from email.mime.text import MIMEText

def send_alert(transaction_details):
    sender = 'anshumansbi@gmail.com'
    receiver = 'xyz_customer@gmail.com'
    
    subject = 'Fraudulent Transaction Detected'
    body = f'Alert! A fraudulent transaction has been detected:\n{transaction_details}'
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, 'your_password')
        server.sendmail(sender, receiver, msg.as_string())

# Example usage
transaction_details = {
    'Amount': 9839.64,
    'Location': '(43.550740883275296, -141.72974723173664)',
    'ip_Address': '15.246.64.212'
}

send_alert(transaction_details)
