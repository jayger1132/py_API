from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import numpy as np
import json
with requests.get("http://127.0.0.1:3000/All/json") as response:
    Ubike_Resource = response.json()
    DT = Ubike_Resource['result']
    
    #  print(type(List))
    print(DT['0'])


for values in DT:
    print(values)
