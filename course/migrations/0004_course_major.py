# Generated by Django 4.0.3 on 2022-05-05 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_alter_student_user'),
        ('course', '0003_course_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='major',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.major'),
        ),
    ]