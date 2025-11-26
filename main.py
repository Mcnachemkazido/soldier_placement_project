import requests

url = "http://localhost:8000/assignWithCsv"

with open("data/hayal_300_no_status (1).csv", "rb") as f:
    files = {
         "file": ("hayal_300_no_status (1).csv", f, "text/csv")}

    response = requests.post(url,files=files)

print(response.json())