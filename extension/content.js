chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
    alert(tabs[0].url);
  });