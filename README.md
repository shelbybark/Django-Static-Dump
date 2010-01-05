Django Static Dump
==================

Django Static Dump was created to meet a need I had while working on "static builds" of design comps. I needed a way to output a set of static html files after using a simple django app used to build out sample pages from design comps.

You will need to have the manage.py runserver running on your machine for the command to work. The default server it looks for is http://127.0.0.1:8000, but you can pass in your own host and port with the --host and --port parameters.

It's very basic. The script will look at all the urls set up in the urls.py file. and try creating the files based on that. It has no error handling, so, the urls must all work. Also, since the need I had did not include any real views, anything other than a "direct_to_template" probably would not work. It also attempts to copy over the contents of "/media/" which would reside in the project folder.

