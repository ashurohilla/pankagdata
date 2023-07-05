# Generated by Django 4.2.3 on 2023-07-05 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(default=None, max_length=100, null=True)),
                ('website', models.CharField(default=None, max_length=100, null=True)),
                ('address', models.CharField(default=None, max_length=150, null=True)),
                ('location', models.CharField(default=None, max_length=150, null=True)),
                ('Gender', models.CharField(default=None, max_length=160, null=True)),
            ],
        ),
    ]
