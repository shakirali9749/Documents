import base64
import uuid
from django.core.files.base import ContentFile
from rest_framework import serializers
import filetype  # New package

ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'svg']


def handle_base64_profile_image(instance, base64_image):
    try:
        format, imgstr = base64_image.split(';base64,')
        ext = format.split('/')[-1].lower()

        if ext not in ALLOWED_EXTENSIONS:
            raise serializers.ValidationError({"profile_image": "Invalid image format."})

        image_data = base64.b64decode(imgstr)

        # Replace imghdr with filetype
        kind = filetype.guess(image_data)
        if not kind or kind.extension not in ALLOWED_EXTENSIONS:
            raise serializers.ValidationError({"profile_image": "Invalid or Corrupt image file."})

        if instance.profile_image:
            instance.profile_image.delete(save=False)

        file_name = f"{uuid.uuid4()}.{ext}"
        instance.profile_image.save(file_name, ContentFile(image_data), save=False)

    except Exception:
        raise serializers.ValidationError({"profile_image": "Invalid image data"})