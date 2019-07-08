# Generated by Django 2.2.3 on 2019-07-07 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40)),
                ('mobile', models.IntegerField(unique=True)),
                ('age', models.IntegerField()),
                ('profession', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerFamily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField(unique=True)),
                ('age', models.IntegerField()),
                ('profession', models.CharField(max_length=40)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
    ]
