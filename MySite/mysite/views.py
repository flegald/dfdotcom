from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/index.jinja2')
def home_view(request):
    """Display the homepage."""
    message = "Hello"
    return {'message': message}


@view_config(route_name='portfolio', renderer='templates/portfolio.jinja2')
def portfolio_view(request):
    """Display portfolio."""
    message = "Hello"
    return {'message': message}


@view_config(route_name='about', renderer='templates/about.jinja2')
def about_view(request):
    """Display About Me."""
    message = "Hello"
    return {'message': message}


@view_config(route_name='contact', renderer='templates/contact.jinja2')
def contact_view(request):
    """Display Contact."""
    message = "Hello"
    return {'message': message}


@view_config(route_name='imager', renderer='templates/imager.jinja2')
def imager_view(request):
    """Display Imager Detail."""
    message = "Hello"
    return {'message': message}
