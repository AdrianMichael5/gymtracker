# Generated by Django 5.1.1 on 2024-09-27 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=254)),
                ('Gender', models.CharField(max_length=25)),
                ('PhoneNumber', models.CharField(max_length=12)),
                ('DOB', models.CharField(max_length=55)),
                ('SelectMembershipplan', models.CharField(max_length=200)),
                ('SelectTrainer', models.CharField(max_length=55)),
                ('Reference', models.CharField(max_length=55)),
                ('Adress', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SelectMembershipPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=185)),
                ('price', models.IntegerField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('gender', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=25)),
                ('salary', models.IntegerField(max_length=25)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
