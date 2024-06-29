# Generated by Django 3.1.6 on 2023-10-14 01:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chores', '0003_chore_chore_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='chore',
            name='assign_chore_to',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
