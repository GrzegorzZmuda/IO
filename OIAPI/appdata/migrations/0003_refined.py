# Generated by Django 3.0.2 on 2020-01-18 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdata', '0002_auto_20200118_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refined',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rpm', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]