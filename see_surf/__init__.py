from __future__ import print_function # Only Python 2.x
import subprocess
import sys
from pathlib import Path

_SCRIPT = Path(__file__).parent / "see-surf.py"

def execute(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)
    return popen

def scan(
    host,
    cookies=None,
    threads=10,
    verbose=False,
    burp=None,
    callback=None,
    provider=None,
    model=None,
    api_key=None,
):
    cmd = [
        sys.executable,
        str(_SCRIPT),
        "-H",
        host,
        "-t",
        str(threads),
    ]

    if cookies:
        cmd += ["-c", cookies]

    if verbose:
        cmd.append("-v")

    if burp:
        cmd += ["-b", burp]

    if callback:
        cmd += ["--callback", callback]

    if provider:
        cmd += ["--provider", provider]

    if model:
        cmd += ["-m", model]

    if api_key:
        cmd += ["--api-key", api_key]


    popen = execute(cmd)
    
    return popen



