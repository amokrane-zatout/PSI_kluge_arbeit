from django.urls import  path

from . import views

from django.contrib import admin
app_name = 'Kluge_arbeit'
urlpatterns = [



    path('', views.login, name='login'),
    path('admin/', admin.site.urls),

    path('<int:utilisateur_id>/index', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('<int:utilisateur_id>/table', views.table, name='table'),
    path('chapitre', views.chapitre, name='chapitre'),
    path('<int:utilisateur_id>/addMatiere', views.addMatiere, name='addMatiere'),
    path('<int:utilisateur_id>/<int:matiere_id>/addChapitre', views.addChapitre, name='addChapitre'),
    path('<int:utilisateur_id>/<int:matiere_id>/modifMatiere', views.modifMatiere, name='modifMatiere'),
    path('<int:utilisateur_id>/<int:matiere_id>/supprimMatiere', views.supprimMatiere, name='supprimMatiere'),
    path('<int:chapitre_id>/modifChapitre', views.modifChapitre, name='modifChapitre'),
    path('<int:chapitre_id>/supprimChapitre', views.supprimChapitre, name='supprimChapitre'),
    path('timer', views.timer, name='timer'),
    path('feedBack', views.feedBack, name='feedback'),
    path('abandonSeance', views.abandonSeance, name='abandonSeance'),
]