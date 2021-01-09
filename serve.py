from beerpbl.frontend.index import app


def main():
    app.run_server(host='0.0.0.0', port=8055)


if __name__ == '__main__':
    main()
