# Generated by Django 4.0 on 2024-03-02 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aiweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='mediaphoto'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
