# pylint: disable-all
# Generated by Django 3.2.23 on 2024-03-09 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_courseoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('GRADE 1-12', 'GRADE 1-12'), ('GRADE R', 'GRADE R'), ('GRADE 1', 'GRADE 1'), ('GRADE 2', 'GRADE 2'), ('GRADE 3', 'GRADE 3'), ('GRADE 4', 'GRADE 4'), ('GRADE 5', 'GRADE 5'), ('GRADE 6', 'GRADE 6'), ('GRADE 7', 'GRADE 7'), ('GRADE 8', 'GRADE 8'), ('GRADE 9', 'GRADE 9'), ('GRADE 10', 'GRADE 10'), ('GRADE 11', 'GRADE 11'), ('GRADE 12', 'GRADE 12')], max_length=25, null=True),
        ),
    ]
