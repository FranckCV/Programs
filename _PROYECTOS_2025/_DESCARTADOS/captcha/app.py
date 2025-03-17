# https://github.com/nextcaptcha/nextcaptcha-python

import os
import sys
from nextcaptcha import NextCaptchaAPI
 
# 6Ld-t8kZAAAAAGWroLwsrpuD5yo1rNGyJ6cmNu23
# 6Ld-t8kZAAAAAGWroLwsrpuD5yo1rNGyJ6cmNu23

WEBSITE_URL = "https://avalue.audit.pe"

client_key = os.getenv('NEXTCAPTCHA_KEY', "YOUR_CLIENT_KEY")
 
api = NextCaptchaAPI(client_key=client_key)
try:
  result = api.recaptchav3(website_url=WEBSITE_URL, website_key="SITE_KEY")
 
except Exception as e:
  sys.exit(e)
 
else:
  sys.exit('solved: ' + str(result))