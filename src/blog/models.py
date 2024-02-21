from django.db import models

# Create your models here.
class BlogPost(models.Model):
    # chaine de carectere de longuer définie, +argument de longeur de char
    # si on veut gérer les clé primaire à la place de Django :
    # title = models.CharField(max_length=100, primary_key=True) 
    # par défaut primary_key=False, et Django gère les id
    title = models.CharField(max_length=100) 
    # Un moyen d'afficher le titre de l'article dans l'url
    slug = models.SlugField()
    # Valeur par défaut, les articles ne seront pas publiés
    published = models.BooleanField(default=False)
    # date : DateField==date seule, DateTimeField==date&heur 
    # blank = pour permettre qu'il n'y ai aucune valeur par défaut, 
    # Ex : quand on ne sait pas quand sera publié l'article, 
    # !!! si False, je dois mettre un titre et/ou slug
    # précisé comme c'est une date que null=true
    date = models.DateField(blank=True, null=True)
    # 
    content = models.TextField()
    description = models.TextField()

