
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from appGPT.forms import *
from appGPT.utils import getCHAT


class MainViewHome(TemplateView):
    template_name = 'appGPT/mainPage.html'




class RegisterView(TemplateView):
    template_name = 'appGPT/register.html'

class LoginView(TemplateView):
    template_name = 'appGPT/login.html'

class ForgotPasswordView(TemplateView):
    template_name = 'appGPT/forgot-password.html'


class GPTChatView(TemplateView):
    template_name = 'appGPT/ask-anything.html'
    view_is_async = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.form = ChatForm()

    def get_context_data(self, *args, **kwargs):
        context =  super(GPTChatView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        temperature = request.POST.get('temperature')
        context_present = request.POST.get('context')
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        if(context_present == "YES"):
            prompt = f"{answer}YOU: {question}"
            response = getCHAT(prompt, temperature)
            dialog = response.strip()
            self.form = ChatForm({'answer' :f"{prompt}\nAARON:{dialog}\n",'context':context,'temperature':temperature})

        else:
            prompt = question
            response = getCHAT(prompt,temperature)
            dialog = response.strip()
            self.form = ChatForm({'answer' :f"AARON: {dialog}",'context':context,'temperature':temperature})
        context['form'] = self.form
        return self.render_to_response(context)




