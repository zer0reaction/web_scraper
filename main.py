from bs4 import BeautifulSoup
import requests

result = requests.get("https://www.youtube.com/watch?v=f8KYX4fDxnk")

doc = BeautifulSoup(result.text, "html.parser")

divs = doc.find_all("div")
content = str(divs[0].find_all("meta")[14])

num = ""
for i in content:
    if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
        num += i

print(int(num))
