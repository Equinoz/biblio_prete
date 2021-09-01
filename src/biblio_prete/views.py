from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def signup(req):
	form = UserCreationForm()

	return render(req, "biblio_prete/signup.html", context={"form": form})