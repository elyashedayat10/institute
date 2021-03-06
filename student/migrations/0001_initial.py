# Generated by Django 4.0.3 on 2022-04-16 21:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import extenstion.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("institute", "__first__"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Grade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=125)),
                ("slug", models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("father_name", models.CharField(max_length=125)),
                ("father_phone_number", extenstion.utils.CustomCharField()),
                ("mother_phone_numer", extenstion.utils.CustomCharField()),
                ("home_number", models.CharField(max_length=10)),
                (
                    "profile",
                    models.ImageField(upload_to=extenstion.utils.get_file_path),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("پسر", "پسر"), ("دختر", "دخنر")], max_length=4
                    ),
                ),
                ("grade", models.ManyToManyField(to="student.grade")),
                (
                    "institute",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="students",
                        to="institute.institute",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
