import smtplib

my_email = "estifwonde211@gmail.com"
password = "21130328@Estif"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user = my_email , password=password)
connection.sendmail(from_addr=my_email, to_addrs="estifanoswondwossen396@gmail.com", msg="yelloooo")
