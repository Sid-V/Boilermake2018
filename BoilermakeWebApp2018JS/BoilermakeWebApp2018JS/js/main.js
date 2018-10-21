// Your code here!
//Task: Open the camera after user clicks the button at the top, and after uploading, 
// the python algorithm should run and set the locations, time and date. Calendar button will add 
//to calendar

var calendarButton = document.getElementById('calendar-button')
var imageInput = document.getElementById('pictureInput')

calendarButton.setEventListener("click", function ({

    //calendar button function
    });

function handleFiles(image) {
    //start python algorithm, probably send request.
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
       
    };
    xhttp.open("GET");
    xhttp.send();
}