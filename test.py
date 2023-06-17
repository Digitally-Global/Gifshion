import smtplib

sender = "Private Person <mailtrap@gifshion.com>"
receiver = "A Test User <dkediaphone@icloud.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("live.smtp.mailtrap.io", 25) as server:
   server.login("api", "1a1a570bd30af32e65b8c1e20f4a2059")
   resp=server.sendmail(sender, receiver, message)
   print(resp)