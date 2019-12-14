# Generated by Django 3.0 on 2019-12-10 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('framework', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]