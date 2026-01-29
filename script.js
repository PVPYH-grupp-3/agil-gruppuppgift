const myBody = document.querySelector("body")


myBody.addEventListener("keydown", function (event) {

    if (event.key === "Enter") {
        console.log("Du har klickat Enter")
    }
    else if (event.key === "Backspace") {
        console.log("Du har klickat Backspace")
    }
    else {
        console.log(event.key)
    }
    
})