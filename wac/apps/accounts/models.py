from django.contrib.auth.models import User
from django.db import models

# App
from wac.apps.core.models import Location, Topic
from wac.storage_backends import MediaStorage

class Profile(models.Model):
    """
    Extends from the user model
    """
    HE = 'he'
    SHE = 'she'
    THEY = 'they'
    PRONOUNS_CHOICE = (
        (HE, HE),
        (SHE, SHE),
        (THEY, THEY)
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    topics = models.ManyToManyField(
        Topic
    )

    image = models.CharField(
        max_length=5000,
        default='data:image/jpeg;base64,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'
    )

    first_name = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    woman = models.NullBooleanField(
        null=True,
        blank=True
    )

    poc = models.NullBooleanField(
        null=True,
        blank=True
    )

    pronouns = models.CharField(
        max_length=10,
        choices=PRONOUNS_CHOICE,
        null=True,
        blank=True
    )

    position = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    organization = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    description = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    twitter = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    linkedin = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    website = models.CharField(
        max_length=250,
        null=True,
        blank=True
    )

    page = models.CharField(
        max_length=25,
        null=True,
        blank=True,
        default='registration'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def display_name(self):
        first_name = self.first_name
        last_name = self.last_name

        if first_name and last_name:
            return u"%s %s".strip() % (first_name, last_name)

        return None

    def __str__(self):
        return self.display_name()

    def __unicode__(self):
        return self.display_name()


class ProfileLocation(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


class ProfileTopic(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    topic = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

class ImageUpload(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    file = models.FileField(blank=False, null=False, storage=MediaStorage())

    created_at = models.DateTimeField(
        auto_now_add=True
    )
