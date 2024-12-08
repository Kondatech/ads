# Generated by Django 5.1.3 on 2024-12-02 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0002_realisation'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrintFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('name', models.CharField(max_length=255, verbose_name='Nom du fichier')),
                ('dimensions', models.CharField(max_length=50, verbose_name='Dimensions (par ex. 30x40 cm)')),
                ('paper_type', models.CharField(choices=[('Glossy', 'Glossy'), ('Matte', 'Matte'), ('Standard', 'Standard')], max_length=20, verbose_name='Type de papier')),
                ('print_type', models.CharField(choices=[('Color', 'Impression couleur'), ('Black & White', 'Impression noir et blanc')], max_length=20, verbose_name="Type d'impression")),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]