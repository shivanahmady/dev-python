import main


def test_index():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get('/')
    assert r.status_code == 200
    assert 'Hello World' in r.data.decode('utf-8')


def test_a():
    main.app.testing = True
    client = main.app.test_client()
    r = client.get('/api/v1/ispangram/fsfd')
    assert r.status_code == 200

def test_b():
    main.app.testing = True
    client = main.app.test_client()
    r = client.get('/api/v1/ispangram/abcdefghijklmnopqrstuvwxyz')
    assert r.status_code == 200
