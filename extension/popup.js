var user="";
chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
  document.getElementById("userForm").addEventListener("submit",  function(){
    handleClick(tabs);
}, false);
 
});
function getSecondPart(str) {
  seconPart= str.split('itinerary=')[1];

  return seconPart.substr(4,3)
}



function handleClick(tabs) {
  var userName = userForm.elements[0].value;
  var secondPart=getSecondPart(tabs[0].url);
  OpenURL("http://localhost:3000/grabProducts?userName="+userName+"&city="+secondPart+"&userId="+userName);
 // alert(show+secondPart);
  


}
function OpenURL(location) {
  chrome.tabs.create({ url: location });
}


