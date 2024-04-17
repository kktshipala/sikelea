# Generated by Django 3.2.23 on 2024-04-17 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_student_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(choices=[('LEARNERSHIP', 'LEARNERSHIP'), ('DIPLOMA', 'DIPLOMA'), ('DEGREE', 'DEGREE'), ('HONOURS', 'HONOURS'), ('MASTERS', 'MASTERS'), ('PHD', 'PHD')], max_length=25, null=True),
        ),
    ]
