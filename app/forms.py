from django import forms
g=[['male','male'],['female','female']]
c=[('python','python'),('sql','sql')]

def validate_for_char(data):
    if not data[0].isalpha():
        raise forms.ValidationError('Error')
    
def validate_for_len(value):
    if len(value)<5:
        raise forms.validationError('Error')




class StudentForm(forms.Form):
    sname=forms.CharField(validators=[validate_for_char])
    sid=forms.IntegerField()
    surl=forms.URLField()
    semail=forms.EmailField(validators=[validate_for_char])
    remail=forms.EmailField()
    botcatcher=forms.CharField(max_length=20,widget=forms.HiddenInput,required=False)


    def clean(self):
       s=self.cleaned_data['semail']
       r=self.cleaned_data['remail']
       if s!=r:
            raise forms.ValidationError('Error')
    def clean_botcatcher(self):
        bot=self.cleaned_data.get('botcatcher')
        if len(bot)>0:
            raise forms.ValidationError('human omly enter data')
            







    #spassword=forms.CharField(widget=forms.PasswordInput)
    #rpassword=forms.CharField(widget=forms.PasswordInput)
    #saddress=forms.CharField(widget=forms.Textarea(attrs={'rows':10,'cols':10}))
    #gender=forms.ChoiceField(choices=g)
    #studentFormgender=forms.CharField(choices=g,widget=forms.RadioSelect())
    #course=forms.multipleChoiceField(choices=c)
    #course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    
    
