import streamlit as st
import subprocess
import pandas as pd

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

def parse_curl_output(output):
    # Parse the curl output into a list of tuples
    data = []
    for line in output.strip().split('\n'):
        key, value = line.split(':', 1)
        data.append({'metric': key, 'time(ms)': float(value)})
    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(data)
    return df

st.title("Curl Performance Metrics App")

url = st.text_input("Enter URL", 'https://www.google.com')

if st.button("Fetch Performance"):
    if url:
        output = run_curl_command(url)
        df = parse_curl_output(output)
        st.dataframe(df)
    else:
        st.error("Please enter a URL.")
