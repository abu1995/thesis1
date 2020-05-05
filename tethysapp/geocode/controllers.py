from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button
# from hs_restclient import HydroShare
from hs_restclient import HydroShare, HydroShareAuthBasic


auth = HydroShareAuthBasic(username='abhishekamal18@gmail.com', password='')

hs =HydroShare(auth=auth)    

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    save_button = Button(
        display_text='',
        name='save-button',
        icon='glyphicon glyphicon-floppy-disk',
        style='success',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Save'
        }
    )

    edit_button = Button(
        display_text='',
        name='edit-button',
        icon='glyphicon glyphicon-edit',
        style='warning',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Edit'
        }
    )

    remove_button = Button(
        display_text='',
        name='remove-button',
        icon='glyphicon glyphicon-remove',
        style='danger',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Remove'
        }
    )

    previous_button = Button(
        display_text='Previous',
        name='previous-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Previous'
        }
    )

    next_button = Button(
        display_text='Next',
        name='next-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Next'
        }
    )

    context = {
        'save_button': save_button,
        'edit_button': edit_button,
        'remove_button': remove_button,
        'previous_button': previous_button,
        'next_button': next_button
    }

    return render(request, 'geocode/home.html', context)

@login_required()
def upload_file(request):

    # f = open("demofile3.txt", "w")
    # f.write("Woops! I have deleted the content!")
    # f.close()
    
    # auth = HydroShareAuthBasic(username='myusername', password='mypassword')
    # hs = HydroShare(auth=auth)
    #fpath = '/apps/geocode/upload_file/output.txt'
    fpath = 'tethysapp/geocode/workspaces/app_workspace/output.txt'


   
    hs = HydroShare(auth=auth)
    abstract = 'My abstract'
    title = 'My resource'
    keywords = ('my keyword 1', 'my keyword 2')
    rtype = 'GenericResource'

    metadata = '[{"coverage":{"type":"period", "value":{"start":"01/01/2000", "end":"12/12/2010"}}}, {"creator":{"name":"John Smith"}}, {"creator":{"name":"Lisa Miller"}}]'
    extra_metadata = '{"key-1": "value-1", "key-2": "value-2"}'
    resource_id = hs.createResource(rtype, title, resource_file=fpath, keywords=keywords, abstract=abstract, metadata=metadata, extra_metadata=extra_metadata)

    resource_id = hs.addResourceFile('99319811b9c44f03aa14f47a32aa4111', fpath)

