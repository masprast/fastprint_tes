# Generated by Django 4.2.7 on 2023-11-27 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id_kategori', models.AutoField(primary_key=True, serialize=False)),
                ('nama_kategori', models.CharField(max_length=80, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id_status', models.AutoField(primary_key=True, serialize=False)),
                ('nama_status', models.CharField(max_length=80, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id_produk', models.AutoField(primary_key=True, serialize=False)),
                ('nama_produk', models.CharField(max_length=255)),
                ('harga', models.IntegerField()),
                ('kategori_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kategori', to='katalog.kategori')),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='katalog.status')),
            ],
        ),
    ]
