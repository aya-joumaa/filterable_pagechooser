from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model_string
from wagtail.models import Page


class Article(Page):
    ARTICLE_TYPE = (
        ("", ""),
        ("sport", "Sport"),
        ("medical", "Medical"),
        ("economics", "Economics"),
        ("technology", "Technology"),
    )

    is_active = models.BooleanField(
        default=True,
        blank=True,
        verbose_name="Is Active?",
    )

    displayed_title = models.CharField(
        default="",
        blank=True,
        max_length=250,
        verbose_name="Displayed Title",
    )

    type = models.CharField(
        default="",
        blank=True,
        max_length=250,
        choices=ARTICLE_TYPE,
        verbose_name="Type",
    )

    description = models.TextField(
        default="",
        blank=True,
        verbose_name="Description",
    )

    gallery_image = models.ForeignKey(
        get_image_model_string(),
        on_delete=models.SET_NULL,
        related_name="+",
        blank=True, null=True,
        verbose_name="Image",
    )

    content_panels = Page.content_panels + [
        FieldPanel("is_active"),
        FieldPanel("type"),
        FieldPanel("displayed_title"),
        FieldPanel("description"),
        FieldPanel("gallery_image"),
    ]

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title
