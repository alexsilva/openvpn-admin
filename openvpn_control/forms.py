from django import forms
import zipfile
import io

from .models import Ovpn


class VPNForm(forms.ModelForm):
    import_zip = forms.FileField(
        label="Importe from zip",
        help_text="import .ovpn files from zip",
        required=False
    )

    def clean_import_zip(self):
        import_zip = self.cleaned_data.get('import_zip')

        if import_zip:
            if not zipfile.is_zipfile(import_zip.file):
                raise forms.ValidationError("Enter a zip file.")
        return import_zip

    def do_import(self, instance):
        """Import zip files"""
        import_zip = self.cleaned_data.get('import_zip')

        if import_zip and instance.pk is not None:
            zipf = zipfile.ZipFile(import_zip.file)

            for filename in zipf.namelist():
                stream = zipf.read(filename)
                ovpn = Ovpn(vpn=instance)
                _stream = io.BytesIO(stream)
                _stream.size = len(stream)
                ovpn.file.save(filename, _stream)
                ovpn.save()

    def save(self, commit=True):
        instance = super(VPNForm, self).save(commit=commit)
        self.do_import(instance)
        return instance
