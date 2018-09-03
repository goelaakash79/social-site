from django.conf.urls import url
from .views import login, add_post, get_posts, like, dislike

urlpatterns = [
    url(r'^login/$',login),
    url(r'^post/$',add_post),
    url(r'^feeds/$',get_posts),
    url(r'^like/$',like),
    url(r'^dislike/$',dislike),

]
