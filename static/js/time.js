function updateTime() {
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var seconds = now.getSeconds();
  
    hours = checkTime(hours);
    minutes = checkTime(minutes);
    seconds = checkTime(seconds);
  
    var timeString = hours + ":" + minutes + ":" + seconds;
    document.getElementById("current-time").innerHTML = timeString;
  
    setTimeout(updateTime, 1000);
  }
  
  function checkTime(i) {
    if (i < 10) {
      i = "0" + i;
    }
    return i;
  }
  
  updateTime();