from django.conf.urls import url
from first_app import views

app_name = 'first_app'
urlpatterns = [
    # url(r'^$', views.users_sign_up, name='users_sign_up'),
    # url(r'^$', views.users, name='users'),
    url(r'^index', views.index_five, name="index_five"),
    url(r'^other/$', views.other_four, name="other_four"),
    url(r'^relative/$', views.relative_four, name="relative_four"),

    url(r'^register/', views.register_five, name='register_five'),
    url(r'^user_login/$',views.user_login,name='user_login')

]
