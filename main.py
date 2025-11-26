import requests

url = "http://localhost:8000/waitingLis"

# with open("data/hayal_300_no_status (1).csv", "rb") as f:
#     files = {
#          "file": ("hayal_300_no_status (1).csv", f, "text/csv")}
#
#
response = requests.get(url)

print(response.json())