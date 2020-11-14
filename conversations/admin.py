from django.contrib import admin
from . import models as conversations_models


@admin.register(conversations_models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """ Conversation Admin Define """

    pass


@admin.register(conversations_models.Message)
class MessageAdmin(admin.ModelAdmin):

    """ Message Admin Define """

    pass
