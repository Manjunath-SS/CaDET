# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=160, null=True, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=510, null=True)),
                ('codename', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=256, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(blank=True, max_length=300, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=60, null=True)),
                ('last_name', models.CharField(blank=True, max_length=60, null=True)),
                ('email', models.CharField(blank=True, max_length=508, null=True)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(blank=True, max_length=400, null=True)),
                ('action_flag', models.IntegerField()),
                ('change_message', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app_label', models.CharField(blank=True, max_length=200, null=True)),
                ('model', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app', models.CharField(blank=True, max_length=510, null=True)),
                ('name', models.CharField(blank=True, max_length=510, null=True)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('session_data', models.TextField(blank=True, null=True)),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FrontendModule',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('label', models.CharField(blank=True, max_length=100, null=True)),
                ('installed', models.BooleanField()),
            ],
            options={
                'db_table': 'frontend_module',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Thehindu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=30, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=800, null=True)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('imgurl', models.CharField(blank=True, max_length=200, null=True)),
                ('pubat', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'thehindu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Toi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=30, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=800, null=True)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('imgurl', models.CharField(blank=True, max_length=200, null=True)),
                ('pubat', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'toi',
                'managed': False,
            },
        ),
    ]
