from rest_framework import serializers

from payments.models import MonetaryTransaction
from .users import CustomUserDetailsSerializer


class TrackIdSerializer(serializers.Serializer):
    trackId = serializers.IntegerField(required=True)

    def validate(self, data):
        trackId = data.get("trackId")
        if (
            trackId is None
            or not MonetaryTransaction.objects.filter(trackId=trackId).exists()
        ):
            raise serializers.ValidationError(
                {"trackId": "invalid trackId."}, "not_found"
            )
        return super().validate(data)


class TransactionSerializer(serializers.ModelSerializer):
    by_user = CustomUserDetailsSerializer(read_only=True)
    for_user = CustomUserDetailsSerializer(read_only=True)
    payment_time = serializers.SerializerMethodField()

    class Meta:
        model = MonetaryTransaction
        fields = [
            "by_user",
            "for_user",
            "get_currency_display",
            "amount",
            "reference_number",
            "extra_information",
            "payment_time",
        ]

    def get_payment_time(self, obj):
        return obj.payment_time.isoformat()
