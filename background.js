var string;
chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
    var background_url = tabs[0].url;
    console.log(background_url);
    string = JSON.stringify(background_url);

    // var fs = require('fs');
    // fs.writeFile("url.json", backgroun_url, function(err, result) {
    // if(err) console.log('error', err);
// });
});

