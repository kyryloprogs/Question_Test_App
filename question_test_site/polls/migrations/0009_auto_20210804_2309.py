# Generated by Django 3.2.5 on 2021-08-04 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_completedtest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testquestions',
            name='question',
        ),
        migrations.RemoveField(
            model_name='testquestions',
            name='test',
        ),
        migrations.RemoveField(
            model_name='test',
            name='questions',
        ),
        migrations.DeleteModel(
            name='CompletedTest',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='TestQuestions',
        ),
    ]
