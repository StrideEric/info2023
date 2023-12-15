# Generated by Django 3.2 on 2023-11-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_auto_20231123_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(default=1, upload_to='noticias'),
            preserve_default=False,
        ),
    ]
