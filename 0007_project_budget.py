# Generated by Django 4.2.3 on 2023-07-22 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='budget',
            field=models.CharField(default=True, max_length=50, null=True),
        ),
    ]
