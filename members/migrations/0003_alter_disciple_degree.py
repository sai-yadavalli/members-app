# Generated by Django 4.2.13 on 2024-06-10 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_student_degree_alter_student_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciple',
            name='degree',
            field=models.CharField(choices=[('Software Engineering', 'Software Engineering'), ('Computer Science', 'Computer Science'), ('Data Science', 'Data Science'), ('Business', 'Business'), ('Engineering', 'Engineering'), ('Architecture', 'Architecture')], default='degree', max_length=255),
        ),
    ]
