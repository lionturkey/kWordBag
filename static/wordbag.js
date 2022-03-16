

const textArea = document.querySelector("#ko-text");
const processButton = document.querySelector("#process-button");
const outputArticle = document.querySelector("#output");

processButton.addEventListener("click", processText);


function processText() {
    let text = textArea.value.replace('(', '( ').replace(')', ' )');
    let post = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({"text": text})
    };
    
    fetch('api/processtext', post)
    .then(response => response.json())
    .then(json => {
        outputArticle.innerHTML = json.html;
    });
}



// let outputHTML;
    
// fetch('api/processtext', post)
// .then(response => response.json())
// .then(json => { outputHTML = JSON.parse(json).html });

// console.log(outputHTML);




// fetch('api/processtext', post)
// .then(response => response.json())
// .then(json => console.log(json));