from django.utils.translation import gettext_lazy as _
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup

from .models import GalleryPage, Category


class GalleryPageViewSet(SnippetViewSet):
    """Makes the adding of gallery pages easy by providing a hook to the menu system thus not needing to use the page hierarchy"""

    model = GalleryPage
    menu_label = _("Gallery")
    menu_icon = "picture"
    list_display = ("first_published_at", "title", "description", "categories")
    list_filter = ("first_published_at", "categories")
    search_fields = ("title", "description", "first_published_at")


class GalleryCategoryViewSet(SnippetViewSet):
    """Makes the adding of categories simply by giving own menu entry"""

    model = Category
    menu_label = _("Categories")
    menu_icon = "group"
    list_display = ("name",)
    search_fields = ("name",)


class GalleryViewSetGroup(SnippetViewSetGroup):
    """Creates the side menu entry with the two other ModelAdmins inside of it"""

    menu_label = _("Gallery")
    menu_icon = "picture"
    menu_order = 300
    items = (GalleryPageViewSet, GalleryCategoryViewSet)
    add_to_admin_menu = True


register_snippet(GalleryViewSetGroup)
