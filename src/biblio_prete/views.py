from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from biblio_prete.models import CustomUser


class CustomSignupForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = UserCreationForm.Meta.fields


def home(req):
	return render(req, "biblio_prete/home.html")

def signup(req):
	context = {}

	if req.method == "POST":
		form = CustomSignupForm(req.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Bienvenue !")
		else:
			context["errors"] = form.errors

	form = CustomSignupForm()
	context["form"] = form

	return render(req, "biblio_prete/signup.html", context=context)