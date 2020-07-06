from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

# def login(request):
# 	return render(request, "login.html")
def oauth(request):
	code = request.GET['code']
	print('code = ' + str(code))

	return redirect('index')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def kakao_login(request):
	login_request_uri = 'https://kauth.kakao.com/oauth/autorize?'

	client_id = 'c38d121cdeb9bf8343904377312fb1a3'
	redirect_uri = 'http://127.0.0.1:8000/oauth'

	login_request_uri += 'client_id=' + client_id
	login_request_uri += '&redirect_uri=' + redirect_uri
	login_request_uri += '&response_type=code'

	return redirect(login_request_uri)