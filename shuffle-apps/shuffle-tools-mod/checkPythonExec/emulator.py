import asyncio
import datetime
import json
import time
import markupsafe
import os
import re
import subprocess
import tempfile
import zipfile
import base64
import ipaddress
import hashlib
from io import StringIO
from contextlib import redirect_stdout


import requests
import binascii
import struct

def execute_python(code):
    f = StringIO()
    with redirect_stdout(f):
        exec(code)
    s = f.getvalue()

    try:
        return {
            "success": True,
            "message": s,
        }
    except Exception as e:
        return {
            "success": False,
            "message": s,
        }
