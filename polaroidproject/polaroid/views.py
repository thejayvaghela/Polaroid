import django
from django.shortcuts import redirect, render
from .models import User, Post, Friend, Like
from django.http.response import HttpResponse, HttpResponseRedirect
from datetime import date, datetime
from django.core.files.storage import FileSystemStorage
from django.http import request
from django.db.models import Q
from django.contrib.auth.hashers import check_password, make_password
from django.core.mail import send_mail
from django.conf import settings
import secrets

def signup(request):
    return render(request, 'signup.html')

def signup_auth(request):
    if request.method == "POST":
        fname=request.POST.get("first_name")
        lname=request.POST.get("last_name")
        email=request.POST.get("your_email")
        password=request.POST.get("password")
        hashed_p=make_password(password)
        dob=request.POST.get("dob")
        if dob == " " or dob == "":
            dob=date(2000, 1, 1)
        gender=request.POST.get("gender")
        country=request.POST.get("country")
        state=request.POST.get("state")
        city=request.POST.get("city")
        phone=request.POST.get("phone")
        profilepic=request.FILES.get("profilepic")
        u=User(first_name=fname,last_name=lname,user_email=email,password=hashed_p,dob=dob,gender=gender,country=country,state=state,city=city,phone=phone,profilepic=profilepic)
        try:
            u_email=User.objects.get(user_email=email)
            return HttpResponse("Email Already Exists")
        except:
            u.save()
            request.session['email']=u.user_email
            request.session['first_name']=u.first_name
            request.session['last_name']=u.last_name
            request.session['dob']=str(u.dob)
            request.session['city']=u.city
            request.session['state']=u.state
            request.session['country']=u.country
            request.session['phone']=str(u.phone)
            #return HttpResponseRedirect('/home/')
            return HttpResponseRedirect('/otpverficationpage/')

def otpverficationpage(request):
    u=User.objects.get(user_email=request.session['email'])
    global otp
    secretsgen=secrets.SystemRandom()
    otp=secretsgen.randrange(100000,999999)
    otpsubject="Welcome to Polaroid"
    otpbody="Thank You! For registration. Here is your OTP: %a" %(otp)
    send_mail(otpsubject, otpbody, settings.EMAIL_HOST_USER, [u.user_email], fail_silently=False)
    return render(request, 'otpverfication.html')

def otpverfication(request):
    u=User.objects.get(user_email=request.session['email'])
    otp_entered=request.POST.get("otp_entered")
    if otp_entered == str(otp):
        u.verified=True
        u.save()
        return HttpResponseRedirect('/home/')
    else:
        u.delete()
        return HttpResponse("Invalid OTP Entered")

def login(request):
    return render(request, 'login.html')

def login_auth(request):
    email=request.POST.get("your_email")
    password=request.POST.get("password")
    try:
        u=User.objects.get(user_email=email)
        if email == u.user_email and check_password(password,u.password):
            request.session['email']=u.user_email
            request.session['first_name']=u.first_name
            request.session['last_name']=u.last_name
            request.session['dob']=str(u.dob)
            request.session['city']=u.city
            request.session['state']=u.state
            request.session['country']=u.country
            request.session['phone']=str(u.phone)
            return HttpResponseRedirect('/home/')
        else:
            return HttpResponse("Invalid Login details.")
    except:
        return HttpResponse("Invalid Login details")

def home(request):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        all_friends=Friend.objects.filter(Q(user1=User.objects.get(user_email=request.session['email'])), Q(friends=True))
        #friends1=Friend.objects.filter(user1=u.user_email, friends=True, request_pending=False)
        #friends2=Friend.objects.filter(user2=u.user_email, friends=True, request_pending=False)
        allposts_mine=Post.objects.filter(user_email=u.user_email)
        allposts=Post.objects.all()
        all_requests=Friend.objects.filter(~Q(request_from=u.user_email), Q(user1=u.user_email), Q(request_pending=True), Q(friends=False))
        all_requests_count=Friend.objects.filter(~Q(request_from=u.user_email), Q(user1=u.user_email), Q(request_pending=True), Q(friends=False)).count()
        all_friends_count=Friend.objects.filter(Q(user1=User.objects.get(user_email=request.session['email'])), Q(friends=True)).count()
        context={
            'email':u.user_email,
            'first_name':u.first_name,
            'last_name':u.last_name,
            'dob':u.dob.strftime('%b %d'),
            'city':u.city,
            'state':u.state,
            'country':u.country,
            'phone':u.phone,
            'uploaded_pic_url': u.profilepic,
            'allposts_mine':allposts_mine.reverse().order_by('posttime'),
            'allposts':allposts.reverse().order_by('posttime'),
            'all_requests':all_requests,
            'all_requests_count':all_requests_count,
            'all_friends_count':all_friends_count,
            'all_friends':all_friends,
        }
        return render(request,'home.html',context)

def logout(request):
    request.session['email']=None
    return HttpResponseRedirect('/login/')

def searchpage(request):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        all_friends_count=Friend.objects.filter(Q(user1=User.objects.get(user_email=request.session['email'])), Q(friends=True)).count()
        context={
            'uploaded_pic_url': u.profilepic,
            'all_friends_count':all_friends_count,
        }
        return render(request, 'search_results.html', context)

def searchresults(request):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        all_friends_count=Friend.objects.filter(Q(user1=User.objects.get(user_email=request.session['email'])), Q(friends=True)).count()
        if request.method=="POST":
            search=request.POST.get("search")
            search_users=User.objects.filter(Q(first_name=search) | Q(last_name=search))
        context={
            'fname':search_users,
            'uploaded_pic_url': u.profilepic,
            'current_user_email':u.user_email,
            'all_friends_count':all_friends_count,
        }
        return render(request, 'search_results.html', context)


'''
    flag1=False
    flag2=False
    try:
        temp1 = Friend.objects.get(request_to=User.objects.get(user_email=request_to), request_from=User.objects.get(user_email=request.session['email']))
    except:
        flag1=True
    try:
        temp2 = Friend.objects.get(request_from=User.objects.get(user_email=request_to),request_to=User.objects.get(user_email=request.session['email']))
    except:
        flag2=True
    if flag1==True and flag2==True:
    
    else:
        return HttpResponse("Already sent")
    
    '''


def addfriend(request, user2):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        f1=Friend(user1=User.objects.get(user_email=request.session['email']), user2=User.objects.get(user_email=user2), request_from=User.objects.get(user_email=request.session['email']))
        f1.request_pending=True
        f1.save()
        f2=Friend(user1=User.objects.get(user_email=user2), user2=User.objects.get(user_email=request.session['email']), request_from=User.objects.get(user_email=request.session['email']))
        f2.request_pending=True
        f2.save()
        return HttpResponseRedirect('/otherusers/%s/'% user2)
    
def accept_request(request, user2):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        o=User.objects.get(user_email=user2)
        f1=Friend.objects.filter(Q(user1=u.user_email) | Q(user1=o.user_email), Q(user2=u.user_email) | Q(user2=o.user_email), Q(request_from=o.user_email), Q(request_pending=True), Q(friends=False)).update(request_pending=False, friends=True)
        f2=Friend.objects.filter(Q(user1=u.user_email) | Q(user1=o.user_email), Q(user2=u.user_email) | Q(user2=o.user_email), Q(request_from=u.user_email), Q(request_pending=True), Q(friends=False)).update(request_pending=False, friends=True)
        return HttpResponseRedirect('/otherusers/%s/'% user2)

def accept_request_from_home(request, user2):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        o=User.objects.get(user_email=user2)
        f1=Friend.objects.filter(Q(user1=u.user_email) | Q(user1=o.user_email), Q(user2=u.user_email) | Q(user2=o.user_email), Q(request_from=o.user_email), Q(request_pending=True), Q(friends=False)).update(request_pending=False, friends=True)
        f2=Friend.objects.filter(Q(user1=u.user_email) | Q(user1=o.user_email), Q(user2=u.user_email) | Q(user2=o.user_email), Q(request_from=u.user_email), Q(request_pending=True), Q(friends=False)).update(request_pending=False, friends=True)
        return HttpResponseRedirect('/home/')

def decline_request(request, user2):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        o=User.objects.get(user_email=user2)
        f1=Friend.objects.filter(Q(user1=u.user_email) | Q(user1=o.user_email), Q(user2=u.user_email) | Q(user2=o.user_email), Q(request_from=o.user_email), Q(request_pending=True), Q(friends=False)).delete()
        f2=Friend.objects.filter(Q(user1=u.user_email) | Q(user1=o.user_email), Q(user2=u.user_email) | Q(user2=o.user_email), Q(request_from=u.user_email), Q(request_pending=True), Q(friends=False)).delete()
        return HttpResponseRedirect('/otherusers/%s/'% user2)

def decline_request_from_home(request, user2):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        o=User.objects.get(user_email=user2)
        f1=Friend.objects.filter(Q(user1=u.user_email) | Q(user1=o.user_email), Q(user2=u.user_email) | Q(user2=o.user_email), Q(request_from=o.user_email), Q(request_pending=True), Q(friends=False)).delete()
        f2=Friend.objects.filter(Q(user1=u.user_email) | Q(user1=o.user_email), Q(user2=u.user_email) | Q(user2=o.user_email), Q(request_from=u.user_email), Q(request_pending=True), Q(friends=False)).delete()
        return HttpResponseRedirect('/home/')

def unfriend(request, user2):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        o=User.objects.get(user_email=user2)
        f1=Friend.objects.filter(Q(user1=u.user_email) | Q(user1=o.user_email), Q(user2=u.user_email) | Q(user2=o.user_email), Q(request_from=o.user_email), Q(request_pending=False), Q(friends=True)).delete()
        f2=Friend.objects.filter(Q(user1=u.user_email) | Q(user1=o.user_email), Q(user2=u.user_email) | Q(user2=o.user_email), Q(request_from=u.user_email), Q(request_pending=False), Q(friends=True)).delete()
        return HttpResponseRedirect('/otherusers/%s/'% user2)

def all_friends(request):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        all_friends=Friend.objects.filter(Q(user1=User.objects.get(user_email=request.session['email'])), Q(friends=True))
        all_friends_count=Friend.objects.filter(Q(user1=User.objects.get(user_email=request.session['email'])), Q(friends=True)).count()
        context={
            'uploaded_pic_url': u.profilepic,
            'all_friends':all_friends,
            'all_friends_count':all_friends_count,
        }
        return render(request,'allfriends.html',context)

def other_users_all_friends(request, user2):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        o=User.objects.get(user_email=user2)
        all_friends_count=Friend.objects.filter(Q(user1=User.objects.get(user_email=request.session['email'])), Q(friends=True)).count()
        other_users_all_friends=Friend.objects.filter(Q(user1=User.objects.get(user_email=user2)), Q(friends=True))
        other_users_all_friends_count=Friend.objects.filter(Q(user1=User.objects.get(user_email=user2)), Q(friends=True)).count()
        context={
            'uploaded_pic_url': u.profilepic,
            'current_user_email':u.user_email,
            'all_friends_count':all_friends_count,
            'other_users_all_friends':other_users_all_friends,
            'other_users_all_friends_count':other_users_all_friends_count,
        }
        return render(request,'otherusersallfriends.html',context)

def userprofile(request):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        allposts=Post.objects.filter(user_email=u.user_email).reverse().order_by('posttime')
        postcount=Post.objects.filter(user_email=u.user_email).count()
        all_friends_count=Friend.objects.filter(Q(user1=User.objects.get(user_email=request.session['email'])), Q(friends=True)).count()
        context={
            'first_name':u.first_name,
            'last_name':u.last_name,
            'dob':u.dob.strftime('%b %d'),
            'city':u.city,
            'state':u.state,
            'country':u.country,
            'phone':u.phone,
            'uploaded_pic_url': u.profilepic,
            'email':u.user_email,
            'bio':u.bio,
            'allposts':allposts,
            'postcount':postcount,
            'all_friends_count':all_friends_count,
        }
        return render(request, 'userprofile.html', context)

def otherusers(request, user2):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        o=User.objects.get(user_email=user2)
        otheruserposts=Post.objects.filter(user_email=o.user_email).reverse().order_by('posttime')
        otheruserpostscount=Post.objects.filter(user_email=o.user_email).count()
        request_sent_user1=Friend.objects.filter(user1=u.user_email, user2=o.user_email, request_pending=True, request_from=u.user_email)
        request_sent_user2=Friend.objects.filter(user1=u.user_email, user2=o.user_email, request_pending=True, request_from=o.user_email)
        friends1=Friend.objects.filter(user1=u.user_email, user2=o.user_email, friends=True, request_pending=False)
        friends2=Friend.objects.filter(user1=o.user_email, user2=u.user_email, friends=True, request_pending=False)
        all_friends_count=Friend.objects.filter(Q(user1=User.objects.get(user_email=request.session['email'])), Q(friends=True)).count()
        other_users_friends_count=Friend.objects.filter(Q(user2=User.objects.get(user_email=user2)), Q(friends=True)).count()
        context={
            'myemail':u.user_email,
            'uploaded_pic_url':u.profilepic,
            'first_name':o.first_name,
            'last_name':o.last_name,
            'dob':o.dob.strftime('%b %d'),
            'city':o.city,
            'state':o.state,
            'country':o.country,
            'phone':o.phone,
            'otheruserprofilepic': o.profilepic,
            'email':o.user_email,
            'bio':o.bio,
            'otheruserposts':otheruserposts,
            'otheruserpostscount':otheruserpostscount,
            'request_sent_user1':request_sent_user1,
            'request_sent_user2':request_sent_user2,
            'friends1':friends1,
            'friends2':friends2,
            'all_friends_count':all_friends_count,
            'other_users_friends_count':other_users_friends_count,
        }
        return render(request, 'otherusers.html', context)



def edituserbiopage(request):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        all_friends_count=Friend.objects.filter(Q(user1=User.objects.get(user_email=request.session['email'])), Q(friends=True)).count()
        context={
            'uploaded_pic_url': u.profilepic,
            'all_friends_count':all_friends_count,
        }
        return render(request, 'editbio.html', context)

def edituserbio(request):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        u.bio=request.POST.get("bio")
        u.save()
        return HttpResponseRedirect('/userprofile/')

def edituserprofilepicpage(request):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        all_friends_count=Friend.objects.filter(Q(user1=User.objects.get(user_email=request.session['email'])), Q(friends=True)).count()
        context={
            'uploaded_pic_url': u.profilepic,
            'all_friends_count':all_friends_count,
        }
        return render(request, 'editprofilepic.html', context)

def edituserprofilepic(request):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        u.profilepic=request.FILES.get("profilepic")
        u.save()
        return HttpResponseRedirect('/userprofile/')

def edituserprofilepage(request):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        all_friends_count=Friend.objects.filter(Q(user1=User.objects.get(user_email=request.session['email'])), Q(friends=True)).count()
        context={
            'uploaded_pic_url': u.profilepic,
            'email':u.user_email,
            'all_friends_count':all_friends_count,
        }
        return render(request, 'editprofile.html', context)

def editprofile(request):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        u.first_name=request.POST.get("first_name")
        u.last_name=request.POST.get("last_name")
        u.dob=request.POST.get("dob")
        if u.dob == " " or u.dob == "":
            u.dob=date(2000, 1, 1)
        u.gender=request.POST.get("gender")
        u.country=request.POST.get("country")
        u.state=request.POST.get("state")
        u.city=request.POST.get("city")
        u.phone=request.POST.get("phone")
        u.save()
        return HttpResponseRedirect('/userprofile/')

def addpost(request):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        user_email=request.session['email']
        postpic=request.FILES.get("postpic")
        postcaption=request.POST.get("postcaption")
        p=Post(postpic=postpic, postcaption=postcaption, user_email=User.objects.get(user_email=user_email))
        p.save()
        return HttpResponseRedirect('/home/')

def deletepost(request, postid):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        p=Post.objects.filter(postid=postid)
        p.delete()
        return HttpResponseRedirect('/userprofile/')


def like(request, postid, post_owner):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        p=Post.objects.get(postid=postid)
        #print("Posts:")
        #print(p.postid)
        l=p.like_set.create(userid=User.objects.get(user_email=request.session['email']))
        if post_owner == u.user_email:
            return HttpResponseRedirect('/userprofile/')
        return HttpResponseRedirect('/otherusers/%s/'% post_owner)

def likefromhome(request, postid, post_owner):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        p=Post.objects.get(postid=postid)
        #print("Posts:")
        #print(p.postid)
        l=p.like_set.create(userid=User.objects.get(user_email=request.session['email']))
        return HttpResponseRedirect('/home/')

def dislike(request, postid, post_owner):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        p=Post.objects.get(postid=postid)
        #print("Posts:")
        #print(p.postid)
        l=p.like_set.filter(userid=User.objects.get(user_email=request.session['email'])).delete()
        if post_owner == u.user_email:
            return HttpResponseRedirect('/userprofile/')
        return HttpResponseRedirect('/otherusers/%s/'% post_owner)

def dislikefromhome(request, postid, post_owner):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        p=Post.objects.get(postid=postid)
        #print("Posts:")
        #print(p.postid)
        l=p.like_set.filter(userid=User.objects.get(user_email=request.session['email'])).delete()
        return HttpResponseRedirect('/home/')

def addcomment(request, postid, post_owner):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        p=Post.objects.get(postid=postid)
        content=request.POST.get("content")
        l=p.comment_set.create(userid=User.objects.get(user_email=request.session['email']), content=content)
        if post_owner == u.user_email:
            return HttpResponseRedirect('/userprofile/')        
        return HttpResponseRedirect('/otherusers/%s/'% post_owner)

def addcommentfromhome(request, postid, post_owner):
    u=User.objects.get(user_email=request.session['email'])
    if u.verified==False:
        u.delete()
        return HttpResponse("Verification Failed. Please Create Your Account Again.")
    else:
        p=Post.objects.get(postid=postid)
        content=request.POST.get("content")
        l=p.comment_set.create(userid=User.objects.get(user_email=request.session['email']), content=content)
        return HttpResponseRedirect('/home/')