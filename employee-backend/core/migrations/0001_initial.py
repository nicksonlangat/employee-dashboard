# Generated by Django 3.2 on 2021-04-19 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('department', models.CharField(max_length=20)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
    ]