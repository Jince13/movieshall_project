# Generated by Django 5.0.3 on 2024-03-15 04:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieshallapp', '0003_alter_review_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='movieshallapp.addmovies'),
        ),
    ]