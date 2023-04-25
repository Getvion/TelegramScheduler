# Generated by Django 4.1.7 on 2023-04-24 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_user_chat_id'),
        ('shedule', '0003_remove_lesson_subject_delete_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='lesson',
            name='academic_couple',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shedule.academiccouple'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='group',
            field=models.ManyToManyField(to='students.group'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson',
            field=models.ManyToManyField(to='shedule.lessondate'),
        ),
    ]
