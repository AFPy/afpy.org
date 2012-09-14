from Products.Archetypes.Registry import registerField            
from Products.Archetypes.public import TextField
from Products.Archetypes.Field import decode, encode
from Products.Archetypes.utils import shasattr

try:
    from Products.SyntaxHighlight.SyntaxHighlight import htmlHighlight
except:
    class SourceCodeField(TextField):pass
else:
    class SourceCodeField(TextField):

        set__roles__ = ()
        def set(self, instance, value, **kwargs):
            TextField.set(self, instance, value, **kwargs)
            self.colorise(instance, value, **kwargs)

        colorise__roles__ = ()
        def colorise(self, instance, value, **kwargs):
            value = TextField.get(self, instance, mimetype='text/html',raw=1)
            if shasattr(value, 'transform'):
                 data = value.transform(instance, 'text/plain')
            else:
                 data = value
            colored_text = htmlHighlight(instance,decode(str(value),instance,**kwargs))
            setattr(instance,'colored_%s' % self.getName(), colored_text)

        get__roles__ = ()
        def get(self, instance, mimetype=None, raw=False, **kwargs):
            name = 'colored_%s' % self.getName()
            if kwargs.has_key('schema') and not raw and hasattr(instance,name):
                colored_text=getattr(instance,name)
                return  encode(colored_text,instance,**kwargs)
            return TextField.get(self, instance, mimetype=mimetype, raw=raw,**kwargs)

    registerField(SourceCodeField,
                  title='SourceCodeField',
                  description='Like AT TextField but with colorise code,pre tags')

