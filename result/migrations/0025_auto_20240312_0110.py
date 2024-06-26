# pylint: disable-all
# Generated by Django 3.2.23 on 2024-03-12 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0024_auto_20240310_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='level',
            field=models.CharField(choices=[('TUTORS', 'TUTORS'), ('GRADE R', 'GRADE R'), ('GRADE 1', 'GRADE 1'), ('GRADE 2', 'GRADE 2'), ('GRADE 3', 'GRADE 3'), ('GRADE 4', 'GRADE 4'), ('GRADE 5', 'GRADE 5'), ('GRADE 6', 'GRADE 6'), ('GRADE 7', 'GRADE 7'), ('GRADE 8', 'GRADE 8'), ('GRADE 9', 'GRADE 9'), ('GRADE 10', 'GRADE 10'), ('GRADE 11', 'GRADE 11'), ('GRADE 12', 'GRADE 12')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='takencourse',
            name='comment',
            field=models.CharField(blank=True, choices=[(' 12/03/24', ' 12/03/24'), ('* 12/03/24', '* 12/03/24')], max_length=200),
        ),
    ]
