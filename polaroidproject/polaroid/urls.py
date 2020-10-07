from django.urls import path
from django.conf.urls import include, url
from polaroid.views import accept_request, accept_request_from_home, addcomment, addcommentfromhome, addfriend, addpost, all_friends, decline_request, decline_request_from_home, deletepost, dislike, dislikefromhome, editprofile, edituserbio, edituserbiopage, edituserprofilepage, edituserprofilepic, edituserprofilepicpage, home, like, likefromhome, login, login_auth, logout, other_users_all_friends, otherusers, searchpage, searchresults, signup, signup_auth, unfriend, userprofile
from polaroid.views import otpverfication, otpverficationpage
#from django.templatetags.static import static
from django.conf.urls.static import static
from polaroidproject import settings

urlpatterns = [
    url('signup/$', signup),
    url('signup_auth/$', signup_auth),
    url('otpverfication/$', otpverfication),
    url('otpverficationpage/$', otpverficationpage),
    url('login/$', login),
    url('login_auth/$', login_auth),
    url('home/$', home),
    url('logout/$', logout),
    url('searchresults/$', searchresults),
    url('searchpage/$', searchpage),
    url('userprofile/$', userprofile),
    url('edituserbio/$', edituserbio),
    url('edituserbiopage/$', edituserbiopage),
    url('edituserprofilepic/$', edituserprofilepic),
    url('edituserprofilepicpage/$', edituserprofilepicpage),
    url('editprofile/$', editprofile),
    url('edituserprofilepage/$', edituserprofilepage),
    url('addpost/$', addpost),
    path('deletepost/<postid>/', deletepost),
    path('otherusers/<user2>/', otherusers),
    path('addfriend/<user2>/', addfriend),
    path('unfriend/<user2>/', unfriend),
    path('accept_request/<user2>/', accept_request),
    path('accept_request_from_home/<user2>/', accept_request_from_home),
    path('decline_request/<user2>/', decline_request),
    path('decline_request_from_home/<user2>/', decline_request_from_home),
    url('all_friends/$', all_friends),
    path('other_users_all_friends/<user2>/', other_users_all_friends),
    path('like/<postid>/<post_owner>/', like),
    path('likefromhome/<postid>/<post_owner>/', likefromhome),
    path('dislike/<postid>/<post_owner>/', dislike),
    path('dislikefromhome/<postid>/<post_owner>/', dislikefromhome),
    path('addcomment/<postid>/<post_owner>/', addcomment),
    path('addcommentfromhome/<postid>/<post_owner>/', addcommentfromhome),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

