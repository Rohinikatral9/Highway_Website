# Generated by Django 4.2.3 on 2023-07-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_maintenance_expenses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('joiningdate', models.CharField(max_length=50)),
                ('worklocation', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]
