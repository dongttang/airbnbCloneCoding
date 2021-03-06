from django.db import models
from core import models as core_models


class Conversation(core_models.AbstractTimeStampModel):

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created_time)


class Message(core_models.AbstractTimeStampModel):

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    message = models.TextField()
    conversation = models.ForeignKey(
        "conversations.Conversation", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"
