# house_puller

You will need to set these environment variables in advance before using this script:
```
EMAIL_ADDRESS (emails will be sent from this account over gmail)
EMAIL_PASSWORD 
RECEIVER_EMAIL_ADDRESS (emails will be received by this account)
```

Run the application in the background and every 4 hours it will give out updates to your email that you set as the RECEIVER
```
$ python3 house_puller.py &
```
