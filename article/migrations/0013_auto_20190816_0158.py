# Generated by Django 2.1.5 on 2019-08-15 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_commentofcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentofcomment',
            name='commentOfComment_content',
            field=models.CharField(max_length=100, null=True, verbose_name='Yorum'),
        ),
    ]
