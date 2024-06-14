from dotenv import load_dotenv
import requests
import os

load_dotenv()

def parse_code(code_response):
    return code_response.split("=")[1]

request_token_url = "https://getpocket.com/v3/oauth/request"
access_token_url = "https://getpocket.com/v3/oauth/authorize"
authenticated_requests_url = "https://getpocket.com/v3/get"
consumer_key = os.getenv('CONSUMER_KEY')

request_token_payload = {
    "consumer_key": consumer_key,
    "redirect_uri": "http://www.google.com"
}

request_token = parse_code(requests.post(url=request_token_url, json=request_token_payload).text)
print(request_token)

access_token_payload = {
    "consumer_key": consumer_key,
    "code": request_token
}
access_token = requests.post(url=access_token_url, json=access_token_payload).text
print(access_token)

authenticated_requests_payload = {
    "consumer_key": consumer_key,
    "access_token": access_token
}