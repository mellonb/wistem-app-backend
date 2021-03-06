# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-28 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20171210_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='applicant_type',
            field=models.ManyToManyField(blank=True, to='api.ApplicantType'),
        ),
        migrations.AlterField(
            model_name='award',
            name='award_purpose',
            field=models.ManyToManyField(blank=True, to='api.AwardPurpose'),
        ),
        migrations.AlterField(
            model_name='award',
            name='stem_field',
            field=models.ManyToManyField(blank=True, to='api.StemField'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='areas_of_interest',
            field=models.ManyToManyField(blank=True, to='api.AreaOfInterest'),
        ),
    ]
