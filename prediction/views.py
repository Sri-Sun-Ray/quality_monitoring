from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .ml_model import predict_water_quality

# Create your views here.
@api_view(["POST"])
def water_quality_prediction(request):
    """
    API endpoint to predict water quality based on input parameters.
    """
    try:
        # Extract data from request
        data = request.data.get("features", [])
        print("Received Data:", data)  # Debugging Step

        if len(data) != 9:
            return Response({"error": "Invalid input. Provide 9 water parameters."}, status=400)

        # Get prediction from ML model
        result = predict_water_quality(data)
        status = "Safe" if result == 1 else "Unsafe"

        print("Prediction:", status)  # Debugging Step

        return Response({"prediction": status})
    except Exception as e:
        print("Error:", str(e))  # Debugging Step
        return Response({"error": str(e)}, status=500)