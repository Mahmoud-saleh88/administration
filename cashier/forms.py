from django import forms
from.models import *

class Menu_form (forms.modelForm):
    class Meta :
        models = MenuItem
        fields = "__all__"
        
class Order_form(forms.modelform):
    class Meta :
        models = Order
        fields = "__all__"
    
