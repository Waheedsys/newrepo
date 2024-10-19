# core/views.py

from django.http import HttpResponse
import socket
from datetime import datetime
import os
import psutil  # Make sure you have this imported for system metrics
import pytz
import subprocess

def htop_view(request):
    # Get server time in IST
    ist_time = datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')
    name = "syed waheed" 
    # username = os.getlogin()
    # ist = pytz.timezone('Asia/kolkata')
    # servertime  = datetime.now(ist).strftime('%Y-%m-%d  %H:%M:%S  %Z%z')
    # top_output = subprocess.getoutput("top -bn 1")
    
    # Get system details
    username = os.getenv('USER') or socket.gethostname()
    # Get system resource usage
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()

    # Prepare the top output
    top_output = f"CPU Usage: {cpu_usage}%\nMemory Usage: {memory_info.percent}% used of {memory_info.total / (1024 ** 2):.2f} MB"

    # Prepare the response
    response = f"""
    <html>
    <head><title>HTop</title></head>
    <body>
        <h1>HTop Output</h1>
        <p>Name: {name}</p>
        <p>Username: {username}</p>
        <p>Server Time in IST: {ist_time}</p>
        <h2>Top Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return HttpResponse(response)


def index(request):
    # A simple index view
    return HttpResponse("<h1>Welcome to the Index Page!</h1>")
