# Generated by Django 4.0.1 on 2022-02-16 01:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('board', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='kanban',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kanbans', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='column',
            name='kanban',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='board.kanban'),
        ),
        migrations.AddField(
            model_name='column',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='card',
            name='column',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='board.column'),
        ),
        migrations.AddField(
            model_name='card',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
