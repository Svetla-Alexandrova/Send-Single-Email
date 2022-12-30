import yagmail
import os
import time

sender = 'mmmm@gmail.com'
receiver = 'nnn@gmail.com'

subject = 'This is the subject'
content = """
Here is the content of the email
"""


yag = yagmail.SMTP(user=sender, password=os.getenv("PASSWORD"))
# First select Tools/Secrets; Give name to the key, then go to your gmail and apply apps password
# Uses getenv to prevent the vialization of password from other users.

while True:
  yag.send(to=receiver, subject=subject, contents=content)
  print('Email is sent')
  time.sleep(60)