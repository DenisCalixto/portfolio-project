# Generated by Django 2.0.2 on 2019-10-31 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20191030_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inspectiontemplateitem',
            name='inspection_section',
        ),
    ]