(function() {
  var point = {
  	id: "point",
    x: 100,
    y: 100,
    z: 0,
  }

  function greet(e) {
      if (this instanceof HTMLElement) {
      	console.log(this.id)
      }
  }
  
  window.addEventListener("load", function() {
      var responder = document.getElementById("widgetOne")
      responder && responder.addEventListener("click", greet)

      var responder = document.getElementById("widgetTwo")
      responder && responder.addEventListener("click", greet)
  })
})()
