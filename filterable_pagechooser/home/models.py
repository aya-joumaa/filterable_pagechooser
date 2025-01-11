from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField

from wagtail.models import Page
from filterable_pagechooser.blocks import FilterPageChooserBlock


class HomePage(Page):
    sport_news = StreamField(
        [
            (
                "sport_news",
                FilterPageChooserBlock(
                    label="Sport Articles",
                    page_type="article.Article",
                    target_model="article.Article",
                    filters_info="filters_info:type=sport;is_active=True",
                ),
            )
        ],
        max_num=3,
        use_json_field=True,
        blank=True, default="",
        verbose_name="Sport News",
    )

    medical_news = StreamField(
        [
            (
                "medical_news",
                FilterPageChooserBlock(
                    label="Medical Articles",
                    page_type="article.Article",
                    target_model="article.Article",
                    filters_info="filters_info:type=medical;is_active=True",
                ),
            )
        ],
        max_num=3,
        use_json_field=True,
        blank=True, default="",
        verbose_name="Medical News",
    )

    content_panels = Page.content_panels + [
        FieldPanel("sport_news"),
        FieldPanel("medical_news"),
    ]
