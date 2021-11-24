# Generated by Django 3.2.9 on 2021-11-24 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('token', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'db_table': 'application',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='events.application')),
            ],
            options={
                'db_table': 'session',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('data', models.JSONField()),
                ('timestamp', models.DateTimeField()),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='events.session')),
            ],
            options={
                'db_table': 'event',
                'ordering': ('-timestamp',),
            },
        ),
        migrations.AddIndex(
            model_name='event',
            index=models.Index(fields=['timestamp'], name='timestamp_idx'),
        ),
    ]