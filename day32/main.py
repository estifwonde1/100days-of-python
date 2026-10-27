import smtplib

#what is the issue with this emailsmtlib
my_email = "estifwonde211@gmail.com"
password = "21130328@Estif"
with smtplib.SMTP("smtp.gmail.com",587) as connection:

    connection.starttls()
    connection.login(user = my_email , password=password)
    connection.sendmail(from_addr=my_email, to_addrs="estifanoswondwossen396@gmail.com", msg="yelloooo")
#alright after this we are gonna makesure we start the oython again like damn work and class is becoming overwhelming
#another
bruh = True
n = 0
while bruh:
    print("damn need to start to code again because am gonna lose my edge soon bruh don't lose ur edge")
    n=+1
    if n >= 20:
        bruh = False

    
    
