from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    """
    Default custom user model for be_test.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Keycap(models.Model):
    class Profile(models.TextChoices):
        DSA = 'DSA', _('DSA')
        SA = 'SA', _('DSA')
        CHERRY = 'CHERRY', _('Cherry')
        XDA = 'XDA', _('XDA')
    class Material(models.TextChoices):
        ABS = 'ABS', _('ABS')
        PTB = 'PTB', _('ABS')
        GMK = 'GMK', _('GMK')
    profile = models.CharField(
        max_length=6,
        choices=Profile.choices,
        default=Profile.DSA,
    )
    material =  models.CharField(
        max_length=5,
        choices=Material.choices,
        default=Material.ABS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "Profile: " + self.profile + " Material: " + self.material

class Keyboard(models.Model):
    class Switches(models.TextChoices):
        RED = 'red', _('Red')
        BLACK = 'black', _('Black')
        BROWN = 'brown', _('Brown')
        BLUE = 'blue', _('Blue')
    name = models.CharField(max_length=200)
    switches = models.CharField(
        max_length=5,
        choices=Switches.choices,
        default=Switches.RED,
    )
    keycap = models.ForeignKey(Keycap, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)