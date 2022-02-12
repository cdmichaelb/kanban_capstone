# Generated by Django 4.0.1 on 2022-02-12 04:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0005_alter_column_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='columns', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
