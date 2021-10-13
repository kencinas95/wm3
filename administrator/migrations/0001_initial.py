# Generated by Django 3.2.5 on 2021-10-12 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminProfile',
            fields=[
                ('code', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=64, unique=True)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'wm_admin_profile',
            },
        ),
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('username', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('pepper', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=128)),
                ('surname', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveBigIntegerField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.adminprofile')),
            ],
            options={
                'db_table': 'wm_admin_user',
            },
        ),
        migrations.CreateModel(
            name='AdminSession',
            fields=[
                ('sid', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('since', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.adminuser', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdminPermission',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('table', models.CharField(max_length=128)),
                ('allow_select', models.BooleanField()),
                ('allow_insert', models.BooleanField()),
                ('allow_update', models.BooleanField()),
                ('allow_delete', models.BooleanField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.adminprofile')),
            ],
            options={
                'db_table': 'wm_admin_permission',
            },
        ),
    ]
