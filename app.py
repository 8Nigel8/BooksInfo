from src.api.utils.settings import create_app, init_db

init_db()
app = create_app()


@app.route('/')
def health_check():
    return 'Still alive!'


if __name__ == '__main__':
    app.run()
    