# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-29 16:56
from __future__ import unicode_literals

from django.db import migrations


def load_branches(apps, schema_editor):
	Branch =  apps.get_model('company', 'Branch')
	
	Branch(name='CO', degree='BTECH').save()
	Branch(name='ME', degree='BTECH').save()
	Branch(name='CE', degree='BTECH').save()
	Branch(name='EE', degree='BTECH').save()
	Branch(name='CH', degree='BTECH').save()
	Branch(name='EC', degree='BTECH').save()

	Branch(name='CO', degree='MTECH').save()
	Branch(name='ME', degree='MTECH').save()
	Branch(name='CE', degree='MTECH').save()
	Branch(name='EE', degree='MTECH').save()
	Branch(name='CH', degree='MTECH').save()
	Branch(name='EC', degree='MTECH').save()

	Branch(name='PHY', degree='MSC').save()
	Branch(name='CHEM', degree='MSC').save()
	Branch(name='MATH', degree='MSC').save()


def load_placement_categories(apps, schema_editor):
	PlacementCategory = apps.get_model('company', 'PlacementCategory')

	PlacementCategory(name='Super Dream', ctc_range='12 LPA +').save()
	PlacementCategory(name='A (Dream)', ctc_range='8-12 LPA').save()
	PlacementCategory(name='B', ctc_range='4-8 LPA').save()
	PlacementCategory(name='C', ctc_range='Less than 4 LPA').save()


def load_job_types(apps, schema_editor):
	JobType = apps.get_model('company', 'JobType')

	JobType(job_domain='C', job_type='Software/IT').save()
	JobType(job_domain='C', job_type='Automobile').save()
	JobType(job_domain='C', job_type='PSU').save()
	JobType(job_domain='C', job_type='Oil, Petroleum and Energy').save()
	JobType(job_domain='C', job_type='Civil and Infrastructure').save()
	JobType(job_domain='C', job_type='Manufacture or Production').save()
	JobType(job_domain='C', job_type='Academic Institutions').save()
	JobType(job_domain='C', job_type='Other').save()

	JobType(job_domain='N', job_type='Business Analyst').save()
	JobType(job_domain='N', job_type='Consultant').save()
	JobType(job_domain='N', job_type='Operations').save()
	JobType(job_domain='N', job_type='Sales and Marketing').save()
	JobType(job_domain='N', job_type='Finance').save()
	JobType(job_domain='N', job_type='Other').save()


def load_selection_procedures(apps, schema_editor):
	SelectionProcedure = apps.get_model('company', 'SelectionProcedure')

	SelectionProcedure(procedure='Pre Placement Talk').save()
	SelectionProcedure(procedure='Technical Test').save()
	SelectionProcedure(procedure='Aptitude Test').save()
	SelectionProcedure(procedure='Coding Test').save()
	SelectionProcedure(procedure='CGPA Based Shortlist').save()
	SelectionProcedure(procedure='Resume Based Shortlist').save()
	SelectionProcedure(procedure='Case Study').save()
	SelectionProcedure(procedure='Group Discussion').save()
	SelectionProcedure(procedure='Group Activity').save()
	SelectionProcedure(procedure='Student Presentation').save()
	SelectionProcedure(procedure='Technical Interview').save()
	SelectionProcedure(procedure='HR Interview').save()
	SelectionProcedure(procedure='Psychometric Test').save()
	SelectionProcedure(procedure='Medical Test').save()
	SelectionProcedure(procedure='Other').save()


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0015_job_resumes_required'),
    ]

    operations = [
    	migrations.RunPython(load_branches),
    	migrations.RunPython(load_placement_categories),
    	migrations.RunPython(load_job_types),
    	migrations.RunPython(load_selection_procedures),
    ]