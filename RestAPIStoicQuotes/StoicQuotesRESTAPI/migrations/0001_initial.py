# Generated by Django 3.0.4 on 2020-03-27 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoicQuotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('philosophers_name', models.CharField(max_length=255)),
                ('quotes', models.TextField()),
            ],
        ),
    ]
