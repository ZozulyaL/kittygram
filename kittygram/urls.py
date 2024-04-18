# from django.urls import path

# from cats.views import cat_list

# urlpatterns = [
#    path('cats/', cat_list),
# ]

# # urls.py обновляем так как используем классы
# from django.urls import path

# from cats.views import APICat

# urlpatterns = [
#     path('cats/', APICat.as_view()),
# ] 


#обновляем так как используем дженерики высшего порядка
# from django.urls import path

# from cats.views import CatList, CatDetail

# urlpatterns = [
#     path('cats/', CatList.as_view()),
#     path('cats/<int:pk>/', CatDetail.as_view()),
# ] 

# обновляем код используем роутеры с вьюсетами
from rest_framework.routers import SimpleRouter

from django.urls import include, path

from cats.views import CatViewSet

# Создаётся роутер
router = SimpleRouter()
# Вызываем метод .register с нужными параметрами
router.register('cats', CatViewSet)
# В роутере можно зарегистрировать любое количество пар "URL, viewset":
# например
# router.register('owners', OwnerViewSet)
# Но нам это пока не нужно

urlpatterns = [
    # Все зарегистрированные в router пути доступны в router.urls
    # Включим их в головной urls.py
    path('', include(router.urls)),
]

#про basename надо помнить читать иногда сам автоматом создается а если через кверисет функцию то надо явно указать