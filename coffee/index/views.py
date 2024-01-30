from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


from .models import MealMenu

# Create your views here.
def index_view(request):
    menu_items = MealMenu.objects.all()
    {'menu_items': menu_items}

    return render(request, 'index.html', {'menu_items': menu_items})

# @method_decorator(csrf_exempt, name='dispatch')
# class ContactFormView(View):
#     def post(self, request, format=None):
#         data = request.data
#
#         try:
#             send_mail(
#                 data['subject'],
#                 f"Name: {data['name']}\nEmail: {data['email']}\n\nMessage:\n{data['message']}",
#                 'your_sender_email@example.com',
#                 ['your_receiver_email@example.com'],
#                 fail_silently=False
#             )
#             return JsonResponse({'message': 'Message sent successfully'})
#         except Exception as e:
#             return JsonResponse({'message': f'Message failed to send. {str(e)}'}, status=500)



