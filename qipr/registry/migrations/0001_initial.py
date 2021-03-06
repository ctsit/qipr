# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 20:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import registry.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gatorlink', models.CharField(max_length=50, null=True)),
                ('http_verb', models.CharField(max_length=10)),
                ('ip', models.GenericIPAddressField()),
                ('request_body', models.TextField(null=True)),
                ('response_code', models.IntegerField(null=True)),
                ('time_requested', models.DateTimeField(auto_now_add=True)),
                ('time_responded', models.DateTimeField(auto_now=True)),
                ('url', models.TextField()),
                ('previous_log', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_log', to='registry.AccessLog')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('address1', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('country', models.CharField(blank=True, max_length=2, null=True)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuditTrail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('json_before', models.TextField(null=True)),
                ('json_after', models.TextField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='audit', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BigAim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('name', models.CharField(max_length=400)),
                ('description', models.CharField(max_length=400, null=True)),
                ('sort_order', models.IntegerField(null=True)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClinicalArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClinicalDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('sort_order', models.IntegerField(null=True)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClinicalSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Descriptor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('date_added', models.DateField(null=True)),
                ('major_revision_date', models.DateField(null=True)),
                ('ui', models.CharField(max_length=10)),
                ('cas_registry_number', models.CharField(max_length=40, null=True)),
                ('descriptor_class', models.CharField(max_length=1, null=True)),
                ('descriptor_entry_version', models.CharField(max_length=100, null=True)),
                ('descriptor_sort_version', models.CharField(max_length=300, null=True)),
                ('major_descriptor_date', models.DateField(null=True)),
                ('mesh_heading', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('name', models.CharField(max_length=50, null=True)),
                ('pipe_separated', models.CharField(max_length=300, null=True)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FocusArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('sort_order', models.IntegerField(null=True)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MeshTreeNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('value', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('org_name', models.CharField(max_length=400)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('account_expiration_time', models.DateTimeField(null=True)),
                ('business_phone', models.CharField(max_length=50, null=True)),
                ('contact_phone', models.CharField(max_length=50, null=True)),
                ('email_address', models.CharField(max_length=100, null=True)),
                ('first_name', models.CharField(max_length=30)),
                ('gatorlink', models.CharField(max_length=50, null=True)),
                ('last_login_time', models.DateTimeField(null=True)),
                ('last_name', models.CharField(max_length=30)),
                ('training', models.CharField(max_length=50, null=True)),
                ('webpage_url', models.CharField(max_length=50, null=True)),
                ('title', models.CharField(max_length=50, null=True)),
                ('department', models.CharField(max_length=50, null=True)),
                ('qi_required', models.SmallIntegerField(null=True)),
                ('other_self_classification', models.CharField(max_length=100, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('clinical_area', models.ManyToManyField(to='registry.ClinicalArea')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('expertise', models.ManyToManyField(to='registry.Expertise')),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ManyToManyField(to='registry.Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PharmacologicalAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('name', models.CharField(max_length=250)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('approval_date', models.DateTimeField(null=True)),
                ('archived', models.BooleanField(default=False)),
                ('description', models.TextField(null=True)),
                ('measures', models.TextField(null=True)),
                ('overall_goal', models.TextField(null=True)),
                ('proposed_end_date', models.DateTimeField(null=True)),
                ('proposed_start_date', models.DateTimeField(null=True)),
                ('title', models.CharField(max_length=300)),
                ('advisor', models.ManyToManyField(related_name='advised_projects', to='registry.Person')),
                ('big_aim', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='registry.BigAim')),
                ('category', models.ManyToManyField(related_name='projects', to='registry.Category')),
                ('clinical_area', models.ManyToManyField(related_name='projects', to='registry.ClinicalArea')),
                ('clinical_setting', models.ManyToManyField(related_name='projects', to='registry.ClinicalSetting')),
                ('collaborator', models.ManyToManyField(related_name='collaborations', to='registry.Person')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='registry.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QI_Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Qualifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('date_added', models.DateField(null=True)),
                ('major_revision_date', models.DateField(null=True)),
                ('ui', models.CharField(max_length=10)),
                ('qualifier_established', models.CharField(max_length=25, null=True)),
                ('abbreviation', models.CharField(max_length=2)),
                ('sub_heading', models.CharField(max_length=50)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RegistryNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('name', models.CharField(max_length=200)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SCR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('date_added', models.DateField(null=True)),
                ('major_revision_date', models.DateField(null=True)),
                ('ui', models.CharField(max_length=10)),
                ('cas_registry_number', models.CharField(max_length=40, null=True)),
                ('frequency', models.IntegerField(null=True)),
                ('note', models.TextField()),
                ('substance_name', models.CharField(max_length=300, null=True)),
                ('substance_name_term_thesaurus', models.CharField(max_length=40, null=True)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('heading_mapped_to', models.ManyToManyField(related_name='scr', to='registry.Descriptor')),
                ('indexing_information', models.ManyToManyField(related_name='scr_indexing', to='registry.Descriptor')),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('pharmacological_action', models.ManyToManyField(to='registry.PharmacologicalAction')),
                ('related_registry_number', models.ManyToManyField(to='registry.RegistryNumber')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Self_Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('name', models.CharField(max_length=400)),
                ('description', models.CharField(max_length=400, null=True)),
                ('sort_order', models.IntegerField(null=True)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SemanticType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('value', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=50, null=True)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('name', models.CharField(max_length=200)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Suffix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Synonym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('name', models.CharField(max_length=50, null=True)),
                ('pipe_separated', models.CharField(max_length=400, null=True)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('guid', models.CharField(default=registry.utils.get_guid, editable=False, max_length=32)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200, null=True)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ua_string', models.TextField()),
                ('ua_hash', models.CharField(editable=False, max_length=32)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='useragent',
            unique_together=set([('id', 'ua_hash')]),
        ),
        migrations.AddField(
            model_name='scr',
            name='semantic_type',
            field=models.ManyToManyField(to='registry.SemanticType'),
        ),
        migrations.AddField(
            model_name='scr',
            name='source',
            field=models.ManyToManyField(to='registry.Source'),
        ),
        migrations.AddField(
            model_name='scr',
            name='synonym',
            field=models.ManyToManyField(to='registry.Synonym'),
        ),
        migrations.AddField(
            model_name='person',
            name='position',
            field=models.ManyToManyField(to='registry.Position'),
        ),
        migrations.AddField(
            model_name='person',
            name='qi_interest',
            field=models.ManyToManyField(to='registry.QI_Interest'),
        ),
        migrations.AddField(
            model_name='person',
            name='self_classification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person', to='registry.Self_Classification'),
        ),
        migrations.AddField(
            model_name='person',
            name='speciality',
            field=models.ManyToManyField(to='registry.Speciality'),
        ),
        migrations.AddField(
            model_name='person',
            name='suffix',
            field=models.ManyToManyField(to='registry.Suffix'),
        ),
        migrations.AddField(
            model_name='descriptor',
            name='allowable_qualifiers',
            field=models.ManyToManyField(related_name='_descriptor_allowable_qualifiers_+', to='registry.Qualifier'),
        ),
        migrations.AddField(
            model_name='descriptor',
            name='created_by',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='descriptor',
            name='entry',
            field=models.ManyToManyField(related_name='descriptor', to='registry.Entry'),
        ),
        migrations.AddField(
            model_name='descriptor',
            name='forward_reference',
            field=models.ManyToManyField(related_name='_descriptor_forward_reference_+', to='registry.Descriptor'),
        ),
        migrations.AddField(
            model_name='descriptor',
            name='last_modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='descriptor',
            name='mesh_tree_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='descriptor', to='registry.MeshTreeNumber'),
        ),
        migrations.AddField(
            model_name='descriptor',
            name='pharmacological_action',
            field=models.ManyToManyField(to='registry.PharmacologicalAction'),
        ),
        migrations.AddField(
            model_name='descriptor',
            name='projects',
            field=models.ManyToManyField(null=True, related_name='mesh_keyword', to='registry.Project'),
        ),
        migrations.AddField(
            model_name='descriptor',
            name='related_registry_number',
            field=models.ManyToManyField(to='registry.RegistryNumber'),
        ),
        migrations.AddField(
            model_name='descriptor',
            name='semantic_type',
            field=models.ManyToManyField(to='registry.SemanticType'),
        ),
        migrations.AddField(
            model_name='address',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_address', to='registry.Organization'),
        ),
        migrations.AddField(
            model_name='address',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business_address', to='registry.Person'),
        ),
        migrations.AddField(
            model_name='accesslog',
            name='user_agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='registry.UserAgent'),
        ),
    ]
