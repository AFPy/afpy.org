# -*- coding: utf-8 -*-

from Products.Archetypes.public import *
from Products.ATContentTypes.content import schemata
from Products.Archetypes import atapi
from afpy.contenttypes.content.Fields import SourceCodeField
from afpy.contenttypes.config import *
from DateTime.DateTime import DateTime


AFPYBaseSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    TextField('description',
              default='',
    	      searchable=True,
    	      isMetadata=True,
    	      accessor="Description",
    	      widget=TextAreaWidget(label='Description',
    		                    description='An administative summary of the content',
    				    label_msgid='label_description',
    				    description_msgid='help_description',
    				    i18n_domain="plone")
    				    ),
    ))


#################################
## Base Fields
#################################


EffectiveDateSchema =  Schema((

    DateTimeField('effectiveDate',
                  searchable=True,
		  accessor="EffectiveDate",
		  mutator="setEffectiveDate",
		  default=DateTime(),
		  required=True,
		  isMetadata=True,
		  widget=CalendarWidget(label='Effective Date',
		                        description='Date when the content should become available on the public site',
					label_msgid='label_effective_date',
					description_msgid='help_effective_date',
					i18n_domain='plone')
					),																			  
    ))

TextSchema = Schema ((

    TextField('text',
              required=False,
	      searchable=True,
	      validators=('isTidyHtmlWithCleanup',),
              default_content_type = 'text/html',
	      default_output_type = 'text/html',
	      allowable_content_types = ('text/html',
	                                 'text/structured',
	                                 'text/restructured',
	                                 'text/plain',),
	      widget = RichWidget(description="The body text of the document.",
				  description_msgid = "help_body_text",
				  label = "Body text",
				  label_msgid = "label_body_text",
				  rows=25,
				  i18n_domain="plone")
				  ),
    ))

SourceCodeSchema = Schema ((

    SourceCodeField('text',
              required=False,
	      searchable=True,
              default_content_type = 'text/html',
	      default_output_type = 'text/html',
	      allowable_content_types = ('text/html',
	                                 'text/structured',
	                                 'text/restructured',
	                                 'text/plain',),
	      widget = RichWidget(description=" ",
				  label = "Text",
				  label_msgid = "label_text",
                                  description_msgid="help_text",
				  rows=25,
				  i18n_domain="afpy")
				  ),
    ))

ImageSchema = Schema ((

    ImageField('image',
               required=False,
	       sizes={'small' : (100,100),
	              'medium' : (200, 200),
		      'large' : (300, 300)},
	       widget=ImageWidget(label='Image',
				  description='You can upload here an image.',
				  label_msgid='label_image',
				  description_msgid='help_image',
				  i18n_domain='plone')
				  ),
															
    ))

FileSchema = Schema ((

     FileField('file',
               storage=AttributeStorage(),
	       widget=FileWidget(label='Attached file',
				 description='Upload here an attached file.',
				 label_msgid='label_file',
				 description_msgid='help_file',
				 i18n_domain='plone')
				 ),
															
    ))

LinkSchema = Schema((

    StringField('link',
	        required=False,
		searchable=True,
		validators=('isURL',),
		widget=StringWidget(label='Link',
		                    description=' ',
				    label_msgid='label_url',
				    i18n_domain='plone')
				    ),																													 
    ))

#####################################
## Content Types Schemas
######################################

PythonHowtoSchema = AFPYBaseSchema.copy() + SourceCodeSchema.copy() + Schema ((
    
    LinesField('python_modules',
               required=False,
	       searchable=True,
	       widget=LinesWidget(label='Python modules',
	                          description='Enter here a list of python modules used inside this howto. Please put only important python modules here.',
				  label_msgid='label_python_modules',
				  description_msgid='help_python_modules',
				  i18n_domain='afpy')
				  ),
    LinesField('categories',
               required=True,
	       searchable=True,
	       vocabulary=DisplayList(PYTHON_HOWTO_CATEGORIES),
	       widget=MultiSelectionWidget(label='Categories',
	                                   description='Select here one or more catagories for this python howto',
					   label_msgid='label_categories',
					   description_msgid='help_categories',
					   i18n_domain='afpy')
					   ),

    StringField('python_version',
                required=True,
                searchable=True,
                widget=StringWidget(label='Version python'),
                                    description=' '
                                       ),
	       
  ))

ZopeHowtoSchema = AFPYBaseSchema.copy() + SourceCodeSchema.copy() + Schema ((
    
    LinesField('categories',
               required=True,
	       searchable=True,
	       vocabulary=ENVIRONMENT_GROUPS,
	       widget=MultiSelectionWidget(label='Categories',
	                                   description='Select here one or more catagories for this python howto',
					   label_msgid='label_categories',
					   description_msgid='help_categories',
					   i18n_domain='afpy')
					   ),
  ))

AFPYNewsSchema = AFPYBaseSchema.copy() + EffectiveDateSchema.copy() + TextSchema.copy() + ImageSchema.copy() + FileSchema.copy() + LinkSchema.copy() + Schema ((

    StringField('section',
                required=True,
		default='AFPY',
		vocabulary=SECTION_GROUPS,
		widget=SelectionWidget(label='Section',
		                       description='Select here a section for this news.',
				       label_msgid='label_section',
				       description_msgid='help_section',
				       i18n_domain='afpy')
				       ),
    ))

AFPYEventSchema = AFPYBaseSchema.copy() + TextSchema.copy() + ImageSchema.copy() + FileSchema.copy() + LinkSchema.copy() + Schema((

    DateTimeField('start_date',
                  required=True,
        	  searchable=True,
		  accessor='start',
		  write_permission = 'Change portal events',
		  default_method=DateTime,
		  widget=CalendarWidget(label='Event starts',
		                        description='Click the calendar icon to select a date or browse the calendar.',
					label_msgid='label_event_start',
					description_msgid='help_event_start',
					i18n_domain='plone')
					),

    DateTimeField('end_date',
		  required=True,
		  searchable=True,
		  accessor='end',
		  write_permission = 'Change portal events',
		  default_method=DateTime,
		  widget=CalendarWidget(label='Event ends',
		                        description='Click the calendar icon to select a date or browse the calendar.',
		                        label_msgid='label_event_end',
					description_msgid='help_event_end',
					i18n_domain='plone')
					),
    ))

AFPYLinkSchema = AFPYBaseSchema.copy() + ImageSchema.copy() + Schema((
  
    StringField('remoteUrl',
                required=True,
		searchable=True,
		validators=('isURL',),
		widget=StringWidget(label='Link',
				    description='Prefix is optional; if not provided, the link will be relative.',
				    label_msgid='label_url',
				    description_msgid='help_url',
				    i18n_domain='plone')
				    ),																													 
    ))

AFPYPressReleaseSchema = AFPYBaseSchema.copy() + EffectiveDateSchema.copy() + TextSchema.copy() + FileSchema.copy()

AFPYProductSchema = AFPYBaseSchema.copy() + TextSchema.copy() + LinkSchema.copy() + ImageSchema.copy() + Schema((

    StringField('version',
                widget=StringWidget(label='Version',
		                    description=' ')
				    ),

    StringField('download_url',
                validators=('isURL',),
		widget=StringWidget(label='Download URL',
		                    description=' ',
				    label_msgid='label_download_url',
				    i18n_domain='afpy')
				    ),

    StringField('valuation',
		required=True,
		default='1',
		vocabulary=VALUATION_GROUPS,
		widget=SelectionWidget(format='radio',
		                       description='Product valuation',
				       label='Valuation',
				       label_msgid='label_valuation',
				       description_msgid='help_valuation',
				       i18n_domain='afpy')
				       ),

    StringField('environment',
                required=True,
		searchable=True,
		vocabulary=ENVIRONMENT_GROUPS,
		widget=MultiSelectionWidget(format='select',
					    description='Product environment',
					    label='Environment',
					    label_msgid='label_environment',
					    description_msgid='help_environment',
					    i18n_domain='afpy')
					    ),

))

FicheSchema = AFPYBaseSchema.copy() + TextSchema.copy() + LinkSchema.copy() + ImageSchema.copy() + Schema((

    StringField('version',
                widget=StringWidget(label='Version',
		                    description=' ')
				    ),

    StringField('download_url',
                validators=('isURL',),
		widget=StringWidget(label='Download URL',
		                    description=' ',
				    label_msgid='label_download_url',
				    i18n_domain='afpy')
				    ),

    StringField('valuation',
		required=True,
		default='1',
		vocabulary=VALUATION_GROUPS,
		widget=SelectionWidget(format='radio',
		                       description='Product valuation',
				       label='Valuation',
				       label_msgid='label_valuation',
				       description_msgid='help_valuation',
				       i18n_domain='afpy')
				       ),

))

FichePythonSchema = FicheSchema.copy()

FicheZopeSchema = FicheSchema.copy() + Schema((

    StringField('environment',
        required=True,
		searchable=True,
		vocabulary=ENVIRONMENT_GROUPS,
		widget=MultiSelectionWidget(format='select',
					    description='Product environment',
					    label='Environment',
					    label_msgid='label_environment',
					    description_msgid='help_environment',
					    i18n_domain='afpy')
					    ),

))




AFPYJobSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema(( 
    TextField('description',
        searchable=True,
        isMetadata=True,
        required=True,
        accessor="Description",
        widget=TextAreaWidget(
            label='Poste',
            description='Description du poste a pourvoir',
        ),
    ),
)) + TextSchema.copy() + Schema((
    StringField('sourceUrl',
        validators=('isURL',),
        widget=StringWidget(label='Url',
                    description='Url de l\'annonce originale',
                )
    ),                                                                                                                     
    StringField('company',
        required=True,
        widget=StringWidget(
            label='Companie',
            description='Nom de votre entreprise',
        ),
    ),
    ImageField('image',
           sizes={'medium' : (200, 200)},
           widget=ImageWidget(label='Logo',
                  description='Logo de l\'entreprise.',
          ),
    ),
    LinesField('address',
        widget=LinesWidget(
            label='Adresse',
            description='Adresse postale de l\'entreprise',
        ),
    ),
    StringField('remoteUrl',
        searchable=True,
        validators=('isURL',),
        widget=StringWidget(label='Web site',
                    description='Url du site web de l\'entreprise',
                )
    ),                                                                                                                     

    StringField('contact',
        required=True,
        widget=StringWidget(
            label='Contact',
            description='Nom du contact',
        ),
    ),
    StringField('email',
        required=True,
        widget=StringWidget(
            label='Email',
            description='Email du contact',
        ),
    ),
    StringField('phone',
        widget=StringWidget(
            label='Téléphone',
            description='Téléphone du contact',
        ),
    ),
))


