import Cu3t0mAPI.CU3T0MAPI 
import json


x=69
print("Simple use of the 'ai_response' function.")
while x == 69:
  q = input("")
  resp = Cu3t0mAPI.ai_response(q)
  response = json.loads(resp)
  print(response["message"])


