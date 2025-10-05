from django.shortcuts import render
from .forms import UserRegistrationForm
import requests
import json
import os

LANGUAGE_CODES = {
    "English": "en",
    "Hindi": "hi",
    "Kannada": "kn",
}

def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone_number"]
            language = form.cleaned_data["language"]
            doctor_name = form.cleaned_data["doctor_name"]
            staff_name = form.cleaned_data["staff_name"]
            if doctor_name == "Test Name":
                doctor_number = "919739811075"
            else:
                doctor_number = "918123273694"

            if staff_name == "Test Name":
                staff_number = "919739811075"
            else:
                staff_number = "918123273694"

            # Map language to code
            language_code = LANGUAGE_CODES.get(language, "en")

            # print("doctor", doctor_name, "name", staff_name , "staff")

            api_body = json.dumps([{
                "phone_number_id": phone_number,
                "user_language": language_code,
                "user_type": "byoebuser",
                "experts": {"byoebexpert": [doctor_number], "byoebexpert2": [staff_number]}
            }])

            # print()
            print(api_body)

            try:
                # Use environment variable or default to production API
                api_url = os.environ.get('API_ENDPOINT', 'https://oncobot-h7fme6hue9f7buds.canadacentral-01.azurewebsites.net/register_users')
                response = requests.post(
                    api_url,
                    headers={"Content-Type": "application/json"},
                    data=api_body
                )
                if response.status_code == 200:
                    return render(request, "registration_app/registration_success.html")
                else:
                    return render(request, "registration_app/registration_form.html", {"form": form, "error": f"API Error: {response.status_code}"})
            except Exception as e:
                return render(request, "registration_app/registration_form.html", {"form": form, "error": str(e)})

    else:
        form = UserRegistrationForm()

    return render(request, "registration_app/registration_form.html", {"form": form})
