# Flask Quick Primer

## Overview

This repo is a quick primer on using the [Flask micro-framework](http://flask.pocoo.org/).

The primer is done via a code progression using tags.  The tags can be viewed by either execvuting ```git tag``` in the
repository or on the [GitHub Tags page](https://github.com/aenglander/lvpython-flask-talk/tags).  Each tag represents
added functionality in the primer.

## Obtaining the Primer

To obtain the primer, simply clone the repository.

Git CLI Example:

```bash
git clone https://github.com/aenglander/lvpython-flask-talk.git
cd lvpython-flask-talk
```

## Viewing the Primer Sections

Primer sections are designated with Git tags.

Git CLI Example:

```bash 
$ git tag
1-hello-world
2-variable-routes
3-jinja-templates
4-reverse-routing-for-links
5-static-assets
6-form-session 
```

## Switching To A Different Primer Section

Switch to the appropriate tag in the repository to show the code for a section.

Git CLI Example:

```bash
$ git reset --hard 1-hello-world
HEAD is now at e1be601 Hello World
```

GitHub Repository Example:

https://github.com/aenglander/lvpython-flask-talk/compare/1-hello-world...2-variable-routes

## Seeing the Code Changes

You can view the code changes between primer sections using *diffs* of the tags.

Git CLI Example:

```bash
$ git diff 1-hello-world 2-variable-routes
diff --git a/app.py b/app.py
index 07b952c..f489716 100644
--- a/app.py
+++ b/app.py
@@ -5,5 +5,9 @@ app = Flask(__name__)
 def hello_world():
     return 'Hello World!'
 
+@app.route('/hello/<noun>')
+def hello_noun(noun):
+    return 'Hello %s!' % noun
+
 if __name__ == '__main__':
     app.run(debug=True)
```

## Primer Sections

### Hello World

The tag [1-hello-world](https://github.com/aenglander/lvpython-flask-talk/releases/tag/1-hello-world) provides the
basic code needed to create an HTTP response for a default route.

### Variable Routes

The tag [2-variable-routes](https://github.com/aenglander/lvpython-flask-talk/releases/tag/2-variable-routes) shows
how to access data provided in the URL within the controller method for a route.

### Jinja Templates

The tag [3-jinja-templates](https://github.com/aenglander/lvpython-flask-talk/releases/tag/3-jinja-templates) shows
how to use Jinja templates to return HTML from your routes.

### Reverse Routing for Links

The tag [4-reverse-routing-for-links](https://github.com/aenglander/lvpython-flask-talk/releases/tag/4-reverse-routing-for-links)
shows how to dynamically reference route locations within a Jinja template for linking within your site.

### Static Assets

The tag [5-static-assets](https://github.com/aenglander/lvpython-flask-talk/releases/tag/5-static-assets) shows how to
reference static assets like CSS, JavaScript, and images within your Jinja templates.

### Forms and Sessions

The tag [6-form-session](https://github.com/aenglander/lvpython-flask-talk/releases/tag/6-form-session) shows how to
process form data, use flash messages and a cookie based session to interact with the user across requests, and redirect
after a POST request using reverse routing inside the controller.

 