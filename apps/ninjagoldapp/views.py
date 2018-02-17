# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random
import datetime


def index(request):
	if 'money' not in request.session:
  		request.session['money']=0
  	if 'activity' not in request.session:
 		request.session['activity']=""
 	context = {'money':request.session['money'], 'activity':request.session['activity']}
	return render(request, "ninjagoldapp/index.html", context)


def process_money(request):
	if not request.method == 'POST':
		return redirect("/ninjagoldapp")
	value= request.POST['building']
  #Location + value+ time + append previous session log
  	if value=='farm':
  		val = random.randint(10, 20)
  		request.session['money']+= val
  		request.session['activity'] = "Entered the farm and got " + str(val) + " gold. "  + str(datetime.datetime.now()) + "\n" + request.session['activity']
  	if value=='cave':
  		val = random.randint(5, 10)
  		request.session['money']+= val
  		request.session['activity'] = "Entered the cave and got " + str(val) + " gold. "  + str(datetime.datetime.now()) + "\n" + request.session['activity']
  	if value=='house':
  		val = random.randint(2, 5)
  		request.session['money']+= val
  		request.session['activity'] = "Entered the house and got " + str(val) + " gold. "  + str(datetime.datetime.now()) + "\n" + request.session['activity']
  	if value=='casino':
  		val = random.randint(-50, 50)
  		request.session['money']+= val
  		request.session['activity'] = "Entered the casino and got " + str(val) + " gold. "  + str(datetime.datetime.now()) + "\n" + request.session['activity']

  	return redirect("/ninjagoldapp")
  # return render_template("index.html", money=request.session['money'], activity=request.session['activity'])