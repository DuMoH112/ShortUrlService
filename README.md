<h1 align="center">Short url service (SUS)</h1>
<p>Service for translate long url to short</p>

<hr>
<hr>
<h2><span>POST</span> create_short_url</h2>
<p>192.168.0.100:5555/create_short_url</p>

<p>BODY raw</p>

```json
{
    "long_url": "https://github.com/DuMoH112/ShortUrlService"
}
```

<p>Response</p>

`"http://192.168.0.100:5555/b27147014756"`

<hr>
<h2><span>GET</span> url_handler</h2>
<p>192.168.0.100:5555/{{short_url}}</p>

Redirected to long url web site

<hr>
<h2><span>GET</span> get_full_url</h2>
<p>192.168.0.100:5555/get_full_url/{{short_url}}</p>

<p>Response</p>

`"https://github.com/DuMoH112/ShortUrlService"`
