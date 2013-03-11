__author__ = 'Dpak Malla'
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from lib.models.users.User import User
from inc.common import Global
import hashlib


def Index(request):
    login_err = None
    if request.method == "POST":
        glb = Global()
        if not glb.checkHost(request.META["HTTP_HOST"]):
            username = request.POST["username"]
            password = request.POST["password"]
            try:
                usr = User()
                usr.setUsername(username).setPassword(hashlib.sha512(password).hexdigest())
                if usr.Authenticate():
                    request.session.delete()
                    request.session["is_login"] = True
                    request.session["uid"] = usr.getUid()
                    request.session["user"] = usr.getUsername()
                else:
                    login_err = "Invalid Username Or Password!"
            except Exception:
                login_err = "Oops something went wrong."
        else:
            login_err = "Request Rejected!"

    if 'is_login' in request.session and request.session["is_login"]:
        return HttpResponseRedirect("/")
    else:
        return render_to_response('auth/index.html', {"login_err": login_err}, RequestContext(request))
