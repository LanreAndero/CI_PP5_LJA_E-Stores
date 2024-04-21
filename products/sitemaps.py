from django.contrib import sitemaps
from django.urls import reverse
from datetime import datetime


class StaticViewsSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return [
            'home',
            'about',
            'contact',
            'view_bag',
            'checkout',
            'contact',
            'products',
            'profile',
        ]

    def lastmod(self, obj):
        return datetime.now()

    def location(self, item):
        return reverse(item)
