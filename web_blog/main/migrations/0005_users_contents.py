# Generated by Django 4.0 on 2021-12-24 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_content_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='contents',
            field=models.JSONField(null=True),
        ),
    ]
