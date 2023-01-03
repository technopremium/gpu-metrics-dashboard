from pyngrok import ngrok
from typing import Union
from fastapi import FastAPI
from subprocess import Popen, PIPE

# Create a FastAPI app and define a single route:
app = FastAPI()


def run_cmd(cmd):
    return Popen(cmd,shell=True, stdout=PIPE).stdout.read()
    ""


@app.get("/gpu-info/")
def get_gpu_info():
    
    temperature = run_cmd("nvidia-smi --query-gpu=temperature.gpu --format=csv | grep -E '[0-9]{1,4}' | tr -d '\n'")
    power = run_cmd("nvidia-smi -q -d power | grep Draw | grep -Eo '[+-]?[0-9]+([.][0-9]+)?' | tr -d '\n'")
    clock = run_cmd("nvidia-smi -q -d clock | grep Graphics | head -n 1 | awk '{print $3}' | tr -d '\n'")
    
    return {
        'temperature': temperature,
        'power': power,
        'clock': clock
    }

# public_url = ngrok.connect(8000)
# print(f"Visit {public_url}")