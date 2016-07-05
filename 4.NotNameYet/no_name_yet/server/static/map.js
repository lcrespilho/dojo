var my_pos = {lat: -22.0101706, lng: -47.887001};

function initMap() {

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: my_pos
  });

  // Try HTML5 geolocation.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };

      my_pos = pos;
      map.setCenter(pos);

    });
  }

  var marker = new google.maps.Marker({
    position: my_pos,
    map: map,
    title: 'Hello World!'
  });

  map.addListener('click', function(e) {
    placeMarkerAndPanTo(e.latLng, marker, map);
  });
}


function placeMarkerAndPanTo(latLng, marker, map) {
  my_pos = { lat: latLng.lat(), lng: latLng.lng()};
  console.log(my_pos)
  marker.setPosition(latLng);
}