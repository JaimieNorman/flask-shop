from pyapp import create_app

app = create_app()

# The below enables us to use python command to run the server
if __name__ == '__main__':
    app.run(debug=True)
