# Generated by Django 4.2.13 on 2024-06-10 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_disciple_degree'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='degree',
            new_name='college_degree',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='year',
            new_name='enrollment_year',
        ),
    ]
