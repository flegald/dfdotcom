from pyramid.view import view_config



@view_config(route_name='home',
            renderer='templates/index.jinja2')
def list_view(request):
    """Show the homepage."""
    message = "Hello"
    return {'message': message}
