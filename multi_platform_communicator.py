"""
import smtplib ,ssl
from twilio.rest import Client
from linkedin_api import Linkedin
import tweepy
from fbchat import Client
from fbchat.models import Message
from instagrapi import Client


def send_email():
       s = smtplib.SMTP("smtp.gmail.com", 587)
       s.starttls()
       s.login(sender_email, password)
       s.sendmail(sender_email, receiver_email, message.as_string())


def send_sms():
        client = Client(account_sid, auth_token)
    client.messages.create( to= "+911234567890", from= "+91xxxxxxxxxx", body= "Hello!!!")


def make_call():
    client = Client(account_sid, auth_token)
    client.calls.create( to= "+911234567890", from= "+91xxxxxxxxxx", url='http://demo.twilio.com/docs/voice.xml')


def post_linkedin():
        api = Linkedin('your_email', 'your_password')
        api.submit_post(
        'text='Hello Everyone!'
        )


def post_twitter():
       api_key = 'YOUR_API_KEY'
  api_key_secret = 'YOUR_API_KEY_SECRET'
  access_token = 'YOUR_ACCESS_TOKEN'
  access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
  auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)
tweet_text = " Hello Everyone!"
response = api.update_status(status=tweet_text)


def post_facebook():
    client = Client(username, password)
    client.send(Message(text="Hello!"), thread_id=client.uid, thread_type=ThreadType.USER)


def post_instagram():
     cl = Client()
   cl.login(username, password)
   cl.send_message("Hello!!!",caption)


def send_whatsapp():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body='Hello!',
    from_='whatsapp:+141234567890', 
    to='whatsapp:+91xxxxxxxxxx'      
)

def main():
    menu =
    Choose a task:
    1. Send Email
    2. Send SMS
    3. Make a Phone Call
    4. Post on Linkedin 
    5. Post on Twitter (X)
    6. Post on Facebook
    7. Post on Instagram
    8. Send WhatsApp Message
    9. Exit

while True:
        print(menu)
        choice = input("Enter choice (1-9): ")
        if choice == '1':
             send_email()
        elif choice == '2':
             send_sms()
        elif choice == '3':
            make_phone_call()
        elif choice == '4':
            post_linkedin()
        elif choice == '5':
            post_twitter()
        elif choice == '6':
            post_facebook()
        elif choice == '7':
            post_instagram()
        elif choice == '8':
            send_whatsapp()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")


    if __name__ == "__main__":
    main_menu()
 """  

