# Generated by Django 2.2 on 2021-09-06 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210906_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Pr_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
