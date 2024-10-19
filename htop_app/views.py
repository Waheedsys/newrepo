from django.shortcuts import render

from django.http import HttpResponse
import os
import time
import subprocess

def htop_view(request):
    # Replace with your full name
    name = "Your Full Name"
    # Get the system username
    username = os.getlogin()
    # Get the current server time in IST
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    ist_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 5.5 * 3600))
    # Get the top command output
    top_output = subprocess.getoutput('top -b -n 1')

    # Construct the HTML response
    response_html = f"""
    <h1>Server Stats</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time}</p>
    <pre>{top_output}</pre>
    """
    return HttpResponse(response_html)
