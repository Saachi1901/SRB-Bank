# Generated by Django 3.2.4 on 2021-06-18 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='saachi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('amt', models.IntegerField(default=0)),
                ('userid', models.IntegerField(default=0)),
            ],
        ),
    ]
