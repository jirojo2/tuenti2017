First we force download resume on the /ghost endpoint and we get a base64 encoded image.
With the numbers in the img file: 4017-8120, we get the following phrase:

curl -v -k -H "range: bytes=4017-8120" https://52.49.91.111:8443/ghost
I feel confined, only free to expand myself within boundaries

HTTP/1.1 => 505 Version not supported
So... lets try with HTTP/1.0... nope
So... HTTP2! PUSH resources... so the favicon DID make sense after all

E:\Dev\tuenti2017\lvl5>h2c connect 52.49.91.111:8443

E:\Dev\tuenti2017\lvl5>h2c get /ghost
iVBORw0KGgoAA

E:\Dev\tuenti2017\lvl5>h2c set range "bytes=4017-8120"

E:\Dev\tuenti2017\lvl5>h2c get /ghost
You found me. Pushing my token, did you get it?


E:\Dev\tuenti2017\lvl5>h2c stream-info
1: GET /ghost closed
2: GET /whisper closed (cached push promise)
3: GET /ghost closed

E:\Dev\tuenti2017\lvl5>h2c get /whisper
YourEffortToRemainWhatYouAreIsWhatLimitsYou
