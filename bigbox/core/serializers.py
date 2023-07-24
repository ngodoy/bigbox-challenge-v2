# serializers.py

from itertools import product
from django.db.models import fields
from rest_framework import serializers
from . import models

# View Activity

# Common fields used in multiple serializers
common_fields = "id", "name", "slug"

# Fields specific to the "Activity" and "Box" product model
product_fields = common_fields + ("description", "category", "purchase_available")


class ReasonSerializer(serializers.ModelSerializer):
    """
    Serializer for the 'models.Reason' model.
    Allows converting 'models.Reason' objects to JSON representations and vice versa.
    """

    class Meta:
        model = models.Reason
        fields = common_fields + ("order",)


class ActivityImageSerializer(serializers.ModelSerializer):
    """
    Serializer for the 'models.ActivityImage' model.
    Allows converting 'models.ActivityImage' objects to JSON representations and vice versa.
    """

    class Meta:
        model = models.ActivityImage
        fields = (
            "id",
            "order",
            "upload",
        )


class ActivitySerializer(serializers.ModelSerializer):
    """
    Serializer for the 'models.Activity' model.
    Allows converting 'models.Activity' objects to JSON representations and vice versa.
    Includes serialization of related fields such as 'Reason' and 'ActivityImage'.
    """

    # Serializer for the one-to-many relationship with the 'models.Reason' model
    reasons = ReasonSerializer(many=True, allow_null=True)

    # Serializer for the one-to-many relationship with the 'models.ActivityImage' model
    activityimage_set = ActivityImageSerializer(many=True, allow_null=True)

    class Meta:
        model = models.Activity
        fields = product_fields + (
            "internal_name",
            "reasons",
            "activityimage_set",
        )


# View Box


class BoxImageSerializer(serializers.ModelSerializer):
    """
    Serializer for the 'models.BoxImage' model.
    Allows converting 'models.BoxImage' objects to JSON representations and vice versa.
    """

    class Meta:
        model = models.BoxImage
        fields = ("id", "order", "upload")


class BoxSerializer(serializers.ModelSerializer):
    """
    Serializer for the 'models.Box' model.
    Allows converting 'models.Box' objects to JSON representations and vice versa.
    Includes serialization of related fields such as 'BoxImage'.
    """

    # Serializer for the one-to-many relationship with the 'models.BoxImage' model
    boximage_set = BoxImageSerializer(many=True, allow_null=True)

    class Meta:
        model = models.Box
        fields = product_fields + ("price", "boximage_set")
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}


# View Category


class BoxChildSerializer(serializers.ModelSerializer):
    """
    Serializer for the 'models.Box', used as a child field in 'CategorySerializer'.
    Allows converting 'models.Box' objects to JSON representations and vice versa.
    """

    class Meta:
        model = models.Box
        fields = common_fields + ("price",)


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the 'models.Category' model.
    Allows converting 'models.Category' objects to JSON representations and vice versa.
    Includes serialization of related fields such as 'Box'.
    """

    # Serializer for the one-to-many relationship with the 'models.Box' model
    box_set = BoxChildSerializer(many=True, allow_null=True)

    class Meta:
        model = models.Category
        fields = common_fields + ("order", "description", "box_set")
