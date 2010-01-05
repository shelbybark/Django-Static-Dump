from django.core.management.base import NoArgsCommand, BaseCommand
from optparse import OptionParser, make_option

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option("--host", dest="host", default="127.0.0.1"),
        make_option("--port", dest="port", default="8000"),
    )
    help = "static build dump"
    
    
    def handle(self, **options):

        from urllib2 import urlopen
        import os
        import shutil
        import re


        print "django static build dump"

        PROJECT_DIR = os.getcwd()
        DUMP_DIR = PROJECT_DIR + '/dump/'

        if os.path.exists(DUMP_DIR):
            print "Sorry, that directory already exists. Delete the 'dump' directory and try again"
        else:
    
            # Create the dump directory
            os.mkdir(DUMP_DIR)

            shutil.copytree('media/',DUMP_DIR + 'media/') 

    
            # import django settings
            #from django.conf import settings
            import urls
            
            url_pat = urls.urlpatterns

            urlStr = 'http://' + options["host"] + ':' + options["port"]

            
            for item in url_pat:
                item = str(item.regex.pattern)
                item=item[item.find("^")+1:item.find("$")]
                
                
                if item != "media/(?P<path>.*)":
                    if item == '':
                        uPath = ''
                        sPath = 'index.html'
                    else:
                        uPath = '/' + item
                        sPath = '/' + item + 'index.html'
                        os.makedirs(DUMP_DIR + uPath)
                    
                    os.system('touch ' + DUMP_DIR + sPath)
                    
                    urlStrNew = urlStr + uPath
                    
                    fHandle = urlopen(urlStrNew)
                    str1 = fHandle.read()
                    fHandle.close()
                    
                    d_file = DUMP_DIR + uPath + 'index.html'
                    
                    new_static = open(d_file, "r+")
                    new_static.write(str1)
                    new_static.close()

        print "====== COMPLETE ======"

