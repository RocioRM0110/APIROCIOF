from django.shortcuts import render, redirect
<<<<<<< HEAD
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
=======
from django.contrib import messages
>>>>>>> eabcdb94dc7ff9719625869e620c28e8f684122b
from django.contrib.auth.views import LoginView
from rest_framework.views import APIView
from django.template.loader import render_to_string
from django.core.mail import send_mail
<<<<<<< HEAD
=======
from .forms import RegistroForm
from .models import Registro  # Asegúrate de importar el modelo correctamente
from django.urls import reverse
>>>>>>> eabcdb94dc7ff9719625869e620c28e8f684122b

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Guarda los datos del formulario en la base de datos
            form.save()
<<<<<<< HEAD
=======
            
>>>>>>> eabcdb94dc7ff9719625869e620c28e8f684122b
            # Redirige a la página de inicio de sesión u otra página que desees
            correo = form.cleaned_data['correo']
            password = form.cleaned_data['password']
            messages.success(request, 'El registro se ha creado con éxito.')  # Añade un mensaje de confirmación
<<<<<<< HEAD
            # Redirige a la página de inicio de sesión u otra página que desees
=======
>>>>>>> eabcdb94dc7ff9719625869e620c28e8f684122b
            
            # Envía el correo de bienvenida
            subject = 'Bienvenido a BURGER TOCHITOS'
            from_email = 'chio7933@gmail.com'
            recipient_list = [correo]
            contexto = {'correo': correo, 'password': password}
            contenido_correo = render_to_string('correo.html', contexto)
            send_mail(subject, '', from_email, recipient_list, html_message=contenido_correo)

<<<<<<< HEAD
        return redirect('iniciar_sesion')
        
    else:
        form = RegistroForm()
=======
            return redirect('iniciar_sesion')
    else:
        form = RegistroForm()

>>>>>>> eabcdb94dc7ff9719625869e620c28e8f684122b
    return render(request, 'registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
<<<<<<< HEAD
        correo1 = request.POST.get('correo')
        contra1 = request.POST.get('password')
        
        try:
            user = Registro.objects.get(correo=correo1, password=password1)
            request.session['correo'] = user.correo
    
            return redirect('Index')
        except: 
             messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')


    

class registroU(APIView):
    template_name = "registro.html"
    def get(self, request):
        return render(request, self.template_name)
    
class Index(APIView): 
    template_name="index.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)
=======
        correo = request.POST.get('correo')
        password = request.POST.get('password')
        
        try:
            user = Registro.objects.get(correo=correo, password=password)
            request.session['correo'] = user.correo
            return redirect('Index')
        except Registro.DoesNotExist:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            
    return render(request, 'login.html')

class RegistroU(APIView):
    template_name = "registro.html"
    
    def get(self, request):
        return render(request, self.template_name)

class Maps(APIView):
    template_name = "maps.html"
    
    def get(self, request):
        return render(request, self.template_name)

class Index(APIView): 
    template_name = "index.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        return render(request, self.template_name)

class Alerts(View):
    template_name = 'alerts.html'

    def get(self, request, *args, **kwargs):
        # Puedes realizar lógica adicional aquí si es necesario
        return render(request, self.template_name)
>>>>>>> eabcdb94dc7ff9719625869e620c28e8f684122b
