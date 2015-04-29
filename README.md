# facebook_post_dumper
A python script for downloading posts from a facebook user, group, event, or page as a CSV file. 

To use this script, you'll need an access token from facebook. You can get one from facebook's Graph API Explorer by clicking "Get Token", giving it whatever permissions you wish, and copying the text in the token box: 
<https://developers.facebook.com/tools/explorer/145634995501895/> (n.b. these tokens expire after a few hours. If this happens, don't worry, just go get another token. They're free and unlimited!)

You'll also need to know the facebook ID of the page you want to download posts from. Often, this can be found in the URL of the page. Otherwise, here is a great tool to find it for you:
<http://findmyfacebookid.com/>

You'll need these libraries: `facebook` and `pandas`. On linux, you can install them with the command:
`sudo pip install facebook pandas` 

To use the script, download (or git clone) the `facebook_post_dumper.py` file. Open it with your favorite editor and fill in the `token` and `pid` values near the top with the token and page ID from facebook. If you like, you can also change the `max_posts` variable to increase or decrease the number of posts downloaded. Then save the file and run the script.

**Planned Features:**
* command line arguments
* optional additional post data
* output file naming
* image downloading
* link downloading
