chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
    var url = tabs[0].url;
    console.log(url);
});

document.addEventListener('DOMContentLoaded', function() {
    var checkPage = document.getElementById('checkPage');
    // onClick's logic below:
    checkPage.addEventListener('click', function() {
        chrome.tabs.create({"url": "https://google.com"});
    });
});
