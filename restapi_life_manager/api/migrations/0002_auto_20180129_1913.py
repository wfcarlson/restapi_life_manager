# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-29 19:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Income Categories',
            },
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='ExpenseCategory',
        ),
        migrations.AlterModelOptions(
            name='expensecategory',
            options={'verbose_name_plural': 'Expense Categories'},
        ),
        migrations.AlterField(
            model_name='income',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.IncomeCategory'),
        ),
    ]