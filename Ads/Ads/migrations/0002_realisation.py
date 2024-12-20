# Generated by Django 5.1.3 on 2024-11-26 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Realisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='galerie/')),
                ('category', models.CharField(choices=[('design', 'Design'), ('impression', 'Impression'), ('peinture', 'Peinture'), ('decoration', 'Décoration')], max_length=100)),
            ],
        ),
    ]
