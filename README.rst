Introduction
===========================================

This is a very basic gallery app that integrates with Wagtail. It allows a person to upload images and order them on a gallery page. Said gallery page then shows the low-res thumbnails, and when clicked it opens up a high res version with captions.

This app is simple, and not feature rich. It does the basics and thats it. I will probably add more features and options to it as time permits, but only if requests are made.

It is also not production ready as there are **no tests currently written** for it. I did put this up on a site and they have been using it extensively and haven't had any reported issues. That said, *apps without tests should always be treated sceptically.*

I hope to write tests in a month or so when I get a bit of free time. I also hope to add a bunch of features in the near future.

Please report any errors you encounter. I will try resolve them quickly and then add tests for them as things come up so it doesn't reoccur. Please visit `wagtail_gallery git <https://gitlab.com/dfmeyer/wagtail_gallery>`_ to make pull requests or log issues etc. Documentation is at readthedocs.io: `wagtail_gallery documentation <https://wagtail-gallery.readthedocs.io/en/latest/>`_

Installation
===================

To install run ``pip install wagtail_gallery``

It should automatically install all the necessary dependencies.

Remember to add ``wagtail_gallery`` (along with the others mentioned) to your installed apps in settings.py i.e.

    .. code-block:: Python

        INSTALLED_APPS = [
            ...
            'wagtail_gallery',
            'wagtail.contrib.routable_page',
            'wagtail.contrib.modeladmin',
            'django_social_share',
        ]

Requirements:

    .. code-block:: Python

        python3
        wagtail
        django
        django-social-share

I'm not quite sure how far back this app works; however, it should work going back quite far. It's currently tested on Python3 with Wagtail >2 and Django >2 on openSUSE. It should work on all platforms and shouldn't break anytime soon. Let me know if you have a combo that doesn't work and I'll see what I can do to support it.

Caveats
============

#.  I haven't implemented sub-categories at all. Its a planned feature.

#. You can only have one Gallery Root Page at this point in time. I really do want to add the ability to have many. I just haven't gotten round to it. It should be quite simple.

#. URLs are not yet fully internationalised as ``/category/`` isn't translated. I'll get to this eventually.

#. All galleries are public. No permissions have been integrated; however, this is a planned feature.