# Generated by Django 2.0.1 on 2018-03-06 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Kluge_arbeit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matiere',
            name='utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Kluge_arbeit.Utilisateur'),
        ),
    ]