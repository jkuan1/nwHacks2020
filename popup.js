document.addEventListener('DOMContentLoaded', function() {
    var checkPageButton = document.getElementById('checkPage');
    checkPageButton.addEventListener('click', function() {
  
        chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
            console.log(tabs[0].url);
        });
        
        location.href = 'http://www.google.com';
    
    }, false);
  }, false);