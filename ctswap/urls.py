"""
URL configuration for ctswap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
import base.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include("django.contrib.auth.urls")),
    path('', base.views.MyPosts.as_view(), name = 'home'),
    path('browse/', base.views.AllPosts.as_view(), name = 'allposts'),
    path('browse/appliances', base.views.AppliancesPosts.as_view(), name = 'applaincesposts'),
    path('browse/clothes', base.views.ClothesPosts.as_view(), name = 'clothesposts'),
    path('browse/education', base.views.EducationPosts.as_view(), name = 'educationposts'),
    path('browse/electronics', base.views.ElectronicsPosts.as_view(), name = 'electronicsposts'),
    path('browse/free', base.views.FreePosts.as_view(), name = 'freeposts'),
    path('browse/homeandgarden', base.views.HomeAndGardenPosts.as_view(), name = 'homeandgardenposts'),
    path('browse/miscellaneous', base.views.MiscellaneousPosts.as_view(), name = 'miscellaneousposts'),
    path('browse/music', base.views.MusicPosts.as_view(), name = 'musicposts'),
    path('browse/sports', base.views.SportsPosts.as_view(), name = 'sportsposts'),
    path('browse/vehicles', base.views.VehiclesPosts.as_view(), name = 'vehiclesposts'),
    path('api/', include('api.urls')),
    path('about/', TemplateView.as_view(template_name='about.html'), name = 'about'),
    path('post/', base.views.new_post, name = 'post'),
    path('update_post/<int:post_id>', base.views.update_post, name='update-post'),
    path('search/', base.views.search_posts, name = 'searchposts'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)