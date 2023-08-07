from django.urls import path

from .views import(
    BlogList,
    BlogDetail,
    BlogCreate,
    BlogUpdate,
    BlogDelete,
    SearchView,
)


urlpatterns = [
    path('', BlogList.as_view(), name = 'blog_list'),
    path('<int:pk>', BlogDetail.as_view(), name = 'blog_detail'),
    path('new/', BlogCreate.as_view(), name = 'blog_new'), 
    path('<int:pk>/update', BlogUpdate.as_view(), name = 'blog_update'),
    path('<int:pk>/delete', BlogDelete.as_view(), name = 'blog_delete'),
    path('search/', SearchView.as_view(), name = 'search_blogs'),
]
