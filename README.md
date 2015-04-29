# facebook_post_dumper
A python script for downloading posts from a facebook user, group, or page as CSV.

To use this script, you'll need an access token from facebook. You can get one from facebook's Graph API Explorer by clicking "Get Token", giving it whatever permissions you wish, and copying the text in the token box: 
<https://developers.facebook.com/tools/explorer/145634995501895/>

You'll also need to know the facebook ID of the page you want to download posts from. Often, this can be found in the URL of the page. Otherwise, here is a great tool to find it for you:
<http://findmyfacebookid.com/>

You'll need these libraries: `facebook` and `pandas`. On linux, you can install them with the command:
`sudo pip install facebook pandas` 

