try:
    from uvicorn import run
    from fastapi import FastAPI
    from auth import auth_router
    from firebase_admin import initialize_app
    from firebase_admin.credentials import Certificate

except ImportError as import_error:
    raise import_error


app = FastAPI()

app.include_router(auth_router)

"""
DOWNLOAD YOUR FIREBASE PROJECT CONFIG JSON FILE BY LOGGING INTO CONSOLE > PROJECT > SETTINGS > SERVICE ACCOUNTS > "GENERATE NEW PRIVATE KEY"
TO GET YOUR WEB API KEY: LOGIN TO CONSOLE > APP > SETTINGS > "WEB API KEY"
"""

# Initilaize firebase app on startup
@app.on_event("startup")
def on_startup():
    creds = Certificate("PATH_TO_FIREBASE_CONFIG_FILE")
    firebase_app = initialize_app(credential=creds)
    return firebase_app

if __name__ == "__main__":
    run(app)





