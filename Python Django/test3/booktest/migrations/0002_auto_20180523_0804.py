# Generated by Django 2.0.5 on 2018-05-23 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('aid', models.IntegerField(primary_key=True, serialize=False)),
                ('atitle', models.CharField(max_length=20)),
                ('aPArea', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='booktest.AreaInfo')),
            ],
        ),
        migrations.DeleteModel(
            name='BookInfo',
        ),
        migrations.DeleteModel(
            name='HeroInfo',
        ),
    ]