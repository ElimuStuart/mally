# Generated by Django 2.2.4 on 2019-08-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20190814_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ref_code',
            field=models.CharField(default='ABVS123', max_length=20),
            preserve_default=False,
        ),
    ]
