from flask import Flask, abort, request
import logging
import random
import math

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", filename='/home/ubuntu/app.log', level=logging.DEBUG)
app = Flask(__name__)

# see http://www.investopedia.com/articles/07/montecarlo.asp
# if you need reminding of the maths here
STDEV = 0.112756
EXPECTED_RETURN = 0.13556
DAYS = 3
dt = 1/250

def mc_sim(start_price, stdev, expected_return, days):
  values = [start_price]
  for num_day in range(days):
    random_num = random.normalvariate(0, 1)
    factor = expected_return * dt + (stdev * random_num * math.sqrt(dt))
    diff = start_price * factor 
    new_price = start_price + diff
    values.append(new_price)
    start_price = new_price
    return values

@app.route('/')
def index():
  logging.debug(request.remote_addr + ":Frontpage")
  return 'This is a test application.!'

@app.route('/404')
def error():
  abort(404)

@app.route("/502")
def error2():
  mc_returns = []
  for i in range(5000):
    mc_returns.append(mc_sim(25.72, 0.112756, 0.135566, 10)[-1])
  abort(502)

@app.route("/login")
def login():
  user = request.args.get('user')
  password = request.args.get('password')
  if user and password:
    logging.warning("Failed login. User: " + user + " Password: " + password)
  abort(403)

