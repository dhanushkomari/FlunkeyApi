# Generated by Django 3.1.4 on 2021-07-29 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlunkeyApp', '0004_auto_20210728_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='ip',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='delivery',
            name='port',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='table_no',
            field=models.IntegerField(null=True),
        ),
    ]
