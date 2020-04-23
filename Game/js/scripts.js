/*window.onload = function () {
	var width = window.innerWidth;
	var	height = window.innerHeight;
	var canvas = document.getElementById('canvas');
	var controls;

	canvas.setAttribute('width', width);
	canvas.setAttribute('height', height);

	var renderer = new THREE.WebGLRenderer({canvas: canvas});
	renderer.setClearColor(0x000000);
	renderer.shadowMapenabled = true;

	var scene = new THREE.Scene();

	var camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 5000);

	controls = new THREE.OrbitControls (camera, renderer.domElement);

	const color = 0xFFFFFF;
	const intensity = 1;
	const light = new THREE.DirectionalLight(color, intensity);
	light.position.set(0, 10, 0);
	light.target.position.set(-5, 0, 0);
	scene.add(light);
	scene.add(light.target);
	camera.position.set(100, 0, 100);

	var tree;
	var parser = new vox.Parser();
	parser.parse("../img/untitled.vox").then(function(voxelData) {
	  voxelData.voxels; 
	  voxelData.size;
	  voxelData.palette;

	  var builder = new vox.MeshBuilder(voxelData, param);
	  tree = builder.createMesh();
	  tree.geometry.center();
	  scene.add(tree);
	});

	var geometry_plane = new THREE.PlaneGeometry(10000,10000);
	var material_plane = new THREE.MeshPhongMaterial( {color: 0x88D9FF,wireframe: false});
	
	var geometry_player = new THREE.CubeGeometry(100,100,100);
	var material_player = new THREE.MeshPhongMaterial( {color: 0xF2FF88,wireframe: false});

	var player = new THREE.Mesh(geometry_player, material_player);
	player.position.y += 50
	scene.add(player);

	var plane = new THREE.Mesh(geometry_plane, material_plane);
	plane.rotation.x=-0.5*Math.PI;
	scene.add(plane);

	plane.receiveShadow = true;
	player.castShadow = true;
	light.castShadow = true;
	let flag = 1
	document.addEventListener("keydown", function(event){
		console.log(flag);
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
	    loop();
	});
	function loop() {
		
		var width = window.innerWidth;
		var	height = window.innerHeight;
		canvas.setAttribute('width', width);
		canvas.setAttribute('height', height);
		

		renderer.render(scene, camera);
		requestAnimationFrame(function(){loop();});
	}
	function updatePlayer(){
		if (flag == 1) {
			player.position.z -= 1;
		} else if (flag == 2) {
	        player.position.z += 1;
	    } else if (flag == 3) {
	        player.position.x -= 1;
	    } else if (flag == 4) {
	        player.position.x += 1;
	    }
	}
	loop();
}*/


	var width = window.innerWidth;
	var	height = window.innerHeight;
	var canvas = document.getElementById('canvas');
	var controls;

	canvas.setAttribute('width', width);
	canvas.setAttribute('height', height);

	var renderer = new THREE.WebGLRenderer({canvas: canvas});
	renderer.setClearColor(0x000000);
	renderer.shadowMapenabled = true;

	var scene = new THREE.Scene();

	var camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 5000);

	controls = new THREE.OrbitControls (camera, renderer.domElement);

	const color = 0xFFFFFF;
	const intensity = 1;
	const light = new THREE.DirectionalLight(color, intensity);
	light.position.set(0, 10, 0);
	light.target.position.set(-5, 0, 0);
	scene.add(light);
	scene.add(light.target);
	camera.position.set(100, 0, 100);

	var tree;
	var parser = new vox.Parser();
	parser.parse("../img/untitled.vox").then(function(voxelData) {
	  voxelData.voxels; 
	  voxelData.size;
	  voxelData.palette;

	  var builder = new vox.MeshBuilder(voxelData, param);
	  tree = builder.createMesh();
	  tree.geometry.center();
	  scene.add(tree);
	});

	light.castShadow = true;

	function loop() {
		var width = window.innerWidth;
		var	height = window.innerHeight;
		canvas.setAttribute('width', width);
		canvas.setAttribute('height', height);
		
		renderer.render(scene, camera);
		requestAnimationFrame(function(){loop();});
	}
loop();
