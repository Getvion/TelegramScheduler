# Generated by Django 4.1.7 on 2023-04-24 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shedule', '0004_lessondate_alter_lesson_academic_couple_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='lesson',
            new_name='lesson_date',
        ),
    ]