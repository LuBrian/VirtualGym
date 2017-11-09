
window.onload = function() { 
	var video = document.querySelector("video"),
		info = document.querySelector("span"),
		initial = document.querySelector("i");
		concanenatedVideoElems = "";
		button = document.querySelector("button");
		vidData = [];
		videoInfo = {};

	function getElementCSSSize(el) {
		var cs = getComputedStyle(el);
		var w = parseInt(cs.getPropertyValue("width"), 10);
		var h = parseInt(cs.getPropertyValue("height"), 10);
		return {width: w, height: h}
	}
	
	function saveText(text, filename){
		var a = document.createElement('a');
		a.setAttribute('href', 'data:text/plain;charset=utf-u,'+encodeURIComponent(text));
		a.setAttribute('download', filename);
		a.click()
	}

	function saveToJSON(event) {
		saveText(JSON.stringify(vidData), "filename.json");
		//alert("test")
	}
	function mouseHandler(event) {
		this.pause();
		var annotation = prompt("Please enter your annotation:");
		var size = getElementCSSSize(this);
		var scaleX = this.videoWidth / size.width;
		var scaleY = this.videoHeight / size.height;

		var rect = this.getBoundingClientRect();  // absolute position of element
		var x = ((event.clientX - rect.left) * scaleX + 0.5)|0;
		var y = ((event.clientY - rect.top ) * scaleY + 0.5)|0;

		//info.innerHTML = "x: " + x + " y: " + y;
		
		if (annotation != "" && annotation != null)
		{
			vidData.push({x: this.videoWidth, y: this.videoHeight, time: this.currentTime, annotation: annotation});

			concanenatedVideoElems = concanenatedVideoElems + "(video: " + this.videoWidth + " x " + this.videoHeight + ")" + "time : "+ this.currentTime + " annotation: "+annotation;
			//initial.innerHTML = concanenatedVideoElems
		}
		this.play();
	}
	
	button.addEventListener("click", saveToJSON);
	video.addEventListener("click", mouseHandler);
	
}


