#!/bin/sh

# Initiate gunicorn
gunicorn -b 0.0.0.0:5000 app --log-file '/var/log/YVH_api.log' --log-level=debug