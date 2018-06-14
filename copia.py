logo = open('python-logo.png', 'rb')
data = logo.read()
logo.close()

logo2 = open('python2-logo.png', 'wb')
logo2.write(data)
logo2.close()