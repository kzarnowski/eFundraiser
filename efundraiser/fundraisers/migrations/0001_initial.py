# Generated by Django 4.0.3 on 2022-03-04 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fundraiser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=2000)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('amount_to_raise', models.FloatField()),
                ('amount_raised', models.FloatField()),
            ],
        ),
    ]