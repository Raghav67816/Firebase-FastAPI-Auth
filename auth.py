from fastapi import APIRouter
from trycourier import Courier
from firebase_admin import auth
from fastapi.responses import JSONResponse
from models import NewUser, UserLogin, EmailAndToken

from requests import post

api_key = "YOUR_FIREBASE_API_kEY"
auth_router = APIRouter(prefix="/auth")
mail_client = Courier(auth_token="YOUR_CURIOUR_API_KEY")

def check_verify(email: str) -> bool:
    user = auth.get_user_by_email(email)
    return user.email_verified

@auth_router.post("/new")
def create_user(user: NewUser):
    try:
        new_user = auth.create_user(
            display_name = user.name,
            password = user.password,
            email = user.email,
            phone_number = user.phone_number,
            email_verified = False
        )
        first_name = user.name.split(" ")[0]
        mail_client.send_message(message={
            "to": {
                "email": user.email
            },
            "template": "YOUR_NEW_USER_TEMPLATE_ID",
            "data":{
                "firstName": first_name,
                "email": user.email
            }
        })
        return JSONResponse(content={
            "message": "user created",
        }, status_code=200)

    except Exception as error:
        return JSONResponse(content={
            "message": "failed to create user",
            "error": str(error)
        })
    
@auth_router.post("/login")
def login_user(login: UserLogin):
    try:
        login_req = post(url=f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}",
                         json={
                             "email": login.email,
                             "password": login.password,
                             "returnSecureToken": True
                         }
                    )
        return JSONResponse(content={
            "data": login_req.json(),
            "is_verified": check_verify(login.email)
        }, status_code=200)

    except Exception as error:
        return JSONResponse(content={
            "message": "login failed",
            "error": str(error)
        }, status_code=500)
    

@auth_router.post("/resetpassword")
def reset_password(email_and_token: EmailAndToken):
    try:
        verify_user = auth.verify_id_token(email_and_token.token)
        if verify_user.get("email") == email_and_token.email:
            reset_link = auth.generate_password_reset_link(email=email_and_token.email)
            user = auth.get_user_by_email(email_and_token.email)
            first_name = user.display_name
            mail_client.send_message(message={
                "to": {
                    "email": email_and_token.email
                },
                "template": "YOUR_RESET_PASSWORD_TEMPLATE_ID",
                "data":{
                    "firstName": first_name.split(" ")[0],
                    "resetPasswordLink": reset_link
                }
            })
            return JSONResponse(
                content={"msg": "reset password link sent"}, status_code=200
            )
        
        else:
            return JSONResponse(
                content={"msg": "invalid token"}, status_code=401
            )
    
    except Exception as error:
        return JSONResponse(content={"msg": "failed to send reset password link",
                                     "error": str(error)
                                     }, status_code=500)
    
@auth_router.post("/verify")
def verify_user(params: EmailAndToken):
    try:
        verify_user = auth.verify_id_token(params.token)
        first_name = verify_user.get("name").split(" ")[0]
        if verify_user.get("email") == params.email:
            verify_link = auth.generate_email_verification_link(params.email)
            mail_client.send_message(message={
                "to": {
                    "email": params.email
                },
                "template": "YOUR_USER_VERIFICATION_TEMPLATE_ID",
                "data":{
                    "firstName": first_name,
                    "verificationLink": verify_link
                }
            })
            return JSONResponse(
                content={"msg": "verification link sent"}, status_code=200
            )
        
        else:
            return JSONResponse(
                content={"msg": "invalid token"}, status_code=401
            )
        
    except Exception as error:
        return JSONResponse(content={"msg": "failed to send verification link",
                                     "error": str(error)
                                     }, status_code=500)

