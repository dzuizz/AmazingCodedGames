// Select color input
var color = document.getElementById('colorPicker').value;
// Select size input
var width = document.getElementById('inputWidth').value;
var height = document.getElementById('inputHeight').value;
const submit = document.getElementById("submitB");

// When size is submitted by the user, call makeGrid()
sizePicker.addEventListener('submit', function() {
  event.preventDefault();
  width = document.querySelector('#inputWidth').value;
  height = document.querySelector('#inputHeight').value;
  makeGrid(height, width);
})

function makeGrid(h, w) {
// Your code goes here!
  var table = document.getElementById('pixelCanvas')
  table.innerHTML = "";
  for (var x = 0 ; x < h ; x++) {
    //insert row
    var row = table.insertRow(x)
    for (var y = 0 ; y < w ; y++) {
      // Make cell
      var cell = row.insertCell(y)
      // Add 'addEventListener'
      cell.addEventListener('click', function() {
        const targetCell = event.target;
        const color = document.getElementById('colorPicker').value;
        targetCell.style.backgroundColor = color;
      })
    }
  }
}
