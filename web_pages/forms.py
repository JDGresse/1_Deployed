from django import forms


class ContactForm(forms.Form):
    your_name = forms.CharField(
        label="Your name",
        max_length=100,
    )
    email = forms.EmailField(
        label="Your email",
        max_length=100,
    )
    contact_number = forms.CharField(
        label="Contact number",
        max_length=20,
    )
    subject = forms.CharField(
        label="Subject",
        max_length=200,
    )
    service = forms.ChoiceField(
        label="Service",
        choices=(
            ("Psychotherapy", "Psychotherapy"),
            ("AD/HD Support", "AD/HD Support"),
            ("Burnout Coaching", "Burnout Coaching"),
        ),
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea,
    )
