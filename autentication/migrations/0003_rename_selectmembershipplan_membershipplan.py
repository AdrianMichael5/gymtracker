# Generated by Django 5.1.1 on 2024-09-27 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autentication', '0002_enrollment_selectmembershipplan_trainer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SelectMembershipPlan',
            new_name='MembershipPlan',
        ),
    ]
