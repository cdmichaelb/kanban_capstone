# Generated by Django 4.0.1 on 2022-02-12 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_alter_kanban_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]