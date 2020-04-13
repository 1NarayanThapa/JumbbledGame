from django.shortcuts import render
from django.http import HttpResponse
import random
words=[
    "python",
    "exhibition",
    "problem",
    "intelligence",
    "poudel",
    "system",
    "computer",
    "robotics",
    "complex",
    "performance",
    "coffee",
    "people",
    "computer",
    "cablecar",
    "solarsystem",
    "windmill",
    "international",
    "programming",
    "academia",
    "django",
    "entertainment",
    "android",
    "animation",
    "photography",

]
def rword():
     global jword
     global word
     word=random.choice(words)
     jum=random.sample(word,len(word))
     jword="".join(jum)
msg = ""





# Create your views here.
def homepage(request):
    # return HttpResponse("THIS IS HOME PAGE")
    # return render(request,'index.html')
    rword()
    global jword,msg
    # return render(request,'index.html',{'msg':"this is the custom message"})
    # return render(request,'index.html',{'jum_word':jword})
    return render(request,'index.html',{'jum_word': jword,'msg': msg})



def checkans(request):
    global word,msg,jword
    user_ans=request.GET['answer']
    # print(user_ans)
    if user_ans==word:
        msg= "you guess the correct word"
        homepage(request)
    else:
        msg="its wrong .try again"
    return render(request,'index.html',{'jum_word':jword,'msg':msg})


