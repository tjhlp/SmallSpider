from . import create_app

app = create_app()


@app.route('/', methods=['get', 'post'])
def hello_world():
    return 'hello world'


if __name__ == '__main__':
    # url = {rule.endpoint: rule.rule for rule in app.url_map.iter_rules()}
    app.run(debug=True)
