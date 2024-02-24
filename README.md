
# Firebase FastAPI Auth FastAPI


This API is designed to facilitate the basic yet essential tasks related to managing user information within a system or application. It includes a variety of endpoints, each dedicated to a specific aspect of user management. 


 - Create New User
 - Login User
 - Reset Password
 - Verify User






## Features

- 🔐 Secure & Fast 
- 📧 Sends Email To Users
- ✅ Returns Proper Status Codes & Messages

It uses **Firebase** and [FastAPI](https://github.com/tiangolo/fastapi) which ensures efficiency and security.

## Setup

Firstly,  install the following dependencies
 - firebase_admin
 - fastapi
- uvicorn[standard]
 - trycuriour

```bash
  pip3 install firebase_admin fastapi uvicorn[standard] trycuriour
```

Clone this GitHub repo using git or download this repo.

```bash
  git clone https://github.com/Raghav67816/Firebase-FastAPI-Auth.git
```
It contains the following files:
 - main.py - You can use your own file, this is only given for basic setup.
 - auth.py - It has **auth router** with a prefix **/auth**. It is the main file containing important endpoints

Import the **auth_router** to your file and include it to your app.

```python3
from auth import auth_router

# Include in your app
app.include_router(auth_router)
```

This will include the endpoints to your app.

**NOTE**: Before running the app it is important to collect the following things:

 - **trycuriour** api key and template IDs of your template
 - Firebase **web api key**
 - Firebase app **private key**

Update the api keys and template ids in the **auth.py** file.

## Run Locally

After setting up, run the following command to run your app.

```bash
  python3 main.py # If your are running the app through script
```
**OR**
```bash
  python3 uvicorn main:your_app_name --reload
```



## Contributing

Contributions are always welcome!
You can add more features to this repo.
