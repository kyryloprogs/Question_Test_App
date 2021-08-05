# Generated by Django 3.2.5 on 2021-07-22 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_content_test_test_info'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='test',
            options={'ordering': ['-created_at'], 'verbose_name': 'Tests', 'verbose_name_plural': 'Tests'},
        ),
        migrations.AlterModelOptions(
            name='testquestions',
            options={'ordering': ['-question_number'], 'verbose_name': 'Test questions', 'verbose_name_plural': 'Test questions'},
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_number',
        ),
        migrations.RemoveField(
            model_name='test',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='testquestions',
            name='question_number',
            field=models.IntegerField(null=True),
        ),
    ]
