window.onload = function () {
	function randomInteger(min, max) {
  		let rand = min + Math.random() * (max + 1 - min);
  		return Math.floor(rand);
	}
	var width = window.innerWidth;
	var	height = window.innerHeight;
	var canvas = document.getElementById('canvas');
	var controls;

	canvas.setAttribute('width', width);
	canvas.setAttribute('height', height);

	var renderer = new THREE.WebGLRenderer({canvas: canvas});
	renderer.setClearColor(0xFFFFFF);
	renderer.shadowMapenabled = true;

	var scene = new THREE.Scene();

	var camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 5000);

	controls = new THREE.OrbitControls (camera, renderer.domElement);

	const color = 0xFFFFFF;
	const intensity = 1;
	light = new THREE.DirectionalLight( 0xffffff );
	light.position.set( 38, 82, 1 );
	light.castShadow = true;
	scene.add(light);
	scene.add(light.target);
	camera.position.set(0, 500, 1000);

	var score = 0;

	var k = 0.5;

	var geometry_plane = new THREE.PlaneGeometry(1000,1000);
	var material_plane = new THREE.MeshPhongMaterial( {color: 0x6C6C6C,wireframe: false});
	
	var geometry_player = new THREE.CubeGeometry(10,10,10);
	var material_player = new THREE.MeshPhongMaterial( {color: 0x06FF18,wireframe: false});

	var geometry_target = new THREE.CubeGeometry(5,5,5);
	var material_target = new THREE.MeshPhongMaterial( {color: 0xFF0000,wireframe: false});

	function generate_targets(geometry_target, material_target){
		for (var i = 1; i<5; i++) {
			window['target'+i] = new THREE.Mesh(geometry_target, material_target);
			window['target'+i].position.x = randomInteger(-400, 400);
			window['target'+i].position.z = randomInteger(-400, 400);
			window['target'+i].position.y += 2,5;
			scene.add(window['target'+i]);
		}
	}
	//принимает имя
	document.querySelector("#start").addEventListener("click", Handler);
	function Handler(event) {
	    fetch('/user_data')
	        .then((response) => {
	            return response.json();
	        })
	        .then((myjson) => {
	            console.log(myjson);
	        });
	}
	function random_position(target){
		target.x = randomInteger(-400, 400);
		target.z = randomInteger(-400, 400);
	}
	generate_targets(geometry_target, material_target);
	var player = new THREE.Mesh(geometry_player, material_player);
	player.position.y += 5;
	player.castShadow = true;
	player.receiveShadow =true;
	scene.add(player);
	camera.lookAt(player.position);

	var plane = new THREE.Mesh(geometry_plane, material_plane);
	plane.rotation.x=-0.5*Math.PI;
	plane.receiveShadow = true;
	scene.add(plane);

	let flag = 1
	var text = document.createElement('div');
	text.style.position = 'absolute';
	text.style.width = 100;
	text.style.height = 100;
	text.innerHTML = "Your speed:" + k;
	text.style.color = 'black';
	text.style.top = 30 + 'px';
	text.style.left = 10 + 'px';
	document.body.appendChild(text);
	var text2 = document.createElement('div');
	text2.style.position = 'absolute';
	text2.style.width = 100;
	text2.style.height = 100;
	text2.innerHTML = "Your score:" + score;
	text2.style.color = 'black';
	text2.style.top = 10 + 'px';
	text2.style.left = 10 + 'px';
	document.body.appendChild(text2);
	document.addEventListener("keydown", function(event){
	    var keyCode = event.which;
	    if (keyCode == 87) {
	        flag = 1;
	    } else if (keyCode == 83) {
	        flag = 2;
	    } else if (keyCode == 65) {
	        flag = 3;
	    } else if (keyCode == 68) {
	        flag = 4;
	    }	
	});
	function loop() {
		updatePlayer()
		if (Math.abs(player.position.x) > 480 || player.position.z > 500 || player.position.z < -515) {
			end();
		}
		check(target1.position, target2.position, target3.position, target4.position);
		camera.lookAt(player.position);
		var width = window.innerWidth;
		var	height = window.innerHeight;
		canvas.setAttribute('width', width);
		canvas.setAttribute('height', height);
		

		renderer.render(scene, camera);
		requestAnimationFrame(function(){loop();});
	}
	function check(t1, t2, t3, t4){
		text2.innerHTML = "Your score:" + score;
		text.innerHTML = "Your speed:" + k;
		if (t4.x > player.position.x - 5 &&
			t4.x < player.position.x + 5 &&
			t4.z > player.position.z - 5 &&
			t4.z < player.position.z + 5){
				random_position(t4);
			k += 0.5;
			score += 1;
		}
		if (t1.x > player.position.x - 5 &&
			t1.x < player.position.x + 5 &&
			t1.z > player.position.z - 5 &&
			t1.z < player.position.z + 5){
				random_position(t1);
			k += 0.5;
			score += 1;
		}
		if (t2.x > player.position.x - 5 &&
			t2.x < player.position.x + 5 &&
			t2.z > player.position.z - 5 &&
			t2.z < player.position.z + 5){
				random_position(t2);
			k += 0.5;
			score += 1;
		}
		if (t3.x > player.position.x - 5 &&
			t3.x < player.position.x + 5 &&
			t3.z > player.position.z - 5 &&
			t3.z < player.position.z + 5){
				random_position(t3);
			k += 0.5;
			score += 1;
		}

	}
	function updatePlayer(){
		if (flag == 1) {
			player.position.z -= 3 + k;
		} else if (flag == 2) {
	        player.position.z += 3 + k;
	    } else if (flag == 3) {
	        player.position.x -= 3 + k;
	    } else if (flag == 4) {
	        player.position.x += 3 + k;
	    }
	}
	function end(){
		renderer.clear();
		//отправляет результаты
		var dd = {'speed': k,
		'score':score};
		$.ajax({
		    type: "POST",
		    url: "{{ url_for('/score') }}",
		    contentType: "application/json",
		    data: JSON.stringify(dd),
		    dataType: "json",
		    success: function(response) {
		        window.location.replace("/");
		    },
		    error: function(err) {
		        window.location.replace("/");
		    }
		});
	loop();
    }
}