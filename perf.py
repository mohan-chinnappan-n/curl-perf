import streamlit as st
import subprocess

def run_curl_command(url):
    command = [
        'curl', '-s', '-w',
        'time_namelookup:%{time_namelookup}\n'
        'time_connect:%{time_connect}\n'
        'time_appconnect:%{time_appconnect}\n'
        'time_pretransfer:%{time_pretransfer}\n'
        'time_redirect:%{time_redirect}\n'
        'time_starttransfer:%{time_starttransfer}\n'
        'time_total:%{time_total}',
        '-o', '/dev/null', url
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

st.title("Curl Performance Metrics App")

url = st.text_input("Enter URL")

if st.button("Fetch Performance"):
    if url:
        result = run_curl_command(url)
        st.text_area("Curl Performance Results", result, height=200)
    else:
        st.error("Please enter a URL.")
