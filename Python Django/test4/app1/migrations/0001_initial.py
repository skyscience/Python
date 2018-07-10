# Generated by Django 2.0.5 on 2018-05-23 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=20)),
                ('bpub_date', models.DateTimeField(db_column='pub_date')),
                ('bread', models.IntegerField(default=0)),
                ('bcommet', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=10)),
                ('hgender', models.BooleanField(default=True)),
                ('hcontent', models.CharField(max_length=1000)),
                ('isDelete', models.BooleanField(default=False)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app1.BookInfo')),
            ],
        ),
    ]