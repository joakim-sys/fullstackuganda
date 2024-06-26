# Generated by Django 4.2.9 on 2024-03-19 13:40

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
        ("home", "0003_homepage_about_body_homepage_about_cta_link_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
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
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "icon",
                    models.CharField(
                        blank=True,
                        help_text='Enter the icon code for this service. This field uses Boxicons, and you can find a variety of icons with the class "bx". For example, use "bx-world" for a world icon. Leave it blank if no icon is needed.',
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        help_text="Provide a title for the service",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="Enter a brief description of the service.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "link",
                    models.ForeignKey(
                        blank=True,
                        help_text="Choose a page to link to when users interact with this service.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="HomeServiceRelation",
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
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="home_service_relation",
                        to="home.homepage",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="service_home_relation",
                        to="services.service",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]
