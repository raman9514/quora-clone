# Generated by Django 5.2 on 2025-04-08 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0002_alter_question_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.TextField(blank=True, null=True),
        ),
    ]
