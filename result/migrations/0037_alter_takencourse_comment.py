# Generated by Django 3.2.23 on 2024-06-13 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0036_alter_takencourse_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takencourse',
            name='comment',
            field=models.CharField(blank=True, choices=[(' 13/06/24', ' 13/06/24'), ('* 13/06/24', '* 13/06/24')], max_length=200),
        ),
    ]