from django import forms

LANGUAGE_CHOICES = [
    ('English', 'English'),
    ('Hindi', 'Hindi'),
    ('Kannada', 'Kannada'),
]

DOCTOR_CHOICES = [
    ('Choose doctor', 'Choose doctor'),
    ('Test Name', 'Test Name'),
    ('Test Name 2', 'Test Name 2'),
]

STAFF_CHOICES = [
    ('Choose staff', 'Choose staff'),
    ('Test Name', 'Test Name'),
    ('Test Name 2', 'Test Name 2'),
]

CONSENT_CHOICES = [
    ('Yes', 'Yes'),
    ('No', 'No'),
]

GENDER_CHOICES = [
    ('Select', 'Select'),
    ('Male', 'Male'),
    ('Female', 'Female'),
]

class UserRegistrationForm(forms.Form):
    full_name = forms.CharField(label="Full Name", max_length=100, required=True)
    phone_number = forms.CharField(label="Phone Number (Whatsapp)", max_length=20, required=True)
    # email = forms.EmailField(label="Email Address", required=False)
    date_of_birth = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    # age = forms.IntegerField(label="Age", required=False)
    gender = forms.ChoiceField(label="Gender", choices=GENDER_CHOICES, required=True)
    language = forms.ChoiceField(label="Preferred Language", choices=LANGUAGE_CHOICES, required=True)
    doctor_name = forms.ChoiceField(label="Doctor Assigned", choices=DOCTOR_CHOICES, required=True)
    staff_name = forms.ChoiceField(label="Staff Assigned", choices=STAFF_CHOICES, required=True)
    # consent = forms.ChoiceField(label="Consents?", choices=CONSENT_CHOICES, widget=forms.RadioSelect, required=True)
