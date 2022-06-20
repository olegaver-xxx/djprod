"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from apps.blog.views import IndexView, ArtView, ArticleCreateView, ArticleUpdateView
from django.contrib.auth.views import LoginView, LogoutView
from apps.blog.views import signup


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('', IndexView.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name = "login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('create/', ArticleCreateView.as_view(), name="create"),
    path('edit/<int:pk>', ArticleUpdateView.as_view(), name="edit"),
    path('detail/<int:pk>', ArtView.as_view(), name = "detail"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)