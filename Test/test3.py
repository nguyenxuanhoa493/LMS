import requests

url = "https://els.aeglobal.edu.vn/common/organizationTreeDataJson"

payload = {}
headers = {
    "Cookie": "XSRF-TOKEN=eyJpdiI6InprUkxReDFJR1IxSm90Q2k3aXhOWmc9PSIsInZhbHVlIjoiT3BZMWNtRGNPK0ZzdWJPL2JJUlgwMzlkOXVXQ2hVYmVkUENUb2dKQWJzN3R5M2VPZlVqYjVQT28yWHVwNzRWbGZodkMzUW8yVGQ3QThkS2t2bnljOE13dXUybGNXcmM0MDBBMVNvSG1MeUZ0ZERDSEJZeE5pUVhtRGlMRm1JSUQiLCJtYWMiOiJiODM3N2JjMjkyYWEyYjhlZDAyYWFmMjBlMjljOTc4NDBmNTNmYWZjZjhjMjcxZWYyZTk1ODE5ZTUwZDFlZDE4IiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IjJpV0FlTmpmRkwxWC92cWhPbUM2K0E9PSIsInZhbHVlIjoidE1TakhPK25aTDdmelptakplNVlrdkFVNmVneTg5aGFLQjNXQUN0cWxFR3dhY3NvVEFaNFpCMzRQN3RScHh3M1h3d3JmdkJuTnI2cS9HdEhTcm9YVUQyWk8xUkpoWU1mYUpSZ0pkS2t3U0JTaEZIWXNrT3BOYmlrL1VnVjJ2Qk8iLCJtYWMiOiIxMjUwMWYzZjc1ZmZiNTE2NDRmZDY2YjJlZDkxM2NlMzM2ODY3YTNjYzVhYjdjOGM3ZTRjNDg4MjQ3NjliY2ExIiwidGFnIjoiIn0%3D"
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
