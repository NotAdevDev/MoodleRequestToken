import requests 

moodleRoot = "YOUR_URL/login/token.php"
moodleUsername ="API_ENABLED_USER"
moodlePassword ="API_USER_PASSWORD"
moodleService ="SERVICE_NAME"

url = moodleRoot + "?username="+moodleUsername+"&password="+moodlePassword+"&service="+moodleService

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print(response.status_code)
