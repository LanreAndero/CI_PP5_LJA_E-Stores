from django.contrib import sitemaps
from django.urls import reverse


class StaticViewsSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        # Replace these with the names of your URL patterns
        return [
            'home',
            'contact',
            'view_bag',
            'checkout',
            'contact',
            'products',
            'profile',
        ]

    def location(self, item):
        return reverse(item)
