
# A very simple Flask Hello World app for you to get started with...
import sys,os,logging,re,datetime
sys.path.append("/home/eminerapps/pymodules")
import genutil

logger=logging.getLogger("flask_app")

from flask import Flask

# Establish logging, if any

class Options:
  debug = None
genutil.G_options = Options()

genutil.G_options.debug = 2

if genutil.G_options.debug == None or genutil.G_options.debug == 0:
   logging.disable(logging.CRITICAL)  # effectively disable all logging
else:
   if genutil.G_options.debug == 9:
      genutil.configureLogging(logdestination='/home/eminerapps/mysite/flask_app.log', loglevel='DEBUG')
   else:
      genutil.configureLogging(logdestination='/home/eminerapps/mysite/flask_app.log')

# Initialization

G_config = genutil.processConfigFile("/home/eminerapps/mysite/flask_app.py.yaml")

# Start of app

logger.info("starting")
app = Flask(__name__)

@app.route('/')
def my_root():
   subject = 'This is a test email sent at %s!' % datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
   bodyText = "This is the body\nAnd more"
   emailTo = G_config["emailTo"]
   genutil.sendEmail(emailTo, subject, bodyText, "<br><b>HTML </b>text<p>", "/etc/hosts")
   return f'{emailTo} was just sent an email. haha'

@app.route('/hello/')
def hello_world():
   remoteUser = os.getenv('REMOTE_USER','')
   remoteAddr = os.getenv('REMOTE_ADDR','')
   environ    = str(os.environ)
   return f'<h1>Hello from me2you.</H1>{remoteUser}{remoteAddr}{environ}'
