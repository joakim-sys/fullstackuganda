# Generated by Django 4.2.9 on 2024-03-19 15:12

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.blocks
import wagtail.contrib.routable_page.models
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("taggit", "0005_auto_20220424_2025"),
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
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
                    "first_name",
                    models.CharField(
                        help_text="Enter the first name of the author",
                        max_length=254,
                        verbose_name="First name",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        help_text="Enter the last name of the author.",
                        max_length=254,
                        verbose_name="Last name",
                    ),
                ),
                (
                    "job_title",
                    models.CharField(
                        blank=True,
                        help_text="Optionally, provide the job title of the author.",
                        max_length=254,
                        null=True,
                        verbose_name="Job Title",
                    ),
                ),
                (
                    "twitter_url",
                    models.URLField(
                        blank=True,
                        help_text="Optionally, enter the Twitter URL of the author.",
                        null=True,
                        verbose_name="X URL",
                    ),
                ),
                (
                    "facebook_url",
                    models.URLField(
                        blank=True,
                        help_text="Optionally, enter the Facebook URL of the author.",
                        null=True,
                        verbose_name="Facebook URL",
                    ),
                ),
                (
                    "instagram_url",
                    models.URLField(
                        blank=True,
                        help_text=" Optionally, enter the Instagram URL of the author.",
                        null=True,
                        verbose_name="Instagram URL",
                    ),
                ),
                (
                    "bio",
                    models.TextField(
                        blank=True,
                        help_text="Optionally, provide a brief biography or description of the author.",
                        null=True,
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BlogListing",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "introduction",
                    models.TextField(
                        blank=True,
                        help_text="This text serves as a brief introduction or overview for the blog listing page. It may provide context or a summary of the content featured on this page.",
                        verbose_name="Introduction Text",
                    ),
                ),
            ],
            options={
                "verbose_name": "Blog Listing",
                "verbose_name_plural": "Blog Listings",
            },
            bases=(
                wagtail.contrib.routable_page.models.RoutablePageMixin,
                "wagtailcore.page",
            ),
        ),
        migrations.CreateModel(
            name="BlogPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "introduction",
                    models.TextField(
                        blank=True,
                        help_text="A brief overview or introduction to the post.",
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            (
                                "heading_block",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "heading_text",
                                            wagtail.blocks.CharBlock(
                                                form_classname="title", required=True
                                            ),
                                        ),
                                        (
                                            "size",
                                            wagtail.blocks.ChoiceBlock(
                                                blank=True,
                                                choices=[
                                                    ("", "Select a header size"),
                                                    ("h2", "H2"),
                                                    ("h3", "H3"),
                                                    ("h4", "H4"),
                                                ],
                                                required=False,
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "paragraph_block",
                                wagtail.blocks.RichTextBlock(
                                    features=["bold", "italic", "link"],
                                    icon="pilcrow",
                                    template="blocks/paragraph_block.html",
                                ),
                            ),
                            (
                                "image_block",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(
                                                required=True
                                            ),
                                        ),
                                        (
                                            "caption",
                                            wagtail.blocks.CharBlock(required=False),
                                        ),
                                        (
                                            "attribution",
                                            wagtail.blocks.CharBlock(required=False),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "block_quote",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("text", wagtail.blocks.TextBlock()),
                                        (
                                            "attribute_name",
                                            wagtail.blocks.CharBlock(
                                                blank=True,
                                                label="e.g. John Doe",
                                                required=False,
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "embed_block",
                                wagtail.embeds.blocks.EmbedBlock(
                                    help_text="Insert an embed URL",
                                    icon="media",
                                    template="blocks/embed_block.html",
                                ),
                            ),
                        ],
                        blank=True,
                        help_text="The main content of the post. You can add and organize different types of content blocks here.",
                        null=True,
                        use_json_field=True,
                        verbose_name="Page Body",
                    ),
                ),
                (
                    "subtitle",
                    models.CharField(
                        blank=True,
                        help_text="A short additional title or description for the post.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "date_published",
                    models.DateField(
                        blank=True,
                        help_text="The date when the post was published.",
                        null=True,
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        help_text="An image that represents or is associated with the post. This image may be used as a thumbnail or featured image.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Featured Image",
                    ),
                ),
            ],
            options={
                "verbose_name": "Blogpage",
                "verbose_name_plural": "Blogpages",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="Category",
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
                    "name",
                    models.CharField(
                        help_text="Enter a unique name for the category. Categories are used to classify and organize blog posts. Choose a descriptive name that reflects the content associated with this category.",
                        max_length=255,
                        unique=True,
                        verbose_name="Category Name",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="BlogPageTag",
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
                    "content_object",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tagged_items",
                        to="blog.blogpage",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_items",
                        to="taggit.tag",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="blogpage",
            name="tags",
            field=modelcluster.contrib.taggit.ClusterTaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="blog.BlogPageTag",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
        migrations.CreateModel(
            name="BlogCategoryRelationship",
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
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="category_blog_relationship",
                        to="blog.category",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blog_category_relationship",
                        to="blog.blogpage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="BlogAuthorRelationship",
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
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="author_blog_relationship",
                        to="blog.author",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blog_author_relationship",
                        to="blog.blogpage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]
