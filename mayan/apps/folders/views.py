import logging

from django.contrib import messages
from django.template import RequestContext
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from mayan.apps.acls.models import AccessControlList
from mayan.apps.views.generics import (
    SimpleView,
)

from .forms import MessageCreateForm, MessageDetailForm
from .icons import (
    icon_message_create,
    icon_message_delete,
    icon_message_detail,
    icon_message_list,
    icon_message_mark_read,
    icon_message_mark_unread,
    icon_message_mark_read_all,
)
from .links import link_message_create
from .models import Message
from .permissions import (
    permission_message_create,
    permission_message_delete,
    permission_message_edit,
    permission_message_view,
)

logger = logging.getLogger(name=__name__)


class FolderView(SimpleView):
    template_name = "folders/folder_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["folder"] = self.get_folder()
        return context

    def get_folder(self):
        return self.request.user.folder
