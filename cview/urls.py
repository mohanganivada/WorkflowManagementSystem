from cview import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('registration',views.registration,name='registration'),
    path('authentication',views.authentication,name='authentication'), #blank means main root webpage
    path('form',views.form,name="form"),
    path('form1',views.form1,name="form1"),
    path('saved',views.saved,name="saved"),
    path('ajax',views.ajax,name='ajax'),
    path('package',views.package,name='package'),
    path('assign',views.assign,name="assign"),
    path('accept',views.accept,name="accept"),
    path('acceptresume',views.acceptresume,name="accept"),
    path('createupdateemployee',views.createUpdateEmployee,name="createupdateemployee"),
    path('addcomments',views.addcomments,name="addcomments"),
    path('updatepackages',views.updatepackages,name="updatepackages"),
    path('uploadcv',views.uploadcv,name="uploadcv"),
    path('feedback',views.feedback,name="feedback"),
    path('user',views.user,name='user'),
    path('editingscreen',views.editingscreen,name='editingscreen'),
    path('test',views.test,name='test'),
    path('ats',views.ats,name="ats")
]