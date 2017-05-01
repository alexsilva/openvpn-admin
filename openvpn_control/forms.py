from  django import forms


class VPNForm(forms.ModelForm):
    import_zip = forms.FileField(
        label="Importe from zip",
        help_text="import .ovpn files from zip"
    )
