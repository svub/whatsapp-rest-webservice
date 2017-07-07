# whatsapp-rest-webservice
A Python/Django REST webservice using Yowsup to send messages to WhatsApp. WIP.

# Getting started

## Setting up the environment
Get the source.
   git clone https://github.com/svub/whatsapp-rest-webservice.git
   cd whatsapp-rest-webservice

Make sure you have Python env installed. Then, open the virtual environment.
   pip install virtualenv
   virtualenv --no-site-packages --distribute env && source env/bin/activate

Install the dependencies.
   pip install django djangorestframework coreapi

Initialize Django by creating a superuser to secure the REST webservices and an empty database.
   python manage.py createsuperuser
   python manage.py migrate

Initialize Yowsup
   python service/yowsup/setup.py install

## Setting up your WhatsApp account.
You'll need a registered WhatsApp account and a working mobile phone number to do the setup.

### 1. Register your phone
   yowsup-cli registration --cc <country code> --phone <country code><phone no> --mcc <MCC code> --requestcode sms
Country code without + or 00, e.g. for Germany 49
Example phone number with German country code: 4917616702776
You can find the MCC for your provider on [Wikipedia](https://en.wikipedia.org/wiki/Mobile_country_code)
Example, there are only three in Germany: O2 26203, Telekom 26201, and Vodafone 26202

### 2. Activiate your phone.
After sending out the registration request, you should have received an SMS with a code that you'll need now.
   yowsup-cli registration --cc <country code> --phone <country code><phone no> --mcc <MCC code> --register <code received via SMS>

This will print you a result similar to this:
   status: ok
   kind: free
   pw: +BaimGldHiWhr0oseHxbSScF3vT=
   price: 0,89 €
   price_expiration: 1501987180
   currency: EUR
   cost: 0.89
   expiration: 4444444444.0
   login: 4910716702776
   type: existing
We'll need the password from the third line (starting with "pw:") - in this example "+BaimGldHiWhr0oseHxbSScF3vT=".

## Configuring the service
Customize your config file, and insert your phone number (again, <country code><phone no>) and the password from the previous step.
   cp service/whatsapp.example.conf service/whatsapp.conf && nano service/whatsapp.conf

## Running the service
The service will be listening on port 8000 by default.
   python manage.py runserver
