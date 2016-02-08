#from django import forms
#from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm

#class RemitenteCreateForm(UserCreationForm):
    

#    class Meta:
 #       model = Remitente
  #      fields = "__all__"
#
 #   def save(self, commit=True):
  #      user = super(UserCreateForm, self).save(commit=False)
   #     user.set_password(self.cleaned_data["password"])
    #    if commit:
     #       user.save()
      #  return user