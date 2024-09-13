from backend import create_server

app = create_server()

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=3000,
            debug=True)
