# Client code to get the requested data from server, API.
import json
import requests
import numpy as np
url_gen = lambda dims: f"http://192.168.1.102:8090/random?size={'x'.join([str(k) for k in dims])}"
dims=[10,20,30]
data = json.loads(requests.get(url_gen(dims)).text)
arr = np.asarray(data['array'])
print("shape : ", arr.shape) #For Verification
"""
Output: shape : (10,20,30)
"""
