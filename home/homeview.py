__author__ = 'Dipak Malla'
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from lib.models.AccessIds.AccessID import AccessID
from lib.models.ProName.Pro import Pro
from lib.models.DataFeed.Feed import FeedData
import hashlib
import random
import json


def Feed(request):
    if request.method == "POST":
        try:
            ai = AccessID()
            data = ai.FetchAccess(request.POST["ACCESS_ID"])
            i = 0
            for d in data:
                i += 1
            if i == 0:
                return HttpResponse(json.dumps({"error": True, "msg": "Invalid Access ID."}))
            else:
                rproName = request.POST["PROCEDURE_NAME"]
                data = json.loads(request.POST["DATA"])
                pr = Pro()
                pdata = pr.FetchPro(proName=rproName)
                q_data = list()
                for qd in data:
                    q_data.append(data[qd])
                fd = FeedData()
                fd.setQuery(pdata[0].getProQry()).setData(q_data)
                rv = fd.Save()
                return HttpResponse(json.dumps({"error": False, "msg": "Success", "rowcount": rv}))

        except Exception, ex:
            return HttpResponse(json.dumps({"error": True, "msg": "Something went wrong!"}))
    else:
        return HttpResponse(json.dumps({"error": True, "msg": "Invalid Request!"}))


def Home(request):
    if 'is_login' in request.session and request.session["is_login"]:
        access_err = None
        pro_err = None
        if 'access_err' in request.session:
            access_err = request.session["access_err"]
            del request.session["access_err"]
        if 'pro_err' in request.session:
            access_err = request.session["pro_err"]
            del request.session["pro_err"]
        rd = list()
        pd = list()
        try:
            ai = AccessID()
            data = ai.FetchAccess()
            for d in data:
                rd.append({"ID": d.getAccessId(), "NAME": d.getAccessName()})
        except Exception, ex:
            access_err = "Oops something went wrong :("

        try:
            pr = Pro()
            pdata = pr.FetchPro()
            for d in pdata:
                pd.append({"ID": d.getProId(), "NAME": d.getProName(),  "QRY": d.getProQry()})
        except Exception, ex:
            pro_err = "Oops something went wrong :("

        return  render_to_response('index.html', {"p_data": pd,
                                                  "pro_err": pro_err,
                                                  "a_data": rd,
                                                  "user": request.session["user"],
                                                  "access_err": access_err},
                                   RequestContext(request))
    else:
        return HttpResponseRedirect("/login")


def Procedure(request):
    request.session["pro_err"] = None
    if request.method == "POST":
        try:
            pr = Pro()
            pr.setProName(request.POST["proCedureName"]).setProQry(request.POST["qry"])
            if pr.Save() <= 0:
                request.session["pro_err"] = "Could not add procedure."
        except Exception, ex:
            request.session["pro_err"] = "Oops something went wrong please try again."
    return HttpResponseRedirect("/")


def AccessIDCall(request):
    request.session["access_err"] = None
    if request.method == "POST":
        try:
            ai = AccessID()
            ai.setAccessId(hashlib.sha384(str(random.randint(1, 899989989))).hexdigest())
            ai.setAccessName(request.POST["accessName"])
            if ai.Save() <= 0:
                request.session["access_err"] = "Could not generate the Access ID."
        except Exception, ex:
            request.session["access_err"] = "Oops something went wrong please try again."
    return HttpResponseRedirect("/")