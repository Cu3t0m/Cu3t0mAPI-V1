import random
import requests



def jokes():
  response = requests.get('https://api.cu3t0m.repl.co/jokes')
  return response.text

def letters():
  response = requests.get('https://api.cu3t0m.repl.co/letters')
  return response.text

def numbers():
  response = requests.get('https://api.cu3t0m.repl.co/numbers')
  return response.text

def words():
  response = requests.get('https://api.cu3t0m.repl.co/words')
  return response.text

def memes(topic="memes", amount="1"):
  response = requests.get(f'https://api.cu3t0m.repl.co/gimme/{topic}/{amount}')
  return response.text

def ai_response(question):
  response = requests.get(f'https://api.cu3t0m.repl.co/ai/response/{question}')
  return response.text