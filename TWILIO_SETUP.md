# Twilio Setup Instructions

## For SMS/OTP Functionality

The Z-Vote system uses Twilio for sending SMS messages with OTP codes and passphrases. Currently, SMS is disabled for testing purposes.

## To Enable SMS:

### 1. Create a Twilio Account
- Go to [https://www.twilio.com/](https://www.twilio.com/)
- Sign up for a free account
- Verify your phone number

### 2. Get Your Credentials
- **Account SID**: Found in your Twilio Console dashboard
- **Auth Token**: Found in your Twilio Console dashboard  
- **Phone Number**: Your Twilio phone number for sending SMS

### 3. Create .env File
Create a `.env` file in your project root with:

```env
# Twilio Configuration
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=your_twilio_phone_number_here

# API Ninjas for password generation
API_NINJA_API=your_api_ninja_key_here
```

### 4. Enable SMS in Code
Uncomment these lines in `poll/views.py`:

```python
# In register function:
sms(voter.ph_country_code+voter.phone_number,"Your OTP is " + str(otp_number))

# In otp function:
sms(Voter.ph_country_code+Voter.phone_number," DO NOT SHARE THIS PASSPHRASE WITH ANYONE! \n\nYour Secret Passphrase is " + phrase)
```

### 5. Remove Test Display
Remove the OTP display from the OTP template when SMS is enabled.

## Current Status: SMS Disabled
- OTP codes are displayed on screen for testing
- Passphrases are displayed on screen for testing
- No external SMS costs during development
- Perfect for testing and development

## Note
- Free Twilio accounts have limitations on SMS
- Test thoroughly before enabling in production
- Consider using Twilio's test credentials for development
