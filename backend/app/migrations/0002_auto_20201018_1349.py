# Generated by Django 3.1.1 on 2020-10-18 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='book',
        ),
        migrations.AddField(
            model_name='favorite',
            name='posting',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='FavoritedPost', to='app.posting', verbose_name='FavoritedPost'),
            preserve_default=False,
        ),
    ]
