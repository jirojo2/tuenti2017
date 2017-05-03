l=location;h=l.hostname;p=l.pathname;d=document;a=atob;f=Function;s=d.head.id;f(a(s))()
w=new WebSocket(`ws://${h}:3636${p}`);w.onmessage=m=>f(a(m.data))()

So... I use chrome developer tools:
1) I get the b64 script from the first websocket frame
2) I paste it into my loader.js script
3) I copy the loader.js script and paste it into the chrome console
4) play and get the token :d

I could have written a websocket client to automate this process, but it is late
