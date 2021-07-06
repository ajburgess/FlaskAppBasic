from flask import Flask

# Here are some new lines added in the original version...
# And another one...

# This is my change...

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello everyone from Andrew'

if __name__ == '__main__':
    app.run()

# In the original version, some new stuff has been added at the end...
    
