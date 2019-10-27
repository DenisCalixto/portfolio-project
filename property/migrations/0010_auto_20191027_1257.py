# Generated by Django 2.0.2 on 2019-10-27 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20191024_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='InspectionTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('property_type', models.CharField(blank=True, choices=[('PL', 'Place'), ('CA', 'Car'), ('EQ', 'Equipment')], max_length=2, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InspectionTemplateItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InspectionTemplateSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('inspection_template', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sections', to='property.InspectionTemplate')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='inspectiontemplateitem',
            name='inspection_section',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subsections', to='property.InspectionTemplateSection'),
        ),
    ]
