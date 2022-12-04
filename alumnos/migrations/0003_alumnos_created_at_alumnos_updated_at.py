# Generated by Django 4.1.3 on 2022-12-04 03:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0002_alter_alumnos_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumnos',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]