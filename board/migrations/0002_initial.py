# Generated by Django 4.0.1 on 2022-02-09 04:45

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
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='column',
            name='kanban',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.kanban'),
        ),
        migrations.AddField(
            model_name='card',
            name='column',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.column'),
        ),
    ]
