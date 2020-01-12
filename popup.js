var tab = new Object;

chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
    tab = tabs[0].url;
    console.log(tab);
    // send tab to backend 
});

//white out this button until parse is finished and then display results
document.addEventListener('DOMContentLoaded', function() {
    var checkPage = document.getElementById('checkPage');
    // onClick's logic below:
    checkPage.addEventListener('click', function() {
        chrome.tabs.create({"url": "https://i.pinimg.com/originals/88/3f/32/883f325d4c3fa9a4d73c4470f9483a22.jpg"});
    });
});
