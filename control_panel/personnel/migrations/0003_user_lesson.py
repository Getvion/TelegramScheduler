# Generated by Django 4.1.7 on 2023-04-24 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shedule', '0003_remove_lesson_subject_delete_subject'),
        ('personnel', '0002_user_telegram_tag_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lesson',
            field=models.ManyToManyField(to='shedule.lesson'),
        ),
    ]