# Generated by Django 2.2.1 on 2019-05-21 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0011_auto_20190521_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='bank.Account'),
        ),
    ]
