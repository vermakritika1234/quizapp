from typing import Coroutine
from django.db.models.query_utils import Q
from django.shortcuts import render,redirect
from .models import Show_Data, User,QuesModel
from django.contrib import messages

from django.contrib.auth import authenticate,login
# Create your views here.


def index(request):
    if request.method =="POST":
        username = request.POST['username']       
        password = request.POST['password']
        user = User(username=username,password=password)
        user.save()
        messages.success(request,f'Hello! {user.username}, You id have been successfully created !!!')
        return redirect('/login')
    else:
        return render(request, 'index.html')

def user_login(request):
    if request.method=="POST":
        m = User.objects.filter(username=request.POST['username'])
        try:
            if m[0].password == request.POST['password']:
                request.session['username'] = m[0].username
               
                messages.success(request,"you have been successfully logged in")
                return redirect('/dashboard')
        except User.DoesNotExist:
            messages.success(request,'Invalid credentials!!!')
            return render(request,'login.html')
                            
    return render(request, 'login.html')
           

def dashboard(request): 
    print('request.session-------',request.session['username'])   
    if request.method =="POST":    
        # print(request.POST.get(q.question))
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        
        user = User.objects.filter(username=request.session['username']).update(score=score)
        # user.save()
        return render(request,'results.html',context)


    else:
        questions=QuesModel.objects.all()
        return render(request, 'dashboard.html',{"questions":questions})

# def dashboard(request):
#     if request.method=="POST":
#         questions = QuesModel.objects.all()
#         score=0
#         wrong=0
#         correct=0
#         total=0
#         for q in questions:            
#             total+=1
#             print(request.POST.get(q.question))
#             print(q.ans)
#             print()
#             if q.ans == request.POST.get('q.question'):
#                 print('ansdfkjfodijf---------------',q.ans)
#                 score+=10
#                 correct+=1
#                 print('score------',score)
#             else:
#                 wrong+=1
#             print('print the dasboard ansewer score-----')
#             context = {
#             'score':score,
            
#              'correct':correct,
#              'wrong':wrong,
#              'total':total
#          }
#         return redirect('results',context)            
#     else:
#         questions=QuesModel.objects.all()
#         return render(request,'dashboard.html',{"questions":questions})

def results(request):    
    if request.method =="POST":
        
        username = request.POST['username']
        score = request.POST['score']
        percent = request.POST['percent']
        correct = request.POST['correct']
        wrong = request.POST['wrong']
        total = request.POST['total']
        data =Show_Data(username=username,score=score,percent=percent,correct=correct,wrong=wrong,total=total)
        data.save()
        return render(request, 'results.html')