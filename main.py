from backend import create_server

app = create_server()

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,
            debug=True)
