import re
import datetime
import smtplib
import random

def check_product_availability(product_name):
    try:
        with open("product.txt", "r") as f:
            txt = f.read()
            x = re.search(product_name, txt)
            return x is not None
    except FileNotFoundError:
        return False

def supermarket():
    your_product = input("Enter your product: ").strip().lower()
    available = check_product_availability(your_product)
    
    if available:
        print(f"Yes, {your_product} is available.")
        
        try:
            how_many = int(input(f"How many {your_product} do you want: "))
            
            # Define product prices and GST calculations
            product_prices = {
                "parfum": (200, 50),
                "boiled rice": (40, 10),
                "idli rice": (30, 20),
                "raw rice": (50, 10),
                "olive oil": (130, 10),
                "butter oil": (170, 20),
                "sunflower oil": (250, 20),
                "salt": (50, 10),
                "sugar": (42, 10),
                "jaggery": (40, 10)
            }
            
            
            if your_product=="parfum":
                parfum=200
                total=parfum*how_many
                offer_total=total-50
                net_price=70.0
                gst_amount=net_price-parfum
                gst_percent=((gst_amount*100)/parfum )
                print("GST=",end=' ')
                print(round(gst_percent),end=' ')
                print("%")
                print(f"your total bill is {total} GST is {gst_percent} % ")
                f=open("product1.txt","w")
                y=datetime.datetime.now()
                f.write(f" your product name '{ your_product}' your total bill is {total} GST is {gst_percent}% date is '{y}'")
                f.write(f" your offer total is '{offer_total}'")
                print("bill generated success fully")
                
            elif your_product=="boiled rice":
                rice=40
                total=rice*how_many
                offer_total=total-50
                net_price=70.0
                gst_amount=net_price-rice
                gst_percent=((gst_amount*100)/rice )
                print("GST=",end=' ')
                print(round(gst_percent),end=' ')
                print("%")
                print(f"your total bill is {total} GST is {gst_percent} % ")
                f=open("product1.txt","w")
                y=datetime.datetime.now()
                f.write(f" your product name '{ your_product}' your total bill is {total} GST is {gst_percent}% date is '{y}'")
                f.write(f" your offer total is '{offer_total}'")
                print("bill generated success fully")
            elif your_product=="idli rice":
                idli_rice= 30
                total=idli_rice*how_many
                offer_total=total-50
                net_price=40.0
                gst_amount=net_price-idli_rice
                gst_percent=((gst_amount*100)/idli_rice )
                print("GST=",end=' ')
                print(round(gst_percent),end=' ')
                print("%")
                print(f"your total bill is {total} GST is {gst_percent} % ")
                f=open("product1.txt","w")
                y=datetime.datetime.now()
                f.write(f" your product name '{ your_product}' your total bill is {total} GST is {gst_percent}% date is '{y}'")
                f.write(f" your offer total is '{offer_total}'")
                print("bill generated success fully")
        
            elif your_product=="raw rice":
                raw_rice=50
                total=raw_rice*how_many
                offer_total=total-50
                net_price=70.0
                gst_amount=net_price-raw_rice
                gst_percent=((gst_amount*100)/raw_rice )
                print("GST=",end=' ')
                print(round(gst_percent),end=' ')
                print("%")
                print(f"your total bill is {total} GST is {gst_percent} % ")
                f=open("product1.txt","w")
                y=datetime.datetime.now()
                f.write(f" your product name '{ your_product}' your total bill is {total} GST is {gst_percent}% date is '{y}'")
                f.write(f" your offer total is '{offer_total}'")
                print("bill generated success fully")
        
            elif your_product=="olive oil":
                olive_oil= 130
                total=olive_oil*how_many
                offer_total=total-50
                net_price=70.0
                gst_amount=net_price-olive_oil
                gst_percent=((gst_amount*100)/olive_oil )
                print("GST=",end=' ')
                print(round(gst_percent),end=' ')
                print("%")
                print(f"your total bill is {total} GST is {gst_percent} % ")
                f=open("product1.txt","w")
                y=datetime.datetime.now()
                f.write(f" your product name '{ your_product}' your total bill is {total} GST is {gst_percent}% date is '{y}'")
                f.write(f" your offer total is '{offer_total}'")
                print("bill generated success fully")
            elif your_product=="butter oil":
                butter_oil= 170
                total=butter_oil*how_many
                offer_total=total-50
                net_price=190.0
                gst_amount=net_price-butter_oil
                gst_percent=((gst_amount*100)/butter_oil )
                print("GST=",end=' ')
                print(round(gst_percent),end=' ')
                print("%")
                print(f"your total bill is {total} GST is {gst_percent} % ")
                f=open("product1.txt","w")
                y=datetime.datetime.now()
                f.write(f" your product name '{ your_product}' your total bill is {total} GST is {gst_percent}% date is '{y}'")
                f.write(f" your offer total is '{offer_total}'")
                print("bill generated success fully")
        
            elif your_product=="sunflower oil":
                sunflower_oil=250
                total=sunflower_oil*how_many
                offer_total=total-50
                net_price=300.0
                gst_amount=net_price-sunflower_oil
                gst_percent=((gst_amount*100)/sunflower_oil )
                print("GST=",end=' ')
                print(round(gst_percent),end=' ')
                print("%")
                print(f"your total bill is {total} GST is {gst_percent} % ")
                f=open("product1.txt","w")
                y=datetime.datetime.now()
                f.write(f" your product name '{ your_product}' your total bill is {total} GST is {gst_percent}% date is '{y}'")
                f.write(f" your offer total is '{offer_total}'")
                print("bill generated success fully")
            elif your_product=="salt":
                salt=50
                total=salt*how_many
                offer_total=total-50
                net_price=60.0
                gst_amount=net_price-salt
                gst_percent=((gst_amount*100)/salt )
                print("GST=",end=' ')
                print(round(gst_percent),end=' ')
                print("%")
                print(f"your total bill is {total} GST is {gst_percent} % ")
                f=open("product1.txt","w")
                y=datetime.datetime.now()
                f.write(f" your product name '{ your_product}' your total bill is {total} GST is {gst_percent}% date is '{y}'")
                f.write(f" your offer total is '{offer_total}'")
                print("bill generated success fully")
            elif your_product=="sugar":
                sugar=42
                total=sugar*how_many
                offer_total=total-50
                net_price=60.0
                gst_amount=net_price-sugar
                gst_percent=((gst_amount*100)/sugar )
                print("GST=",end=' ')
                print(round(gst_percent),end=' ')
                print("%")
                print(f"your total bill is {total} GST is {gst_percent} % ")
                f=open("product1.txt","w")
                y=datetime.datetime.now()
                f.write(f" your product name '{ your_product}' your total bill is {total} GST is {gst_percent}% date is '{y}'")
                f.write(f" your offer total is '{offer_total}'")
                print("bill generated success fully")
        
            elif your_product=="jaggery":
                jaggery=40
                total=jaggery*how_many
                offer_total=total-50
                net_price=60.0
                gst_amount=net_price-jaggery
                gst_percent=((gst_amount*100)/jaggery )
                print("GST=",end=' ')
                print(round(gst_percent),end=' ')
                print("%")
                print(f"your total bill is {total} GST is {gst_percent} % ")
                f=open("product1.txt","w")
                y=datetime.datetime.now()
                f.write(f" your product name '{ your_product}' your total bill is {total} GST is {gst_percent}% date is '{y}'")
                f.write(f" your offer total is '{offer_total}'")
                print("bill generated success fully") 
            
            original_price, discount = product_prices.get(your_product, (0, 0))
            total = original_price * how_many
            offer_total = total - discount
            
            net_price = original_price + (original_price * discount / total)
            gst_percent = (discount * 100) / original_price
            
            print(f"GST: {round(gst_percent)} %")
            print(f"Your total bill is {total} GST is {gst_percent} %")
            
            with open("product1.txt", "a") as f:
                now = datetime.datetime.now()
                f.write(f"Product: {your_product}, Total Bill: {total}, GST: {gst_percent}%, Date: {now}\n")
                f.write(f"Offer Total: {offer_total}\n")
                
            print("Bill generated successfully.")
            var = input("Do you want to receive the bill via email? (yes/no): ")
            if var.lower() == "yes":
                email(your_product,total,gst_percent)
            else:
                print("Your email id is not verified.")
                
        except ValueError:
            print("Invalid input for quantity.")
    else:
        print(f"{your_product} is not available.")

def email(your_product,total,gst_percent):
    try:
        receive = input("Enter your email: ").strip()
        otp_number = random.randint(1000, 9999)
        
        send = smtplib.SMTP("smtp.gmail.com", 587)
        send.starttls()
        send.login("your_gmail@gmail.com", "your_password")
        
        message = f"Your OTP is: {otp_number}"
        message += f"Your {your_product} bill details:\n"
        message += f"Total Bill: {total}\n"
        message += f"GST: {gst_percent}%\n"
        send.sendmail("your_gmail@gmail.com", receive, message)
        
        send.quit()
        print("Mail sent successfully.")
        
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your email and password.")
    except smtplib.SMTPException as e:
        print(f"Mail not sent. Error: {e}")

supermarket()

