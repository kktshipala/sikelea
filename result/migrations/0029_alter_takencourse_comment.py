# Generated by Django 3.2.23 on 2024-04-21 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0028_auto_20240417_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takencourse',
            name='comment',
            field=models.CharField(blank=True, choices=[(' 21/04/24', ' 21/04/24'), ('* 21/04/24', '* 21/04/24')], max_length=200),
        ),
    ]
