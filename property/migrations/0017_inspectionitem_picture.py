# Generated by Django 2.0.2 on 2019-11-19 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20191115_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspectionitem',
            name='picture',
            field=models.ImageField(null=True, upload_to='inspections_files/'),
        ),
    ]
