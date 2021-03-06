# Generated by Django 2.0.2 on 2019-10-31 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20191030_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspectionfile',
            name='inspection',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inspection_files', to='property.Inspection'),
        ),
        migrations.AlterField(
            model_name='inspectionfile',
            name='inspection_item',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_files', to='property.InspectionItem'),
        ),
        migrations.AlterField(
            model_name='inspectionitem',
            name='inspection_section',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='property.InspectionSection'),
        ),
        migrations.AlterField(
            model_name='inspectionsection',
            name='inspection',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='property.Inspection'),
        ),
    ]
