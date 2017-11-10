
// moved to addAnnotation html
// because can't get {{instance}} used by ajax
window.onload = function() {
	
	var video = document.querySelector("video"),
		info = document.querySelector("span"),
		initial = document.querySelector("i");
		concanenatedVideoElems = "";
		button = document.querySelector("button");
		annotationSubmit =  document.getElementById("annotation_submit")
		vidData = [];
		videoInfo = {};
		details = "";
		Xval = 0.0;
		Yval = 0.0;
		timeStep = 0.0;
		localdata = "";

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
		document.getElementById("annotationForm_container").style.display = "block";


		// var annotation = prompt("Please enter your annotation:");
		// var annotation = "nice"
		var size = getElementCSSSize(this);
		var scaleX = this.videoWidth / size.width;
		var scaleY = this.videoHeight / size.height;

		var rect = this.getBoundingClientRect();  // absolute position of element
		var x = ((event.clientX - rect.left) * scaleX + 0.5)|0;
		var y = ((event.clientY - rect.top ) * scaleY + 0.5)|0;
		Xval = x;
		Yval = y;
		// console.log(x);
		// console.log(y);
		timeStep = this.currentTime;
		
	}

<<<<<<< HEAD
			concanenatedVideoElems = concanenatedVideoElems + "(video: " + this.videoWidth + " x " + this.videoHeight + ")" + "time : "+ this.currentTime + " annotation: "+annotation;
			//initial.innerHTML = concanenatedVideoElems
		}
		console.log(vidData);
		this.play();
=======
	function callback(){
		console.log('success call back');
>>>>>>> 70df6f2b3a1b07bb7a54e36ab03d44e07ceabae9
	}
	
	// button.addEventListener("click", saveToJSON);
	video.addEventListener("click", mouseHandler);

	annotationSubmit.addEventListener('click', function() {
	    details = $("textarea").val();
	    console.log(details);
	    if (details != "" && details != null)
		{
			vidData.push({x: Xval, y: Yval, time: timeStep, annotation: details});
			localdata = JSON.stringify(vidData);
			// concanenatedVideoElems = concanenatedVideoElems + "(video: " + this.videoWidth + " x " + this.videoHeight + ")" + "time : "+ this.currentTime + " annotation: "+annotation;
			//initial.innerHTML = concanenatedVideoElems

			$.ajax({
				type: 'POST',
				url: '/annotations/{{ instance.video_id }}/',
				data :  localdata,
				dataType:'Json'
			}).done(function(){
			// This is the ajax.done() method, where you can fire events after the ajax method is complete 

			// For instance, you could hide/display your add/remove button here
				console.log('success call back');
			});
		}


		// https://stackoverflow.com/questions/36201666/submit-without-refresh-in-django
		
		document.getElementById("annotation_detial").value = "";
		video.play();
		document.getElementById("annotationForm_container").style.display = "none";
		


		
	}, false);
 	
 	$('#annotation_vid').on('timeupdate',function(event){
 		console.log(this.currentTime);
 		if(vidData.length != 0){
 			console.log(vidData);
 		};


 	});
	
}


