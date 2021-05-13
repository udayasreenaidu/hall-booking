from django.urls import path
from HallBooking import views
from django.contrib.auth import views as v

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('src/',views.search,name="sc"),
	path('cnt/',views.contact,name="cn"),
	path('reg/',views.register,name="rg"),
	path('dashboard/',views.dashboard,name="dsh"),
	path('login/',v.LoginView.as_view(template_name="html/login.html"),name="lg"),
	path('logout/',v.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
	path('pfle/',views.prfle,name="pf"),
	path('updf/',views.updfple,name="upf"),
	path('bkn/',views.booknow,name="book"),


]