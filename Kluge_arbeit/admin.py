from django.contrib import admin

from .models import Utilisateur
admin.site.register(Utilisateur)

from .models import Matiere
admin.site.register(Matiere)

from .models import Seance
admin.site.register(Seance)

from .models import Chapitre
admin.site.register(Chapitre)
