from django.urls import path, include

from .views import (
    TestListView,
    test_results,
    test_results_info,
    test_run,
    thanks,
    search,
    find_by_date,
    register_request,
    login_request,
    switch_lang,
    lang
)
from django.utils.translation import gettext_lazy as _

app_name = 'tests'

urlpatterns = [
    path('', TestListView.as_view(), name="index"),
    path('<int:pk>', test_run, name="test_details"),
    path('completed', test_results, name="test_results"),
    path('completed/<int:pk>', test_results_info, name="test_results_info"),
    path('thanks', thanks, name="thanks"),
    path('search', search, name="search-text"),
    path('find_by_date', find_by_date, name="find_by_date"),
    path("register", register_request, name="register"),
    path("login", login_request, name="login_request"),
    # path('i18n/', include('django.conf.urls.i18n')),
    path('langswitch/', switch_lang),
    path('lng/<str:lang_code>', lang)
]

