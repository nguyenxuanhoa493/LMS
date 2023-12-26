import requests

url = "https://els.aeglobal.edu.vn/quiz-kit/reviewAll/28323?level="

payload = {"_token": "cDupqHbsaRwE0Z00VWgIQ4l8Yo7X367obCN3MyyP"}
files = []
headers = {
    "authority": "els.aeglobal.edu.vn",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "vi,en-US;q=0.9,en;q=0.8",
    "cookie": "laravel_session=eyJpdiI6ImlzMkY1cXg3OWtZYmlOYkJjS0J0cEE9PSIsInZhbHVlIjoiQ3pOeGZnc1JGNlJNMEltZEh0cGs5TVdTaGxjd1d5dklaaS9HUmRVSDFGc0w2SkVuOEYydE5NdEV5Z3pkZUZidGJqcjB1MkRGSng2OTM0ME5TeGlMOFhVMzZNZnA0YmR5aTByQmt1MDJxZW84VjNjUVdtZWQ3b2FpMUhDSWdZdG0iLCJtYWMiOiIxMjMxOGY3MDhlZGE0M2QwYThjNDMxYWZkODdhNjdhM2IwNmQ1NzZjMzk3YTM5Y2Q5ZTQxZjI3MDkxNDNjMTM0IiwidGFnIjoiIn0%3D",
    "origin": "https://els.aeglobal.edu.vn",
    "referer": "https://els.aeglobal.edu.vn/quiz-kit",
    "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
