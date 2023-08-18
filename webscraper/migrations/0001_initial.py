# Generated by Django 4.1.5 on 2023-05-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blacklist",
            fields=[
                (
                    "id",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("h_self", models.CharField(max_length=10)),
                ("father", models.CharField(max_length=10)),
                ("mother", models.CharField(max_length=10)),
                ("spouse", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Household",
            fields=[
                (
                    "id",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("marriage_f", models.CharField(max_length=10)),
                ("marriage_m", models.CharField(max_length=10)),
                ("relmast", models.CharField(max_length=10, null=True)),
                ("aborigine", models.CharField(max_length=10, null=True)),
                ("education", models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Judge",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pid", models.CharField(max_length=10)),
                ("name", models.CharField(max_length=10)),
                ("court", models.CharField(max_length=10)),
                ("crime_type", models.CharField(max_length=10)),
                ("event_time", models.DateTimeField()),
                ("event_age", models.IntegerField(default=0)),
                ("amount", models.CharField(default=0, max_length=20)),
                ("company", models.TextField(blank=True)),
                ("map_family", models.CharField(max_length=10)),
                ("map_address", models.CharField(max_length=10)),
                ("link", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Lender",
            fields=[
                (
                    "id",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=10)),
                ("age", models.IntegerField(default=0)),
                ("fatherName", models.CharField(blank=True, max_length=10, null=True)),
                ("motherName", models.CharField(blank=True, max_length=10, null=True)),
                ("residenceAddress", models.TextField(null=True)),
                ("companyAddress", models.TextField(null=True)),
                ("currentAdddress", models.TextField(null=True)),
                ("source", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="loan_table",
            fields=[
                (
                    "id",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("payment", models.IntegerField()),
                ("left_amount", models.IntegerField()),
                ("default_amount", models.IntegerField()),
                ("total_amount", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="TFE_table",
            fields=[
                (
                    "id",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("payment", models.IntegerField()),
                ("left_amount", models.IntegerField()),
                ("default_amount", models.IntegerField()),
                ("total_amount", models.IntegerField()),
                ("bid_sell", models.IntegerField()),
            ],
        ),
    ]
