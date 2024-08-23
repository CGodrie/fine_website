from django.shortcuts import render
from .models import Discussion, Message
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def home(request):
    return render(request, template_name='main/home.html')

@login_required
def chat(request, id):

    # Vérifier si la discussion existe déjà entre ces deux utilisateurs
    discussion = Discussion.objects.filter(id=id)

    if discussion.exists():
        user_a = discussion.first().users.all()[0]
        messages = Message.objects.filter(discussion=discussion.first())
        if len(discussion.first().users.all()) > 2 and user_a != request.user:
            discussion.users.add(request.user)
    else:
        # Si la discussion n'existe pas, vous pouvez choisir de la créer ici
        # Notez que cela dépend de votre logique métier, vous pourriez créer la discussion à un autre endroit.
        discussion = Discussion.objects.create()
        discussion.users.add(request.user)
        messages = Message.objects.none()  # Pas de messages pour une nouvelle discussion

    return render(request, 'main/chat.html', {'discussion_id': discussion.first().id, 'users_messages': messages})


@csrf_exempt
def send_message(request, id):
    if request.method == 'POST':
        message_content = request.POST.get('message_content', '')
        try:
            discussion = Discussion.objects.get(id=id)
            new_message = Message.objects.create(discussion=discussion, user=request.user, content=message_content)

            serialized_message = {
                'user': new_message.user.username,
                'message': new_message.content,
                'sent_at': new_message.sent_at.strftime('%Y-%m-%dT%H:%M:%S'),
            }

            return JsonResponse({'status': 'success', 'message': serialized_message})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    return JsonResponse({'error': 'Invalid request method'})


@login_required
def get_messages(request, id):
    try:
        messages = Message.objects.filter(discussion=Discussion.objects.get(id=id))

        # Serialize messages
        serialized_messages = []
        for message in messages:
            serialized_message = {
                'user': message.user.username,
                'message': message.content,
                'sent_at': message.sent_at.strftime('%Y-%m-%dT%H:%M:%S'),
            }
            serialized_messages.append(serialized_message)
        return JsonResponse({'status': 'success', 'messages': serialized_messages})
    except Exception as e:
        return JsonResponse({'status': 'error', 'error_message': str(e)})