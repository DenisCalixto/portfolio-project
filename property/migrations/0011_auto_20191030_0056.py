# Generated by Django 2.0.2 on 2019-10-30 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20191027_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='InspectionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('status', models.CharField(blank=True, max_length=16, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InspectionSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('inspection', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sections', to='property.Inspection')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='inspectiontemplateitem',
            name='inspection_section',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='property.InspectionTemplateSection'),
        ),
        migrations.AddField(
            model_name='inspectionitem',
            name='inspection_section',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='property.InspectionSection'),
        ),
    ]
