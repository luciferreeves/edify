from edify.library import url

def test_valid_http_url():
    assert url("http://example.com")

def test_valid_https_url():
    assert url("https://example.com/path")

def test_bad_url():
    assert not url("nope !!!")
