from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
#router.register(r'activity_dates', views.ActivityDatesViewSet.as_view(), base_name='activity_dates')
router.register(r'actividades_all', views.ActivityViewSet)
router.register(r'actividades_simple', views.CategoryItemViewSet, basename='categoryItem')
router.register(r'actividades', views.CategoryNestedItemViewSet, basename='categoryNestedItem')
# router.register(r'asistentes', views.AsistenteViewSet)
# router.register(r'profesores', views.ProfesorCategoryViewSet)
# router.register(r'sponsors', views.SponsorViewSet)
# router.register(r'anuncios', views.AnuncioViewSet)
urlpatterns = [
    path('', include(router.urls)),

]