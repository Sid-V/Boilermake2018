// Your code here!
//Task: Open the camera after user clicks the button at the top, and after uploading, 
// the python algorithm should run and set the locations, time and date. Calendar button will add 
//to calendar

$('#calendar-button').click(
    function(){
        $.ajax({
            type: "POST",
            url: "/../../ocr.py",
            data: { param: "https://calendar.purdue.edu/calendar/displaymedia.aspx?whatToDo=picture&id=100697" },
            success: callbackFunc
        });
});


var calendarButton = document.getElementById('calendar-button');
var imageInput = document.getElementById('pictureInput');


function callbackFunc(response){
    console.log(response);
}