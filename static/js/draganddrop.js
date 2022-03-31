const dropArea = document.querySelector('.drag-area');
const dragText = document.querySelector('.header');

const initialdragText = document.querySelector('.header');

let button = dropArea.querySelector('.button');
let input = dropArea.querySelector('input');

let file;

// when file is inside drag area
dropArea.addEventListener('dragover', (event) => {
    event.preventDefault();
    dropArea.classList.add('active');
    dragText.textContent = 'Release to Upload';
    // console.log('File is inside the drag area');
  });
  
  // when file leave the drag area
  dropArea.addEventListener('dragleave', () => {
    dropArea.classList.remove('active');
    dragText.textContent = 'Drag and Drop'
  });
  
  // when file is dropped
  dropArea.addEventListener('drop', (event) => {
    event.preventDefault();  
    file = event.dataTransfer.files[0];
    displayFile();
  });
  
  function displayFile() {
    let fileType = file.type;
    console.log(file.type);

    let validExtensions = ['text/plain', 'application/msword', 'application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'];
  
    if (validExtensions.includes(fileType)) {
      dragText.innerHTML = "File Successfully uploaded."
      
    } else {
      //alert('File Type not supported.');
      dropArea.classList.remove('active');
    }
  }
  
  button.onclick = () => {
    input.click();
  };
  
  // when browse
  input.addEventListener('change', function () {
    file = this.files[0];
    dropArea.classList.add('active');
    displayFile();
  });
  
  
  